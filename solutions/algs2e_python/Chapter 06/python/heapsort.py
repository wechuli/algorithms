import tkinter as tk
import time


class Cell:
    def __init__(self, value, next):
        self.value = value
        self.next = next


def heapsort(values):
    """ Use heapsort to sort the array."""
    # Make the array into a heap.
    make_heap(values)

    # Pop items from the root to the end of the array.
    for i in range(len(values) - 1, 0, -1):
        # Remove the top item and restore the heap property.
        value = remove_top_item(values, i + 1)

        # Save the top item past the end of the tree.
        values[i] = value

def make_heap(values):
    """ Make the array into a heap."""
    # Add each item to the heap one at a time.
    for i in range(len(values)):
        # Start at the new item and work up to the root.
        index = i
        while index != 0:
            # Find the parent's index.
            parent = (index - 1) // 2

            # If child <= parent, we're done so
            # break out of the while loop.
            if values[index] <= values[parent]:
                break

            # Swap the parent and child.
            values[index], values[parent] = values[parent], values[index]

            # Move to the parent.
            index = parent

def remove_top_item(values, count):
    """
    Remove the top item from a heap with
    count items and restore its heap property.
    """
    # Save the top item to return later.
    result = values[0]

    # Move the last item to the root.
    values[0] = values[count - 1]

    # Restore the heap property.
    index = 0
    while True:
        # Find the child indices.
        child1 = 2 * index + 1
        child2 = 2 * index + 2

        # If a child index is off the end of the tree,
        # use the parent's index.
        if child1 >= count:
            child1 = index
        if child2 >= count:
            child2 = index

        # If the heap property is satisfied, we're done.
        if (values[index] >= values[child1]) and \
           (values[index] >= values[child2]):
            break

        # Get the index of the child with the larger value.
        if values[child1] > values[child2]:
            swap_child = child1
        else:
            swap_child = child2

        # Swap with the larger child.
        values[index], values[swap_child] = values[swap_child], values[index]

        # Move to the child node.
        index = swap_child

    # Return the value we removed from the root.
    return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("heapsort")
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
        self.items = []
        for i in range(num_items):
            self.items.append(random.randint(10000, 99999))
        self.show_values()

    def sort(self):
        """ Sort the items."""
        start_time = time.time()
        heapsort(self.items)
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
