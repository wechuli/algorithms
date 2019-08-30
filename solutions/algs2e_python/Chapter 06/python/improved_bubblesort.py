import tkinter as tk
import time


def improved_bubblesort(values):
    """ Use improved bubblesort to sort the array."""
    # Bounds for the items that are not yet sorted.
    imin = 0
    imax = len(values) - 1

    # Repeat until the array is sorted.
    while imin < imax:
        # Record the index of the last swapped item.
        last_swap = imin

        # Downward pass.
        for i in range(imin, imax):
            # See if items i and i + 1 are out of order.
            if values[i] > values[i + 1]:
                # Swap them.
                values[i], values[i + 1] = values[i + 1], values[i]

                # Update the index of the last swapped item.
                last_swap = i

        # Update imax.
        imax = last_swap

        # See if we're done.
        if imin >= imax:
            break

        # Upward pass.
        last_swap = imax
        for i in range(imax, imin, -1):
            # See if items i and i - 1 are out of order.
            if values[i] < values[i - 1]:
                # Swap them.
                values[i], values[i - 1] = values[i - 1], values[i]

                # Update the index of the last swapped item.
                last_swap = i

        # Update imin.
        imin = last_swap

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("improved_bubblesort")
        self.window.protocol("WM_sort_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="# Items:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=12)
        self.num_items_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.num_items_entry.insert(0, "1000")
        generate_button = tk.Button(frame, width=8, text="Generate", command=self.generate)
        generate_button.grid(padx=5, pady=2, row=0, column=2)
        sort_button = tk.Button(frame, width=8, text="Sort", command=self.sort)
        sort_button.grid(padx=5, pady=2, row=0, column=3)

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
        self.items = []
        for i in range(num_items):
            self.items.append(random.randint(100000, 999999))
        self.show_values()

    def sort(self):
        """ Sort the items."""
        start_time = time.time()
        improved_bubblesort(self.items)
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
