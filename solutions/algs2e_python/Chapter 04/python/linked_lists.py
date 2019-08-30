import tkinter as tk


class ListCell:
    """ Holds a single item in the list."""
    def __init__(self, value, next):
        self.value = value
        self.next = next


class SortedLinkedList:
    def __init__(self):
        # The top sentinel.
        self.sentinel = ListCell("<sentinel>", None)

    def add(self, value):
        """ Add an item to the list."""
        # Find the cell before the one holding the item.
        before = self.find_cell_before(value)

        # If you like, make sure the item isn't already in the list.
        if (before.next != None) and (before.next.value == value):
            raise ValueError(f"Duplicate value. The SortedLinkedList already holds the value {value}")

        # Insert the new item.
        new_cell = ListCell(value, before.next)
        before.next = new_cell

    def delete(self, value):
        """ Delete an item from the list."""
        # Find the cell before the one holding the item.
        before = self.find_cell_before(value)

        # If there's no such value, throw an exception.
        if (before.next == None) or (before.next.value != value):
            raise ValueError(f"Missing value. The SortedLinkedList does not hold the value {value}")

        # Delete the cell containing the item.
        cell = before.next
        before.next = cell.next

    def find_cell_before(self, value):
        """ Return the last cell before the indicated value."""
        before = self.sentinel
        while (before.next != None) and (before.next.value < value):
            before = before.next
        return before

    def __iter__(self):
        """ Iterator."""
        self.position = self.sentinel
        return self

    def __next__(self):
        if self.position != None:
            result = self.position.value
            self.position = self.position.next
            return result
        else:
            raise StopIteration


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("linked_list")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x300")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="Value:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(frame, width=12)
        self.value_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        add_button = tk.Button(frame, width=8, text="Add", command=self.add)
        add_button.grid(padx=5, pady=2, row=0, column=2)
        delete_button = tk.Button(frame, width=8, text="Delete", command=self.delete)
        delete_button.grid(padx=5, pady=2, row=0, column=3)

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=2, fill=tk.BOTH, expand=True)

        # Make an empty list.
        self.sorted_list = SortedLinkedList()
        self.display_list()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=add_button: add_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=delete_button: delete_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def add(self):
        """ Add an item to the list."""
        try:
            self.sorted_list.add(self.value_entry.get())
            self.value_entry.delete(0, tk.END)
            self.display_list()
        except ValueError as e:
            messagebox.showinfo("Add Error", str(e))
            return

    def delete(self):
        """ Delete an item from the list."""
        try:
            self.sorted_list.delete(self.value_entry.get())
            self.value_entry.delete(0, tk.END)
            self.display_list()
        except ValueError as e:
            messagebox.showinfo("Delete Error", str(e))
            return

    def display_list(self):
        """ Display the people in the list."""
        self.listbox.delete(0, tk.END)

        for value in self.sorted_list:
            self.listbox.insert(tk.END, value)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
