import tkinter as tk


class TriangularArray:
    def __init__(self, num_rows):
        """ Initialize the array by allocating the Values array."""
        self.num_rows = num_rows
        num_items = self.num_cells_for_rows(num_rows)
        self.values = [None for i in range(num_items)]

    def row_column_to_index(self, row, col):
        """ Convert a row and column into a linear array index."""
        if row >= self.num_rows:
            raise ValueError(f"The row value {row} must be less than the number of rows {self.num_rows}")
        if col >= self.num_rows:
            raise ValueError(f"The column value {col} must be less than the number of rows {self.num_rows}")

        # Convert upper-triangular to lower-triangular.
        if col > row:
            row, col = col, row

        # Return the index.
        return self.num_cells_for_rows(row) + col

    def num_cells_for_rows(self, rows):
        """ Return the number of cells in an array with this many rows."""
        return (rows * rows + rows) // 2

    def __getitem__(self, rc):
        """ Get an array value."""
        row, col = rc
        index = self.row_column_to_index(row, col)
        return self.values[index]

    def __setitem__(self, rc, value):
        """ Set an array value."""
        row, col = rc
        index = self.row_column_to_index(row, col)
        self.values[index] = value


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("triangular_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("290x200")

        frame = tk.Frame(self.window)
        frame.pack(expand=True)

        label_a00 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a00.grid(padx=2, pady=2, row=0, column=0, sticky=tk.W)
        label_a10 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a10.grid(padx=2, pady=2, row=1, column=0, sticky=tk.W)
        label_a11 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a11.grid(padx=2, pady=2, row=1, column=1, sticky=tk.W)
        label_a20 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a20.grid(padx=2, pady=2, row=2, column=0, sticky=tk.W)
        label_a21 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a21.grid(padx=2, pady=2, row=2, column=1, sticky=tk.W)
        label_a22 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a22.grid(padx=2, pady=2, row=2, column=2, sticky=tk.W)
        label_a30 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a30.grid(padx=2, pady=2, row=3, column=0, sticky=tk.W)
        label_a31 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a31.grid(padx=2, pady=2, row=3, column=1, sticky=tk.W)
        label_a32 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a32.grid(padx=2, pady=2, row=3, column=2, sticky=tk.W)
        label_a33 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_a33.grid(padx=2, pady=2, row=3, column=3, sticky=tk.W)

        label_b00 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b00.grid(padx=2, pady=2, row=0, column=3, sticky=tk.W)
        label_b01 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b01.grid(padx=2, pady=2, row=0, column=4, sticky=tk.W)
        label_b02 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b02.grid(padx=2, pady=2, row=0, column=5, sticky=tk.W)
        label_b03 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b03.grid(padx=2, pady=2, row=0, column=6, sticky=tk.W)
        label_b11 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b11.grid(padx=2, pady=2, row=1, column=4, sticky=tk.W)
        label_b12 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b12.grid(padx=2, pady=2, row=1, column=5, sticky=tk.W)
        label_b13 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b13.grid(padx=2, pady=2, row=1, column=6, sticky=tk.W)
        label_b22 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b22.grid(padx=2, pady=2, row=2, column=5, sticky=tk.W)
        label_b23 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b23.grid(padx=2, pady=2, row=2, column=6, sticky=tk.W)
        label_b33 = tk.Label(frame, width=4, height=2, borderwidth=2, relief=tk.RIDGE)
        label_b33.grid(padx=2, pady=2, row=3, column=6, sticky=tk.W)

        # Demonstrate a triangular array.
        num_rows = 4

        # Make a lower triangular array.
        array1 = TriangularArray(num_rows)
        for row in range(num_rows):
            for col in range(row + 1):
                array1[(row, col)] = f"({row}, {col})"

        # Make a 2-D array holding the first array's labels.
        a_labels = [
            [ label_a00,      None,      None,      None],
            [ label_a10, label_a11,      None,      None],
            [ label_a20, label_a21, label_a22,      None],
            [ label_a30, label_a31, label_a32, label_a33]
        ]

        # Display the array values.
        for row in range(num_rows):
            for col in range(row + 1):
                a_labels[row][col]["text"] = array1[(row, col)]

        # Make an upper triangular array.
        array2 = TriangularArray(num_rows)
        for row in range(num_rows):
            for col in range(row, num_rows):
                array2[(row, col)] = f"({row}, {col})"

        # Make a 2-D array holding the first array's labels.
        b_labels = [
            [ label_b00, label_b01, label_b02, label_b03],
            [      None, label_b11, label_b12, label_b13],
            [      None,      None, label_b22, label_b23],
            [      None,      None,      None, label_b33],
        ]

        # Display the array values.
        for row in range(num_rows):
            for col in range(row, num_rows):
                b_labels[row][col]["text"] = array2[(row, col)]

        # Force focus so Alt+F4 closes this window and not the Python shell.
        label_a00.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
