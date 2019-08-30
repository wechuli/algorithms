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

    def copy_entries(self, from_entry, to_entry):
        """
        Copy the entries starting at from_entry into
        the destination entry list after to_entry.
        """
        while from_entry != None:
            to_entry.next_entry = ArrayEntry(from_entry.column_number, from_entry.value, None)
            to_entry = to_entry.next_entry

            # Move to the next entry.
            from_entry = from_entry.next_entry

    def add_entries(self, from_entry1, from_entry2, to_entry):
        """
        Add the entries in the two lists from_entry1 and from_entry2
        and save the sums in the destination entry list after to_entry.
        """
        # Repeat as long as either from list has items.
        while (from_entry1 != None) and (from_entry2 != None):
            # Make the new result entry.
            # See which column number is smaller.
            if from_entry1.column_number < from_entry2.column_number:
                # Copy the from_entry1 entry.
                to_entry.next_entry = ArrayEntry(from_entry1.column_number, from_entry1.value, None)
                from_entry1 = from_entry1.next_entry
            elif from_entry2.column_number < from_entry1.column_number:
                # Copy the from_entry2 entry.
                to_entry.next_entry = ArrayEntry(from_entry2.column_number, from_entry2.value, None)
                from_entry2 = from_entry2.next_entry
            else:
                # The column numbers are the same. Add both entries.
                to_entry.next_entry = ArrayEntry(from_entry1.column_number, \
                    from_entry1.value + from_entry2.value, None)
                from_entry1 = from_entry1.next_entry
                from_entry2 = from_entry2.next_entry

            to_entry = to_entry.next_entry

        # Add the rest of the entries from the list that is not empty.
        if from_entry1 != None:
            self.copy_entries(from_entry1, to_entry)
        if from_entry2 != None:
            self.copy_entries(from_entry2, to_entry)

    def add(self, other):
        """ Add two SparseArrays representing matrices."""
        result = SparseArray(self.default_value)

        # Variables to move through all of the arrays.
        array1_row = self.top_sentinel.next_row
        array2_row = other.top_sentinel.next_row
        result_row = result.top_sentinel

        while (array1_row != None) and (array2_row != None):
            row_sentinel = ArrayEntry(float("-inf"), None, None)

            # See which input row has the smaller row number.
            if array1_row.row_number < array2_row.row_number:
                # array1_row comes first. Copy its values into result.
                result_row.next_row = ArrayRow(array1_row.row_number, None, row_sentinel)
                result_row = result_row.next_row
                self.copy_entries(array1_row.row_sentinel.next_entry, result_row.row_sentinel)
                array1_row = array1_row.next_row
            elif array2_row.row_number < array1_row.row_number:
                # array2_row comes first. Copy its values into result.
                result_row.next_row = ArrayRow(array2_row.row_number, None, row_sentinel)
                result_row = result_row.next_row
                self.copy_entries(array2_row.row_sentine2.next_entry, result_row.row_sentinel)
                array2_row = array2_row.next_row
            else:
                # The row numbers are the same. Add their values.
                result_row.next_row = ArrayRow(array1_row.row_number, None, row_sentinel)
                result_row = result_row.next_row
                self.add_entries( \
                    array1_row.row_sentinel.next_entry, \
                    array2_row.row_sentinel.next_entry, \
                    result_row.row_sentinel)
                array1_row = array1_row.next_row
                array2_row = array2_row.next_row

        # Add any remaining rows.
        while array1_row != None:
            # Make a new result row.
            row_sentinel = ArrayEntry(float("-inf"), None, None)
            result_row.next_row = ArrayRow(array1_row.row_number, None, row_sentinel)
            result_row = result_row.next_row
            self.copy_entries(array1_row.row_sentinel.next_entry, result_row.row_sentinel)
            array1_row = array1_row.next_row
        while array2_row != None:
            # Make a new result row.
            row_sentinel = ArrayEntry(float("-inf"), None, None)
            result_row.next_row = ArrayRow(array2_row.row_number, None, row_sentinel)
            result_row = result_row.next_row
            self.copy_entries(array2_row.row_sentinel.next_entry, result_row.row_sentinel)
            array2_row = array2_row.next_row

        return result


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("add_sparse_arrays")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("200x370")

        result_listbox = tk.Listbox(self.window)
        result_listbox.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Make some sparse arrays.
        array1 = SparseArray(0)
        array1[(1, 1)] = 101
        array1[(-1, -1)] = -101
        array1[(3, 3)] = 303
        array1[(2, 4)] = 204
        array1[(4, 1)] = 401

        array2 = SparseArray(0)
        array2[(1, 0)] = 100
        array2[(3, 3)] = 303
        array2[(1, 4)] = 104
        array2[(4, 1)] = 401
        array2[(10, 10)] = 1010
        array2[(11, 11)] = 1111

        # Add them.
        array3 = array1.add(array2)

        # Display the arrays.
        array1.list(result_listbox)
        result_listbox.insert(tk.END, "")
        array2.list(result_listbox)
        result_listbox.insert(tk.END, "")
        array3.list(result_listbox)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()
