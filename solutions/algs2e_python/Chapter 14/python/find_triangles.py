import tkinter as tk
from tkinter import ttk
import itertools


def find_all_triangles(nodes):
    """ Find the network's triangles."""
    results = []

    # Iterate over the nodes.
    for node in nodes:
        # Mark the node's neighbors.
        mark_neighbors(node, True)

        # Check each neighbor to see if it forms a
        # triangle with this node.
        for nbr in node.neighbors:
            if nbr.name <= node.name:
                continue

            for nbr_nbr in nbr.neighbors:
                if nbr_nbr.name <= node.name:
                    continue
                if nbr_nbr.name <= nbr.name:
                    continue
                if nbr_nbr.marked:
                    results.append([node, nbr, nbr_nbr])

        # Unark the node's neighbors.
        mark_neighbors(node, False)

    return results

def mark_neighbors(node, marked):
    """ Mark this node's neighbors."""
    for neighbor in node.neighbors:
        neighbor.marked = marked


class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.marked = False

        self.neighbors = []
        self.bg_color = "white"
        self.fg_color = "black"
        self.link_color = "blue"

    def __str__(self):
        return self.name

    def add_link(self, other):
        """ Add an undirected link between these nodes."""
        self.neighbors.append(other)
        other.neighbors.append(self)

    def draw_links(self, canvas):
        """ Draw the node's links."""
        for neighbor in self.neighbors:
            # Draw each link only once.
            if self.name < neighbor.name:
                canvas.create_line(self.location, neighbor.location, fill=self.link_color)

    def draw_node(self, canvas):
        """ Draw this node's body."""
        canvas.create_oval( \
            self.location[0] - Node.radius, \
            self.location[1] - Node.radius, \
            self.location[0] + Node.radius, \
            self.location[1] + Node.radius, \
            fill=self.bg_color, outline=self.fg_color)
        canvas.create_text(self.location[0], self.location[1], \
            text=self.name, fill=self.fg_color)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("find_triangles")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("360x300")

        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill=tk.BOTH)
        frame.columnconfigure(0, weight=1)
        frame.rowconfigure(1, weight=1, uniform="rows")

        self.find_button = tk.Button(frame, width=12, text="Find", command=self.find_triangles_click)
        self.find_button.grid(padx=5, pady=5, row=0, column=0, columnspan=2)

        self.canvas = tk.Canvas(frame, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.grid(padx=(5, 2), pady=5, row=1, column=0, sticky=tk.NSEW)

        list_frame = tk.Frame(frame, borderwidth=2, relief=tk.SUNKEN)
        list_frame.grid(padx=(2, 5), pady=5, row=1, column=1, sticky=tk.NS)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.triangles_list = tk.Listbox(list_frame, width=8)
        self.triangles_list.pack(fill=tk.BOTH, expand=True)

        # Attach the scrollbar to the listbox.
        self.triangles_list.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.triangles_list.yview)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.find_button: self.find_button.invoke()))

        # Make the network.
        node_a = Node("A", (60, 20))
        node_b = Node("B", (200, 20))
        node_c = Node("C", (130, 70))
        node_d = Node("D", (90, 110))
        node_e = Node("E", (170, 110))
        node_f = Node("F", (40, 170))
        node_g = Node("G", (220, 170))

        node_a.add_link(node_b)
        node_a.add_link(node_c)
        node_a.add_link(node_d)
        node_a.add_link(node_f)

        node_b.add_link(node_c)
        node_b.add_link(node_e)
        node_b.add_link(node_g)

        node_c.add_link(node_d)
        node_c.add_link(node_e)

        node_d.add_link(node_e)
        node_d.add_link(node_f)
        node_d.add_link(node_g)

        node_e.add_link(node_f)
        node_e.add_link(node_g)

        node_f.add_link(node_g)

        self.nodes = [ node_a, node_b, node_c, node_d, node_e, node_f, node_g ]

        self.draw_network()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def find_triangles_click(self):
        """ Find triangles."""
        self.triangles_list.delete(0, tk.END)

        # Find the triangles.
        triangles = find_all_triangles(self.nodes)

        # List the triangles.
        for triangle in triangles:
            txt = f"{triangle[0]} {triangle[1]} {triangle[2]}"
            self.triangles_list.insert(tk.END, txt)

        print(f"Found {len(triangles)} triangles")

    def draw_network(self):
        """ Draw the network."""
        self.canvas.delete(tk.ALL)
        for node in self.nodes:
            node.draw_links(self.canvas)
        for node in self.nodes:
            node.draw_node(self.canvas)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
