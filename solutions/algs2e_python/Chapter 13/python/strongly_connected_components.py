import tkinter as tk
from tkinter import ttk
import math
import time
import random

class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.links = []
        self.in_links = []

        self.bg_color = "lightblue"
        self.name_color = "black"
        self.circle_color = "blue"
        self.visited = False
        self.component_root = None

    def add_link(self, other):
        """ Add a link to this node."""
        self.links.append(Link(self, other))

    def draw_links(self, canvas):
        """ Draw this node's links."""
        for link in self.links:
            link.draw(canvas)

    def draw_node(self, canvas):
        """ Draw this node's body."""
        canvas.create_oval( \
            self.location[0] - Node.radius, \
            self.location[1] - Node.radius, \
            self.location[0] + Node.radius, \
            self.location[1] + Node.radius, \
            fill=self.bg_color, outline=self.circle_color)
        canvas.create_text(self.location[0], self.location[1], \
            text=self.name, fill=self.name_color)


class Link:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self.color = "blue"

    def draw(self, canvas):
        draw_arrow(canvas, self.from_node.location, self.to_node.location, Node.radius, self.color)


def draw_arrow(canvas, point1, point2, radius, color):
    """ Draw an arrow between two nodes."""
    # Find the end points.
    dx = point2[0] - point1[0]
    dy = point2[1] - point1[1]
    length = math.sqrt(dx * dx + dy * dy)
    dx /= length
    dy /= length
    x2 = point2[0] - dx * radius
    y2 = point2[1] - dy * radius
    x1 = x2 - radius * dx + radius * dy / 2
    y1 = y2 - radius * dy - radius * dx / 2
    x3 = x2 - radius * dx - radius * dy / 2
    y3 = y2 - radius * dy + radius * dx / 2
    canvas.create_polygon(x1, y1, x2, y2, x3, y3, fill=color)
    canvas.create_line(point1[0], point1[1], point2[0], point2[1], fill=color)


def draw_network(nodes, canvas):
    """ Draw a network on a canvas."""
    if nodes == None:
        return
    canvas.delete(tk.ALL)

    for node in nodes:
        node.draw_links(canvas)
    for node in nodes:
        node.draw_node(canvas)


def set_strongly_connected_components(nodes):
    """ Find the strongly connected components."""
    # Clear each node's visited,
    # component_root, and in_links values.
    for node in nodes:
        node.visited = False
        node.component_root = None
        node.in_links = []

    # Set each node's in_links.
    for node in nodes:
        for link in node.links:
            to_node = link.to_node
            to_node.in_links.append(Link(node, to_node))

    # Make a list to hold visited nodes.
    visited_nodes = []

    # Visit each node.
    for node in nodes:
        visit(node, visited_nodes)

    # Add the nodes to components.
    for node in visited_nodes:
        assign(node, node)


def visit(node, visited_nodes):
    """ Recursively visit nodes that are reachable from this one."""
    if node.visited:
        return

    node.visited = True
    for link in node.links:
        visit(link.to_node, visited_nodes)
    visited_nodes.insert(0, node)


def assign(node, root):
    """ Recursively assign nodes to a component root."""
    if node.component_root != None:
        return

    node.component_root = root
    for link in node.in_links:
        assign(link.from_node, root)


def color_components(nodes):
    """ Color the strongly connected components."""
    # Color the nodes.
    colors = [ "pink", "yellow", "lightblue", "lime", "white", "lightgreen", "orange", "magenta", "cyan" ]
    root_colors = { }

    for node in nodes:
        if not (node.component_root in root_colors):
            root_colors[node.component_root] = colors[len(root_colors)]
        node.bg_color = root_colors[node.component_root]


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("strongly_connected_components")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("275x320")

        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, width=256, height=256)
        self.canvas.pack(padx=5, pady=5, side=tk.TOP)

        self.go_button = tk.Button(self.window, width=15, text="Find Components", command=self.go_click)
        self.go_button.pack(padx=5, pady=5, side=tk.TOP)

        # Make the network.
        node_a = Node("A", (27, 36))
        node_b = Node("B", (80, 35))
        node_c = Node("C", (20, 104))
        node_d = Node("D", (70, 140))
        node_e = Node("E", (131, 155))
        node_f = Node("F", (109, 202))
        node_g = Node("G", (170, 210))
        node_h = Node("H", (130, 45))
        node_i = Node("I", (206, 18))
        node_j = Node("J", (230, 83))
        node_k = Node("K", (188, 60))
        node_l = Node("L", (180, 120))
        node_m = Node("M", (210, 180))
        node_a.add_link(node_b)
        node_a.add_link(node_c)
        node_b.add_link(node_d)
        node_b.add_link(node_e)
        node_c.add_link(node_d)
        node_d.add_link(node_a)
        node_d.add_link(node_e)
        node_e.add_link(node_g)
        node_g.add_link(node_f)
        node_f.add_link(node_e)
        node_h.add_link(node_l)
        node_i.add_link(node_h)
        node_i.add_link(node_k)
        node_j.add_link(node_i)
        node_k.add_link(node_j)
        node_l.add_link(node_e)
        node_l.add_link(node_g)
        node_l.add_link(node_k)
        node_m.add_link(node_l)
        self.nodes = [ node_a, node_b, node_c, node_d, node_e, node_f, \
            node_g, node_h, node_i, node_j, node_k, node_l, node_m ]

        # Draw the original and cloned networks.
        draw_network(self.nodes, self.canvas)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.go_button: self.go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def go_click(self):
        """ Find the strongly connected components."""
        # Find the strongly connected components.
        set_strongly_connected_components(self.nodes)

        # Color the strongly connected components.
        color_components(self.nodes)

        # Redraw the network.
        draw_network(self.nodes, self.canvas)


if __name__ == '__main__':
    app = App()

# app.root.destroy()

