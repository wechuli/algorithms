import tkinter as tk


class TriangularArray:
    def __init__(self, num_rows):
        """ Initialize the array by allocating the values array."""
        self.num_rows = num_rows

        # Make the linear array where we store items.
        num_items = self.num_cells_for_rows(self.num_rows)
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

    def to_string(self):
        """ Return a textual representation of the array."""
        result = ""
        for row in range(self.num_rows):
            for col in range(row + 1):
                result += f"{self[(row, col)]} "
            result += "\n"
        return result

    def times_full(self, other):
        """ Multiply this array on the right by another array."""
        result = TriangularArray(self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_rows):
                # Calculate the [i, j] entry.
                total = 0
                for k in range(self.num_rows):
                    if (i >= k) and (k >= j):
                        total += self[(i, k)] * other[(k, j)]
                result[(i, j)] = total
        return result

    def times(self, other):
        """ Multiply this array on the right by another array."""
        result = TriangularArray(self.num_rows)
        for i in range(self.num_rows):
            for j in range(self.num_rows):
                # Calculate the [i, j] entry.
                total = 0
                for k in range(j, i + 1):
                    total += self[(i, k)] * other[(k, j)]
                result[(i, j)] = total
        return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("multiply_triangular_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x300")

        self.text = tk.Text(self.window)
        self.text.pack(padx=5, pady=5, fill=tk.BOTH)

        # Make two triangular arrays.
        num_rows = 3
        array1 = TriangularArray(num_rows)
        array1[0, 0] = 1
        array1[1, 0] = 2
        array1[1, 1] = 3
        array1[2, 0] = 4
        array1[2, 1] = 5
        array1[2, 2] = 6

        array2 = TriangularArray(num_rows)
        array2[0, 0] = 10
        array2[1, 0] = 20
        array2[1, 1] = 30
        array2[2, 0] = 40
        array2[2, 1] = 50
        array2[2, 2] = 60

        array3 = array1.times_full(array2)
        array4 = array1.times(array2)

        self.text.insert(tk.END, array1.to_string() + "\n")
        self.text.insert(tk.END, array2.to_string() + "\n")
        self.text.insert(tk.END, array3.to_string() + "\n")
        self.text.insert(tk.END, array4.to_string())

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.text.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
