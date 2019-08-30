import tkinter as tk
import time


class Cell:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def countingsort(values, max_value):
    """ Use countingsort to sort the array."""
    # Make an array to hold the counts.
    counts = [0 for i in range(max_value + 1)]

    # Count the items with each value.
    for value in values:
        # Add 1 to the count for this value.
        counts[value] += 1

    # Copy the values back into the array.
    index = 0
    for i in range(max_value + 1):
        # Copy the value i into the array counts[i] times.
        for j in range(counts[i]):
            values[index] = i
            index += 1


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("countingsort")
        self.window.protocol("WM_sort_WINDOW", self.kill_callback)
        self.window.geometry("300x400")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="# Items:", width=10)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=12, justify=tk.RIGHT)
        self.num_items_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.num_items_entry.insert(0, "10000")
        generate_button = tk.Button(frame, width=8, text="Generate", command=self.generate)
        generate_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Max Value:", width=10)
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.max_value_entry = tk.Entry(frame, width=12, justify=tk.RIGHT)
        self.max_value_entry.grid(padx=5, pady=(2, 7), row=1, column=1, sticky=tk.W)
        self.max_value_entry.insert(0, "1000")
        sort_button = tk.Button(frame, width=8, text="Sort", command=self.sort)
        sort_button.grid(padx=5, pady=2, row=1, column=2)

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
        start_time = time.time()
        countingsort(self.items, self.max_value)
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
