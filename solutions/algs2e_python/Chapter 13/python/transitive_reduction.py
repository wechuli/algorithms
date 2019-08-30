import tkinter as tk
from tkinter import ttk
import math
import time
import random


infinity = 1000000


class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location
        self.links = []
        self.index = -1

    def add_link(self, other):
        """ Add a link to this node."""
        self.links.append(Link(self, other))

    def draw_links(self, canvas):
        """ Draw this node's links."""
        for link in self.links:
            link.draw(canvas, Node.radius)

    def draw_node(self, canvas):
        """ Draw this node's body."""
        x0 = self.location[0] - Node.radius
        y0 = self.location[1] - Node.radius
        x1 = x0 + 2 * Node.radius
        y1 = y0 + 2 * Node.radius
        canvas.create_oval(x0, y0, x1, y1, fill="lightblue", outline="blue")
        canvas.create_text(self.location[0], self.location[1], text=self.name, fill="black")

    def is_at_point(self, point):
        """ Return true if the node is at this point."""
        dx = self.location[0] - point[0]
        dy = self.location[1] - point[1]
        return math.sqrt(dx * dx + dy * dy) <= Node.radius


class Link:
    def __init__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        dx = from_node.location[0] - to_node.location[0]
        dy = from_node.location[1] - to_node.location[1]
        self.length = math.sqrt(dx * dx + dy * dy)

    def draw(self, canvas, radius):
        """ Draw an arrow between two nodes."""
        # Find the end points.
        dx = self.to_node.location[0] - self.from_node.location[0]
        dy = self.to_node.location[1] - self.from_node.location[1]
        length = math.sqrt(dx * dx + dy * dy)
        dx /= length
        dy /= length
        end1 = (
            self.from_node.location[0] + dx * radius,
            self.from_node.location[1] + dy * radius)
        end2 = (
            self.to_node.location[0] - dx * radius,
            self.to_node.location[1] - dy * radius)
        canvas.create_line(end1[0], end1[1], end2[0], end2[1], fill="blue")
        arrowhead = [
            end2[0] - radius * dx + radius * dy / 2,
            end2[1] - radius * dy - radius * dx / 2,
            end2[0],
            end2[1],
            end2[0] - radius * dx - radius * dy / 2,
            end2[1] - radius * dy + radius * dx / 2]
        canvas.create_polygon(arrowhead, fill="blue")



class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("transitive_reduction")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x300")
        self.window.columnconfigure(0, weight=1)
        self.window.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.grid(padx=5, pady=5, row=0, column=0, sticky=tk.NSEW)

        find_reduction_button = tk.Button(self.window, text="Find Reduction", command=self.find_reduction)
        find_reduction_button.grid(padx=5, pady=5, row=1, column=0)

        # Build and display the network.
        self.build_network()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=find_reduction_button: find_reduction_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        find_reduction_button.focus_force()
        self.window.mainloop()

    def find_reduction(self):
        """ Find the transitive reduction."""
        # Find the transitive reduction.
        self.find_transitive_reduction(self.nodes, self.distances)

        # Find all pairs shortest paths.
        self.diistances, self.via = self.find_all_pair_paths(self.nodes)

        # Print the reachability matrix.
        self.print_reachability_matrix(self.nodes, self.distances)

        # Redraw the network.
        self.draw_canvas()

    def find_transitive_reduction(self, nodes, distances):
        """ Find the transitive reduction."""
        num_nodes = len(nodes)

        # Remove self-links.
        for i in range(num_nodes):
            distances[i][i] = infinity

        # Remove other unnecessary links.
        for i in range(num_nodes):
            for j in range(num_nodes):
                # Consider link i --> j.
                if distances[i][j] < infinity:
                    # See if there is a node k with
                    # paths i --> k and k --> j.
                    for k in range(num_nodes):
                        if (distances[i][k] < infinity and distances[k][j] < infinity):
                            distances[i][j] = infinity
                            break

        # Update the nodes to remove unnecessary links.
        for node in nodes:
            for i in range(len(node.links) - 1, -1, -1):
                link = node.links[i]
                from_index = link.from_node.index
                to_index = link.to_node.index
                if distances[from_index][to_index] >= infinity:
                    del node.links[i]

    def build_network(self):
        # Build and display the network.
        self.nodes = []

        # Build the first network.
        node_a = Node("A", (130, 40))
        node_b = Node("B", (60, 90))
        node_c = Node("C", (200, 90))
        node_d = Node("D", (40, 150))
        node_e = Node("E", (200, 150))
        node_f = Node("F", (100, 210))
        node_a.add_link(node_c)
        node_a.add_link(node_d)
        node_a.add_link(node_e)
        node_b.add_link(node_d)
        node_b.add_link(node_e)
        node_b.add_link(node_f)
        node_c.add_link(node_d)
        node_c.add_link(node_e)
        node_c.add_link(node_f)
        node_e.add_link(node_f)
        self.nodes = [ node_a, node_b, node_c, node_d, node_e, node_f ]

        # Set the node indices.
        for i in range(len(self.nodes)):
            self.nodes[i].index = i

        # Find all pairs shortest paths.
        self.distances, self.via = self.find_all_pair_paths(self.nodes)

        # Print the reachability matrix.
        self.print_reachability_matrix(self.nodes, self.distances)

        # Draw the network.
        self.draw_canvas()

    def draw_canvas(self):
        """ Draw the network."""
        self.canvas.delete(tk.ALL)

        # Draw the links.
        for node in self.nodes:
            node.draw_links(self.canvas)

        # Draw the nodes.
        for node in self.nodes:
            node.draw_node(self.canvas)

    def find_all_pair_paths(self, nodes):
        """ Find all pairs shortest paths."""
        # Create the distance and via arrays.
        num_nodes = len(nodes)

        # Initialize the distance array.
        distances = [[infinity for i in range(num_nodes)] for j in range(num_nodes)]
        for i in range(num_nodes):
            distances[i][i] = 0
        for node in nodes:
            for link in node.links:
                from_node = link.from_node.index
                to_node = link.to_node.index
                if distances[from_node][to_node] > link.length:
                    distances[from_node][to_node] = link.length

        # Initialize the via array.
        via = [[-1 for i in range(num_nodes)] for j in range(num_nodes)]

        # Set via[i][j] = j if there is a link from i to j.
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distances[i][j] < infinity:
                    via[i][j] = j

        # Find improvements.
        for via_node in range(0, num_nodes):
            for from_node in range(0, num_nodes):
                for to_node in range(num_nodes):
                    new_dist = \
                        distances[from_node][via_node] + \
                        distances[via_node][to_node]
                    if new_dist < distances[from_node][to_node]:
                        # This is an improved path. Update it.
                        distances[from_node][to_node] = new_dist
                        via[from_node][to_node] = via_node

        return distances, via

    def print_reachability_matrix(self, nodes, distances):
        """ Print the reachability matrix."""
        num_nodes = len(distances)

        # Write node names across the top.
        print("   ", end="")
        for c in range(num_nodes):
            print(f" {self.nodes[c].name} ", end="")
        print()

        for r in range(num_nodes):
            print(f"{self.nodes[r].name}: ", end="")
            for c in range(num_nodes):
                if distances[r][c] < infinity:
                    print(" X ", end="")
                else:
                    print("   ", end="")
            print()


if __name__ == '__main__':
    app = App()

# app.root.destroy()

