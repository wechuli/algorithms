import tkinter as tk
import re

class LetterCell:
    """Store an item for a linked list."""
    def __init__(self, letter, next, prev):
        self.letter = letter
        self.next = next
        self.prev = prev

    def insert_after(self, letter):
        """ Insert a new cell after this one."""
        cell = LetterCell(letter, self.next, self)
        self.next = cell
        cell.next.prev = cell

    @staticmethod
    def from_string(txt):
        """ Return a list that represents a string."""
        # Create the sentinels.
        bottom_sentinel = LetterCell("<sentinel>", None, None)
        top_sentinel = LetterCell("<sentinel>", bottom_sentinel, None)
        bottom_sentinel.prev = top_sentinel

        # Make it into a list.
        first_cell = bottom_sentinel
        for ch in txt:
            top_sentinel.insert_after(ch)

        # Return the top sentinel.
        return top_sentinel

    def __str__(self):
        return f"{self.letter}"

    def is_list_palindrome(self):
        """ Return True if the cells after this one form a palindrome."""
        # Check each cell for a palindrome.
        cell = self.next
        while cell != None:
            if cell.is_palindrome_at_cell():
                return True
            cell = cell.next
        return False

    def is_palindrome_at_cell(self):
        """ Return True if the cells before and after this one form a palindrome."""
        return self.is_even_palindrome_at_cell() or self.is_odd_palindrome_at_cell()

    def is_even_palindrome_at_cell(self):
        """
        Return True if the cells before and after this
        one form a palindrome of odd length.
        """
        # Go forward and backward comparing letters.
        next = self
        prev = self
        while (next != None) and (prev != None):
            if (next.letter != prev.letter):
                return False
            next = next.next
            prev = prev.prev
        if (next != None) or (prev != None):
            return False
        return True

    def is_odd_palindrome_at_cell(self):
        """
        Return True if the cells before this one and this
        one to the end one form a palindrome of even length.
        """
        # Go forward and backward comparing letters.
        next = self
        prev = self.prev
        while (next != None) and (prev != None):
            if (next.letter != prev.letter):
                return False
            next = next.next
            prev = prev.prev
        if (next != None) or (prev != None):
            return False
        return True


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("doubly_linked_list_palindrome")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x120")

        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=10, fill=tk.BOTH)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(frame, text="String:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.string_entry = tk.Entry(frame)
        self.string_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.string_entry.insert(0, "Drab as a fool, aloof as a bard")

        check_button = tk.Button(frame, text="Check", width=8, command=self.check)
        check_button.grid(row=1, column=0, columnspan=2, pady=10)

        label = tk.Label(frame, text="At Cell:")
        label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        self.at_cell_entry = tk.Entry(frame)
        self.at_cell_entry.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=check_button: check_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def check(self):
        """ See if the string is a palindrome."""
        # Make the string into a list.
        txt = self.string_entry.get().upper()
        regex = re.compile("[^A-Z]")
        txt = regex.sub("", txt)
        top_sentinel = LetterCell.from_string(txt)

        # Check for a palindrome in various ways.
        self.at_cell_entry.delete(0, tk.END)
        if top_sentinel.next.is_list_palindrome():
            self.at_cell_entry.insert(0, "Is a palindrome")
        else:
            self.at_cell_entry.insert(0, "Not a palindrome")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
