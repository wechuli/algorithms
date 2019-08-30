import tkinter as tk
from tkinter import messagebox
import random


class DataItem:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return f"[{self.key}:{self.value}]"


class MyHashTable:
    def __init__(self, num_entries):
        self.num_entries = num_entries
        self.num_used = 0
        self.table = [None for i in range(self.num_entries)]

    def add(self, key, value):
        """
        Add an item to the hash table.
        Raise an error if the item is already in the table.
        Return the number of probes.
        """
        # See if the table is full.
        if self.num_used == self.num_entries:
            raise ValueError(f"Cannot add key {key}. The hash table is full.")

        probe = key % self.num_entries
        num_probes = 0
        while True:
            num_probes += 1

            # See if this spot is empty.
            if self.table[probe] == None:
                # Put the value here.
                self.table[probe] = DataItem(key, value)
                self.num_used += 1
                return num_probes

            # See if the target key is here.
            if self.table[probe].key == key:
                raise ValueError(f"Key {key} is already in the hash table at index {probe}. ({num_probes} probes.)")

            # See if the key in this location is larger than the new key.
            if self.table[probe].key > key:
                # Swap the values and rehash the larger one.
                old_item = self.table[probe]
                self.table[probe] = DataItem(key, value)
                key = old_item.key
                value = old_item.value

                # Rehash the larger item.
                new_num_probes = self.add(key, value)
                num_probes += new_num_probes
                return num_probes

            # If we have tried too many times, give up.
            if num_probes == self.num_entries:
                raise ValueError(f"Cannot add key {key}. Did not find an empty entry in {num_probes} probes.)")

            # Try the next probe.
            probe = (key + num_probes * num_probes) % self.num_entries

    def find(self, key):
        """
        Return the item's cell or None if it's not present.
        Also return the number of probes.
        """
        probe = key % self.num_entries
        num_probes = 0
        while True:
            num_probes += 1

            # See if this spot is empty or the key in this
            # location is larger than the new key.
            if (self.table[probe] == None) or (self.table[probe].key > key):
                # The key isn't in the table.
                return None, num_probes

            # See if the key is here.
            if self.table[probe].key == key:
                # We found the key.
                return self.table[probe], num_probes

            if num_probes == self.num_entries:
                # The key isn't in the table and the table is full.
                return None, num_probes

            # Try the next probe.
            probe = (key + num_probes * num_probes) % self.num_entries

    def __str__(self):
        """ Return a textual representation of the table."""
        text = ""
        for i in range(self.num_entries):
            if self.table[i] == None:
                text += "[--------] "
            else:
                text += f"{self.table[i]} "

            if (i + 1) % 10 == 0:
                text += "\n"

        return text

    def fill_percentage(self):
        """ Return the fill percentage."""
        return 100 * self.num_used / self.num_entries

    def get_sequence_lengths(self, min_value, max_value):
        """ Return the average and maximum sequence lengths for the given values."""
        total_probes = 0
        max_length = 0
        for key in range(min_value, max_value + 1):
            item, num_probes= self.find(key)
            total_probes += num_probes
            if max_length < num_probes:
                max_length = num_probes

        ave_length = total_probes / (max_value - min_value + 1)
        return ave_length, max_length

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # The hash table.
        self.table = None

        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("ordered_quadratic_probing")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("630x420")

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
        self.size_entry.insert(0, "101")
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
        self.num_items_entry.insert(0, "80")

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

        frame = tk.LabelFrame(frame_frame, text="Statistics:")
        frame.pack(padx=5, pady=5, side=tk.TOP, anchor=tk.W, fill=tk.X)
        label = tk.Label(frame, width=label_width, text="Fill %", anchor=tk.W, justify=tk.LEFT)
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.fill_percentage_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.fill_percentage_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W+tk.E)
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

        # Define a value to represent an empty space.
        # Note that integers are basically unbounded in python 3+,
        # so this is really just a value that we don't allow as a valid key.
        self.empty = -1000000000

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def create(self):
        """ Make the hash table."""
        table_size = int(self.size_entry.get())
        self.table = MyHashTable(table_size)
        self.num_used = 0
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
                value = f"v{key:3}"
                self.table.add(key, value)
                items_added += 1
            except ValueError as e:
                if "is already in the hash table at index" not in str(e):
                    # Unknown error.
                    self.show_statistics()
                    messagebox.showinfo("Add Error", str(e))
                    return
                # Otherwise it is a duplicate value. Try again.

        self.show_statistics()

    def show_statistics(self):
        """Display the table's contents and statistics."""
        # Display the items in the table.
        self.table_text.delete(1.0, tk.END)
        self.table_text.insert(tk.END, f"{self.table}")

        # Fill percentage.
        self.fill_percentage_entry.delete(0, tk.END)
        self.fill_percentage_entry.insert(tk.END, f"{self.table.fill_percentage():0.2f}")

        # Probe sequence lengths.
        ave_length, max_length = self.table.get_sequence_lengths(self.min_value, self.max_value)
        self.ave_probe_entry.delete(0, tk.END)
        self.ave_probe_entry.insert(tk.END, f"{ave_length:0.2f}")
        self.max_probe_entry.delete(0, tk.END)
        self.max_probe_entry.insert(tk.END, f"{max_length}")

    def insert_item(self):
        """ Insert an item."""
        try:
            key = int(self.item_entry.get())
            value = f"v{key:3}"
            num_probes = self.table.add(key, value)
            messagebox.showinfo("Add Item", f"Item {key} added in {num_probes} probes")
            self.show_statistics()
        except ValueError as e:
            messagebox.showinfo("Add Error", str(e))

    def find_item(self):
        """ Find an item."""
        key = int(self.item_entry.get())
        item, num_probes = self.table.find(key)
        if item == None:
            messagebox.showinfo("Find Item", f"Did not find key {key} in {num_probes} probes")
        else:
            messagebox.showinfo("Find Item", f"Found {item} in {num_probes} probes")


if __name__ == '__main__':
    app = App()

# app.root.destroy()

