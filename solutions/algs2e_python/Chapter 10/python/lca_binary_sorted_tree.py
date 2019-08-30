import tkinter as tk
from tkinter import ttk


class TreeNode:
    # Space to skip horizontally between siblings
    # and vertically between tree levels.
    h_offset = 10
    v_offset = 20

    # The circle's radius.
    radius = 12

    def __init__(self):
        self.value = -1
        self.left_child = None
        self.right_child = None
        self.x = 0
        self.y = 0

        # The node's background color.
        background = "white"

    def make_tree(self, app, canvas):
        """ Make the subtree's links and nodes."""
        self.make_subtree_links(canvas)
        self.make_subtree_nodes(app, canvas)

    def make_subtree_links(self, canvas):
        """ Draw the subtree's links."""
        if (self.left_child != None):
            canvas.create_line(self.x, self.y, self.left_child.x, self.left_child.y)
            self.left_child.make_subtree_links(canvas)
        if (self.right_child != None):
            canvas.create_line(self.x, self.y, self.right_child.x, self.right_child.y)
            self.right_child.make_subtree_links(canvas)

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
        if (self.left_child != None):
            self.left_child.make_subtree_nodes(app, canvas)
        if (self.right_child != None):
            self.right_child.make_subtree_nodes(app, canvas)

    @staticmethod
    def build_full_tree(height, xmin, ymin):
        """ Build a full binary tree with the indicated upper left corner."""
        # Build the nodes.
        root = TreeNode()
        root.build_subtree(height)

        # Assign node values.
        root.assign_values(1)

        # Position the nodes.
        # Calculate the tree's width.
        num_leaf_nodes = 2 ** height
        width = num_leaf_nodes * (2 * TreeNode.radius) + (num_leaf_nodes - 1) * TreeNode.h_offset
        ymin += TreeNode.radius
        xmax = xmin + width
        root.position_subtree(ymin, xmin, xmax)

        return root

    def build_subtree(self, height):
        """ Build a subtree below this node of the given height."""
        if (height == 0):
            return

        # Build child subtrees.
        self.left_child = TreeNode()
        self.left_child.build_subtree(height - 1)

        self.right_child = TreeNode()
        self.right_child.build_subtree(height - 1)

    def assign_values(self, value):
        """
        Perform an inorder traversal and assign values to the nodes.
        Return the next available value.
        """
        if (self.left_child != None):
            value = self.left_child.assign_values(value)
        self.value = value
        value += 1
        if (self.right_child != None):
            value = self.right_child.assign_values(value)
        return value

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
        y += TreeNode.radius + TreeNode.v_offset
        if (self.left_child != None):
            self.left_child.position_subtree(y, xmin, xmid)
        if (self.right_child != None):
            self.right_child.position_subtree(y, xmid, xmax)

    def find_lca(self, value1, value2):
        """ Find the LCA for the two nodes."""
        # See if both nodes belong down the same child branch.
        if (value1 < self.value) and (value2 < self.value):
            return self.left_child.find_lca(value1, value2)
        if (value1 > self.value) and (value2 > self.value):
            return self.right_child.find_lca(value1, value2)

        # This is the LCA.
        return self


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with no nodes selected.
        self.lca_node = None
        self.node1 = None
        self.node2 = None

        self.window = tk.Tk()
        self.window.title("lca_binary_sorted_tree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x235")

        params_frame = tk.Frame(self.window)
        params_frame.pack(fill=tk.BOTH)

        height_label = tk.Label(params_frame, text="Tree Height:")
        height_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.height_entry = tk.Entry(params_frame, width=4, justify=tk.RIGHT)
        self.height_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.height_entry.insert(tk.END, "3")
        build_tree_button = tk.Button(params_frame, text="Build Tree", width=8, command=self.build_tree)
        build_tree_button.grid(row=0, column=2, padx=5, pady=5)

        # Tree.
        self.tree_canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.tree_canvas.pack(padx=5, pady=(0,5), side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=build_tree_button: build_tree_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.height_entry.focus_force()
        self.window.mainloop()

    def build_tree(self):
        """ Build the tree."""
        self.tree_canvas.delete(tk.ALL)
        height = int(self.height_entry.get())
        self.root = TreeNode.build_full_tree(height, 10, 10)
        self.root.make_tree(self, self.tree_canvas)

        # Clear previous node selections.
        self.lca_node = None
        self.node1 = None
        self.node2 = None

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
            self.lca_node = self.root.find_lca(self.node1.value, self.node2.value)
            self.tree_canvas.itemconfig(self.lca_node.oval, fill="pink")

if __name__ == '__main__':
    app = App()

# app.root.destroy()
