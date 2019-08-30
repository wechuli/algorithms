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
        self.window.title("tic_tac_toe")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("355x342")

        # Control area.
        menubar = tk.Menu(self.window)

        game_menu = tk.Menu(menubar, tearoff=False)
        game_menu.add_command(label="Play X", command=self.play_x, underline=5)
        game_menu.add_command(label="Play O", command=self.play_o, underline=5)
        game_menu.add_separator()
        game_menu.add_command(label="Exit", command=self.window.destroy, underline=0)
        menubar.add_cascade(label="Game", menu=game_menu)

        level_menu = tk.Menu(menubar, tearoff=False)
        self.skill_level = tk.IntVar()
        level_menu.add_radiobutton(label="Random", variable=self.skill_level, value=int(SkillLevels.random))
        level_menu.add_radiobutton(label="Beginner", variable=self.skill_level, value=int(SkillLevels.beginner))
        level_menu.add_radiobutton(label="Advanced", variable=self.skill_level, value=int(SkillLevels.advanced))
        self.skill_level.set(SkillLevels.random)
        menubar.add_cascade(label="Level", menu=level_menu)

        #  Build the board.
        font = tk_font.Font(size=65)
        sq_width = 2
        sq_height = 1
        padx = 5
        pady = 5
        row = 1
        self.squares = [[None for c in range(3)] for r in range(3)]
        self.squares[0][0] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="00", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[0][0].grid(padx=padx, pady=pady, row=row, column=0)
        self.squares[0][0].bind("<Button-1>", lambda event: self.square_clicked(event, (0, 0)))

        self.squares[0][1] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="01", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[0][1].grid(padx=padx, pady=pady, row=row, column=1)
        self.squares[0][1].bind("<Button-1>", lambda event: self.square_clicked(event, (0, 1)))

        self.squares[0][2] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="02", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[0][2].grid(padx=padx, pady=pady, row=row, column=2)
        self.squares[0][2].bind("<Button-1>", lambda event: self.square_clicked(event, (0, 2)))

        row += 1
        self.squares[1][0] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="10", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[1][0].grid(padx=padx, pady=pady, row=row, column=0)
        self.squares[1][0].bind("<Button-1>", lambda event: self.square_clicked(event, (1, 0)))

        self.squares[1][1] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="11", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[1][1].grid(padx=padx, pady=pady, row=row, column=1)
        self.squares[1][1].bind("<Button-1>", lambda event: self.square_clicked(event, (1, 1)))

        self.squares[1][2] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="12", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[1][2].grid(padx=padx, pady=pady, row=row, column=2)
        self.squares[1][2].bind("<Button-1>", lambda event: self.square_clicked(event, (1, 2)))

        row += 1
        self.squares[2][0] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="20", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[2][0].grid(padx=padx, pady=pady, row=row, column=0)
        self.squares[2][0].bind("<Button-1>", lambda event: self.square_clicked(event, (2, 0)))

        self.squares[2][1] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="21", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[2][1].grid(padx=padx, pady=pady, row=row, column=1)
        self.squares[2][1].bind("<Button-1>", lambda event: self.square_clicked(event, (2, 1)))

        self.squares[2][2] = tk.Label(self.window, width=sq_width, height=sq_height, bg="white", text="22", borderwidth=2, relief=tk.SUNKEN, font=font)
        self.squares[2][2].grid(padx=padx, pady=pady, row=row, column=2)
        self.squares[2][2].bind("<Button-1>", lambda event: self.square_clicked(event, (2, 2)))

        # Bind some shortcut keys.
        self.window.bind_all("<Control-x>", self.shortcut_play_x)
        self.window.bind_all("<Control-o>", self.shortcut_play_o)

        # Prepare for a game.
        self.play_x()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.config(menu=menubar)
        self.window.mainloop()

    def shortcut_play_x(self, event):
        self.play_x()

    def shortcut_play_o(self, event):
        self.play_o()

    def play_x(self):
        self.reset_game("X", "O")

    def play_o(self):
        self.reset_game("O", "X")

        # Let the computer move.
        self.make_computer_move()

    def reset_game(self, player, computer):
        """ Prepare for a new game."""
        self.board = [[" " for r in range(3)] for c in range(3)]
        for r in range(3):
            for c in range(3):
                self.squares[r][c]["text"] = ""
                self.board[r][c] = " "

        self.user_player = player
        self.computer_player = computer
        self.current_player = "X"
        self.num_squares_taken = 0

    def square_clicked(self, event, rc):
        """ The user clicked a square."""

        # See if a game is in progress.
        if self.current_player == " ":
            return

        # Get the row and column.
        r, c = rc

        # See if the spot is already taken.
        if self.board[r][c] != " ":
            beep()
            return

        # Take this square.
        self.board[r][c] = self.current_player
        self.squares[r][c]["text"] = self.current_player
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
        self.current_player = self.computer_player

        # Let the computer move.
        self.make_computer_move()

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

    def make_computer_move(self):
        """ Make the computer take a move."""
        # Check the skill level.
        skill_level = self.skill_level.get()
        if skill_level == SkillLevels.random:
            # Random moves.
            best_r, best_c = self.random_move()
            # print("Random")
        elif skill_level == SkillLevels.beginner:
            # Minimax looking 3 moves ahead.
            best_value, best_r, best_c = self.board_value(self.computer_player, self.user_player, 1, 3)
            # print("Beginner")
        else:
            # Minimax looking 9 moves ahead.
            best_value, best_r, best_c = self.board_value(self.computer_player, self.user_player, 1, 9)
            # print("Advanced")

        # Make the move.
        self.board[best_r][best_c] = self.computer_player
        self.squares[best_r][best_c]["text"] = self.computer_player
        self.num_squares_taken += 1

        # See if there is a winner.
        if self.is_winner(best_r, best_c):
            self.show_winner()
            return
        elif self.num_squares_taken == 9:
            # We have a cat's game.
            self.show_cats_game()
            return

        # Switch whose move it is.
        self.current_player = self.user_player

    def random_move(self):
        """ Move randomly."""
        best_r = -1
        best_c = -1

        # Pick a random move.
        move = random.randint(0, 9 - self.num_squares_taken)

        # Find that move.
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == " ":
                    move -= 1
                    if move < 0:
                        best_r = row
                        best_c = col
                        break
            if best_r >= 0:
                break

        return best_r, best_c

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

