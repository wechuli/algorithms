import random
import tkinter as tk


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("sparse_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("260x350")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="# Rows:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_rows_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.num_rows_entry.grid(padx=5, pady=2, row=0, column=1)
        self.num_rows_entry.insert(0, "5")
        go_button = tk.Button(frame, width=10, text="Go", command=self.go)
        go_button.grid(padx=5, pady=2, row=0, column=2, rowspan=2)

        label = tk.Label(frame, text="# Columns:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.num_columns_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.num_columns_entry.grid(padx=5, pady=2, row=1, column=1)
        self.num_columns_entry.insert(0, "7")

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_rows_entry.focus_force()
        self.window.mainloop()

    def go(self):
        """ Fill arrays in various ways."""
        self.listbox.delete(0, tk.END)

        num_rows = int(self.num_rows_entry.get())
        num_columns = int(self.num_columns_entry.get())

        # Make the array.
        values = [[0 for c in range(num_columns)] for r in range(num_rows)]

        # Fill with 0\1.
        self.fill_array_ll_to_ur(values, 0, 1)
        self.list_array(values, self.listbox)
        self.listbox.insert(tk.END, "")

        # Fill with 0/1.
        self.fill_array_ul_to_lr(values, 0, 1)
        self.list_array(values, self.listbox)
        self.listbox.insert(tk.END, "")

        # Fill by circles.
        self.fill_array_with_distances(values)
        self.list_array(values, self.listbox)

    def fill_array_ll_to_ur(self, values, ll_value, ur_value):
        """
        Fill the array diagonally with the
        indicated values on the lower left and upper right.
        """
        for row in range(len(values)):
            for col in range(len(values[row])):
                if row >= col:
                    values[row][col] = ur_value
                else:
                    values[row][col] = ll_value

    def fill_array_ul_to_lr(self, values, ul_value, lr_value):
        """
        Fill the array diagonally with the
        indicated values on the upper left and lower right.
        """
        max_col = len(values[0]) - 1
        for row in range(len(values)):
            for col in range(len(values[row])):
                if row > max_col - col:
                    values[row][col] = ul_value
                else:
                    values[row][col] = lr_value

    def fill_array_with_distances(self, values):
        """ Fill each entry with its distance to the edge."""
        max_row = len(values) - 1
        max_col = len(values[0]) - 1

        for row in range(max_row + 1):
            for col in range(max_col + 1):
                values[row][col] = min( \
                    min(row, col), \
                    min(max_row - row, max_col - col))

    def list_array(self, array, listbox):
        """ List the items in an array."""
        for row in array:
            listbox.insert(tk.END, " ".join(map(str, row)))


if __name__ == '__main__':
    app = App()
