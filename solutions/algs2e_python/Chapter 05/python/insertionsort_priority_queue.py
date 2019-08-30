import tkinter as tk
from tkinter import messagebox


class Cell:
    def __init__(self, value, priority, next):
       self.value = value
       self.priority = priority
       self.next = next


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("insertionsort_priority_queue")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("350x300")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="Item:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.value_entry.grid(padx=5, pady=2, row=0, column=1)
        enqueue_button = tk.Button(frame, width=10, text="Enqueue", command=self.enqueue)
        enqueue_button.grid(padx=5, pady=2, row=0, column=2)
        dequeue_button = tk.Button(frame, width=10, text="Dequeue", command=self.dequeue)
        dequeue_button.grid(padx=5, pady=2, row=0, column=3)

        label = tk.Label(frame, text="Priority:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.priority_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.priority_entry.grid(padx=5, pady=2, row=1, column=1)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        self.listbox = tk.Listbox(frame)
        self.listbox.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.listbox.yview)
        scrollbar.pack(padx=(0,5), pady=5, side=tk.RIGHT, fill=tk.Y)
        self.listbox.configure(yscrollcommand=scrollbar.set)

        # Make the priority queue.
        self.queue_sentinel = Cell("", float("-inf"), None)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=enqueue_button: enqueue_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=dequeue_button: dequeue_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def enqueue(self):
        """ Enqueue an item."""
        value = self.value_entry.get()
        priority = int(self.priority_entry.get())

        self.value_entry.delete(0, tk.END)
        self.priority_entry.delete(0, tk.END)
        self.value_entry.focus_force()

        # See where the item belongs.
        after_me = self.queue_sentinel
        while (after_me.next != None) and (after_me.next.priority < priority):
            after_me = after_me.next

        # Insert the item.
        new_cell = Cell(value, priority, after_me.next)
        after_me.next = new_cell

        # Display the list.
        self.display_items()

    def dequeue(self):
        """ Dequeue an item."""
        # Make sure there is something to dequeue.
        if self.queue_sentinel.next == None:
            messagebox.showinfo("Dequeue Error", "The queue is empty.")
            return

        # Display the value and priority.
        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(0, self.queue_sentinel.next.value)
        self.priority_entry.delete(0, tk.END)
        self.priority_entry.insert(0, self.queue_sentinel.next.priority)
        self.value_entry.focus_force()

        # Remove the item.
        self.queue_sentinel = self.queue_sentinel.next

        # Display the items.
        self.display_items()

    def display_items(self):
        self.listbox.delete(0, tk.END)
        cell = self.queue_sentinel.next
        while cell != None:
            self.listbox.insert(tk.END, f"{cell.value} ({cell.priority})")
            cell = cell.next


if __name__ == '__main__':
    app = App()
