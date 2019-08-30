import random
import tkinter as tk
from tkinter import ttk


def sort_stack(values):
    # Make the temporary stack.
    temp = []

    # Sort.
    num_items = len(values)
    for i in range(num_items):
        # Pull off the first item.
        next_item = values.pop()

        # Move the other unsorted items to the second stack.
        for j in range(num_items - i - 1):
            temp.append(values.pop())

        # Move sorted items to the second stack until
        # we find out where next_item belongs.
        while len(values) > 0:
            test_item = values.pop()
            if test_item <= next_item:
                # The value next_item belongs after test_item in the sorted list.
                # Put test_item back in the list.
                values.append(test_item)
                break
            temp.append(test_item)

        # Add next_item at this position.
        values.append(next_item)

        # Move the remaining items back onto the list.
        while len(temp) > 0:
            values.append(temp.pop())


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("stack_insertionsort")
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

