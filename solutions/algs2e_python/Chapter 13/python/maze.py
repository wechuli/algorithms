import tkinter as tk
from tkinter import ttk
import math
import time
import random

def make_network(num_rows, num_columns):
    """ Build the network."""
    # Make an array of nodes.
    nodes = [[None for c in range(num_columns)] for r in range(num_rows)]
    for r in range(num_rows):
        for c in range(num_columns):
            nodes[r][c] = Node(r, c)

    # Make horizontal links.
    for r in range(num_rows):
        for c in range(1, num_columns):
            link = Link(nodes[r][c - 1], nodes[r][c])
            nodes[r][c - 1].links.append(link)
            nodes[r][c].links.append(link)

    # Make vertical links.
    for c in range(num_columns):
        for r in range(1, num_rows):
            link = Link(nodes[r - 1][c], nodes[r][c])
            nodes[r - 1][c].links.append(link)
            nodes[r][c].links.append(link)

    return nodes


def find_spanning_tree(nodes):
    """ Find a random spanning tree."""
    # Start with a random node.
    row = random.randint(0, len(nodes) - 1)
    column = random.randint(0, len(nodes[0]) - 1)
    root = nodes[row][column]
    root.visited = True

    # Create the candidate list.
    candidates = root.links.copy()

    # Process the candidate list.
    results = []
    while len(candidates) > 0:
        # Pick a random link.
        index = random.randint(0, len(candidates) - 1)
        best_link = candidates[index]
        del candidates[index]
        results.append(best_link)

        # See which node is not yet in the tree.
        new_node = best_link.node1
        if (new_node.visited):
            new_node = best_link.node2

        # Add the node to the tree.
        new_node.visited = True

        # Add the node's links to the candidate list.
        for link in new_node.links:
            if (not link.node1.visited) or (not link.node2.visited):
                candidates.append(link)

        # Remove any unneeded candidates.
        for i in range(len(candidates) - 1, -1, -1):
            if candidates[i].node1.visited and candidates[i].node2.visited:
                del candidates[i]

    # Return the tree's links.
    return results


def build_walls(tree_links, num_rows, num_columns, x0, y0, dx, dy):
    """ Build segments representing the maze's walls."""
    # Make arrays to indicates whether a node's
    # left or top wall is broken by the tree.
    left_side_broken = [[False for c in range(num_columns + 1)] for r in range(num_rows)]
    top_side_broken = [[False for c in range(num_columns)] for r in range(num_rows + 1)]

    # Mark the walls that should be broken.
    for link in tree_links:
        # See if this is a vertical or horizontal link.
        if link.node1.row == link.node2.row:
            # Horizontal link.
            row = link.node1.row
            column = max(link.node1.column, link.node2.column)
            left_side_broken[row][column] = True
        else:
            # Vertical link.
            row = max(link.node1.row, link.node2.row)
            column = link.node1.column
            top_side_broken[row][column] = True

    # Build the wall list.
    walls = []
    for r in range(num_rows):
        for c in range(num_columns + 1):
            if not left_side_broken[r][c]:
                # Make this wall.
                x = x0 + c * dx
                y = y0 + r * dx
                p0 = (x, y)
                p1 = (x, y + dy)
                walls.append((p0, p1))
    for c in range(num_columns):
        for r in range(num_rows + 1):
            if not top_side_broken[r][c]:
                # Make this wall.
                x = x0 + c * dx
                y = y0 + r * dx
                p0 = (x, y)
                p1 = (x + dx, y)
                walls.append((p0, p1))

    return walls



class Node:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = []
        self.visited = False


class Link:
    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        self.tree_links = []
        self.walls = []

        self.window = tk.Tk()
        self.window.title("maze")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("420x280")

        # Parameters.
        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        r = 0
        pady = 2
        padx = 5
        num_rows_label = tk.Label(frame, text="# Rows:")
        num_rows_label.grid(padx=5, pady=pady, row=r, column=0, sticky=tk.W)
        self.num_rows_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_rows_entry.grid(padx=5, pady=pady, row=r, column=1)
        self.num_rows_entry.insert(tk.END, "10")

        r += 1
        num_columns_label = tk.Label(frame, text="# Columns:")
        num_columns_label.grid(padx=5, pady=pady, row=r, column=0, sticky=tk.W)
        self.num_columns_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_columns_entry.grid(padx=padx, pady=pady, row=r, column=1)
        self.num_columns_entry.insert(tk.END, "10")

        r += 1
        self.button_is_checked = tk.IntVar()
        self.button_is_checked.trace("w", self.is_checked_changed)
        self.show_tree_checkbutton = tk.Checkbutton(frame, text="Show Tree", variable=self.button_is_checked)
        self.show_tree_checkbutton.grid(padx=5, pady=pady, row=r, column=0, columnspan=2)

        r += 1
        self.go_button = tk.Button(frame, text="Go", width=8, command=self.go_click)
        self.go_button.grid(padx=padx, pady=pady+20, row=r, column=0, columnspan=2)

        # The drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, width=256, height=256)
        self.canvas.pack(padx=padx, pady=padx, side=tk.TOP)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.go_button: self.go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_rows_entry.focus_force()
        self.window.mainloop()

    def is_checked_changed(self, *args):
        self.draw_canvas()

    def go_click(self):
        """ Build the maze."""
        # Make the network.
        num_rows = int(self.num_rows_entry.get())
        num_columns = int(self.num_columns_entry.get())
        maze_nodes = make_network(num_rows, num_columns)

        # Find a random spanning tree.
        self.tree_links = find_spanning_tree(maze_nodes)

        # Build the walls.
        self.x0 = self.canvas.winfo_width() / (num_columns + 2)
        self.y0 = self.canvas.winfo_height() / (num_rows + 2)
        self.walls = build_walls(self.tree_links, num_rows, num_columns, self.x0, self.y0, self.x0, self.y0)

        # Draw the maze.
        self.draw_canvas()

    def draw_canvas(self):
        """ Draw the maze."""
        self.canvas.delete(tk.ALL)

        # Draw the walls.
        for wall in self.walls:
            self.canvas.create_line(wall[0][0], wall[0][1], wall[1][0], wall[1][1], fill="black")

        # Draw the spanning tree.
        if self.button_is_checked.get():
            for link in self.tree_links:
                x1 = self.x0 * (link.node1.column + 1.5)
                y1 = self.y0 * (link.node1.row + 1.5)
                x2 = self.x0 * (link.node2.column + 1.5)
                y2 = self.y0 * (link.node2.row + 1.5)
                self.canvas.create_line(x1, y1, x2, y2, fill="red")


if __name__ == '__main__':
    app = App()

# app.root.destroy()

