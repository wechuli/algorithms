import tkinter as tk
import time


class Cell:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def bucketsort(values, max_value, num_buckets):
    """ Use bucketsort to sort the array."""
    # Make the buckets.
    buckets = [Cell(float("-inf"), None) for i in range(num_buckets)]

    # Calculate the number of values per bucket.
    items_per_bucket = (max_value + 1) / num_buckets

    # Distribute.
    for value in values:
        # Calculate the bucket number.
        num = int(value / items_per_bucket)

        # Insert the item in this bucket.
        after_me = buckets[num]
        while (after_me.next != None) and (after_me.next.value < value):
            after_me = after_me.next
        cell = Cell(value, after_me.next)
        after_me.next = cell

    # Gather the values back into the array.
    index = 0
    for i in range(num_buckets):
        # Copy the values in bucket i into the array (skipping the sentinel).
        cell = buckets[i].next
        while cell != None:
            values[index] = cell.value
            index += 1
            cell = cell.next


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("bucketsort")
        self.window.protocol("WM_sort_WINDOW", self.kill_callback)
        self.window.geometry("300x400")

        frame = tk.LabelFrame(self.window, text="Make Items")
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="# Items:", width=10)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=12, justify=tk.RIGHT)
        self.num_items_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.num_items_entry.insert(0, "100000")
        generate_button = tk.Button(frame, width=8, text="Generate", command=self.generate)
        generate_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Max Value:", width=10)
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.max_value_entry = tk.Entry(frame, width=12, justify=tk.RIGHT)
        self.max_value_entry.grid(padx=5, pady=(2, 7), row=1, column=1, sticky=tk.W)
        self.max_value_entry.insert(0, "1000000")

        frame = tk.LabelFrame(self.window, text="Sort")
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="# Buckets:", width=10)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_buckets_entry = tk.Entry(frame, width=12, justify=tk.RIGHT)
        self.num_buckets_entry.grid(padx=5, pady=(2, 7), row=0, column=1, sticky=tk.W)
        self.num_buckets_entry.insert(0, "1000")
        sort_button = tk.Button(frame, width=8, text="Sort", command=self.sort)
        sort_button.grid(padx=5, pady=2, row=0, column=2)

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=generate_button: generate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_items_entry.focus_force()
        self.window.mainloop()

    def generate(self):
        """ Make random items."""
        num_items = int(self.num_items_entry.get())
        self.max_value = int(self.max_value_entry.get())
        self.items = []
        for i in range(num_items):
            self.items.append(random.randint(0, self.max_value))
        self.show_values()

    def sort(self):
        """ Sort the items."""
        num_buckets = int(self.num_buckets_entry.get())

        start_time = time.time()
        bucketsort(self.items, self.max_value, num_buckets)
        elapsed_time = time.time() - start_time
        print(f"{elapsed_time} seconds")
        self.show_values()

        # Verify the sort.
        for i in range(1, len(self.items)):
            assert self.items[i] >= self.items[i - 1], f"Item {i} ({self.items[i]}) is smaller than item {i-1} ({self.items[i-1]})"

    def show_values(self):
        """ Show up to 1000 values."""
        self.listbox.delete(0, tk.END)
        for i in range(min(len(self.items), 1000)):
            self.listbox.insert(tk.END, self.items[i])


if __name__ == '__main__':
    app = App()

# app.root.destroy()
