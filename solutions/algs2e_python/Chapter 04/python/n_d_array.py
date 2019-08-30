import random
import tkinter as tk
import tkinter.font as tk_font

BORDER_WIDTH = 3

class NDArray:
    def __init__(self, bounds):
        """ Save the lower bounds."""
        # Make sure there is an even number of bounds.
        if len(bounds) % 2 == 1:
            raise ValueError("Number of bounds must be even.")

        # Make sure there are at least two bounds.
        if len(bounds) < 2:
            raise ValueError("There must be at least two bounds, one upper and one lower.")

        # Get the bounds.
        self.num_dimensions = len(bounds) // 2
        self.lower_bounds = [0 for d in range(self.num_dimensions)]
        self.slice_sizes = [0 for d in range(self.num_dimensions)]

        # Initialize lower_bounds and slice_sizes.
        slice_size = 1
        for i in range(self.num_dimensions - 1, -1, -1):
            self.slice_sizes[i] = slice_size

            self.lower_bounds[i] = bounds[2 * i]
            upper_bound = bounds[2 * i + 1]
            bound_size = upper_bound - self.lower_bounds[i] + 1
            slice_size *= bound_size

        # Allocate room for all of the items.
        self.values = [None for i in range(slice_size)]

    def __getitem__(self, indices):
        """ Get a value."""
        if len(indices) != self.num_dimensions:
            raise ValueError("The number of indices does not match the number of dimensions.")
        return self.values[self.index(indices)]

    def __setitem__(self, indices, value):
        """ Set a value."""
        if len(indices) != self.num_dimensions:
            raise ValueError("The number of indices does not match the number of dimensions.")
        self.values[self.index(indices)] = value

    def index(self, indices):
        """ Calculate the array location for a series of indices."""
        if len(indices) != self.num_dimensions:
            raise ValueError("The number of indices does not match the number of dimensions.")

        index = 0
        for i in range(self.num_dimensions):
            index += (indices[i] - self.lower_bounds[i]) * self.slice_sizes[i]
        return index

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("n_d_array")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("200x260")

        list_box = tk.Listbox(self.window)
        list_box.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Demonstrate the NDArray class.
        # Array bounds.
        lb0 = 1
        ub0 = 3
        lb1 = 2
        ub1 = 4
        lb2 = 10
        ub2 = 12

        # Make and fill an array.
        values = NDArray((lb0, ub0, lb1, ub1, lb2, ub2))
        for row in range(lb0, ub0 + 1):
            for col in range(lb1, ub1 + 1):
                for hgt in range(lb2, ub2 + 1):
                    values[(row, col, hgt)] = f"({row}, {col}, {hgt})"

        # Get the values.
        for row in range(lb0, ub0 + 1):
            list_box.insert(tk.END, f"Row {row}")
            for col in range(lb1, ub1 + 1):
                txt = "    "
                for hgt in range(lb2, ub2 + 1):
                    txt += f"{values[(row, col, hgt)]} "
                list_box.insert(tk.END, txt)
            list_box.insert(tk.END, "")

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()
