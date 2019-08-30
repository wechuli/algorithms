import sys
import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox


def beep():
    print("\a", end="")
    sys.stdout.flush()


class BoardValues():
    """ Board values."""
    none = 0
    loss = 1
    draw = 2
    unknown = 3
    win = 4


class SkillLevels():
    """ Skill levels."""
    random = 0
    beginner = 1
    advanced = 2


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        self.tree_links = []
        self.walls = []

        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("count_tic_tac_toe_boards")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("200x200")

        # Make the right parameter area.
        frame = tk.Frame(self.window)
        frame.pack(expand=True)

        count_button = tk.Button(frame, text="Count", width=8, command=self.count)
        count_button.grid(padx=5, pady=2, row=0, column=1)
        label = tk.Label(frame, text="X Wins:")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.xwins_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.xwins_entry.grid(padx=5, pady=2, row=1, column=1)
        label = tk.Label(frame, text="O Wins:")
        label.grid(padx=5, pady=2, row=2, column=0)
        self.owins_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.owins_entry.grid(padx=5, pady=2, row=2, column=1)
        label = tk.Label(frame, text="Tie:")
        label.grid(padx=5, pady=2, row=3, column=0)
        self.ties_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.ties_entry.grid(padx=5, pady=2, row=3, column=1)
        label = tk.Label(frame, text="Total:")
        label.grid(padx=5, pady=2, row=4, column=0)
        self.total_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.total_entry.grid(padx=5, pady=2, row=4, column=1)

        # Prepare for a game.
        self.reset()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=count_button: count_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        count_button.focus_force()
        self.window.mainloop()

    def count(self):
        self.num_squares_taken = 0
        self.num_x_wins = 0
        self.num_o_wins = 0
        self.num_ties = 0

        self.count_games("X", "O")

        self.xwins_entry.delete(0, tk.END)
        self.xwins_entry.insert(tk.END, f"{self.num_x_wins:,}")
        self.owins_entry.delete(0, tk.END)
        self.owins_entry.insert(tk.END, f"{self.num_o_wins:,}")
        self.ties_entry.delete(0, tk.END)
        self.ties_entry.insert(tk.END, f"{self.num_ties:,}")
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(tk.END, f"{self.num_x_wins + self.num_o_wins + self.num_ties:,}")

    def count_games(self, player1, player2):
        """ Recursively examine all possible games."""
        for row in range(3):
            for col in range(3):
                # See if this position is taken.
                if self.board[row][col] == " ":
                    # Try this move.
                    self.board[row][col] = player1
                    self.num_squares_taken += 1

                    # See if this ends the game.
                    if self.is_winner(row, col):
                        # player1 won.
                        if player1 == "X":
                            self.num_x_wins += 1
                        else:
                            self.num_o_wins += 1
                    elif self.num_squares_taken == 9:
                        # Cat's game.
                        self.num_ties += 1
                    else:
                        # The game is not over.
                        self.count_games(player2, player1)

                    # Unmake the move.
                    self.board[row][col] = " "
                    self.num_squares_taken -= 1

    def reset(self):
        """ Prepare for a new game."""
        self.board = [[" " for r in range(3)] for c in range(3)]
        for r in range(3):
            for c in range(3):
                self.board[r][c] = " "
        self.current_player = "X"
        self.num_squares_taken = 0

    def square_clicked(self, event, rc):
        """ The user clicked a square."""

        # Get the row and column.
        r, c = rc

        # See if the spot is already taken.
        if self.board[r][c] != " ":
            beep()
            return

        # Take this square.
        self.board[r][c] = self.current_player
        self.num_squares_taken += 1

        # See if there is a winner.
        if self.is_winner(r, c):
            self.show_winner()
            return
        elif self.num_squares_taken == 9:
            # We have a cat's game.
            self.show_cats_game()
            return

        # Switch players.
        if self.current_player == "X":
            self.current_player = "O"
        else:
            self.current_player = "X"

    def is_winner(self, r, c):
        """ Return true if the player who just took spare [r, c] has won."""
        player = self.board[r][c]
        if ((player == self.board[r][0]) and \
            (player == self.board[r][1]) and \
            (player == self.board[r][2])):
                return True
        if ((player == self.board[0][c]) and \
            (player == self.board[1][c]) and \
            (player == self.board[2][c])):
                return True
        if ((r == c) or (r + c == 2)):
            if ((player == self.board[0][0]) and \
                (player == self.board[1][1]) and \
                (player == self.board[2][2])):
                    return True
            if ((player == self.board[0][2]) and \
                (player == self.board[1][1]) and \
                (player == self.board[2][0])):
                    return True

        return False

    def show_winner(self):
        """ Display a winner message."""
        text = f"{self.current_player} Wins!"
        messagebox.showinfo(text, text)
        self.current_player = " "

    def show_cats_game(self):
        text = "It's a tie!"
        messagebox.showinfo(text, text)
        self.current_player = " "

    def board_value(self, player1, player2, depth, max_depth):
        """ Find the best board value for player1."""
        # If we are too deep, then we don't know.
        if (depth > max_depth) or (self.num_squares_taken == 9):
            return BoardValues.unknown, -1, -1

        # Track the worst move for player2.
        player2_value = BoardValues.win

        # Make test moves.
        for row in range(3):
            for col in range(3):
                # See if this move is taken.
                if self.board[row][col] == ' ':
                    # Try this move.
                    self.board[row][col] = player1
                    self.num_squares_taken += 1

                    # See if this gives player1 a win.
                    if self.is_winner(row, col):
                        # This gives player1 a win and therefore player2 a loss.
                        # Take this move.
                        best_r = row
                        best_c = col
                        player2_value = BoardValues.loss
                    else:
                        # Recursively try moves for player2.
                        test_r = -1
                        test_c = -1
                        test_value = BoardValues.none
                        test_value, test_r, test_c = self.board_value(player2, player1, depth + 1, max_depth)

                        # See if this is an improvement for player 2.
                        if player2_value >= test_value:
                            best_r = row
                            best_c = col
                            player2_value = test_value

                    # Undo the move.
                    self.board[row][col] = " "
                    self.num_squares_taken -= 1

                # If player2 will lose, stop searching.
                if player2_value == BoardValues.loss:
                    break

            # If player2 will lose, stop searching.
            if player2_value == BoardValues.loss:
                break

        # We now know the worst we can force player2 to do.
        # Convert that into a board value for player1.
        if player2_value == BoardValues.loss:
            best_value = BoardValues.win
        elif player2_value == BoardValues.win:
            best_value = BoardValues.loss
        else:
            best_value = player2_value

        return best_value, best_r, best_c


if __name__ == '__main__':
    app = App()

# app.root.destroy()

