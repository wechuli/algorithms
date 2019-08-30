import tkinter as tk
import tkinter.font as tk_font
from tkinter import ttk
import random

def pigeonhole_sort(values, max):
    """ Use pigeonhole sort to sort the array."""
    # Make the pigeonholes.
    pigeonholes = [None for i in range(max + 1)]

    # Move items into the pigeonholes.
    for value in values:
        # Add this item to its pigeonhole.
        cell = Cell(value)
        cell.next = pigeonholes[value]
        pigeonholes[value] = cell

    # Copy the items back into the values array.
    index = 0
    for i in range(max + 1):
        # Copy the items in pigeonhole i into the values array.
        cell = pigeonholes[i]
        while cell != None:
            values[index] = cell.value
            index += 1
            cell = cell.next

class Cell:
    def __init__(self, value):
        self.value = value
        self.next = None

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # The main heap.
        self.the_heap = BinomialHeap()

        self.window = tk.Tk()
        self.window.title("pigeonhole_sort")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("248x288")

        # Parameters.
        params_frame = tk.Frame(self.window)
        params_frame.pack(padx=5, pady=5, side=tk.TOP)

        num_items_label = tk.Label(params_frame, text="# Items:", width=9, anchor=tk.W)
        num_items_label.grid(row=0, column=0, padx=5, pady=2)
        self.num_items_entry = tk.Entry(params_frame, width=8, justify=tk.RIGHT)
        self.num_items_entry.grid(row=0, column=1, padx=5, pady=2)
        self.num_items_entry.insert(tk.END, "1000")
        generate_button = tk.Button(params_frame, text="Generate", width=8, command=self.generate)
        generate_button.grid(row=0, column=2, padx=5, pady=2)

        max_label = tk.Label(params_frame, text="Max Value:", width=9, anchor=tk.W)
        max_label.grid(row=1, column=0, padx=5, pady=2)
        self.max_entry = tk.Entry(params_frame, width=8, justify=tk.RIGHT)
        self.max_entry.grid(row=1, column=1, padx=5, pady=2)
        self.max_entry.insert(tk.END, "1000")
        sort_button = tk.Button(params_frame, text="Sort", width=8, command=self.sort)
        sort_button.grid(row=1, column=2, padx=5, pady=2)

        # List.
        list_frame = tk.Frame(self.window)
        list_frame.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        self.values_list = tk.Listbox(list_frame)
        self.values_list.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(list_frame, orient="vertical", command=self.values_list.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.values_list.configure(yscrollcommand=scrollbar.set)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=generate_button: generate_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=sort_button: sort_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_items_entry.focus_force()
        self.window.mainloop()

    def generate(self):
        """ Generate random values."""
        self.values_list.delete(0, tk.END)
        num_items = int(self.num_items_entry.get())
        self.items = [0 for i in range(num_items)]

        self.max_value = int(self.max_entry.get())
        for i in range(min(num_items, 1000)):
            self.items[i] = random.randint(0, self.max_value)

        self.list_values()

    def sort(self):
        """ Sort the items."""
        # Sort.
        pigeonhole_sort(self.items, self.max_value)

        # Validate the sort.
        for i in range(1, len(self.items)):
            assert self.items[i] >= self.items[i - 1], \
                f"items[{i}] = {self.items[i]} is less than items[{i - 1}] = {self.items[i - 1]}"

        self.list_values()

    def list_values(self):
        self.values_list.delete(0, tk.END)
        num_to_show = min(len(self.items), 1000)
        for i in range(num_to_show):
            self.values_list.insert(tk.END, f"{self.items[i]}")

if __name__ == '__main__':
    app = App()

# app.root.destroy()
