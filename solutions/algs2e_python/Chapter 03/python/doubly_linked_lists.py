import tkinter as tk
import re
from tkinter import messagebox

class ListCell:
    """ Holds a single item in the list."""
    def __init__(self, key, value, next, prev):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    """ The sentinel."""
    def __init__(self):
        self.sentinel = ListCell("sentinel", "sentinel", None, None)

    def __getitem__(self, key):
        """ Get the value for a key."""
        cell = self.find_cell(key)
        if cell == None:
            raise ValueError(f"Key {key} was not found in the list.")
        return cell.value

    def __setitem__(self, key, value):
        """ Set the value for a key."""
        # Find the cell holding this key.
        cell = self.find_cell(key)

        # If the cell doesn't exist, create it.
        # Otherwise give it the new value.
        if cell == None:
            self.add(key, value)
        else:
            cell.value = value

    def add(self, key, value):
        """ Add an item to the top of the list."""
        # Create a new cell.
        cell = ListCell(key, value, self.sentinel.next, self.sentinel)
        if cell.next != None:
            cell.next.prev = cell
        self.sentinel.next = cell

    def delete(self, key):
        """ Delete an item from the list."""
        # Find the cell holding the item.
        cell = self.find_cell(key)

        # If there's no such value, raise an error.
        if cell == None:
            raise ValueError(f"Key {key} was not found in the list.")

        # Delete the cell containing the item.
        if cell.next != None:
            cell.next.prev = cell.prev
        cell.prev.next = cell.next

    def find_cell(self, key):
        """ Return the cell holding the indicated value."""
        cell = self.sentinel.next
        while (cell != None) and (cell.key != key):
            cell = cell.next
        return cell

    def to_list(self):
        """ Iterator."""
        result = []
        cell = self.sentinel.next
        while cell != None:
            result.append((cell.key, cell.value))
            cell = cell.next
        return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("doubly_linked_lists")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x300")

        # Make the list.
        self.my_list = DoublyLinkedList()

        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=2, fill=tk.BOTH)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(frame, text="Key:")
        label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.key_entry = tk.Entry(frame)
        self.key_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        set_button = tk.Button(frame, text="Set", width=8, command=self.set)
        set_button.grid(row=0, column=2, pady=2)

        label = tk.Label(frame, text="Value:")
        label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.value_entry = tk.Entry(frame)
        self.value_entry.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        find_button = tk.Button(frame, text="Find", width=8, command=self.find)
        find_button.grid(row=1, column=2, pady=2)

        delete_button = tk.Button(frame, text="Delete", width=8, command=self.delete)
        delete_button.grid(row=2, column=2, pady=2)

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=set_button: set_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.key_entry.focus_force()
        self.window.mainloop()

    def set(self):
        """ Set an item's value in the list."""
        self.my_list[self.key_entry.get()] = self.value_entry.get()
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.key_entry.focus_force()
        self.show_values()

    def find(self):
        """ Find an item."""
        try:
            self.value_entry.delete(0, tk.END)
            self.value_entry.insert(0, self.my_list[self.key_entry.get()])
        except Exception as e:
            messagebox.showinfo("Error", str(e))
        self.show_values()

    def delete(self):
        """ See if the string is a palindrome."""

    def show_values(self):
        """ Display the values."""
        self.listbox.delete(0, tk.END)
        for (key, value) in self.my_list.to_list():
            self.listbox.insert(0, f"{key}: {value}")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
