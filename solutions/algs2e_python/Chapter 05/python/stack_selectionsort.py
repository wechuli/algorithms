import random
import tkinter as tk
from tkinter import ttk


def sort_stack(values):
    # Make the temporary stack.
    temp = []

    # Sort.
    num_items = len(values)
    num_sorted = 0
    num_unsorted = num_items
    for i in range(num_items):
        # Find the item that belongs in sorted position i.

        # Pull the first item off the stack.
        # Assume it will be the biggest item considered.
        biggest = values.pop()

        # Move the other unsorted items into the
        # temporary stack, keeping track of the biggest.
        for j in range(num_unsorted - 1):
            test_item = values.pop()
            if test_item < biggest:
                # This item is bigger. Move the old biggest item to
                # the temporary stack and replace it with this item.
                temp.append(biggest)
                biggest = test_item
            else:
                # This item is not bigger. Just move it
                # to the temporary stack.
                temp.append(test_item)

        # Add the biggest item to the end of the queue.
        values.append(biggest)

        # Move the unsorted items back into the original stack.
        while len(temp) > 0:
            values.append(temp.pop())

        # Update the counts.
        num_sorted += 1
        num_unsorted -= 1


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("stack_selectionsort")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("260x350")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="# Items:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.num_items_entry.grid(padx=5, pady=2, row=0, column=1)
        self.num_items_entry.insert(0, "100")
        make_items_button = tk.Button(frame, width=10, text="Make Items", command=self.make_items)
        make_items_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Minimum:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.min_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.min_entry.grid(padx=5, pady=2, row=1, column=1)
        self.min_entry.insert(0, "1000")
        sort_button = tk.Button(frame, width=10, text="Sort", command=self.sort)
        sort_button.grid(padx=5, pady=2, row=1, column=2)

        label = tk.Label(frame, text="Maximum:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.max_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.max_entry.grid(padx=5, pady=2, row=2, column=1)
        self.max_entry.insert(0, "9999")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(padx=(0,5), pady=5, side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=make_items_button: make_items_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_items_entry.focus_force()
        self.window.mainloop()

    def make_items(self):
        """ Make random items."""
        num_items = int(self.num_items_entry.get())
        minimum = int(self.min_entry.get())
        maximum = int(self.max_entry.get())
        self.values = []
        for i in range(num_items):
            self.values.append(random.randint(minimum, maximum))
        self.display_items()

    def display_items(self):
        self.listbox.delete(0, tk.END)
        for value in self.values:
            self.listbox.insert(tk.END, value)

    def sort(self):
        """ Sort the items."""
        sort_stack(self.values)

        # Verify the sort.
        for i in range(1, len(self.values)):
            assert self.values[i - 1] <= self.values[i], \
                f"value[{i - 1}] = {self.values[i - 1]} is greater than value[{i}] = {self.values[i]}"

        # Display the sorted items.
        self.display_items()



if __name__ == '__main__':
    app = App()

