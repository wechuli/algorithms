import tkinter as tk
from tkinter import messagebox
import random


infinity = 1000000000


class Cell:
    def __init__(self, key, value, next):
        self.key = key
        self.value = value
        self.next = next

    def __str__(self):
        return f"[{self.key}:{self.value}]"


class MyHashTable:
    def __init__(self, num_buckets):
        """ Make the bucket sentinels."""
        self.num_buckets = num_buckets
        self.num_used = 0
        self.buckets = []
        for i in range(self.num_buckets):
            bottom_sentinel = Cell(infinity, "BOTTOM", None)
            self.buckets.append(Cell(-infinity, "TOP", bottom_sentinel))

    def add(self, key, value):
        """
        Add an item to the hash table.
        Raise an error if the item is already in the table.
        """
        # Find the cell before where this key belongs.
        cell_before, num_probes = self.find_cell_before(key)
        num_probes += 1

        # Make sure the item isn't already in the table.
        if cell_before.next.key == key:
            raise ValueError(f"The key {key} is already in the hash table.")

        # Add the item.
        new_cell = Cell(key, value, cell_before.next)
        cell_before.next = new_cell

        # Update num_used.
        self.num_used += 1
        return num_probes

    def find(self, key):
        """ Return the item's cell or None if it's not present."""
        # Find the cell before this one.
        cell_before, num_probes = self.find_cell_before(key)
        num_probes += 1
        if cell_before.next.key != key:
            return None, num_probes

        # Return the cell.
        return cell_before.next, num_probes

    def delete(self, key):
        """
        Delete an item and return the number of probes required.
        Raise an error if the item isn't in the hash table.
        """
        # Find the cell before the target cell.
        cell_before, num_probes = self.find_cell_before(key)

        # See if the item is present.
        if cell_before.next.key != key:
            raise ValueError(f"The key {key} is not in the hash table.")

        # Remove the target cell.
        num_probes += 1
        cell_before.next = cell_before.next.next

        # Update num_used.
        self.num_used -= 1
        return num_probes

    def find_cell_before(self, key):
        """
        Return the cell before the one containing
        the key or None if the key is not present.
        """
        # Find the key's bucket.
        bucket_num = key % self.num_buckets
        sentinel = self.buckets[bucket_num]

        # Find the desired cell.
        num_probes = 0
        cell = sentinel
        while cell.next.key < key:
            num_probes += 1
            cell = cell.next
        return cell, num_probes

    def __str__(self):
        """ Return a textual representation of the table."""
        text = ""
        for cell in self.buckets:
            text += ">"
            cell = cell.next
            while cell.next != None:
                text += f" {cell}"
                cell = cell.next
            text += "\n"
        return text

    def average_bucket_size(self):
        """ Return the average number of keys per bucket."""
        return self.num_used / self.num_buckets

    def get_sequence_lengths(self, min_value, max_value):
        """ Return the average probe and maximum sequence lengths for the given values."""
        total_probes = 0
        max_length = 0
        for key in range(min_value, max_value + 1):
            cell, num_probes = self.find(key)
            total_probes += num_probes
            if max_length < num_probes:
                max_length = num_probes

        ave_length = total_probes / (max_value - min_value + 1)
        return ave_length, max_length


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("sorted_chaining")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("660x420")

        label_width = 10
        entry_width = 6
        button_width = 10
        frame_frame = tk.Frame(self.window)
        frame_frame.pack(padx=5, pady=5, side=tk.LEFT, anchor=tk.NW)

        frame = tk.LabelFrame(frame_frame, text="Hash Table")
        frame.pack(padx=5, pady=5, side=tk.TOP, anchor=tk.W)
        label = tk.Label(frame, width=label_width, text="Size:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.size_entry = tk.Entry(frame, width=entry_width, justify=tk.RIGHT)
        self.size_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.size_entry.insert(0, "10")
        create_button = tk.Button(frame, width=button_width, text="Create", command=self.create)
        create_button.grid(padx=5, pady=2, row=0, column=2, sticky=tk.W)

        frame = tk.LabelFrame(frame_frame, text="Load Table")
        frame.pack(padx=5, pady=5, side=tk.TOP, anchor=tk.W)
        label = tk.Label(frame, width=label_width, text="Min:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.min_entry = tk.Entry(frame, width=entry_width, justify=tk.RIGHT)
        self.min_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.min_entry.insert(0, "100")
        label = tk.Label(frame, width=label_width, text="Max:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.max_entry = tk.Entry(frame, width=entry_width, justify=tk.RIGHT)
        self.max_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        self.max_entry.insert(0, "999")
        make_items_button = tk.Button(frame, width=button_width, text="Make Items", command=self.make_items)
        make_items_button.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        label = tk.Label(frame, width=label_width, text="# Items:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.num_items_entry = tk.Entry(frame, width=entry_width, justify=tk.RIGHT)
        self.num_items_entry.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)
        self.num_items_entry.insert(0, "20")

        frame = tk.LabelFrame(frame_frame, text="Create/Find")
        frame.pack(padx=5, pady=5, side=tk.TOP, anchor=tk.W)
        insert_button = tk.Button(frame, width=button_width, text="Insert", command=self.insert_item)
        insert_button.grid(padx=5, pady=2, row=0, column=2, sticky=tk.W)
        label = tk.Label(frame, width=label_width, text="Item:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.item_entry = tk.Entry(frame, width=entry_width, justify=tk.RIGHT)
        self.item_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        self.item_entry.insert(0, "123")
        find_button = tk.Button(frame, width=button_width, text="Find", command=self.find_item)
        find_button.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        delete_button = tk.Button(frame, width=button_width, text="Delete", command=self.delete_item)
        delete_button.grid(padx=5, pady=2, row=2, column=2, sticky=tk.W)

        frame = tk.LabelFrame(frame_frame, text="Statistics:")
        frame.pack(padx=5, pady=5, side=tk.TOP, anchor=tk.W, fill=tk.X)
        label = tk.Label(frame, width=label_width, text="Keys/Bucket:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.keys_per_bucket_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.keys_per_bucket_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W+tk.E)
        label = tk.Label(frame, width=label_width, text="Max Probe:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.max_probe_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.max_probe_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W+tk.E)
        label = tk.Label(frame, width=label_width, text="Ave Probe:", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.ave_probe_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.ave_probe_entry.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W+tk.E)

        frame = tk.LabelFrame(self.window, text="Table:")
        frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)
        frame.grid_rowconfigure(0, weight=1)
        frame.grid_columnconfigure(0, weight=1)
        self.table_text = tk.Text(frame, wrap=tk.NONE)
        self.table_text.grid(padx=5, pady=5, row=0, column=0, sticky=tk.NSEW)
        vscrollbar = tk.Scrollbar(frame)
        vscrollbar.grid(row=0, column=1, sticky=tk.E+tk.N+tk.S)
        hscrollbar = tk.Scrollbar(frame, orient=tk.HORIZONTAL)
        hscrollbar.grid(row=1, column=0, sticky=tk.E+tk.W+tk.S)

        self.table_text.config(xscrollcommand=hscrollbar.set)
        self.table_text.config(yscrollcommand=vscrollbar.set)
        hscrollbar.config(command=self.table_text.xview)
        vscrollbar.config(command=self.table_text.yview)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def create(self):
        """ Make the hash table."""
        num_buckets = int(self.size_entry.get())
        self.table = MyHashTable(num_buckets)

        self.min_value = 0
        self.max_value = 0
        self.show_statistics()

    def make_items(self):
        """ Make some items."""
        num_items = int(self.num_items_entry.get())
        self.min_value = int(self.min_entry.get())
        self.max_value = int(self.max_entry.get())
        items_added = 0
        while items_added < num_items:
            try:
                key = random.randint(self.min_value, self.max_value)
                value = f"v{key:3d}";
                self.table.add(key, value)
                items_added += 1
            except ValueError as e:
                if "is already in the hash table" not in str(e):
                    # Unknown error.
                    messagebox.showinfo("Add Error", str(e))
                # Otherwise it is a duplicate value. Try again.

        self.show_statistics()

    def show_statistics(self):
        """Display the table's contents and statistics."""
        # Display the items in the table.
        self.table_text.delete(1.0, tk.END)
        self.table_text.insert(tk.END, f"{self.table}")

        # Keys per bucket.
        self.keys_per_bucket_entry.delete(0, tk.END)
        self.keys_per_bucket_entry.insert(tk.END, f"{self.table.average_bucket_size()}")

        # Probe sequence lengths.
        ave_length, max_length = self.table.get_sequence_lengths(self.min_value, self.max_value)
        self.max_probe_entry.delete(0, tk.END)
        self.max_probe_entry.insert(tk.END, f"{max_length}")
        self.ave_probe_entry.delete(0, tk.END)
        self.ave_probe_entry.insert(tk.END, f"{ave_length:.2f}")

    def insert_item(self):
        """ Insert an item."""
        try:
            key = int(self.item_entry.get())
            value = f"v{key:3d}";
            num_probes = self.table.add(key, value)
            messagebox.showinfo("Add Item", f"Item {key} added in {num_probes} probes")
            self.show_statistics()
        except ValueError as e:
            messagebox.showinfo("Add Error", str(e))

    def find_item(self):
        """ Find an item."""
        key = int(self.item_entry.get())
        cell, num_probes = self.table.find(key)
        if cell != None:
            messagebox.showinfo("Find Item", f"Found {key} in {num_probes} probes")
        else:
            messagebox.showinfo("Find Item", f"Did not find {key} in {num_probes} probes")

    def delete_item(self):
        """ Delete an item."""
        try:
            key = int(self.item_entry.get())
            num_probes = self.table.delete(key)
            messagebox.showinfo("Delete Item", f"Deleted {key} in {num_probes} probes")
            self.show_statistics()
        except ValueError as e:
            messagebox.showinfo("Add Error", str(e))


if __name__ == '__main__':
    app = App()

# app.root.destroy()

