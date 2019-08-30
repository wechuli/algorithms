import tkinter as tk
from tkinter import ttk
import itertools


class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location

        self.neighbors = []
        self.bg_color = "white"
        self.fg_color = "black"
        self.link_color = "blue"

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
        self.window.title("find_clique_brute_force")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("260x245")

        frame1 = tk.Frame(self.window)
        frame1.pack(side=tk.TOP, fill=tk.X)
        label = tk.Label(frame1, text="Clique Size:")
        label.pack(side=tk.LEFT)
        self.clique_size_entry = tk.Entry(frame1, width=3, justify=tk.RIGHT)
        self.clique_size_entry.pack(padx=5, pady=5, side=tk.LEFT)
        self.clique_size_entry.insert(tk.END, "4")

        self.find_button = tk.Button(frame1, width=12, text="Find", command=self.find_clique_click)
        self.find_button.pack(padx=5, pady=5, side=tk.LEFT)

        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

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
        self.clique_size_entry.focus_force()
        self.window.mainloop()

    def find_clique_click(self):
        """ Find the clique."""
        size = int(self.clique_size_entry.get())
        clique = self.find_clique(self.nodes, size)

        # Color the clique.
        for node in self.nodes:
            node.fg_color = "black"
            node.bg_color = "white"
        for node in clique:
            node.fg_color = "red"
            node.bg_color = "pink"
        self.draw_network()

    def find_clique(self, nodes, size):
        """ Find a clique of the given size."""
        for combination in itertools.combinations(nodes, size):
            if self.is_clique(combination):
                return combination
        return []

    def is_clique(self, nodes):
        """ Return true if the nodes form a clique."""
        num_nodes = len(nodes)
        for i in range(num_nodes):
            for j in range(i + 1, num_nodes):
                if nodes[j] not in nodes[i].neighbors:
                    return False
        return True

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

