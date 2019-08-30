import tkinter as tk


class TetrahedralArray:
    def __init__(self, num_rows):
        """ Initialize the array by allocating the values array."""
        self.num_rows = num_rows

        # Make the linear array where we store items.
        num_items = self.num_cells_for_tetrahedral_rows(self.num_rows)
        self.values = [None for i in range(num_items)]

    def row_column_height_to_index(self, row, col, hgt):
        """ Convert a row, column, and height into a linear array index."""
        if row >= self.num_rows:
            raise ValueError(f"The row value {row} must be less than the number of rows {self.num_rows}")
        if col >= self.num_rows:
            raise ValueError(f"The column value {col} must be less than the number of rows {self.num_rows}")
        if hgt >= self.num_rows:
            raise ValueError(f"The height value {hgt} must be less than the number of rows {self.num_rows}")

        # Convert upper-triangular to lower-triangular.
        if hgt > col:
            hgt, col = col, hgt
        if col > row:
            row, col = col, row

        # Return the index.
        return self.num_cells_for_tetrahedral_rows(row) + self.num_cells_for_triangle_rows(col) + hgt

    def num_cells_for_triangle_rows(self, rows):
        """ Return the number of cells in a triangular array with this many rows."""
        return (rows * rows + rows) // 2

    def num_cells_for_tetrahedral_rows(self, rows):
        """ Return the number of cells in a tetrahedral array with this many rows."""
        return (rows * rows * rows + 3 * rows * rows + 2 * rows) // 6

    def __getitem__(self, rch):
        """ Get an array value."""
        row, col, hgt = rch
        index = self.row_column_height_to_index(row, col, hgt)
        return self.values[index]

    def __setitem__(self, rch, value):
        """ Set an array value."""
        row, col, hgt = rch
        index = self.row_column_height_to_index(row, col, hgt)
        self.values[index] = value


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tetrahedral_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("580x100")

        self.entry000 = tk.Entry(self.window, width=6)
        self.entry000.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        label = tk.Label(self.window, width=3)
        label.grid(row=0, column=1, sticky=tk.W)

        self.entry100 = tk.Entry(self.window, width=6)
        self.entry100.grid(padx=5, pady=2, row=0, column=2, sticky=tk.W)
        self.entry110 = tk.Entry(self.window, width=6)
        self.entry110.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        self.entry111 = tk.Entry(self.window, width=6)
        self.entry111.grid(padx=2, pady=2, row=1, column=3, sticky=tk.W)
        label = tk.Label(self.window, width=3)
        label.grid(row=0, column=4, sticky=tk.W)

        self.entry200 = tk.Entry(self.window, width=6)
        self.entry200.grid(padx=5, pady=2, row=0, column=5, sticky=tk.W)
        self.entry210 = tk.Entry(self.window, width=6)
        self.entry210.grid(padx=5, pady=2, row=1, column=5, sticky=tk.W)
        self.entry220 = tk.Entry(self.window, width=6)
        self.entry220.grid(padx=5, pady=2, row=2, column=5, sticky=tk.W)
        self.entry211 = tk.Entry(self.window, width=6)
        self.entry211.grid(padx=5, pady=2, row=1, column=6, sticky=tk.W)
        self.entry221 = tk.Entry(self.window, width=6)
        self.entry221.grid(padx=5, pady=2, row=2, column=6, sticky=tk.W)
        self.entry222 = tk.Entry(self.window, width=6)
        self.entry222.grid(padx=5, pady=2, row=2, column=7, sticky=tk.W)
        label = tk.Label(self.window, width=3)
        label.grid(row=0, column=8, sticky=tk.W)

        self.entry300 = tk.Entry(self.window, width=6)
        self.entry300.grid(padx=5, pady=2, row=0, column=9, sticky=tk.W)
        self.entry310 = tk.Entry(self.window, width=6)
        self.entry310.grid(padx=5, pady=2, row=1, column=9, sticky=tk.W)
        self.entry320 = tk.Entry(self.window, width=6)
        self.entry320.grid(padx=5, pady=2, row=2, column=9, sticky=tk.W)
        self.entry330 = tk.Entry(self.window, width=6)
        self.entry330.grid(padx=5, pady=2, row=3, column=9, sticky=tk.W)
        self.entry311 = tk.Entry(self.window, width=6)
        self.entry311.grid(padx=5, pady=2, row=1, column=10, sticky=tk.W)
        self.entry321 = tk.Entry(self.window, width=6)
        self.entry321.grid(padx=5, pady=2, row=2, column=10, sticky=tk.W)
        self.entry331 = tk.Entry(self.window, width=6)
        self.entry331.grid(padx=5, pady=2, row=3, column=10, sticky=tk.W)
        self.entry322 = tk.Entry(self.window, width=6)
        self.entry322.grid(padx=5, pady=2, row=2, column=11, sticky=tk.W)
        self.entry332 = tk.Entry(self.window, width=6)
        self.entry332.grid(padx=5, pady=2, row=3, column=11, sticky=tk.W)
        self.entry333 = tk.Entry(self.window, width=6)
        self.entry333.grid(padx=5, pady=2, row=3, column=12, sticky=tk.W)

        # Demonstrate a tetrahedral array.
        num_rows = 4

        # Make a tetrahedral array.
        tet_array = TetrahedralArray(num_rows)
        for row in range(num_rows):
            for col in range(row + 1):
                for hgt in range(col + 1):
                    tet_array[(row, col, hgt)] = f"({row},{col},{hgt})"

        # Display the values.
        self.entry000.insert(0, tet_array[(0, 0, 0)])

        self.entry100.insert(0, tet_array[(1, 0, 0)])
        self.entry110.insert(0, tet_array[(1, 1, 0)])
        self.entry111.insert(0, tet_array[(1, 1, 1)])

        self.entry200.insert(0, tet_array[(2, 0, 0)])
        self.entry210.insert(0, tet_array[(2, 1, 0)])
        self.entry220.insert(0, tet_array[(2, 2, 0)])
        self.entry211.insert(0, tet_array[(2, 1, 1)])
        self.entry221.insert(0, tet_array[(2, 2, 1)])
        self.entry222.insert(0, tet_array[(2, 2, 2)])

        self.entry300.insert(0, tet_array[(3, 0, 0)])
        self.entry310.insert(0, tet_array[(3, 1, 0)])
        self.entry320.insert(0, tet_array[(3, 2, 0)])
        self.entry330.insert(0, tet_array[(3, 3, 0)])
        self.entry311.insert(0, tet_array[(3, 1, 1)])
        self.entry321.insert(0, tet_array[(3, 2, 1)])
        self.entry331.insert(0, tet_array[(3, 3, 1)])
        self.entry322.insert(0, tet_array[(3, 2, 2)])
        self.entry332.insert(0, tet_array[(3, 3, 2)])
        self.entry333.insert(0, tet_array[(3, 3, 3)])

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.entry000.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
