import tkinter as tk
from tkinter import ttk
import itertools


""" Search for #@ to find statements that print information about the calls to the algorithm."""


def print_set(s):
    """ Return a string holding the items in the set."""
    if len(s) == 0:
        return "{ }"

    txt = ""
    for item in s:
        txt += f", {item}"
    return "{" + txt[2:] + "}"

def bron_kerbosch(R, P, X):
    """ Find maximal cliques for these sets."""
    #@ print(f"BK - R: {print_set(R)}, P: {print_set(P)}, X: {print_set(X)}")
    results = []

    # See if P and X are both empty.
    if (len(P) == 0) and (len(X) == 0):
        # R is a maximal clique.
        results.append(R.copy())
        #@ print(f"Maximal: {print_set(R)}")

    for node in P.copy():
        # Make the recursive call.
        new_R = R.copy()
        new_R.add(node)
        new_P = neighbors(node, P)
        new_X = neighbors(node, X)
        results.extend(bron_kerbosch(new_R, new_P, new_X))

        # Update P and X.
        P.remove(node)
        X.add(node)

    return results

def neighbors(node, test_set):
    """ Return the neighbors of this node that are within test_set."""
    result = set()
    for  neighbor in node.neighbors:
        if neighbor in test_set:
            result.add(neighbor)
    return result


class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location

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
        self.window.title("find_clique_bron_kerbosch")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("600x300")

        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill=tk.BOTH)
        frame.columnconfigure(0, weight=1, uniform="columns")
        frame.columnconfigure(1, weight=1, uniform="columns")
        frame.rowconfigure(1, weight=1, uniform="rows")

        self.find_button = tk.Button(frame, width=12, text="Find", command=self.find_clique_click)
        self.find_button.grid(padx=5, pady=5, row=0, column=0, columnspan=2)

        self.canvas = tk.Canvas(frame, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.grid(padx=(5, 2), pady=5, row=1, column=0, sticky=tk.NSEW)

        self.clique_list = tk.Listbox(frame, borderwidth=2, relief=tk.SUNKEN)
        self.clique_list.grid(padx=(5, 2), pady=5, row=1, column=1, sticky=tk.NSEW)

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

    def find_clique_click(self):
        """ Find maximal cliques."""
        self.clique_list.delete(0, tk.END)

        # Make the initial sets of nodes.
        R = set()
        P = set(self.nodes)
        X = set()

        # Find the cliques.
        cliques = bron_kerbosch(R, P, X)

        # List the cliques.
        for clique in cliques:
            txt = ""
            for node in clique:
                txt += f"{node} "
            self.clique_list.insert(tk.END, txt)

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
