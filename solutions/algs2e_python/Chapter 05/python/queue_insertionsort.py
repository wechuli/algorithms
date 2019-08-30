import random
import tkinter as tk
from tkinter import ttk


def sort_stack(values):
    num_items = len(values)

    # Initially consider the last item in the queue to be sorted.
    num_sorted = 1
    num_unsorted = num_items - 1

    for i in range(num_items - 1):
        # Take the next item and position it.
        # Pull the first item off the queue.
        next_item = values.pop(0)    # Dequeue

        # Pull the other unsorted items off the queue.
        for j in range(num_unsorted - 1):
            values.append(values.pop(0))

        # Move the sorted items to the beginning of the queue,
        # inserting next_item in its proper position.
        added_next_item = False;
        for j in range(num_sorted):
            test_item = values.pop(0)    # Dequeue
            if (not added_next_item) and (test_item >= next_item):
                # Insert next_item first.
                values.append(next_item)
                added_next_item = True
            values.append(test_item)

        # If we haven't added next_item (because it is
        # bigger than the sorted items), do so now.
        if not added_next_item:
            values.append(next_item)

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
        self.window.title("queue_insertionsort")
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
