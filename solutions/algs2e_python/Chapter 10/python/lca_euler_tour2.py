import tkinter as tk
from tkinter import ttk

class TreeNode:
    # Space to skip horizontally between siblings
    # and vertically between tree levels.
    h_offset = 10
    v_offset = 20

    # The circle's radius.
    radius = 12

    def __init__(self, parent, value):
        if parent != None:
            parent.children.append(self)
            self.depth = parent.depth + 1
        else:
            self.depth = 0

        self.value = value
        self.children = []
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

        # The node's first and last locations in the Euler tour.
        self.euler_tour_first_location = -1
        self.euler_tour_last_location = -1

        # The node's background color.
        background = "white"

    def make_tree(self, app, canvas):
        """ Make the subtree's links and nodes."""
        self.make_subtree_links(canvas)
        self.make_subtree_nodes(app, canvas)

    def make_subtree_links(self, canvas):
        """ Draw the subtree's links."""
        for child in self.children:
            canvas.create_line(self.x, self.y, child.x, child.y)
            child.make_subtree_links(canvas)

    def make_subtree_nodes(self, app, canvas):
        """ Draw the subtree's nodes."""
        # Make the circle.
        x0 = self.x - TreeNode.radius
        y0 = self.y - TreeNode.radius
        x1 = x0 + 2 * TreeNode.radius
        y1 = y0 + 2 * TreeNode.radius
        self.oval = canvas.create_oval(x0, y0, x1, y1, fill="white")

        # Register to receive mouse clicks on the node.
        canvas.tag_bind(self.oval, '<ButtonPress-1>', lambda event, arg=self: app.oval_left_click(self))
        canvas.tag_bind(self.oval, '<ButtonPress-3>', lambda event, arg=self: app.oval_right_click(self))

        # Make the label.
        text = canvas.create_text((self.x, self.y), text=str(self.value))
        canvas.tag_bind(text, '<ButtonPress-1>', lambda event, arg=self: app.oval_left_click(self))
        canvas.tag_bind(text, '<ButtonPress-3>', lambda event, arg=self: app.oval_right_click(self))

        # Make the child subtrees.
        for child in self.children:
            child.make_subtree_nodes(app, canvas)

    def arrange_tree(self, xmin, ymin):
        """
        Arrange the tree.
        Call this method only for the root node.
        """
        self.set_size()
        self.position_subtree(ymin, xmin, xmin + self.width)

    def set_size(self):
        """ Set the size needed by this subtree."""
        # Start with the size needed for this node.
        self.width = 2 * TreeNode.radius
        self.height = 2 * TreeNode.radius

        # Get child subtree sizes.
        if len(self.children) > 0:
            width = TreeNode.h_offset * (len(self.children) - 1)
            height = 0
            for child in self.children:
                child.set_size()
                width += child.width

                if height < child.height:
                    height = child.height

            if self.width < width:
                self.width = width
            self.height += height + TreeNode.v_offset

    def position_subtree(self, y, xmin, xmax):
        """
        Position the node at this y position 
        centered between xmin and xmax horizontally.
        """
        # Position this node.
        xmid = (xmin + xmax) / 2
        y += TreeNode.radius
        self.x = xmid
        self.y = y

        # Position our child nodes.
        x = xmin
        y += TreeNode.radius + TreeNode.v_offset
        for child in self.children:
            child.position_subtree(y, x, x + child.width)
            x += child.width + TreeNode.h_offset

    def add_to_euler_tour(self, tour):
        # Make an Euler tour for the subtree.
        if self.euler_tour_first_location <0:
            self.euler_tour_first_location = len(tour)
        self.euler_tour_last_location = len(tour)

        tour.append(self)
        if len(self.children) > 0:
            for child in self.children:
                child.add_to_euler_tour(tour)
                tour.append(self)

    def find_lca(self, tour, node1, node2):
        """
        Find the LCA for the two nodes.
        Call this method only for the root node.
        """
        # Find the nodes' locations in the Euler tour.
        if node1.euler_tour_last_location <= node2.euler_tour_first_location:
            # Node1 is to the left of node2.
            location1 = node1.euler_tour_last_location
            location2 = node2.euler_tour_first_location
        elif node1.euler_tour_first_location >= node2.euler_tour_last_location:
            # Node1 is to the right of node2.
            location1 = node2.euler_tour_last_location
            location2 = node1.euler_tour_first_location
        elif node1.euler_tour_first_location >= node2.euler_tour_first_location:
            # Node1 lies within node2's subtree so node2 is the LCA.
            return node2
        else:
            # Node2 lies within node1's subtree so node1 is the LCA.
            return node1

        # Find the highest node in the interval location1 --> location2.
        lca = tour[location1]
        for i in range(location1 + 1, location2 + 1):
            if tour[i].depth < lca.depth:
                lca = tour[i]

        return lca

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with no nodes selected.
        self.lca_node = None
        self.node1 = None
        self.node2 = None

        self.window = tk.Tk()
        self.window.title("lca_euler_tour2")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x190")

        # Tree.
        self.tree_canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.tree_canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        self.root = TreeNode(None, 0)
        node1 = TreeNode(self.root, 1)
        node5 = TreeNode(node1, 5)
        node6 = TreeNode(node1, 6)
        node2 = TreeNode(self.root, 2)
        node7 = TreeNode(node2, 7)
        node8 = TreeNode(node2, 8)
        node9 = TreeNode(node2, 9)
        node11 = TreeNode(node7, 11)
        node3 = TreeNode(self.root, 3)
        node4 = TreeNode(self.root, 4)
        node10 = TreeNode(node4, 10)
        node12 = TreeNode(node10, 12)
        node13 = TreeNode(node10, 13)
        node14 = TreeNode(node10, 14)
        self.root.arrange_tree(10, 10)
        self.root.make_tree(self, self.tree_canvas)

        # Make the Euler tour.
        self.euler_tour = []
        self.root.add_to_euler_tour(self.euler_tour)
        for node in self.euler_tour:
            print(f"{node.value} ", end="")
        print()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.tree_canvas.focus_force()
        self.window.mainloop()

    def oval_left_click(self, node):
        # Deselect the current node1 selection.
        if self.node1 != None:
            self.tree_canvas.itemconfig(self.node1.oval, fill="white")

        # Select the clicked node.
        self.node1 = node
        self.tree_canvas.itemconfig(self.node1.oval, fill="lightgreen")

        # Find the LCA.
        self.find_lca()

    def oval_right_click(self, node):
        # Deselect the current node2 selection.
        if self.node2 != None:
            self.tree_canvas.itemconfig(self.node2.oval, fill="white")

        # Select the clicked node.
        self.node2 = node
        self.tree_canvas.itemconfig(self.node2.oval, fill="lightblue")

        # Find the LCA.
        self.find_lca()

    def find_lca(self):
        """ Find the LCA."""
        # Deselect the current LCA.
        if self.lca_node != None:
            self.tree_canvas.itemconfig(self.lca_node.oval, fill="white")
            if self.node1 != None:
                self.tree_canvas.itemconfig(self.node1.oval, fill="lightgreen")
            if self.node2 != None:
                self.tree_canvas.itemconfig(self.node2.oval, fill="lightblue")
        self.lca_node = None

        # See if we have two nodes selected.
        if (self.node1 != None) and (self.node2 != None):
            # Find the LCA.
            self.lca_node = self.root.find_lca(self.euler_tour, self.node1, self.node2)
            self.tree_canvas.itemconfig(self.lca_node.oval, fill="pink")

if __name__ == '__main__':
    app = App()

# app.root.destroy()
