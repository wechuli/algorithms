import tkinter as tk
import time


def mergesort(values):
    """ Prepare to use mergesort and then call mergesort."""
    # Make a scratch array.
    scratch = [0 for i in len(values)]

    # Sort.
    do_mergesort(values, scratch, 0, len(values) - 1)

def do_mergesort(values, scratch, start, end):
    """ Use mergesort to sort the array."""
    # If the array contains only 1 item, it is already sorted.
    if start == end:
        return

    # Break the array into left and right halves.
    midpoint = (start + end) // 2

    # Call do_mergesort to sort the two halves.
    do_mergesort(values, scratch, start, midpoint)
    do_mergesort(values, scratch, midpoint + 1, end)

    # Merge the two sorted halves together.
    left_index = start
    right_index = midpoint + 1
    scratch_index = left_index
    while (left_index <= midpoint) and (right_index <= end):
        if values[left_index] <= values[right_index]:
            scratch[scratch_index] = values[left_index]
            left_index += 1
        else:
            scratch[scratch_index] = values[right_index]
            right_index += 1
        scratch_index += 1

    # Finish copying whichever half is not empty.
    # This can be improved with slicing.
    for i in range(left_index, midpoint + 1):
        scratch[scratch_index] = values[i]
        scratch_index += 1
    for i in range(right_index, end + 1):
        scratch[scratch_index] = values[i]
        scratch_index += 1

    # Copy the values back into the values array.
    # This can be improved with slicing.
    for i in range(start, end + 1):
        values[i] = scratch[i]


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("mergesort")
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
        mergesort(self.items)
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
