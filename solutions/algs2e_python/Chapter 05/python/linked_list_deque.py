import tkinter as tk
from tkinter import messagebox


class Cell:
    def __init__(self, value, prev, next):
       self.value = value
       self.next = next
       self.prev = prev


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("linked_list_deque")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("400x300")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="Item:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.value_entry.grid(padx=5, pady=2, row=0, column=1)
        enqueue_top_button = tk.Button(frame, width=15, text="Enqueue Top", command=self.enqueue_top)
        enqueue_top_button.grid(padx=5, pady=2, row=0, column=2)
        dequeue_top_button = tk.Button(frame, width=15, text="Dequeue Top", command=self.dequeue_top)
        dequeue_top_button.grid(padx=5, pady=2, row=0, column=3)

        enqueue_bottom_button = tk.Button(frame, width=15, text="Enqueue Bottom", command=self.enqueue_bottom)
        enqueue_bottom_button.grid(padx=5, pady=2, row=1, column=2)
        dequeue_bottom_button = tk.Button(frame, width=15, text="Dequeue Bottom", command=self.dequeue_bottom)
        dequeue_bottom_button.grid(padx=5, pady=2, row=1, column=3)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(padx=(0,5), pady=5, side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        # Deque variables.
        self.top_sentinel = Cell("<TOP SENTINEL>", None, None)
        self.bottom_sentinel = Cell("<BOTTOM SENTINEL>", self.top_sentinel, None)
        self.top_sentinel.next = self.bottom_sentinel

        # Display the items.
        self.display_items()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=enqueue_top_button: enqueue_top_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=dequeue_top_button: dequeue_top_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def enqueue_top(self):
        """ Add an item at the top of the deque."""
        value = self.value_entry.get()
        self.value_entry.delete(0, tk.END)

        cell = Cell(value, self.top_sentinel, self.top_sentinel.next)
        cell.next.prev = cell
        self.top_sentinel.next = cell

        # Display the list.
        self.display_items()

    def dequeue_top(self):
        """ Remove an item from the top of the deque."""
        # Make sure there is something to dequeue.
        if self.top_sentinel.next == self.bottom_sentinel:
            messagebox.showinfo("Deque Error", "The deque is empty.")
            return

        # Display the value.
        cell = self.top_sentinel.next
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, cell.value)

        # Remove the item.
        self.top_sentinel.next = cell.next
        cell.next.prev = self.top_sentinel

        # Display the items.
        self.display_items()

    def enqueue_bottom(self):
        """ Add an item at the bottom of the deque."""
        value = self.value_entry.get()
        self.value_entry.delete(0, tk.END)

        cell = Cell(value, self.bottom_sentinel.prev, self.bottom_sentinel)
        cell.prev.next = cell
        self.bottom_sentinel.prev = cell

        # Display the list.
        self.display_items()

    def dequeue_bottom(self):
        """ Remove an item from the bottom of the deque."""
        # Make sure there is something to dequeue.
        if self.top_sentinel.next == self.bottom_sentinel:
            messagebox.showinfo("Deque Error", "The deque is empty.")
            return

        # Display the value.
        cell = self.bottom_sentinel.prev
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, cell.value)

        # Remove the item.
        self.bottom_sentinel.prev = cell.prev
        cell.prev.next = self.bottom_sentinel

        # Display the items.
        self.display_items()

    def display_items(self):
        self.listbox.delete(0, tk.END)
        cell = self.top_sentinel
        while cell != None:
            self.listbox.insert(tk.END, f"{cell.value}")
            cell = cell.next


if __name__ == '__main__':
    app = App()
