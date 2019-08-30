import tkinter as tk
from tkinter import ttk
import math
import time
import random

class Node:
    def __init__(self, location):
        self.location = location
        self.links = []
        self.visited = False


class Link:
    def __init__(self, node1, node2, length):
        self.node1 = node1
        self.node2 = node2
        self.length = length

    def draw(self, canvas, color):
        canvas.create_line( \
            self.node1.location.x, self.node1.location.y, \
            self.node2.location.x, self.node2.location.y, \
            fill=color)


def distance(point1, point2):
    """ Return the distance between two points."""
    dx = point1.x - point2.x
    dy = point1.y - point2.y
    return math.hypot(dx, dy)

def find_emst(points):
    """ Find a Eucliden minimum spanning tree for the points."""
    result = []
    if len(points) < 2:
        return []
    # Build the nodes.
    num_nodes = len(points)
    nodes = []
    for i in range(num_nodes):
        nodes.append(Node(points[i]))

    # Build the links.
    for i in range(num_nodes):
        for j in range(i + 1, num_nodes, 1):
            length = distance(points[i], points[j])
            link = Link(nodes[i], nodes[j], length)
            nodes[i].links.append(link)
            nodes[j].links.append(link)

    # Make a candidate list.
    root = nodes[0]
    candidates = root.links.copy()

    # Build the EMST.
    results = []
    while len(candidates) > 0:
        # Find the shortest candidate.
        best_length = 1000000
        best_link = None
        for link in candidates:
            if link.length < best_length:
                best_length = link.length
                best_link = link

        # Use this candidate.
        results.append(best_link)

        # See which node is not yet in the tree.
        new_node = best_link.node1
        if new_node.visited:
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

    return results

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.points = []
        self.links = []

        self.window = tk.Tk()
        self.window.title("euclidean_minimum_spanning_tree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("350x350")

        # The drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, side=tk.BOTTOM)
        self.go_button = tk.Button(frame, text="Go", width=8, command=self.go_click)
        self.go_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.clear_button = tk.Button(frame, text="Clear", width=8, command=self.clear_click)
        self.clear_button.pack(padx=5, pady=5, side=tk.LEFT)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.go_button: self.go_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=self.clear_button: self.clear_button.invoke())) 

        # Track mouse clicks.
        self.canvas.bind("<Button-1>", self.mouse_click)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def mouse_click(self, event):
        self.points.append(event)
        self.draw_canvas()

    def go_click(self):
        """ Find the Euclidean minimum spanning tree."""
        self.links = find_emst(self.points)
        self.draw_canvas()

    def clear_click(self):
        """ Clear the points and links."""
        self.points = []
        self.links = []
        self.draw_canvas()

    def draw_canvas(self):
        """ Draw the points and tree if it exists."""
        self.canvas.delete(tk.ALL)

        # Draw the links.
        for link in self.links:
            link.draw(self.canvas, "black")

        # Draw the points.
        for i in range(len(self.points)):
            self.draw_circle(self.points[i], 5, "lightblue", "blue")

    def draw_circle(self, center, radius, bg_color, fg_color):
        """ Draw a circle."""
        self.canvas.create_oval( \
            center.x - radius, center.y - radius, \
            center.x + radius, center.y + radius, \
            fill=bg_color, outline=fg_color)

if __name__ == '__main__':
    app = App()

# app.root.destroy()

