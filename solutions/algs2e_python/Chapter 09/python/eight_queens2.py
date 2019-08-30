import tkinter as tk
import math
import time


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("eight_queens2")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x370")

        # Canvas.
        frame = tk.Frame(self.window, borderwidth=2, relief="groove")
        frame.pack(padx=5, pady=5)
        self.canvas = tk.Canvas(frame, bg="white", width=260, height=260)
        self.canvas.pack()

        solve_button = tk.Button(self.window, text="Solve", width=8, command=self.solve)
        solve_button.pack(padx=5, pady=5)

        frame = tk.Frame(self.window)
        frame.pack()

        label = tk.Label(frame, text="Positions Tried:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.positions_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.positions_entry.grid(row=0, column=1, padx=5, pady=2)

        label = tk.Label(frame, text="Time:")
        label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.time_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.time_entry.grid(row=1, column=1, padx=5, pady=2)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Set drawing parameters.
        self.num_rows = 8
        self.num_cols = 8
        self.num_queens = 8
        canvas_wid = self.canvas.winfo_width()
        canvas_hgt = self.canvas.winfo_height()
        self.col_wid = canvas_wid / self.num_cols
        self.row_hgt = canvas_hgt / self.num_rows

        # Force focus so Alt+F4 closes this window and not the Python shell.
        solve_button.focus_force()
        self.window.mainloop()

    def solve(self):
        """ Solve the problem and draw the chess board."""
        # The board.
        spot_taken = [[False for c in range(self.num_cols)] for r in range(self.num_rows)]
        num_attacks = [[0 for c in range(self.num_cols)] for r in range(self.num_rows)]

        num_attempts = 0
        start_time = time.time()
        success, num_attempts = self.eight_queens(spot_taken, num_attacks, 0)
        stop_time = time.time()

        # Clear the display.
        self.show_empty_board()

        # If we have a solution, display it.
        if success:
            self.show_solution(spot_taken)

        self.positions_entry.delete(0, tk.END)
        self.positions_entry.insert(tk.END, f"{num_attempts}")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(tk.END, f"{stop_time - start_time:0.2f} sec")

    def eight_queens(self, spot_taken, num_attacks, num_queens_positioned):
        """
        Explore this test solution.
        Return False if it cannot be extended to a full solution.
        Return True if a recursive call to eight_queens finds a full solution.
        Also return the number or attempts.
        """
        # See if the test solution is already illegal.
        if not self.is_legal(spot_taken):
            return False, 0

        # See if we have positioned all of the queens.
        if num_queens_positioned == self.num_queens:
            return True, 0

        # Extend the partial solution.
        # Try all positions for the next queen.
        num_attempts = 0
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                if (not spot_taken[row][col]) and (num_attacks[row][col] == 0):
                    num_attempts += 1
                    spot_taken[row][col] = True

                    # Mark the spots this queen can attack.
                    self.mark_attacked_spots(num_attacks, row, col, +1)

                    # Recursively see if this leads to a solution.
                    success, new_num_attempts = self.eight_queens(spot_taken, num_attacks, num_queens_positioned + 1)
                    num_attempts += new_num_attempts
                    if success:
                        return True, num_attempts

                    # Unmark the spots this queen can attack.
                    self.mark_attacked_spots(num_attacks, row, col, -1)
                    spot_taken[row][col] = False

        # If we get here, we could not find a valid solution.
        return False, num_attempts

    def mark_attacked_spots(self, num_attacks, row, col, amount):
        """
        Add "amount" to the number of attacks on the 
        squares that this queen can attack.
        """
        # Mark the row and column.
        for c in range(self.num_cols):
            num_attacks[row][c] += amount
        for r in range(self.num_rows):
            num_attacks[r][col] += amount

        # Mark the upper left/lower right diagonal.
        min_dx1 = -min(row, col)
        max_dx1 = min(self.num_rows - row - 1, self.num_cols - col - 1)
        for dx in range(min_dx1, max_dx1 + 1):
            num_attacks[row + dx][col + dx] += amount

        # Mark the upper right/lower left diagonal.
        min_dx2 = -min(row, self.num_cols - col - 1)
        max_dx2 = min(self.num_rows - row - 1, col)
        for dx in range(min_dx2, max_dx2 + 1):
            num_attacks[row + dx][col - dx] += amount

    def is_legal(self, spot_taken):
        """ Return True if this board position is legal."""
        for row in range(self.num_rows):
            for col in range(self.num_cols):
                # See if this position is taken.
                if spot_taken[row][col]:
                    # See if this position attacks another queen.
                    # Check the row.
                    for c in range(self.num_cols):
                        if (c != col) and spot_taken[row][c]:
                            return False
                    # Check the column.
                    for r in range(self.num_rows):
                        if (r != row) and spot_taken[r][col]:
                            return False

                    # Check the upper left/lower right diagonal.
                    min_dx1 = -min(row, col)
                    max_dx1 = min(self.num_rows - row - 1, self.num_cols - col - 1)
                    for dx in range(min_dx1, max_dx1 + 1):
                        # Skip this queen's position.
                        if dx != 0:
                            # See if there is a queen here.
                            if spot_taken[row + dx][col + dx]:
                                return False

                    # Check the upper right/lower left diagonal.
                    min_dx2 = -min(row, self.num_cols - col - 1)
                    max_dx2 = min(self.num_rows - row - 1, col)
                    for dx in range(min_dx2, max_dx2 + 1):
                        # Skip this queen's position.
                        if dx != 0:
                            # See if there is a queen here.
                            if spot_taken[row + dx][col - dx]:
                                return False
        return True

    def show_empty_board(self):
        """ Display a blank chess board."""
        self.canvas.delete(tk.ALL)
        self.canvas_wid = self.canvas.winfo_width()
        self.canvas_hgt = self.canvas.winfo_height()
        self.col_wid = self.canvas_wid / self.num_cols
        self.row_hgt = self.canvas_hgt / self.num_rows
        for row in range(self.num_rows):
            y = row * self.row_hgt
            for col in range(self.num_cols):
                x = col * self.col_wid
                if (row + col) % 2 == 0:
                    self.canvas.create_rectangle(x, y, x + self.col_wid, y + self.row_hgt, fill="white", outline="")
                else:
                    self.canvas.create_rectangle(x, y, x + self.col_wid, y + self.row_hgt, fill="lightgray", outline="")

    def show_solution(self, spot_taken):
        """ Display the solution."""
        # Draw the queens.
        for row in range(self.num_rows):
            y = row * self.row_hgt
            for col in range(self.num_cols):
                x = col * self.col_wid
                if spot_taken[row][col]:
                    self.draw_queen(
                        self.col_wid * (col + 0.5),
                        self.row_hgt * (row + 0.5),
                        self.col_wid * 0.4,
                        self.row_hgt * 0.4)

    def draw_queen(self, cx, cy, rx, ry):
        """ Draw a queen."""
        # Make the points.
        num_points = 7
        pts = []
        theta = -math.pi / 2
        dtheta = math.pi / num_points
        for i in range(0, 2 * num_points + 1, 2):
            pts.append(cx + rx * math.cos(theta))
            pts.append(cy + ry * math.sin(theta))
            theta += dtheta
            pts.append(cx + 0.5 * rx * math.cos(theta))
            pts.append(cy + 0.5 * ry * math.sin(theta))
            theta += dtheta

        # Draw the queen.
        self.canvas.create_polygon(pts, fill="lightblue", outline="blue")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
