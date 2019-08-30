import random
import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox
import math

BORDER_WIDTH = 3

def FindPolynomialLeastSquaresFit(points, degree):
    if degree >= len(points):
        raise Exception("The degree should be smaller than the number of points.")

    # Allocate space for degree + 1 equations with
    # unknowns degree + 2 unknowns.
    coeffs = [[0 for i in range(degree + 1)] for i in range(degree + 1)]

    # Calculate in the coefficients.
    for k in range(degree + 1):
        # Fill in coefficients for the partial
        # derivative with respect to Ak.
        for a_sub in range(degree + 1):
            # Calculate in the A<a_sub> term.
            coeffs[k][a_sub] = 0
            for i in range(len(points)):
                coeffs[k][a_sub] += math.pow(points[i][0], k + a_sub)

    # Calculate the constant values.
    values = [0 for i in range(degree + 1)]
    for k in range(degree + 1):
        values[k] = 0
        for i in range(len(points)):
            values[k] += points[i][1] * math.pow(points[i][0], k)

    # Solve the equations.
    return gaussian_eliminate(coeffs, values)

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with no data points.
        self.points = []
        self.solved = False
        self.m = 0
        self.b = 0

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("linear_least_squares")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x378")

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=50, height=50,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        # Parameters.
        parameter_frame = tk.Frame(self.window)
        parameter_frame.pack(padx=5, pady=5, side=tk.BOTTOM)

        degree_label = tk.Label(parameter_frame, text="Degree:")
        degree_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.degree_entry = tk.Entry(parameter_frame, width=4, justify=tk.RIGHT)
        self.degree_entry.grid(row=0, column=1, padx=5, pady=2)
        self.degree_entry.insert(tk.END, "3")

        solve_button = tk.Button(parameter_frame, text="Solve", width=10, command=self.solve)
        solve_button.grid(row=0, column=2, padx=5, pady=2)
        reset_button = tk.Button(parameter_frame, text="Reset", width=10, command=self.reset)
        reset_button.grid(row=0, column=3, padx=5, pady=2)

        a_values_label = tk.Label(parameter_frame, text="As:")
        a_values_label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W+tk.N)
        self.a_values_list = tk.Listbox(parameter_frame, height=5)
        self.a_values_list.grid(row=1, column=1, columnspan=3, padx=5, pady=2, sticky=tk.W+tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Catch mouse clicks.
        self.canvas.bind("<Button-1>", self.mouse_click)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def mouse_click(self, event):
        self.points.append((event.x, event.y))
        self.solved = False
        self.draw()

    def reset(self):
        self.points = []
        self.solved = False
        self.draw()

    def solve(self):
        """Perform linear least squares."""
        try:
            self.a_values_list.delete(0, tk.END)
            self.solved = False

            degree = int(self.degree_entry.get())
            self.a_values = FindPolynomialLeastSquaresFit(self.points, degree)

            # Display the As.
            for k in range(len(self.a_values)):
                self.a_values_list.insert(tk.END, f"A[{k}] = {self.a_values[k]}")
            self.solved = True
        except Exception as e:
            messagebox.showinfo("Error", str(e))

        self.draw()

    def draw(self):
        """ Draw the points and least squares fit."""
        self.canvas.delete(tk.ALL)

        # Draw the points.
        radius = 2
        for point in self.points:
            x0 = point[0] - radius
            y0 = point[1] - radius
            x1 = x0 + 2 * radius
            y1 = y0 + 2 * radius
            self.canvas.create_oval(x0, y0, x1, y1, fill="red", outline="red")

        # If we have a solution, draw it.
        if self.solved:
            curve = []
            for x in range(self.canvas.winfo_width()):
                curve.append((x, F(self.a_values, x)))
            self.canvas.create_line(curve, fill="blue")

def F(a_values, x):
    result = 0
    factor = 1
    for i in range(len(a_values)):
        result += a_values[i] * factor
        factor *= x
    return result

def gaussian_eliminate(coeffs, values):
    """Perform Gaussian elimination and return the results in a list."""

    # The values num_rows and num_cols are the number of rows
    # and columns in the matrix, not the augmented matrix.
    num_rows = len(coeffs)
    num_cols = len(coeffs[0])

    # Build the agumented array.
    aug = []
    for r in range(0, num_rows):
        aug.append([])
        for value in coeffs[r]:
            aug[r].append(value)
        aug[r].append(float(values[r]))

    # Solve.
    for r in range(0, num_rows - 1):
        # Zero out all entries in column r after this row.
        # See if this row has a non-zero entry in column r.
        if abs(aug[r][r]) < TINY:
            # Too close to zero. Try to swap with a later row.
            for r2 in range(r + 1, num_rows):
                if abs(aug[r2][r]) > TINY:
                    # This row will work. Swap them.
                    for c in range(0, num_cols + 1):
                        aug[r][c], aug[r2][c] = aug[r2][c], aug[r][c]
                    break

        # See if aug[r][r] is still zero.
        if abs(aug[r][r]) < TINY:
            # No later row has a non-zero entry in this column.
            raise ValueError("There is no unique solution.")

        # Zero out this column in later rows.
        for r2 in range(r + 1, num_rows):
            factor = -aug[r2][r] / aug[r][r]
            for c in range(r, num_cols + 1):
                aug[r2][c] = aug[r2][c] + factor * aug[r][c]

    # See if we have a solution.
    if abs(aug[num_rows - 1][num_cols - 1]) < TINY:
        # We have no solution.
        # See if all of the entries in this row are 0.
        all_zeros = True
        for c in range(0, num_cols + 2):
            if abs(aug[num_rows - 1][c]) > TINY:
                all_zeros = False
                break

        if all_zeros:
            raise ValueError("The solution is not unique.")
        else:
            raise ValueError("There is no solution.")

    # Back substitute.
    xs = [0 for c in range(num_rows)]
    for r in range(num_rows - 1, -1, -1):
        xs[r] = aug[r][num_cols]
        for r2 in range(r + 1, num_rows):
            xs[r] -= aug[r][r2] * xs[r2]
        xs[r] /= aug[r][r]
    return xs

if __name__ == '__main__':
    app = App()
