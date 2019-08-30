import random
import tkinter as tk
import tkinter.font as tk_font


class ArrayRow:
    """ Holds data to represnet a row."""
    def __init__(self, row_number, next_row, row_sentinel):
        self.row_number = row_number
        self.next_row = next_row
        self.row_sentinel = row_sentinel


class ArrayEntry:
    """ Holds data for an array entry."""
    def __init__(self, column_number, value, next_entry):
        self.column_number = column_number
        self.value = value
        self.next_entry = next_entry


class SparseArray:
    def __init__(self, default_value):
        """ Create the sentinels."""
        # Save the default value.
        self.default_value = default_value

        # Create the row sentinel.
        self.top_sentinel = ArrayRow(float("-inf"), None, None)

    def __getitem__(self, rc):
        """ Get a value."""
        r, c = rc

        # Find the entry.
        entry = self.find_entry(r, c, False)

        # If we didn't find it, return the default value.
        if entry == None:
            return self.default_value

        # Return the entry's value.
        return entry.value

    def __setitem__(self, rc, value):
        """ Set a value."""
        r, c = rc

        # See if this is the default value.
        if value == self.default_value:
            # Remove the entry from the array.
            self.delete_entry(r, c)
        else:
            # Save the new value.
            # Find the entry, creating it if necessary.
            entry = self.find_entry(r, c, True)

            # Save the value.
            entry.value = value

    def find_row_before(self, row):
        """ Find the ArrayRow before this row."""
        # Start at the sentinel.
        array_row = self.top_sentinel

        # Find the row before the required one.
        while (array_row.next_row != None) and (array_row.next_row.row_number < row):
            array_row = array_row.next_row

        # Return the ArrayRow before the row or None.
        return array_row

    def find_row(self, row, create):
        """
        Find the ArrayRow for this row.
        If create is True, create the ArrayRow if it doesn't exist.
        """
        # Find the ArrayRow before the one we want.
        before = self.find_row_before(row)

        # If we found it, return it.
        if (before.next_row != None) and (before.next_row.row_number == row):
            return before.next_row

        # We didn't find it. See if we should create it.
        if create:
            # Create the new row's sentinel.
            row_sentinel = ArrayEntry(float("-inf"), None, None)

            # Create the new ArrayRow.
            new_row = ArrayRow(row, before.next_row, row_sentinel)

            # Insert it in the row list.
            before.next_row = new_row

            # Return it.
            return new_row

        # We didn't find it and shouldn't create it. Return None.
        return None

    def find_column_before(self, entry, col):
        """ Find the ArrayEntry for this column."""
        # Find the entry before the required one.
        while (entry.next_entry != None) and (entry.next_entry.column_number < col):
            entry = entry.next_entry

        # Return the ArrayRow before the entry or None.
        return entry

    def find_column(self, entry, col, create):
        """
        Find the ArrayEntry for this column.
        If create is True, create the ArrayEntry if it doesn't exist.
        """
        # Find the entry before the required one.
        before = self.find_column_before(entry, col)

        # If we found it, return it.
        if (before.next_entry != None) and (before.next_entry.column_number == col):
            return before.next_entry

        # We didn't find it. See if we should create it.
        if create:
            # Create the new ArrayEntry.
            new_entry = ArrayEntry(col, None, before.next_entry)

            # Insert it in the row's column list.
            before.next_entry = new_entry

            # Return it.
            return new_entry

        # We didn't find it and shouldn't create it. Return None.
        return None

    def find_entry(self, row, col, create):
        """
        Find the ArrayEntry for this row and column.
        If create is True, create the ArrayEntry if it doesn't exist.
        """
        # Find the entry's row.
        array_row = self.find_row(row, create)

        # If we didn't find it (or create it), return None.
        if array_row == None:
            return None

        # Find the entry in this row and return it.
        return self.find_column(array_row.row_sentinel, col, create)

    def delete_entry(self, row, col):
        """ Delete the indicated entry if it exists."""
        # Find the row before the entry's row.
        row_before = self.find_row_before(row)

        # If we didn't find the row, we're done.
        array_row = row_before.next_row
        if (array_row == None) or (array_row.row_number != row):
            return

        # Find the entry before this entry's entry.
        entry_before = self.find_column_before(array_row.row_sentinel, col)
        array_entry = entry_before.next_entry

        # If we didn't find the entry, we're done.
        if (array_entry == None) or (array_entry.column_number != col):
            return

        # Remove the entry from the row's list.
        entry_before.next_entry = array_entry.next_entry

        # If there are no more entries in the row, remove it.
        array_sentinel = array_row.row_sentinel
        if array_sentinel.next_entry == None:
            row_before.next_row = array_row.next_row

    def list(self, listbox):
        """ Display the array's entries in a Listbox."""
        row = self.top_sentinel.next_row
        while row != None:
            value = row.row_sentinel.next_entry
            while value != None:
                listbox.insert(tk.END, f"({row.row_number}, {value.column_number}): {value.value}")
                value = value.next_entry
            row = row.next_row


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make a SparseArray.
        self.array = SparseArray("---")

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("sparse_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("230x370")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="Row:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.row_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.row_entry.grid(padx=5, pady=2, row=0, column=1)
        get_button = tk.Button(frame, width=10, text="Get", command=self.get)
        get_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Column:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.column_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.column_entry.grid(padx=5, pady=2, row=1, column=1)
        set_button = tk.Button(frame, width=10, text="Set", command=self.set)
        set_button.grid(padx=5, pady=2, row=1, column=2)

        label = tk.Label(frame, text="Value:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.value_entry.grid(padx=5, pady=2, row=2, column=1)
        clear_button = tk.Button(frame, width=10, text="Clear", command=self.clear)
        clear_button.grid(padx=5, pady=2, row=2, column=2)

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.row_entry.focus_force()
        self.window.mainloop()

    def get(self):
        """ Get a value."""
        r = int(self.row_entry.get())
        c = int(self.column_entry.get())
        value = self.array[(r, c)]
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, value)

    def set(self):
        """ Set a value."""
        r = int(self.row_entry.get())
        c = int(self.column_entry.get())
        value = self.value_entry.get()
        self.array[(r, c)] = value
        self.show_array()

    def clear(self):
        """ Clear a value."""
        r = int(self.row_entry.get())
        c = int(self.column_entry.get())
        self.array[(r, c)] = self.array.default_value
        self.show_array()

    def show_array(self):
        """ Display the array."""
        self.listbox.delete(0, tk.END)
        self.array.list(self.listbox)


if __name__ == '__main__':
    app = App()
