import tkinter as tk
import re
from tkinter import messagebox

class Cell:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def copy_list(self):
        """ Copy a list."""
        # Make the new list's sentinel.
        new_sentinel = Cell(self.value, None)

        # Keep track of the last item we've added so far.
        last_added = new_sentinel

        # Copy items.
        old_cell = self.next
        while old_cell != None:
            last_added.next = Cell(old_cell.value, None)
            last_added = last_added.next
            old_cell = old_cell.next

        # Return the new list's sentinel.
        return new_sentinel

    def insertionsort(self):
        """ Use insertionsort to sort the list."""
        # Make a sentinel for the sorted list.
        sentinel = Cell(float("-inf"), None)

        # Skip the input list's sentinel.
        self = self.next

        # Repeat until we have inserted all of the items in the new list.
        while self != None:
            # Get the next cell to add to the list.
            next_cell = self

            # Move self to self.next for the next trip through the loop.
            self = self.next

            # See where to add the next item in the sorted list.
            after_me = sentinel
            while (after_me.next != None) and (after_me.next.value < next_cell.value):
                after_me = after_me.next

            # Insert the item in the sorted list.
            next_cell.next = after_me.next
            after_me.next = next_cell

        # Return the sorted list.
        return sentinel

    def selectionsort(self):
        """ Use selectionsort to sort the list."""
        # Make a sentinel for the sorted list.
        sentinel = Cell(float("-inf"), None)

        # Repeat until the input list is empty.
        while self.next != None:
            # Find the largest item in the input list.
            # The cell after_me will be the cell before
            # the one with the largest value.
            best_after_me = self
            best_value = best_after_me.next.value

            # Start looking with the next item.
            after_me = self.next
            while after_me.next != None:
                if after_me.next.value > best_value:
                    best_after_me = after_me
                    best_value = after_me.next.value
                after_me = after_me.next

            # Remove the best cell from the unsorted list.
            best_cell = best_after_me.next
            best_after_me.next = best_cell.next

            # Add the best cell at the beginning of the sorted list.
            best_cell.next = sentinel.next
            sentinel.next = best_cell

        # Return the sorted list.
        return sentinel

    def verify_sorted(self):
        """ Verify that this list is sorted, after the sentinel."""
        # If the list has 1 item, then it's sorted.
        self.next = self.next
        if self.next == None:
            return True

        # Compare the other items.
        next_cell = self.next
        while next_cell != None:
            assert self.value <= next_cell.value, f"List not sorted: {self.value} is greater than {next_cell.value}"
            self = next_cell
            next_cell = next_cell.next


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("linked_list_insertionsort")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("430x350")

        frame = tk.Frame(self.window)
        frame.pack(padx=0, pady=5, fill=tk.BOTH, expand=True)
        frame.rowconfigure(1, weight=1)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)

        button = tk.Button(frame, text="Randomize", width=10, command=self.randomize)
        button.grid(row=0, column=0, padx=5, pady=2)
        button = tk.Button(frame, text="Insertionsort", width=10, command=self.insertionsort)
        button.grid(row=0, column=1, padx=5, pady=2)
        button = tk.Button(frame, text="Selectionsort", width=10, command=self.selectionsort)
        button.grid(row=0, column=2, padx=5, pady=2)

        frame2 = tk.Frame(frame)
        frame2.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(frame2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.unsorted_listbox = tk.Listbox(frame2)
        self.unsorted_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.unsorted_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.unsorted_listbox.yview)

        frame2 = tk.Frame(frame)
        frame2.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(frame2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.insertionsort_listbox = tk.Listbox(frame2)
        self.insertionsort_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.insertionsort_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.insertionsort_listbox.yview)

        frame2 = tk.Frame(frame)
        frame2.grid(row=1, column=2, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(frame2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.selectionsort_listbox = tk.Listbox(frame2)
        self.selectionsort_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.selectionsort_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.selectionsort_listbox.yview)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def randomize(self):
        """ Make some random items."""

        # Add random items.
        num_items = 100
        top = None
        for i in range(num_items):
            new_cell = Cell(random.randint(10000, 99999), top)
            top = new_cell
        self.unsorted_sentinel = Cell(float("-inf"), top)

        # Display the items.
        self.display_list(self.unsorted_sentinel, self.unsorted_listbox)

        self.insertionsort_listbox.delete(0, tk.END)
        self.selectionsort_listbox.delete(0, tk.END)

    def insertionsort(self):
        """ Use insertionsort to sort the items."""
        # Copy the unsorted list so we don't destroy it.
        copy = self.unsorted_sentinel.copy_list()

        # Sort the items.
        sorted = copy.insertionsort()

        # Verify the sort.
        sorted.verify_sorted()

        # Display the sorted items.
        self.display_list(sorted, self.insertionsort_listbox)

    def selectionsort(self):
        """ Use selectionsort to sort the items."""
        # Copy the unsorted list so we don't destroy it.
        copy = self.unsorted_sentinel.copy_list()

        # Sort the items.
        sorted = copy.selectionsort()

        # Verify the sort.
        sorted.verify_sorted()

        # Display the sorted items.
        self.display_list(sorted, self.selectionsort_listbox)

    def display_list(self, sentinel, listbox):
        """ Display the list in the indicated ListBox."""
        # Display the list.
        listbox.delete(0, tk.END)
        cell = sentinel.next
        while cell != None:
            listbox.insert(tk.END, cell.value)
            cell = cell.next


if __name__ == '__main__':
    app = App()

# app.root.destroy()
