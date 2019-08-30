import tkinter as tk
import re

class LetterCell:
    """Store an item for a linked list."""
    def __init__(self, letter, next):
        self.letter = letter
        self.next = next

    def insert_after(self, letter):
        """ Insert a new cell after this one."""
        cell = LetterCell(letter, self.next)
        self.next = cell

    @staticmethod
    def from_string(txt):
        """ Return a list that represents a string."""
        # Create the sentinels.
        top_sentinel = LetterCell("<sentinel>", None)

        # Make it into a list.
        first_cell = top_sentinel
        for ch in txt:
            first_cell.insert_after(ch)
            first_cell = first_cell.next

        # Return the top sentinel.
        return top_sentinel

    def __str__(self):
        return f"{self.letter}"

    def to_string(self):
        txt = ""
        while self != None:
            txt += self.letter
            self = self.next
        return txt

    def is_palindrome_reverse(self):
        """
        Use a reversed list to return True if the
        cells after this one form a palindrome.
        """
        # Make a reversed list.
        new_top = None
        old_cell = self
        while old_cell != None:
            new_cell = LetterCell(old_cell.letter, new_top)
            new_top = new_cell
            old_cell = old_cell.next

        # Compare the lists.
        cell1 = self
        cell2 = new_top
        while cell1 != None:
            if cell1.letter != cell2.letter:
                return False
            cell1 = cell1.next
            cell2 = cell2.next

        return True

    def is_palindrome_reverse_half(self):
        """
        Use half a reversed list to return True if the
        cells after this one form a palindrome.
        """
        # Lists with 0 or 1 letters are palindromes.
        if (self.next == None) or (self.next.next == None):
            return True

        # Find the list's halfway point.
        second_half = self.find_second_half(False)

        # Make a reversed list.
        last_cell = None
        old_cell = second_half
        while old_cell != None:
            new_cell = LetterCell(old_cell.letter, last_cell)
            last_cell = new_cell
            old_cell = old_cell.next

        # Compare the lists.
        cell1 = last_cell
        cell2 = self
        while cell1 != None:
            if cell1.letter != cell2.letter:
                return False
            cell1 = cell1.next
            cell2 = cell2.next
        return True

    def find_second_half(self, count_middle_cell):
        """
        Return the first cell in the second half of the list.
        If the list has an odd number of cells and
        count_middle_cell is True, return the middle cell.
        If the list has an odd number of cells and
        count_middle_cell is False, return the cell after the middle.
        """
        # Find the list's halfway point.
        slow_cell = self
        fast_cell = slow_cell
        while True:
            # Move slow_cell.
            slow_cell = slow_cell.next

            # Move fast_cell.
            fast_cell = fast_cell.next
            if fast_cell == None:
                # The list has an even number of items and
                # slow_cell is the first cell in the second half.
                return slow_cell

            fast_cell = fast_cell.next
            if fast_cell == None:
                # The list has an odd number of items
                # and slow_cell is the middle item.
                if not count_middle_cell:
                    slow_cell = slow_cell.next
                return slow_cell

    def is_palindrome_recurse(self):
        """
        Recursively see if the
        cells after this one form a palindrome.
        """
        # Find the start of the second half.
        second_half = self.find_second_half(False)

        # Recursively compare the second and first halves.
        first_half = self
        result, first_half = self.compare_halves(first_half, second_half)
        return result

    def compare_halves(self, first_half, second_half):
        """
        Recursively compare the second and first halves.
        Return a True/False result and an updated value for first_half.
        """

        # See if we're at the end of the second half.
        if second_half.next == None:
            # Compare the last cell in the second half
            # to the first cell in the first half.
            our_result = (second_half.letter == first_half.letter)

            # Move first_half to the next item.
            first_half = first_half.next

            # Return so the next level up can continue checking.
            return our_result, first_half

        # We are not at the end of the second half.
        # Recursively check one cell farther in the second half.
        # If the recursive call returns False,
        # this is not a palindrome.
        our_result, first_half = self.compare_halves(first_half, second_half.next)
        if not our_result:
            return False, None

        # Compare the next cells in the two halves.
        if first_half.letter != second_half.letter:
            return False, None

        # If we get this far, it is a palindrome so far.
        # Move first_half to the next item.
        first_half = first_half.next

        # So far so good.
        return True, first_half

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("list_second_half")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x140")

        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=10, fill=tk.BOTH)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(frame, text="String:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.string_entry = tk.Entry(frame)
        self.string_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.string_entry.insert(0, "ABCDEFG")

        go_button = tk.Button(frame, text="Go", width=8, command=self.go)
        go_button.grid(row=1, column=0, columnspan=2, pady=10)

        label = tk.Label(frame, text="W/o Middle:")
        label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        self.wo_middle_entry = tk.Entry(frame)
        self.wo_middle_entry.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        label = tk.Label(frame, text="W/Middle:")
        label.grid(row=3, column=0, padx=5, pady=2, sticky=tk.W)
        self.w_middle_entry = tk.Entry(frame)
        self.w_middle_entry.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.string_entry.focus_force()
        self.window.mainloop()

    def go(self):
        """ Display the second halves of the text."""
        self.wo_middle_entry.delete(0, tk.END)
        self.w_middle_entry.delete(0, tk.END)

        # Make the string into a list.
        txt = self.string_entry.get().upper()
        regex = re.compile("[^A-Z]")
        txt = regex.sub("", txt)
        top_sentinel = LetterCell.from_string(txt)
        if top_sentinel.next.next == None:
            return

        # Get the second halves.
        half = top_sentinel.find_second_half(False)
        self.wo_middle_entry.insert(0, half.to_string())

        half = top_sentinel.find_second_half(True)
        self.w_middle_entry.insert(0, half.to_string())


if __name__ == '__main__':
    app = App()

# app.root.destroy()
