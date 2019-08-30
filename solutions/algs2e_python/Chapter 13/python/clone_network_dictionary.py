import tkinter as tk
from tkinter import ttk
import math
import time
import random

class Node:
    radius = 10

    def __init__(self, name, location, bg_color, name_color, circle_color, link_color):
        self.name = name
        self.location = location
        self.neighbors = []
        self.bg_color = bg_color
        self.name_color = name_color
        self.circle_color = circle_color
        self.link_color = link_color

    def draw_links(self, canvas):
        """ Draw this node's links."""
        for neighbor in self.neighbors:
            draw_arrow(canvas, self.location, neighbor.location, Node.radius, self.link_color)

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


def clone_network(nodes):
    """ Clone the network."""
    # Make a dictionary to hold the new nodes.
    node_dict = {}

    # Clone the nodes.
    new_nodes = [None for i in range(len(nodes))]
    for i in range(len(nodes)):
        old_node = nodes[i]
        new_node = Node(old_node.name.lower(), old_node.location, "pink", "black", "red", "red")
        new_nodes[i] = new_node
        node_dict[old_node] = new_node

    # Clone the links.
    for i in range(len(nodes)):
        old_node = nodes[i]
        new_node = new_nodes[i]
        for neighbor in old_node.neighbors:
            new_neighbor = node_dict[neighbor]
            new_node.neighbors.append(new_neighbor)

    return new_nodes


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        self.tree_links = []
        self.walls = []

        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("clone_network_dictionary")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("550x280")

        canvas1 = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, width=256, height=256)
        canvas1.pack(padx=5, pady=5, side=tk.LEFT)
        canvas2 = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, width=256, height=256)
        canvas2.pack(padx=5, pady=5, side=tk.LEFT)

        # Make the network.
        node_a = Node("A", (40, 80), "lightblue", "black", "blue", "blue")
        node_b = Node("B", (120, 30), "lightblue", "black", "blue", "blue")
        node_c = Node("C", (230, 75), "lightblue", "black", "blue", "blue")
        node_d = Node("D", (180, 140), "lightblue", "black", "blue", "blue")
        node_e = Node("E", (230, 190), "lightblue", "black", "blue", "blue")
        node_f = Node("F", (160, 225), "lightblue", "black", "blue", "blue")
        node_g = Node("G", (120, 120), "lightblue", "black", "blue", "blue")
        node_h = Node("H", (60, 215), "lightblue", "black", "blue", "blue")
        node_i = Node("I", (25, 145), "lightblue", "black", "blue", "blue")
        node_a.neighbors.append(node_b)
        node_a.neighbors.append(node_g)
        node_b.neighbors.append(node_c)
        node_c.neighbors.append(node_g)
        node_c.neighbors.append(node_d)
        node_g.neighbors.append(node_a)
        node_g.neighbors.append(node_f)
        node_a.neighbors.append(node_b)
        node_d.neighbors.append(node_e)
        node_e.neighbors.append(node_d)
        node_e.neighbors.append(node_f)
        node_h.neighbors.append(node_i)
        nodes1 = [ node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h, node_i ]

        # Clone.
        nodes2 = clone_network(nodes1)

        # Draw the original and cloned networks.
        draw_network(nodes1, canvas1)
        draw_network(nodes2, canvas2)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


    def draw_canvas(self):
        """ Draw the maze."""
        canvas.delete(tk.ALL)

        # Draw the walls.
        for wall in self.walls:
            canvas.create_line(wall[0][0], wall[0][1], wall[1][0], wall[1][1], fill="black")

        # Draw the spanning tree.
        if self.button_is_checked.get():
            for link in self.tree_links:
                x1 = self.x0 * (link.node1.column + 1.5)
                y1 = self.y0 * (link.node1.row + 1.5)
                x2 = self.x0 * (link.node2.column + 1.5)
                y2 = self.y0 * (link.node2.row + 1.5)
                canvas.create_line(x1, y1, x2, y2, fill="red")


if __name__ == '__main__':
    app = App()

# app.root.destroy()

