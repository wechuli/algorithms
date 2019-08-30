import sys
import tkinter as tk
from tkinter import ttk
import math
import time
import random
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


ord_a = ord("A")
infinity = 1000000

def beep():
    print("\a", end="")
    sys.stdout.flush()

def number_to_letters(number):
    """ Return a number converted into letters as in A, B, C, ..., AA, AB, AC, ..., BA, BB, BC, ..."""
    result = ""
    while True:
        letter_num = number % 26
        number //= 26
        ch = chr(ord_a + letter_num)
        result = ch + result
        if number <= 0:
            break
    return result

def array_to_string(array, pad, as_letter):
    """ Return a string representation of a two-dimensional array."""
    txt = ""
    num_rows = len(array)
    num_cols = len(array[0])
    for r in range(num_rows):
        for c in range(num_cols):
            value = ""
            if ((array[r][c] == infinity) or (array[r][c] < 0)):
                value = "-"
            elif as_letter:
                value = number_to_letters(array[r][c])
            else:
                value = f"{array[r][c]}"
            txt += value.rjust(pad)
        txt += "\n"
    return txt


class Modes:
    """ What the user is doing on the PictureBox."""
    none = 0
    add_node = 1
    add_link1 = 2
    add_link2 = 3
    df_traversal = 4
    bf_traversal = 5
    spanning_tree = 6
    minimal_spanning_tree = 7
    any_path = 8
    label_setting_tree = 9
    label_setting_path = 10
    label_correcting_tree = 11
    label_correcting_path = 12
    connected_components = 13
    all_pairs = 14


def draw_arrowhead(canvas, color, head, nx, ny, length):
    """ Draw an arrowhead at the given point in the normalized direction <nx, ny>."""
    ax = length * (-ny - nx)
    ay = length * (nx - ny)
    points = \
    [
        head[0] + ax, head[1] + ay,
        head[0], head[1],
        head[0] - ay, head[1] + ax
    ]
    canvas.create_polygon(points, fill=color)


class Node:
    radius = 11
    radius_squared = radius * radius

    def __init__(self, name, location, index):
        self.name = name
        self.text = name
        self.location = location
        self.index = index
        self.links = []

        # Properties used by algorithms.
        self.visited = False

        # The node and link before this one in a spanning tree or path.
        self.from_node = None
        self.from_link = None

        # The distance from the root node to this node.
        self.distance = -1

    def __str__(self):
        """ Return the node's current text."""
        return self.name

    def draw(self, canvas, show_text, fill_color, outline_color, text_color):
        """ Draw the node."""
        # Fill and outline the node.
        x0 = self.location[0] - Node.radius
        y0 = self.location[1] - Node.radius
        x1 = self.location[0] + Node.radius
        y1 = self.location[1] + Node.radius
        canvas.create_oval(x0, y0, x1, y1, fill=fill_color, outline=outline_color)

        # Draw the node's current text.
        if ((show_text) and (self.text != None)):
            canvas.create_text(self.location[0], self.location[1], text=self.text, fill=text_color)
        else:
            canvas.create_text(self.location[0], self.location[1], text=self.name, fill=text_color)

    def is_at(self, location):
        """ Return True if the node is at the indicated location."""
        dx = self.location[0] - location[0]
        dy = self.location[1] - location[1]
        return dx * dx + dy * dy <= Node.radius_squared

    def add_link_to(self, node):
        """ Add a link to the indicated node."""
        Link(self, node)


class Link:
    def __init__(self, node0, node1):
        self.node0 = node0
        self.node1 = node1
        self.visited = False

        dx = node0.location[0] - node1.location[0]
        dy = node0.location[1] - node1.location[1]
        self.cost = int(math.sqrt(dx * dx + dy * dy))
        self.capacity = random.randint(1, 4) + random.randint(0, 2)

    def __str__(self):
        """ Return the names of the nodes."""
        return f"{self.node0.name} --> {self.node1.name}"
	
    def draw(self, canvas, show_costs, show_capacities, link_width, line_color, text_color):
        """ Draw the link."""
        dx = self.node1.location[0] - self.node0.location[0]
        dy = self.node1.location[1] - self.node0.location[1]
        dist = math.sqrt(dx * dx + dy * dy)
        nx = dx / dist
        ny = dy / dist
        head = (
            self.node1.location[0] - Node.radius * nx,
            self.node1.location[1] - Node.radius * ny)

        # Draw the link.
        canvas.create_line(
            self.node0.location[0],
            self.node0.location[1],
            self.node1.location[0],
            self.node1.location[1],
            fill=line_color, width=link_width)
        draw_arrowhead(canvas, line_color, head, nx, ny, Node.radius / 2)

        # Draw the link's cost.
        if show_costs:
            dx *= 3 * Node.radius / dist
            dy *= 3 * Node.radius / dist
            x = self.node0.location[0] + dx
            y = self.node0.location[1] + dy
            canvas.create_text(x, y, text=f"{self.cost}")

        # Draw the link's capacity.
        if show_capacities:
            dx *= 3 * Node.radius / dist
            dy *= 3 * Node.radius / dist
            x = self.node0.location[0] + dx
            y = self.node0.location[1] + dy
            canvas.create_text(x, y, text=f"{self.capacity}")


