import tkinter as tk
from tkinter import messagebox
import time

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
        self.window.title("linked_sorts")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x350")

        frame = tk.Frame(self.window)
        frame.pack(padx=0, pady=5)

        label = tk.Label(frame, text="# Items:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.num_items_entry.grid(row=0, column=1, padx=5, pady=2)
        self.num_items_entry.insert(0, "2000")

        label = tk.Label(frame, text="Minimum:")
        label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.minimum_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.minimum_entry.grid(row=1, column=1, padx=5, pady=2)
        self.minimum_entry.insert(0, "100000000")
        button = tk.Button(frame, text="Make Items", width=15, command=self.make_items)
        button.grid(row=1, column=2, padx=5, pady=2)

        label = tk.Label(frame, text="Maximum:")
        label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)
        self.maximum_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.maximum_entry.grid(row=2, column=1, padx=5, pady=2)
        self.maximum_entry.insert(0, "999999999")

        frame = tk.Frame(self.window)
        frame.pack(padx=0, pady=5, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.items_listbox = tk.Listbox(frame)
        self.items_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.items_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.items_listbox.yview)

        frame = tk.Frame(self.window)
        frame.pack(padx=0, pady=5)
        button = tk.Button(frame, text="Reset", width=15, command=self.reset)
        button.grid(row=4, column=0, padx=5, pady=2)
        button = tk.Button(frame, text="Selectionsort", width=15, command=self.selectionsort)
        button.grid(row=4, column=1, padx=5, pady=2)
        button = tk.Button(frame, text="Insertionsort", width=15, command=self.insertionsort)
        button.grid(row=4, column=2, padx=5, pady=2)

        frame = tk.Frame(self.window)
        frame.pack(padx=0, pady=5)
        label = tk.Label(frame, text="Time:")
        label.grid(row=5, column=0, padx=5, pady=2, sticky=tk.W)
        self.time_label = tk.Label(frame)
        self.time_label.grid(row=5, column=1, padx=5, pady=2, sticky=tk.W)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_items_entry.focus_force()
        self.window.mainloop()

    def reset(self):
        """ Reset the list to the original unsorted values."""
        # Display the items.
        self.display_list(self.unsorted_sentinel, self.items_listbox)
        self.time_label["text"] = ""

    def make_items(self):
        """ Make some random items."""

        # Add random items.
        num_items = int(self.num_items_entry.get())
        minimum = int(self.minimum_entry.get())
        maximum = int(self.maximum_entry.get())
        top = None
        for i in range(num_items):
            new_cell = Cell(random.randint(minimum, maximum), top)
            top = new_cell
        self.unsorted_sentinel = Cell(float("-inf"), top)

        # Display the items.
        self.display_list(self.unsorted_sentinel, self.items_listbox)
        self.time_label["text"] = ""

    def insertionsort(self):
        """ Use insertionsort to sort the items."""
        # Copy the unsorted list so we don't destroy it.
        copy = self.unsorted_sentinel.copy_list()

        # Sort the items.
        start_time = time.time()
        sorted = copy.insertionsort()
        elapsed_time = time.time() - start_time

        # Verify the sort.
        sorted.verify_sorted()

        # Display the sorted items and time.
        self.display_list(sorted, self.items_listbox)
        self.time_label["text"] = f"{elapsed_time:.2f} seconds"

    def selectionsort(self):
        """ Use selectionsort to sort the items."""
        # Copy the unsorted list so we don't destroy it.
        copy = self.unsorted_sentinel.copy_list()

        # Sort the items.
        start_time = time.time()
        sorted = copy.selectionsort()
        elapsed_time = time.time() - start_time

        # Verify the sort.
        sorted.verify_sorted()

        # Display the sorted items and time.
        self.display_list(sorted, self.items_listbox)
        self.time_label["text"] = f"{elapsed_time:.2f} seconds"

    def display_list(self, sentinel, listbox):
        """ Display the list in the indicated ListBox."""
        # Display the list.
        listbox.delete(0, tk.END)
        count = 0
        cell = sentinel.next
        while cell != None:
            listbox.insert(tk.END, cell.value)
            cell = cell.next
            count += 1
            if count > 1000:
                break


if __name__ == '__main__':
    app = App()

# app.root.destroy()
