import random
import tkinter as tk
import tkinter.font as tk_font

BORDER_WIDTH = 3

class TwoDArray:
    def __init__(self, lower_bound0, upper_bound0, lower_bound1, upper_bound1):
        """ Save the lower bounds."""
        self.lower_bound0 = lower_bound0
        self.lower_bound1 = lower_bound1

        # Allocate the array.
        num_rows = upper_bound0 - lower_bound0 + 1
        num_columns = upper_bound1 - lower_bound1 + 1
        self.values = [[None for c in range(num_columns)] for r in range(num_columns)]

    def __getitem__(self, rc):
        """ Get a value."""
        r, c = rc
        return self.values[r - self.lower_bound0][c - self.lower_bound1]

    def __setitem__(self, rc, value):
        """ Set a value."""
        r, c = rc
        self.values[r - self.lower_bound0][c - self.lower_bound1] = value


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("two_d_array")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("600x200")

        list_box = tk.Listbox(self.window)
        list_box.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Demonstrate the TwoDArray class.
        # Make the array.
        array = TwoDArray(1, 10, 2000, 2010)

        # Fill the array.
        for r in range(1, 11):
            for c in range(2000, 2011):
                array[(r, c)] = f"({r:02d}, {c})"

        # Display the values.
        for r in range(1, 11):
            txt = ""
            for c in range(2000, 2011):
                txt += array[(r, c)] + " "
            list_box.insert(tk.END, txt)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()