class Network:
    def __init__(self):
        # A list holding all nodes.
        self.all_nodes = []

    def save_network(self, filename):
        """ Save the network into the file."""
        with open(filename, "w") as output:
            # Save the number of nodes.
            output.write(f"{len(self.all_nodes)}" + "\n")

            # Renumber the nodes.
            for i in range(len(self.all_nodes)):
                self.all_nodes[i].index = i

            # Save the node information.
            for node in self.all_nodes:
                # Save this node's information.
                output.write(f"{node.name},{node.location[0]},{node.location[1]}")

                # Save information about this node's links.
                for link in node.links:
                    other_node = link.node0
                    if (link.node0 == node):
                        other_node = link.node1
                    output.write(f",{other_node.index},{link.cost},{link.capacity}")
                output.write("\n")

    @staticmethod
    def load_network(filename):
        """ Create a network from a network file."""
        # Make a new network.
        network = Network()

        # Read the data.
        with open(filename, "r") as input:
            all_text = input.read()
        all_lines = all_text.split("\n")

        # Get the number of nodes.
        num_nodes = int(all_lines[0])

        # Create the nodes.
        for i in range(num_nodes):
            network.all_nodes.append(Node("*", (-1, -1), i))

        # Read the nodes.
        for i in range(1, num_nodes + 1):
            node = network.all_nodes[i - 1]
            node_fields = all_lines[i].split(",")

            # Get the node's text and coordinates.
            name = node_fields[0]
            location = (
                int(node_fields[1]),
                int(node_fields[2])
            )
            node.name = name
            node.text = name
            node.location = location

            # Get the node's links.
            for j in range(3, len(node_fields), 3):
                # Get the next link.
                index = int(node_fields[j])
                link = Link(node, network.all_nodes[index])
                link.cost = int(node_fields[j + 1])
                link.capacity = int(node_fields[j + 2])
                node.links.append(link)

        return network

    def draw(self, canvas, show_node_text, show_costs, show_capacities,
        link_width, link_color, link_text_color, link_width2, link_color2, link_text_color2,
        node_fill_color, node_outline_color, node_text_color,
        node_fill_color2, node_outline_color2, node_text_color2):
        """ Draw the network."""
        # Draw the non-highlighted links.
        for node in self.all_nodes:
            for link in node.links:
                if not link.visited:
                    link.draw(canvas, show_costs, show_capacities, link_width, link_color, link_text_color2)

        # Draw the highlighted links.
        for node in self.all_nodes:
            for link in node.links:
                if link.visited:
                    link.draw(canvas, show_costs, show_capacities, link_width2, link_color2, link_text_color2)

        # Draw the non-highlighted nodes.
        for node in self.all_nodes:
            if not node.visited:
                node.draw(canvas, show_node_text, node_fill_color, node_outline_color, node_text_color)

        # Draw the highlighted nodes.
        for node in self.all_nodes:
            if node.visited:
                node.draw(canvas, show_node_text, node_fill_color2, node_outline_color2, node_text_color2)

    def find_node(self, location):
        """ Find the node at the given position."""
        for node in self.all_nodes:
            if node.is_at(location):
                return node
        return None

    def make_link(self, node0, node1):
        """ Make a link from node0 to node1."""
        Link(node0, node1)

    def make_links(self, node0, node1):
        """ Make links from node0 to node1 and node1 to node0."""
        Link(node0, node1)
        Link(node1, node0)

    def reset_network(self):
        """ Reset the network."""
        # Deselect all nodes and branches.
        self.deselect_nodes()
        self.deselect_links()

        # Clear the nodes' text properties.
        for node in self.all_nodes:
            node.from_link = None
            node.from_node = None
            node.text = None

    def deselect_nodes(self):
        """ Deselect all nodes."""
        for node in self.all_nodes:
            node.visited = False

    def deselect_links(self):
        """ Deselect all links."""
        for node in self.all_nodes:
            for link in node.links:
                link.visited = False

    def depth_first_traverse(self, start_node):
        """ Traverse the network in depth-first order."""
        # Reset the network.
        self.reset_network()

        # Keep track of the number of nodes in the traversal.
        num_done = 0

        # Push the start node onto the stack.
        stack = []
        stack.append(start_node)

        # Visit the start node.
        traversal = []
        traversal.append(start_node)
        start_node.visited = True
        start_node.text = f"{num_done}"
        num_done += 1

        # Process the stack until it's empty.
        while len(stack) > 0:
            # Get the next node from the stack.
            node = stack.pop()

            # Process the node's links.
            for link in node.links:
                to_node = link.node1

                # Only use the link if the destination
                # node hasn't been visited.
                if not to_node.visited:
                    # Mark the node as visited.
                    to_node.visited = True
                    to_node.text = f"{num_done}"
                    num_done += 1

                    # Add the node to the traversal.
                    traversal.append(to_node)

                    # Add the link to the traversal.
                    link.visited = True

                    # Push the node onto the stack.
                    stack.append(to_node)

        # See if the network is connected.
        is_connected = True
        for node in self.all_nodes:
            if not node.visited:
                is_connected = False
                break

        return traversal, is_connected

    def breadth_first_traverse(self, start_node):
        """ Traverse the network in breadth-first order."""
        # Reset the network.
        self.reset_network()

        # Keep track of the number of nodes in the traversal.
        num_done = 0

        # Add the start node to the queue.
        queue = []
        queue.insert(0, start_node)

        # Visit the start node.
        traversal = []
        traversal.append(start_node)
        start_node.visited = True
        start_node.text = f"{num_done}"
        num_done += 1

        # Process the queue until it's empty.
        while len(queue) > 0:
            # Get the next node from the queue.
            node = queue.pop()

            # Process the node's links.
            for link in node.links:
                to_node = link.node1

                # Only use the link if the destination
                # node hasn't been visited.
                if not to_node.visited:
                    # Mark the node as visited.
                    to_node.visited = True
                    to_node.text = f"{num_done}"
                    num_done += 1

                    # Add the node to the traversal.
                    traversal.append(to_node)

                    # Add the link to the traversal.
                    link.visited = True

                    # Add the node onto the queue.
                    queue.insert(0, to_node)

        # See if the network is connected.
        is_connected = True
        for node in self.all_nodes:
            if not node.visited:
                is_connected = False
                break

        return traversal, is_connected

    def get_connected_components(self):
        """ Return the network's connected components."""
        # Reset the network.
        self.reset_network()

        # Keep track of the number of nodes visited.
        num_visited = 0

        # Make the result list of lists.
        components = []

        # Repeat until all nodes are in a connected component.
        while num_visited < len(self.all_nodes):
            # Find a node that hasn't been visited.
            start_node = None
            for node in self.all_nodes:
                if not node.visited:
                    start_node = node
                    break

            # Make sure we found one.
            assert start_node != None

            # Add the start node to the stack.
            stack = []
            stack.append(start_node)
            start_node.visited = True
            num_visited += 1

            # Add the node to a new connected component.
            component = []
            components.append(component)
            component.append(start_node)

            # Process the stack until it's empty.
            while len(stack) > 0:
                # Get the next node from the stack.
                node = stack.pop()

                # Process the node's links.
                for link in node.links:
                    # Only use the link if the destination
                    # node hasn't been visited.
                    to_node = link.node1
                    if not to_node.visited:
                        # Mark the node as visited.
                        to_node.visited = True

                        # Mark the link as part of the tree.
                        link.visited = True
                        num_visited += 1

                        # Add the node to the current connected component.
                        component.append(to_node)

                        # Push the node onto the stack.
                        stack.append(to_node)

        # Return the components.
        return components

    def make_spanning_tree(self, root):
        """ Build a spanning tree. Return its total cost and whether it is connected."""
        # Reset the network.
        self.reset_network()

        # The total cost of the links in the spanning tree.
        total_cost = 0

        # Push the root node onto the stack.
        stack = []
        stack.append(root)

        # Visit the root node.
        root.visited = True

        # Process the stack until it's empty.
        while len(stack) > 0:
            # Get the next node from the stack.
            node = stack.pop()

            # Process the node's links.
            for link in node.links:
                # Only use the link if the destination
                # node hasn't been visited.
                to_node = link.node1
                if not to_node.visited:
                    # Mark the node as visited.
                    to_node.visited = True

                    # Record the node that got us here.
                    to_node.from_node = node

                    # Mark the link as part of the tree.
                    link.visited = True

                    # Push the node onto the stack.
                    stack.append(to_node)

                    # Add the link's cost to the total cost.
                    total_cost += link.cost

        # See if the network is connected.
        is_connected = True
        for node in self.all_nodes:
            if not node.visited:
                is_connected = False
                break

        return total_cost, is_connected

    def make_minimal_spanning_tree(self, root):
        """"
        Build a minimal spanning tree. Return its total cost and whether it is connected.
        When it adds a node to the spanning tree, the algorithm
        also adds its links that lead outside of the tree to a list.
        Later it searches that list for a minimal link.
        """
        # Reset the network.
        self.reset_network()

        # The total cost of the links in the spanning tree.
        total_cost = 0

        # Add the root node's links to the link candidate list.
        candidate_links = []
        for link in root.links:
            candidate_links.append(link)

        # Visit the root node.
        root.visited = True

        # Process the list until it's empty.
        while len(candidate_links) > 0:
            # Find the link with the lowest cost.
            best_link = candidate_links[0]
            best_cost = best_link.cost
            for i in range(1, len(candidate_links)):
                if candidate_links[i].cost < best_cost:
                    # Save this improvement.
                    best_link = candidate_links[i]
                    best_cost = best_link.cost

            # Remove the link from the list.
            candidate_links.remove(best_link)

            # Get the node at the other end of the link.
            to_node = best_link.node1

            # See if the link's node is still unmarked.
            if not to_node.visited:
                # Use the link.
                best_link.visited = True
                total_cost += best_link.cost
                to_node.visited = True

                # Record the node that got us here.
                to_node.from_node = best_link.node0

                # Process to_node's links.
                for new_link in to_node.links:
                    # If the node hasn't been visited,
                    # add the link to the list.
                    if not new_link.node1.visited:
                        candidate_links.append(new_link)

        # See if the network is connected.
        is_connected = True
        for node in self.all_nodes:
            if not node.visited:
                is_connected = False
                break

        return total_cost, is_connected

    def find_any_path(self, from_node, to_node):
        """
        Find any path between the two nodes. Return the path's total cost,
        the nodes in the path, and the links in the path.
        """
        # Make a spanning tree.
        self.make_spanning_tree(from_node)

        # Follow the tree's links back from to_node to from_node.
        return self.find_spanning_tree_path(from_node, to_node)

    def find_label_setting_path_tree(self, from_node):
        """
        Find a shortest path tree rooted at from_node
        by using a label setting algorithm. Return the tree's total cost.
        """
        # Reset the network.
        self.reset_network()

        # Keep track of the number of nodes in the tree.
        num_done = 0

        # Add the start node to the shortest path tree.
        from_node.visited = True
        from_node.distance = 0
        from_node.text = f"{num_done}"
        num_done += 1

        # Track the tree's total cost.
        cost = 0

        # Make the candidate list.
        candidate_links = []

        # Add the start node's links to the candidate list.
        for link in from_node.links:
            candidate_links.append(link)

        # Make a shortest path tree.
        while len(candidate_links) > 0:
            # Find the best link.
            best_link = None
            best_cost = infinity

            for i in range(len(candidate_links) - 1, -1, -1):
                test_link = candidate_links[i]

                # See if the link leads outside the tree.
                if test_link.node1.visited:
                    # Remove this link.
                    del candidate_links[i]
                else:
                    # See if this link is an improvement.
                    test_cost = test_link.node0.distance + test_link.cost
                    if test_cost < best_cost:
                        best_cost = test_cost
                        best_link = test_link

            # If we found no link, then the candidate
            # list must be empty and we're done.
            if best_link == None:
                assert len(candidate_links) == 0
                break

            # Use this link.
            # Remove it from the candidate list.
            candidate_links.remove(best_link)

            # Add the node to the tree.
            best_node = best_link.node1
            best_node.distance = best_link.node0.distance + best_link.cost
            best_node.visited = True
            best_link.visited = True
            best_node.from_node = best_link.node0
            best_node.text = f"{num_done}"
            num_done += 1

            # Add the node's links to the tree.
            for new_link in best_node.links:
                if not new_link.node1.visited:
                    candidate_links.append(new_link)

            # Add the link's cost to the tree's total cost.
            cost += best_link.cost

        # Return the total cost.
        return cost

    def find_label_setting_path(self, from_node, to_node):
        """
        Find a shortest path between the two nodes
        by using a label setting algorithm.
        Return the path's total cost, nodes, and links.
        """
        # Build a shortest path tree.
        self.find_label_setting_path_tree(from_node)

        # Follow the tree's links back from to_node to from_node.
        return self.find_spanning_tree_path(from_node, to_node)

    def find_spanning_tree_path(self, from_node, to_node):
        """"
        Follow a spanning tree's links to find a path from from_node to to_node.
        Return the nodes and links in the path.
        """
        # Follow the tree's links back from to_node to from_node.
        path_nodes = []
        path_links = []
        current_node = to_node
        while current_node != from_node:
            # Add this node to the path.
            path_nodes.append(current_node)

            # Find the previous node.
            prev_node = current_node.from_node

            # Find the link that leads to current_node.
            prev_link = None
            for link in prev_node.links:
                if link.node1 == current_node:
                    prev_link = link
                    break

            # Make sure we found the link.
            assert prev_link != None

            # Add the link to the path.
            path_links.append(prev_link)

            # Move to the next node.
            current_node = prev_node

        # Add the start node.
        path_nodes.append(from_node)

        # Reverse the order of the nodes and links.
        path_nodes.reverse()
        path_links.reverse()

        # Unmark all nodes and links.
        self.deselect_nodes()
        self.deselect_links()

        # Marks the path's nodes and links.
        for node in path_nodes:
            node.visited = True
        for link in path_links:
            link.visited = True

        # Calculate the cost of the path.
        cost = 0
        for link in path_links:
            cost += link.cost

        # Return the cost.
        return cost, path_nodes, path_links

    def find_label_correcting_path_tree(self, from_node):
        """
        Find a shortest path tree rooted at from_node
        by using a label correcting algorithm.
        Return the tree's total cost.
        """
        # Reset the network.
        self.reset_network()

        # Set all nodes' distances to infinity and their labels to 0.
        for node in self.all_nodes:
            node.distance = infinity
            node.text = "0"

        # Add the start node to the shortest path tree.
        from_node.visited = True
        from_node.distance = 0

        # Make the candidate list.
        candidate_links = []

        # Add the start node's links to the candidate list.
        for link in from_node.links:
            candidate_links.append(link)

        # Make a shortest path tree.
        while len(candidate_links) > 0:
            # Use the first link in the candidate list.
            link = candidate_links.pop(0)

            # See if this link improves its destination node's distance.
            new_distance = link.node0.distance + link.cost
            to_node = link.node1
            if new_distance < to_node.distance:
                # This is an improvement.
                # Update the node's distance.
                to_node.distance = new_distance

                # Update the node's from_node and from_link.
                to_node.from_node = link.node0
                to_node.from_link = link

                # Update the node's label.
                num_updates = int(to_node.text)
                num_updates += 1
                to_node.text = f"{num_updates}"

                # Add the node's links to the candidate list.
                for new_link in to_node.links:
                    candidate_links.append(new_link)

        # Set the visited properties for the visited nodes and links.
        cost = 0
        for node in self.all_nodes:
            node.visited = True
            if node.from_link != None:
                node.from_link.visited = True
                cost += node.from_link.cost

        # Return the total cost.
        return cost

    def find_label_correcting_path(self, from_node, to_node):
        """
        Find a shortest path between the two nodes
        by using a label correcting algorithm.
        Return the path's total cost, nodes, and links.
        """
        # Build a shortest path tree.
        self.find_label_correcting_path_tree(from_node)

        # Follow the tree's links back from to_node to from_node.
        return self.find_spanning_tree_path(from_node, to_node)

    def find_all_pairs_paths(self):
        """ Find all pairs shortest paths. Return the distance and via arrays."""
        # Renumber the nodes.
        num_nodes = len(self.all_nodes)
        for i in range(num_nodes):
            self.all_nodes[i].index = i

        # Initialize the distance array.
        distance = [[infinity for i in range(num_nodes)] for j in range(num_nodes)]

        # The distance from a node to itself is 0.
        for i in range(num_nodes):
            distance[i][i] = 0

        # Set distances for links.
        for node in self.all_nodes:
            for link in node.links:
                from_node = link.node0.index
                to_node = link.node1.index
                if distance[from_node][to_node] > link.cost:
                    distance[from_node][to_node] = link.cost

        # Initialize the via array.
        via = [[-1 for i in range(num_nodes)] for j in range(num_nodes)]

        # Set via[i][j] = j if there is a link from i to j.
        for i in range(num_nodes):
            for j in range(num_nodes):
                if distance[i][j] < infinity:
                    via[i][j] = j

        # Find improvements.
        for via_node in range(num_nodes):
            for from_node in range(num_nodes):
                for to_node in range(num_nodes):
                    new_dist = \
                        distance[from_node][via_node] + \
                        distance[via_node][to_node]
                    if new_dist < distance[from_node][to_node]:
                        # This is an improved path. Update it.
                        distance[from_node][to_node] = new_dist
                        via[from_node][to_node] = via_node
        return distance, via

    def find_all_pairs_path(self, distance, via, start_node, end_node):
        """ Return an all pairs path."""
        # See if there is a path between these nodes.
        if distance[start_node][end_node] == infinity:
            return None

        # Get the via node for this path.
        via_node = via[start_node][end_node]

        # Make the list to return.
        path = []

        # See if there is a direct connection.
        if via_node == end_node:
            # There is a direct connection.
            # Return a list that contains only end_node.
            path.append(self.all_nodes[end_node])
        else:
            # There is no direct connection.
            # Return start_node --> via_node plus via_node --> end_node.
            path.extend(self.find_all_pairs_path(distance, via, start_node, via_node))
            path.extend(self.find_all_pairs_path(distance, via, via_node, end_node))

        return path


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.mode = Modes.none

        # The nodes selected by the user while adding a link or finding a path.
        self.node0 = None
        self.node1 = None

        # The currently loaded network.
        self.the_network = Network()

        # User interface.
        self.window = tk.Tk()
        self.window.title("network_maker")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("500x500")

        # Menu.
        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)
        filemenu = tk.Menu(menubar, tearoff=0)
        filemenu.add_command(label="New", command=self.new, accelerator="Ctrl+N")
        filemenu.add_command(label="Open", command=self.open, accelerator="Ctrl+O")
        filemenu.add_command(label="Save As", command=self.save_as, accelerator="Ctrl+S")
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=self.kill_callback)
        menubar.add_cascade(label="File", menu=filemenu)

        # Tool strip.
        self.buttons = []
        self.images = []
        toolstrip = tk.Frame(self.window)
        toolstrip.pack(padx=5, pady=(5, 0), side=tk.TOP, fill=tk.X)

        self.deselect_button = self.make_button(toolstrip, "deselect.png", self.deselect)
        self.make_separator(toolstrip)
        self.add_node_button = self.make_button(toolstrip, "add_node.png", self.add_nodes)
        self.add_link_button = self.make_button(toolstrip, "add_link.png", self.add_links)
        self.add_link2_button = self.make_button(toolstrip, "add_link2.png", self.add_links2)
        self.make_separator(toolstrip)
        self.df_traversal_button = self.make_button(toolstrip, "df_traversal.png", self.df_traversal)
        self.bf_traversal_button = self.make_button(toolstrip, "bf_traversal.png", self.bf_traversal)
        self.connected_components_button = self.make_button(toolstrip, "connected_components.png", self.connected_components)
        self.spanning_tree_button = self.make_button(toolstrip, "spanning_tree.png", self.spanning_tree)
        self.minimal_spanning_tree_button = self.make_button(toolstrip, "minimal_spanning_tree.png", self.minimal_spanning_tree)
        self.any_path_button = self.make_button(toolstrip, "any_path.png", self.any_path)
        self.label_setting_tree_button = self.make_button(toolstrip, "label_setting_tree.png", self.label_setting_tree)
        self.label_setting_path_button = self.make_button(toolstrip, "label_setting_path.png", self.label_setting_path)
        self.label_correcting_tree_button = self.make_button(toolstrip, "label_correcting_tree.png", self.label_correcting_tree)
        self.label_correcting_path_button = self.make_button(toolstrip, "label_correcting_path.png", self.label_correcting_path)
        self.all_pairs_button = self.make_button(toolstrip, "all_pairs.png", self.all_pairs)

        # The status label.
        self.status_label = tk.Label(self.window, anchor=tk.W, relief=tk.RIDGE)
        self.status_label.pack(padx=5, pady=2, side=tk.BOTTOM, fill=tk.X)

        # The drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, cursor="crosshair")
        self.canvas.pack(padx=5, pady=(5, 0), side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Control-n>', self.key_new)
        self.window.bind('<Control-o>', self.key_open)
        self.window.bind('<Control-s>', self.key_save_as)

        # Catch mouse clicks.
        self.canvas.bind("<Button-1>", self.mouse1_click)
        self.canvas.bind("<Button-3>", self.mouse3_click)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def key_new(self, event):
        self.new()
    def new(self):
        """ Start a new network."""
        self.the_network = Network()
        self.draw_canvas()

    def key_open(self, event):
        self.open()
    def open(self):
        """ Load a network file."""
        filename = askopenfilename(defaultextension=".net",
            filetypes=(("Network Files", "*.net"), ("All Files", "*.*")))
        if filename:
            try:
                # Load the network.
                network = Network.load_network(filename)

                # Start using the new network.
                self.the_network = network

                # Draw the new network.
                self.draw_canvas()
            except Exception as e:
                messagebox.showinfo("Load Error", str(e))
                return

    def key_save_as(self, event):
        self.save_as()
    def save_as(self):
        """ Save the network in a file."""
        filename = asksaveasfilename(defaultextension=".net",
            filetypes=(("Network Files", "*.net"), ("All Files", "*.*")))
        if filename:
            # Save the network.
            try:
                # Save the network.
                self.the_network.save_network(filename)
            except Exception as e:
                messagebox.showinfo("Load Error", str(e))
                return

    def make_button(self, toolstrip, file, command):
        button = tk.Button(toolstrip, command=command)
        self.buttons.append(button)

        image = ImageTk.PhotoImage(file=file)
        self.images.append(image)

        button.config(image=image)
        button.pack(padx=2, pady=2, side=tk.LEFT)
        return button

    def make_separator(self, toolstrip):
        separator = ttk.Separator(toolstrip, orient=tk.VERTICAL)
        separator.pack(padx=2, pady=2, side=tk.LEFT, fill=tk.Y)

    """ Toolstrip buttons."""
    def deselect(self):
        self.select_tool(None, Modes.none, "")

    def add_nodes(self):
        self.select_tool(self.add_node_button, Modes.add_node, "Click to add a node")

    def add_links(self):
        self.select_tool(self.add_link_button, Modes.add_link1, "Directed Link: left-click to select start node, right-click to select end node")

    def add_links2(self):
        self.select_tool(self.add_link2_button, Modes.add_link2, "Undirected Link: left- and right-click to select the two nodes")

    def df_traversal(self):
        self.select_tool(self.df_traversal_button, Modes.df_traversal, "Depth-First Traversal: click a root node")

    def bf_traversal(self):
        self.select_tool(self.bf_traversal_button, Modes.bf_traversal, "Breadth-First Traversal: click a root node")

    def connected_components(self):
        """ Find the connected components."""
        # Deselect all tools.
        self.select_tool(None, Modes.none, "")

        # Get the components.
        components = self.the_network.get_connected_components()

        # Display the components.
        txt = ""
        for component in components:
            component_txt = ""
            for component_node in component:
                component_txt += f" {component_node}"
            txt += "{" + component_txt[1:] + "} "
        self.status_label["text"] = txt

        # Redraw the network.
        self.draw_canvas()

    def spanning_tree(self):
        self.select_tool(self.spanning_tree_button, Modes.spanning_tree, "Spanning Tree")

    def minimal_spanning_tree(self):
        self.select_tool(self.minimal_spanning_tree_button, Modes.minimal_spanning_tree, "Minimal Spanning Tree")

    def any_path(self):
        self.select_tool(self.any_path_button, Modes.any_path, "Any Path")

    def label_setting_tree(self):
        self.select_tool(self.label_setting_tree_button, Modes.label_setting_tree, "Label Setting Tree")

    def label_setting_path(self):
        self.select_tool(self.label_setting_path_button, Modes.label_setting_path, "Label Setting Path")

    def label_correcting_tree(self):
        self.select_tool(self.label_correcting_tree_button, Modes.label_correcting_tree, "Label Correcting Tree")

    def label_correcting_path(self):
        self.select_tool(self.label_correcting_path_button, Modes.label_correcting_path, "Label Correcting Path")

    def all_pairs(self):
        # Deselect all tools.
        self.select_tool(None, Modes.none, "")

        self.status_label["text"] = "Working..."
        self.status_label.update()

        # Find all pairs shortest paths.
        distance, via = self.the_network.find_all_pairs_paths()

        # Display the arrays.
        print("\nFinal arrays:")
        print("Distance:")
        print(array_to_string(distance, 4, False))
        print("Via:")
        print(array_to_string(via, 3, True))

        # Display all of the paths.
        num_nodes = len(self.the_network.all_nodes)
        for i in range(num_nodes):
            for j in range(num_nodes):
                if i != j:
                    path = self.the_network.find_all_pairs_path(distance, via, i, j)
                    start_node = self.the_network.all_nodes[i]
                    end_node = self.the_network.all_nodes[j]
                    print(f"{start_node} --> {end_node} ", end="")
                    if path == None:
                        print("No path")
                    else:
                        print(f"[{distance[i][j]}] : ", end="")
                        for via_node in path:
                            print(f"{via_node} ", end="")
                        print()
        self.status_label["text"] = "See the Output Window for results."


    def select_tool(self, button, mode, status):
        """ Select this tool."""
        if self.mode == mode:
            self.mode = Modes.none
            button = None
        self.untoggle_buttons(button)
        self.mode = mode
        self.status_label["text"] = status

        # Reset and redraw the network.
        self.the_network.reset_network()
        self.draw_canvas()

    def untoggle_buttons(self, button):
        """ Untoggle all buttons except this one."""
        for test_buttton in self.buttons:
            if test_buttton == button:
                test_buttton.configure(relief=tk.SUNKEN)
            else:
                test_buttton.configure(relief=tk.RAISED)

        # Clear the status label.
        self.status_label["text"] = ""

    def draw_canvas(self):
        """ Draw the network."""
        self.canvas.delete(tk.ALL)

        show_node_text = False
        show_costs = False
        show_capacities = False
        self.the_network.draw(self.canvas, show_node_text, show_costs, show_capacities,
            1, "blue", "blue", 3, "red", "red",
            "white", "blue", "blue",
            "lightblue", "red", "red")

    def mouse1_click(self, event):
        self.mouse_click(event, 1)

    def mouse3_click(self, event):
        self.mouse_click(event, 3)

    def mouse_click(self, event, button_number):
        """ Add a node or link if appropriate."""
        location = (event.x, event.y)

        if self.mode == Modes.add_node:
            # Add a node.
            index = len(self.the_network.all_nodes)
            name = number_to_letters(index)
            node = Node(name, location, index)
            self.the_network.all_nodes.append(node)
            self.draw_canvas()
        elif (
            (self.mode == Modes.add_link1) or
            (self.mode == Modes.add_link2)):
            # Add a link.
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                if button_number == 1:
                    self.node0 = node
                else:
                    self.node1 = node

                # See if we have both nodes.
                if ((self.node0 != None) and (self.node1 != None)):
                    # See if the nodes are the same.
                    if self.node0 == self.node1:
                        beep()
                    else:
                        # Make the link.
                        if self.mode == Modes.add_link1:
                            self.the_network.make_link(self.node0, self.node1)
                        else:
                            self.the_network.make_links(self.node0, self.node1)

                    # We're done with this link.
                    self.node0 = None
                    self.node1 = None

                    # Redraw.
                    self.draw_canvas()
        elif self.mode == Modes.df_traversal:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Traverse the network.
                traversal, is_connected = self.the_network.depth_first_traverse(node)

                # Display the traversal.
                txt = "Traversal: "
                for traversal_node in traversal:
                    txt += f" {traversal_node}"
                if is_connected:
                    txt += " Connected."
                else:
                    txt += " Not connected."
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.bf_traversal:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Traverse the network.
                traversal, is_connected = self.the_network.breadth_first_traverse(node)

                # Display the traversal.
                txt = "Traversal: "
                for traversal_node in traversal:
                    txt += f" {traversal_node}"
                if is_connected:
                    txt += " Connected."
                else:
                    txt += " Not connected."
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.spanning_tree:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Build a spanning tree.
                cost, is_connected = self.the_network.make_spanning_tree(node)
                if is_connected:
                    txt = "Connected. "
                else:
                    txt = "Not connected. "
                txt += f"Total cost: {cost}"
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.minimal_spanning_tree:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Build a spanning tree.
                cost, is_connected = self.the_network.make_minimal_spanning_tree(node)
                if is_connected:
                    txt = "Connected. "
                else:
                    txt = "Not connected. "
                txt += f"Total cost: {cost}"
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.any_path:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                if button_number == 1:
                    self.node0 = node
                else:
                    self.node1 = node

                # See if we have both nodes.
                if ((self.node0 != None) and (self.node1 != None)):
                    # See if the nodes are the same.
                    if self.node0 == self.node1:
                        beep()
                    else:
                        # Find a path between the nodes.
                        cost, path_nodes, path_links = self.the_network.find_any_path(self.node0, self.node1)

                        txt = "Path: "
                        for path_node in path_nodes:
                            txt += f"{path_node} "
                        txt += f"Total cost: {cost}"
                        self.status_label["text"] = txt

                        # Redraw the network.
                        self.draw_canvas()
        elif self.mode == Modes.label_setting_tree:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Build a label setting shortest path tree.
                cost = self.the_network.find_label_setting_path_tree(node)
                txt = f"Total cost: {cost}"
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.label_setting_path:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                if button_number == 1:
                    self.node0 = node
                else:
                    self.node1 = node

                # See if we have both nodes.
                if ((self.node0 != None) and (self.node1 != None)):
                    # See if the nodes are the same.
                    if self.node0 == self.node1:
                        beep()
                    else:
                        # Find a path between the nodes.
                        cost, path_nodes, path_links = self.the_network.find_label_setting_path(self.node0, self.node1)

                        txt = "Path: "
                        for path_node in path_nodes:
                            txt += f"{path_node} "
                        txt += f"Total cost: {cost}"
                        self.status_label["text"] = txt

                        # Redraw the network.
                        self.draw_canvas()
        elif self.mode == Modes.label_correcting_tree:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                # Build a label setting shortest path tree.
                cost = self.the_network.find_label_correcting_path_tree(node)
                txt = f"Total cost: {cost}"
                self.status_label["text"] = txt

                # Redraw the network.
                self.draw_canvas()
        elif self.mode == Modes.label_correcting_path:
            # See if there is a node here.
            node = self.the_network.find_node(location)
            if node == None:
                beep()
            else:
                if button_number == 1:
                    self.node0 = node
                else:
                    self.node1 = node

                # See if we have both nodes.
                if ((self.node0 != None) and (self.node1 != None)):
                    # See if the nodes are the same.
                    if self.node0 == self.node1:
                        beep()
                    else:
                        # Find a path between the nodes.
                        cost, path_nodes, path_links = self.the_network.find_label_correcting_path(self.node0, self.node1)

                        txt = "Path: "
                        for path_node in path_nodes:
                            txt += f"{path_node} "
                        txt += f"Total cost: {cost}"
                        self.status_label["text"] = txt

                        # Redraw the network.
                        self.draw_canvas()


if __name__ == '__main__':
    app = App()

# app.root.destroy()

