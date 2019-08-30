import tkinter as tk
from tkinter import ttk
import itertools


def find_eulerian_cycle(nodes):
    """ Find an Eulerian cycle in the network."""
    # Make a copy of the network and work with the copy.
    copy_nodes = clone_network(nodes)

    # Set the node indices.
    for i in range(len(nodes)):
        nodes[i].index = i
        copy_nodes[i].index = i

    # Start with a cycle that only includes the first node.
    copy_cycle = []
    copy_cycle.append(copy_nodes[0])

    # Repeat until all links have been removed.
    while True:
        # Find a node in the cycle that has unvisited links.
        start_index = -1
        for i in range(len(copy_cycle)):
            if len(copy_cycle[i].neighbors) > 0:
                start_index = i
                break

        # If there is no node with unvisited links, then we're done.
        if start_index < 0:
            break

        # Make a loop starting at this node.
        start_node = copy_cycle[start_index]
        new_cycle = find_loop(start_node)

        print(f"Old: {nodes_to_string(copy_cycle)}")
        print(f"New: {nodes_to_string(new_cycle)}")

        # Insert the new cycle before the node in the main loop.
        copy_cycle = copy_cycle[:start_index] + new_cycle + copy_cycle[start_index:]
        print(f"Res: {nodes_to_string(copy_cycle)}")
        print()

    # Convert the cycle in the copied network
    # into a cycle in the original network.
    cycle = []
    for i in range(len(copy_cycle)):
        cycle.append(nodes[copy_cycle[i].index])

    return cycle

def find_loop(start_node):
    """ Find a loop starting at the indicated node."""
    cycle = []
    current_node = start_node

    while True:
        cycle.append(current_node)

        # Move to a neighboring node.
        next_node = current_node.neighbors[0]
        del current_node.neighbors[0]
        next_node.neighbors.remove(current_node)
        current_node = next_node
        if current_node == start_node:
            break

    return cycle

def clone_network(nodes):
    """ Clone the network."""
    # Make a dictionary to hold the new nodes.
    node_dict = {}

    # Clone the nodes.
    new_nodes = [None for i in range(len(nodes))]
    for i in range(len(nodes)):
        old_node = nodes[i]
        new_node = Node(old_node.name, old_node.location)

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

def nodes_to_string(nodes):
    result = ""
    for node in nodes:
        result += " " + f"{node}"
    return result[1:]

def make_network1():
    """ Make the network."""
    node_a = Node("A", (20, 20))
    node_b = Node("B", (140, 20))
    node_c = Node("C", (80, 50))
    node_d = Node("D", (50, 80))
    node_e = Node("E", (110, 80))
    node_f = Node("F", (80, 110))
    node_g = Node("G", (20, 140))
    node_h = Node("H", (140, 140))

    node_a.add_link(node_b)
    node_a.add_link(node_c)
    node_a.add_link(node_d)
    node_a.add_link(node_g)

    node_b.add_link(node_c)
    node_b.add_link(node_e)
    node_b.add_link(node_h)

    node_c.add_link(node_d)
    node_c.add_link(node_e)

    node_d.add_link(node_f)
    node_d.add_link(node_g)

    node_e.add_link(node_f)
    node_e.add_link(node_h)

    node_f.add_link(node_g)
    node_f.add_link(node_h)

    node_g.add_link(node_h)

    return [ node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h ]

def make_network2():
    """ Build a network."""
    node_a = Node("A", (100, 20))
    node_b = Node("B", (100, 50))
    node_c = Node("C", (70, 80))
    node_d = Node("D", (130, 80))
    node_e = Node("E", (40, 110))
    node_f = Node("F", (100, 110))
    node_g = Node("G", (160, 110))
    node_h = Node("H", (70, 140))
    node_i = Node("I", (130, 140))
    node_j = Node("J", (100, 170))
    node_k = Node("K", (100, 200))

    node_a.add_link(node_c)
    node_a.add_link(node_d)

    node_b.add_link(node_c)
    node_b.add_link(node_d)

    node_c.add_link(node_e)
    node_c.add_link(node_f)

    node_d.add_link(node_f)
    node_d.add_link(node_g)

    node_e.add_link(node_h)

    node_f.add_link(node_h)
    node_f.add_link(node_i)

    node_g.add_link(node_i)

    node_h.add_link(node_j)
    node_h.add_link(node_k)

    node_i.add_link(node_j)
    node_i.add_link(node_k)


    return [ node_a, node_b, node_c, node_d, node_e, node_f, node_g, node_h, node_i, node_j, node_k ]


class Node:
    radius = 10

    def __init__(self, name, location):
        self.name = name
        self.location = location

        self.neighbors = []
        self.bg_color = "white"
        self.fg_color = "black"
        self.link_color = "blue"
        self.index = -1
        self.times_visited = 0

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
        self.window.title("hierholzers_algorithm")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("210x300")

        self.find_button = tk.Button(self.window, width=12, text="Find", command=self.find_cycle)
        self.find_button.pack(padx=5, pady=5)

        self.canvas = tk.Canvas(self.window, bg="white", width=10, height=10, borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, expand=True, fill=tk.BOTH)

        self.cycle_entry = tk.Entry(self.window, borderwidth=2, relief=tk.SUNKEN, justify=tk.LEFT)
        self.cycle_entry.pack(padx=5, pady=5, fill=tk.BOTH)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.find_button: self.find_button.invoke()))

        # Make the network.
        #self.nodes = make_network1()
        self.nodes = make_network2()
        self.draw_network()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def find_cycle(self):
        """ Find an Eulerian cycle."""
        self.cycle_entry.delete(0, tk.END)

        # Find an Eulerian cycle.
        cycle = find_eulerian_cycle(self.nodes)

        # Show the nodes in the cycle.
        self.cycle_entry.insert(tk.END, nodes_to_string(cycle))
        
        # Validate the cycle. If a node has N neighbors,
        # then it should be visited N / 2 times.
        # Except for the start node,
        # which is visited an extra time.
        for node in self.nodes:
            node.times_visited = 0
        for i in range(len(cycle)):
            self.nodes[cycle[i].index].times_visited += 1
        for node in self.nodes:
            print(f"{node}: Visited {node.times_visited} times")

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
