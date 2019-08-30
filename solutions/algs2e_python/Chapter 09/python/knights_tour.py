from tkinter import messagebox
import tkinter as tk
import math
import time


def knights_tour(row, col, move_number, num_moves_taken, num_attempts):
    """
    Move the knight to position [row][col]. Then recursively try
    to make other moves. Return true if we find a valid solution.
    Return a auccess code and the number of attempts.
    """
    # Move the knight to this position.
    num_attempts += 1
    num_moves_taken += 1
    move_number[row][col] = num_moves_taken

    # See if we have taken all of the required moves.
    num_rows = len(move_number)
    num_cols = len(move_number[0])
    num_squares = num_rows * num_cols
    if num_moves_taken == num_squares:
        return True, num_attempts

    # Build a  list of legal moves with respect to this position.
    moves = [(-2, -1), (-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2)]

    # Try all legal positions for the next move.
    for dr, dc in moves:
        r = row + dr
        c = col + dc
        if (r >= 0) and (r < num_rows) and \
           (c >= 0) and (c < num_cols) and \
           (move_number[r][c] == 0):
            # This move is legal and available. Make this move
            # and then recursively try other assignments.
            success, num_attempts = knights_tour(r, c, move_number, num_moves_taken, num_attempts)
            if success:
                return True, num_attempts

    # This move didn't work out. Undo it.
    move_number[row][col] = 0

    # If we get here, we did not find a valid solution.
    return False, num_attempts


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("knights_tour")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x400")

        # Canvas.
        frame = tk.Frame(self.window, borderwidth=2, relief="groove")
        frame.pack(padx=5, pady=5)
        self.canvas = tk.Canvas(frame, bg="white", width=260, height=260)
        self.canvas.pack()

        frame = tk.Frame(self.window)
        frame.pack()
        label = tk.Label(frame, text="# Rows:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_rows_entry = tk.Entry(frame, width=3, justify=tk.RIGHT)
        self.num_rows_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_rows_entry.insert(tk.END, "6")
        label = tk.Label(frame, text="# Cols:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_cols_entry = tk.Entry(frame, width=3, justify=tk.RIGHT)
        self.num_cols_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_cols_entry.insert(tk.END, "6")

        solve_button = tk.Button(self.window, text="Solve", width=8, command=self.solve)
        solve_button.pack(padx=5, pady=5)

        frame = tk.Frame(self.window)
        frame.pack()
        label = tk.Label(frame, text="Positioned Tried:")
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
        canvas_wid = self.canvas.winfo_width()
        canvas_hgt = self.canvas.winfo_height()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_rows_entry.focus_force()
        self.window.mainloop()

    def solve(self):
        """ Solve the problem and draw the chess board."""
        # Clear the display.
        self.num_rows = int(self.num_rows_entry.get())
        self.num_cols = int(self.num_cols_entry.get())
        self.canvas_wid = self.canvas.winfo_width()
        self.canvas_hgt = self.canvas.winfo_height()
        self.col_wid = self.canvas_wid / self.num_cols
        self.row_hgt = self.canvas_hgt / self.num_rows

        self.positions_entry.delete(0, tk.END)
        self.time_entry.delete(0, tk.END)
        self.show_empty_board()
        self.canvas.update()

        move_number = [[0 for r in range(self.num_rows)] for c in range(self.num_cols)]

        start_time = time.time()

        # Try starting from [0, 0].
        num_attempts = 0
        success, num_attempts = knights_tour(0, 0, move_number, 0, num_attempts)
        stop_time = time.time()

        # If we have a solution. Display it.
        if success:
            self.show_solution(move_number)
        else:
            # We did not find a solution.
            messagebox.showinfo("No Solution", "No solution found.")

        self.positions_entry.delete(0, tk.END)
        self.positions_entry.insert(tk.END, f"{num_attempts}")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(tk.END, f"{stop_time - start_time:0.2f} sec")

    def show_empty_board(self):
        """ Display a blank chess board."""
        self.canvas.delete(tk.ALL)
        for row in range(self.num_rows):
            y = row * self.row_hgt
            for col in range(self.num_cols):
                x = col * self.col_wid
                if (row + col) % 2 == 0:
                    self.canvas.create_rectangle(x, y, x + self.col_wid, y + self.row_hgt, fill="white", outline="")
                else:
                    self.canvas.create_rectangle(x, y, x + self.col_wid, y + self.row_hgt, fill="lightgray", outline="")

    def show_solution(self, move_number):
        """ Display the solution."""
        # Draw the moves.
        pts = []
        for i in range(1, self.num_rows * self.num_cols + 1):
            found_it = False;
            for row in range(self.num_rows):
                for col in range(self.num_cols):
                    if move_number[row][col] == i:
                        x = self.col_wid * (col + 0.5)
                        y = self.row_hgt * (row + 0.5)
                        pts.append(x)
                        pts.append(y)
                        found_it = True
                        break
                if found_it:
                    break
        self.canvas.create_line(pts, fill="blue")

        for row in range(self.num_rows):
            for col in range(self.num_cols):
                cx = self.col_wid * (col + 0.5)
                cy = self.row_hgt * (row + 0.5)
                self.canvas.create_text(cx, cy, text=f"{move_number[row][col]}")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
