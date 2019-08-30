from enum import Enum
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import itertools


class Direction(Enum):
    """ The direction we are traveling through the edit graph."""
    unknown = 0
    from_above = 1
    from_left = 2
    from_diagonal = 3


class Node:
    """ A node in the edit graph."""
    def __init__(self):
        self.distance = 0
        self.direction = Direction.unknown

    def __str__(self):
        return f"{self.distance}:{self.direction}"

def make_edit_graph(lines1, lines2):
    """ Create an edit graph for two arrays of strings."""
    # Make the edit graph array.
    num_cols = len(lines1) + 1
    num_rows = len(lines2) + 1
    nodes = [[Node() for col in range(num_cols)] for row in range(num_rows)]

    # Initialize the leftmost column.
    for r in range(num_rows):
        nodes[r][0].distance = r
        nodes[r][0].direction = Direction.from_above

    # Initialize the top row.
    for c in range(num_cols):
        nodes[0][c].distance = c
        nodes[0][c].direction = Direction.from_left

    # Fill in the rest of the array.
    for c in range(1, num_cols):
        # Fill in column c.
        for r in range(1, num_rows):
            # Fill in entry [r][c].
            # Check the three possible paths to here and pick the best.
            # From above.
            nodes[r][c].distance = nodes[r - 1][c].distance + 1
            nodes[r][c].direction = Direction.from_above

            # From the left.
            if nodes[r][c].distance > nodes[r][c - 1].distance + 1:
                nodes[r][c].distance = nodes[r][c - 1].distance + 1
                nodes[r][c].direction = Direction.from_left

            # Diagonal.
            if (lines1[c - 1] == lines2[r - 1]) and (nodes[r][c].distance > nodes[r - 1][c - 1].distance):
                nodes[r][c].distance = nodes[r - 1][c - 1].distance
                nodes[r][c].direction = Direction.from_diagonal

    return nodes


def display_results(lines1, lines2, nodes, text):
    """ Display the changes in a text widget."""
    # Build a list of the moves from finish to start.
    num_rows = len(nodes)
    num_cols = len(nodes[0])
    r = num_rows - 1
    c = num_cols - 1

    # Make some fonts.
    text.tag_configure("keep_font", font=("Arial", 10), foreground="black")
    text.tag_configure("insert_font", font=("Arial", 10, "underline"), foreground="blue")
    text.tag_configure("delete_font", font=("Arial", 10, "overstrike"), foreground="red")
    text.delete("1.0", tk.END)

    # Continue until we reach the upper left corner.
    while (r > 0) or (c > 0):
        if nodes[r][c].direction == Direction.from_above:
            print(f"Insertd: {lines2[r-1]}")#@
            text.insert("1.0", lines2[r - 1], "insert_font")
            r -= 1
        elif nodes[r][c].direction == Direction.from_left:
            print(f"Deleted: {lines1[c-1]}")#@
            text.insert("1.0", lines1[c - 1], "delete_font")
            c -= 1
        elif nodes[r][c].direction == Direction.from_diagonal:
            print(f"Kept: {lines2[r-1]}")#@
            text.insert("1.0", lines2[r - 1], "keep_font")
            r -= 1
            c -= 1


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("file_edit_distance")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("600x300")

        self.window.grid_rowconfigure(4, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="File 1:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.file1_entry = tk.Entry(self.window, width=1)
        self.file1_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        self.file1_entry.insert(tk.END, "Sample1.txt")

        label = tk.Label(self.window, text="File 2:")
        label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.file2_entry = tk.Entry(self.window, width=1)
        self.file2_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        self.file2_entry.insert(tk.END, "Sample2.txt")

        compare_button = tk.Button(self.window, text="Compare", width=8, command=self.compare)
        compare_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        label = tk.Label(self.window, text="Distance:")
        label.grid(row=3, column=0, padx=5, pady=5, sticky=tk.W)
        self.distance_entry = tk.Entry(self.window, width=5)
        self.distance_entry.grid(row=3, column=1, padx=5, pady=5, sticky=tk.W)

        label = tk.Label(self.window, text="Edits:")
        label.grid(row=4, column=0, padx=5, pady=5, sticky=tk.NW)
        self.edits_text = tk.Text(self.window, width=1, height=1)
        self.edits_text.grid(row=4, column=1, padx=5, pady=5, sticky=tk.NSEW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=compare_button: compare_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.file1_entry.focus_force()
        self.window.mainloop()

    def compare(self):
        """ Compare the files."""
        self.distance_entry.delete(0, tk.END)
        self.edits_text.delete("1.0", tk.END)

        # Get the files.
        filename1 = self.file1_entry.get()
        filename2 = self.file2_entry.get()
        with open(filename1, "r") as file1:
            lines1 = file1.readlines()
        with open(filename2, "r") as file2:
            lines2 = file2.readlines()

        # Build the edit graph.
        nodes = make_edit_graph(lines1, lines2)

        # Display the edits.
        display_results(lines1, lines2, nodes, self.edits_text)

        # Display the edit distance.
        distance = nodes[len(nodes) - 1][len(nodes[0]) - 1].distance
        self.distance_entry.insert(tk.END, f"{distance}")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
