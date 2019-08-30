import tkinter as tk
import random

def interpolation_search(values, target):
    """
    Return the index of the target item in the values array.
    If the item appears more than once in the array,
    this method doesn't necessarily return the first instance.
    Return -1 if the item isn't in the array.
    """
    steps = 0
    min = 0
    max = len(values) - 1
    while min <= max:
        steps += 1

        # Prevent division by zero.
        if values[min] == values[max]:
            # This must be the item (if it's in the array).
            if values[min] == target:
                return min, steps
            return -1, steps

        # Find the dividing item.
        mid = min + (max - min) * (target - values[min]) // (values[max] - values[min])

        # If mid is out of bounds, then the target isn't in the array.
        if (mid < min) or (mid > max):
            return -1, steps

        # See if we need to search the left or right half.
        if values[mid] < target:
            min = mid + 1
        elif values[mid] > target:
            max = mid - 1
        else:
            return mid, steps

    # If get here, the target isn't in the array.
    return -1, steps


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("interpolation_search")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("320x300")

        frame = tk.LabelFrame(self.window, text="Create Items")
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="Min:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.min_entry = tk.Entry(frame, width=12)
        self.min_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.min_entry.insert(0, "10000")

        label = tk.Label(frame, text="Max:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.max_entry = tk.Entry(frame, width=12)
        self.max_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        self.max_entry.insert(0, "99999")
        create_button = tk.Button(frame, width=8, text="Create", command=self.create)
        create_button.grid(padx=5, pady=2, row=1, column=2)

        label = tk.Label(frame, text="# Items:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=12)
        self.num_items_entry.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)
        self.num_items_entry.insert(0, "10000")

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.rowconfigure(4, weight=1)

        frame2 = tk.Frame(frame)
        frame2.grid(padx=5, pady=2, row=0, column=0, rowspan=5, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(frame2)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(frame2)
        self.listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox.config(yscrollcommand=scrollbar.set)
        self.listbox.bind('<<ListboxSelect>>', self.listbox_select)
        scrollbar.config(command=self.listbox.yview)

        label = tk.Label(frame, text="Item:")
        label.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.target_entry = tk.Entry(frame, width=12)
        self.target_entry.grid(padx=5, pady=2, row=0, column=2, sticky=tk.W)
        self.target_entry.insert(0, "55555")

        find_button = tk.Button(frame, width=8, text="Find", command=self.find)
        find_button.grid(padx=5, pady=2, row=1, column=1, columnspan=2)

        label = tk.Label(frame, text="Index:")
        label.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)
        self.index_entry = tk.Entry(frame, width=12)
        self.index_entry.grid(padx=5, pady=2, row=2, column=2, sticky=tk.W)

        label = tk.Label(frame, text="# Steps:")
        label.grid(padx=5, pady=2, row=3, column=1, sticky=tk.W)
        self.num_steps_entry = tk.Entry(frame, width=12)
        self.num_steps_entry.grid(padx=5, pady=2, row=3, column=2, sticky=tk.W)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=create_button: create_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.min_entry.focus_force()
        self.window.mainloop()

    def create(self):
        """ Make and sort the items."""
        # Get the parameters.
        min = int(self.min_entry.get())
        max = int(self.max_entry.get())
        num_items = int(self.num_items_entry.get())

        # Make the items.
        self.items = []
        for i in range(num_items):
            self.items.append(random.randint(min, max))

        # Sort the items.
        self.items.sort()

        # Display the items.
        self.listbox.delete(0, tk.END)
        for item in self.items:
            self.listbox.insert(tk.END, item)

    def find(self):
        """ Find the indicated item."""
        target = int(self.target_entry.get())
        index, steps = interpolation_search(self.items, target)

        self.index_entry.delete(0, tk.END)
        self.index_entry.insert(tk.END, f"{index}")

        self.num_steps_entry.delete(0, tk.END)
        self.num_steps_entry.insert(tk.END, f"{steps}")

    def listbox_select(self, event):
        """ Copy the selection into the target entry field."""
        listbox = event.widget
        selection = listbox.curselection()
        if len(selection) == 0:
            return
        index = int(listbox.curselection()[0])
        value = listbox.get(index)
        self.target_entry.delete(0, tk.END)
        self.target_entry.insert(0, value)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
