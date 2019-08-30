import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox

TINY = 0.00001

class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("gaussian_elimination")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x480")

        # A fixed-width font.
        self.fixed_font = tk_font.Font(family="Courier New", size=10)

        # Parameters.
        self.coeffs_text = tk.Text(self.window, width=20, height=5, font=self.fixed_font)
        self.coeffs_text.insert(tk.END,
"""   1   1   1  1 1
  32  16   8  4 2
 243  81  27  9 3
1024 256  64 16 4
3125 625 125 25 5""")
        self.coeffs_text.grid(row=0, column=0, padx=5, pady=5)

        xs_label = tk.Label(self.window, width=3, height=5,
           font=self.fixed_font, text=
"""x0  
x1  
x2 =
x3  
... """)
        xs_label.grid(row=0, column=1, padx=5, pady=5)

        self.values_text = tk.Text(self.window, width=5, height=5, font=self.fixed_font)
        self.values_text.insert(tk.END,
"""  1
 -1
  8
-56
569""")
        self.values_text.grid(row=0, column=2, padx=5, pady=5)

        # Button.
        button = tk.Button(self.window, text="Calculate", command=self.calculate)
        button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

        # Results.
        xs_label = tk.Label(self.window, text="Xs:", justify=tk.LEFT)
        xs_label.grid(row=2, column=0, padx=5, pady=(5, 0), sticky=tk.W)
        self.xs_list = tk.Listbox(self.window, height=5)
        self.xs_list.grid(row=3, column=0, columnspan=3, padx=5, pady=0, sticky=tk.W+tk.E)

        check_label = tk.Label(self.window, text="Check:", justify=tk.LEFT)
        check_label.grid(row=4, column=0, padx=5, pady=(5, 0), sticky=tk.W)
        self.check_list = tk.Listbox(self.window, height=5)
        self.check_list.grid(row=5, column=0, columnspan=3, padx=5, pady=0, sticky=tk.W+tk.E)

        errors_label = tk.Label(self.window, text="Errors:", justify=tk.LEFT)
        errors_label.grid(row=6, column=0, padx=5, pady=(5, 0), sticky=tk.W)
        self.errors_list = tk.Listbox(self.window, height=5)
        self.errors_list.grid(row=7, column=0, columnspan=3, padx=5, pady=0, sticky=tk.W+tk.E)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def calculate(self):
        """Build and solve the augmented matrix."""

        # Get the coefficients and values.
        coeffs = self.load_coeffs()
        values = self.load_values()

        # Solve.
        self.xs_list.delete(0, tk.END)
        self.check_list.delete(0, tk.END)
        self.errors_list.delete(0, tk.END)
        try:
            xs = gaussian_eliminate(coeffs, values)
        except ValueError as e:
            messagebox.showinfo("Calculation Error", str(e))
            return

        # Display the values.
        for r in range(len(xs)):
            self.xs_list.insert(tk.END, f"x[{r}] = {xs[r]}")

        # Verify.
        num_rows = len(coeffs)
        num_cols = len(coeffs[0])
        for r in range(num_rows):
            tmp = 0
            for c in range(num_cols):
                tmp += coeffs[r][c] * xs[c]
            self.check_list.insert(tk.END, f"{tmp}")

            error = tmp - values[r]
            self.errors_list.insert(tk.END, f"{error}")

    def load_coeffs(self):
        """Load the coefficients array."""

        # Get the coefficients text.
        coeffs_text = self.coeffs_text.get("1.0", tk.END)

        # Split the text into rows.
        coeffs_rows = list(filter(None, coeffs_text.split("\n")))

        # Process the rows.
        arr = list(map(lambda x: list(map(float, x.split())), coeffs_rows))

        return arr

    def load_values(self):
        """Load the values array."""

        # Get the values text.
        values_text = self.values_text.get("1.0", tk.END)

        # Split the text into rows.
        values_rows = list(filter(None, values_text.split("\n")))

        # Process the rows.
        arr = list(map(float, values_rows))
        return arr

    def kill_callback(self):
        self.window.destroy()

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
        xs[r] = aug[r][num_cols];
        for r2 in range(r + 1, num_rows):
            xs[r] -= aug[r][r2] * xs[r2]
        xs[r] /= aug[r][r]
    return xs


if __name__ == '__main__':
    app = App()

# app.root.destroy()
