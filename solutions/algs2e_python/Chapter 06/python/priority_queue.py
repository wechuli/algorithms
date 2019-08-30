import tkinter as tk


class PriorityQueue:
    def __init__(self, capacity):
        """ Make arrays to hold the priority queue."""
        self.max_items = 100
        self.count = 0
        self.values = ["" for i in range(self.max_items)]
        self.priorities = [float("-inf") for i in range(self.max_items)]

    def push(self, value, priority):
        """ Add the item to the priority queue."""
        # Add the item at the bottom of the heap.
        self.values[self.count] = value
        self.priorities[self.count] = priority
        self.count += 1

        # Start at the new item and work up to the root.
        index = self.count - 1
        while index != 0:
            # Find the parent's index.
            parent = (index - 1) // 2

            # If child <= parent, we're done so
            # break out of the while loop.
            if self.priorities[index] <= self.priorities[parent]:
                break

            # Swap the parent and child.
            self.values[index], self.values[parent] = \
                self.values[parent], self.values[index]
            self.priorities[index], self.priorities[parent] = \
                self.priorities[parent], self.priorities[index]

            # Move to the parent.
            index = parent

    def pop(self):
        """ Remove the highest priority item from the priority queue."""
        # Save the return values.
        value = self.values[0]
        priority = self.priorities[0]

        # Replace the root with the last node.
        self.values[0] = self.values[self.count - 1]
        self.priorities[0] = self.priorities[self.count - 1]
        self.count -= 1

        # Restore the heap property.
        index = 0
        while True:
            # Find the child indices.
            child1 = 2 * index + 1
            child2 = 2 * index + 2

            # If a child index is off the end of the tree,
            # use the parent's index.
            if child1 >= self.count:
                child1 = index
            if child2 >= self.count:
                child2 = index

            # If the heap property is satisfied, we're done.
            if (self.priorities[index] >= self.priorities[child1]) and \
               (self.priorities[index] >= self.priorities[child2]):
                break

            # Get the index of the child with the larger value.
            if self.priorities[child1] > self.priorities[child2]:
                swap_child = child1
            else:
                swap_child = child2

            # Swap with the larger child.
            self.values[index], self.values[swap_child] = \
                self.values[swap_child], self.values[index]
            self.priorities[index], self.priorities[swap_child] = \
                self.priorities[swap_child], self.priorities[index]

            # Move to the child node.
            index = swap_child

        # Return the value and priority.
        return (value, priority)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("priority_queue")
        self.window.protocol("WM_pop_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="Value:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(frame, width=12)
        self.value_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W+tk.E)
        self.value_entry.insert(0, "Apple")
        push_button = tk.Button(frame, width=8, text="Push", command=self.do_push)
        push_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Priority:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.priority_entry = tk.Entry(frame, width=12)
        self.priority_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W+tk.E)
        self.priority_entry.insert(0, "10")
        pop_button = tk.Button(frame, width=8, text="Pop", command=self.pop)
        pop_button.grid(padx=5, pady=2, row=1, column=2)

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Make the priority queue.
        self.priority_queue = PriorityQueue(100)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=push_button: push_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=pop_button: pop_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def do_push(self):
        """ Add an item to the priority queue."""
        value = self.value_entry.get()
        priority = int(self.priority_entry.get())
        self.priority_queue.push(value, priority)

        self.value_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.value_entry.focus_force()
        self.show_values()


    def pop(self):
        """ Remove an item from the priority queue."""
        value, priority = self.priority_queue.pop()

        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, value)
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(0, priority)
        self.value_entry.focus_force()
        self.show_values()

    def show_values(self):
        """ Show up to 1000 values."""
        self.listbox.delete(0, tk.END)
        for i in range(self.priority_queue.count):
            self.listbox.insert(tk.END, f"{self.priority_queue.values[i]} ({self.priority_queue.priorities[i]})")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
