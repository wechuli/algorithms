import tkinter as tk


infinity = 1000000000


class BinaryNode:
    # Class-level drawing parameters.
    node_radius = 10
    x_spacing = 20
    y_spacing = 20

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

        # Drawing parameters.
        self.center = (0, 0)
        self.subtree_bounds = (
            self.center[0] - BinaryNode.node_radius, 
            self.center[1] - BinaryNode.node_radius, 
            self.center[0] + BinaryNode.node_radius, 
            self.center[1] + BinaryNode.node_radius)

    def position_subtree(self, xmin, ymin):
        """ Position the node."""
        # Set ymax to the bottom of this node.
        ymax = ymin + 2 * BinaryNode.node_radius
        xmax = xmin

        # See if the node has any children.
        if (self.left_child == None) and (self.right_child == None):
            # There are no children. Put the node here.
            xmax += 2 * BinaryNode.node_radius
            self.subtree_bounds = (xmin, ymin, xmax, ymax)
        else:
            ymax += BinaryNode.y_spacing

            # Position the left subtree.
            subtree_bottom = ymax

            if self.left_child != None:
                self.left_child.position_subtree(xmax, ymax)

                # Update xmax to allow room for the left subtree.
                xmax = self.left_child.subtree_bounds[2]

                # Update the subtree bottom.
                subtree_bottom = self.left_child.subtree_bounds[3]

            xmax += BinaryNode.x_spacing

            # Position the right subtree.
            if self.right_child != None:
                self.right_child.position_subtree(xmax, ymax)

                # Update xmax.
                xmax = self.right_child.subtree_bounds[2]

                # Update the subtree bottom.
                if self.right_child.subtree_bounds[3] > subtree_bottom:
                    subtree_bottom = self.right_child.subtree_bounds[3]

            # Position this node centered over the subtrees.
            ymax = subtree_bottom
            self.subtree_bounds = (xmin, ymin, xmax, ymax)

        # Position the node.
        cx = (self.subtree_bounds[0] + self.subtree_bounds[2]) / 2
        cy = ymin + BinaryNode.node_radius
        self.center = (cx, cy)

    def draw_subtree_links(self, canvas, color):
        """ Draw the subtree's links."""
        if self.left_child != None:
            self.left_child.draw_subtree_links(canvas, color)
            canvas.create_line(self.center[0], self.center[1], self.left_child.center[0], self.left_child.center[1])
        if self.right_child != None:
            self.right_child.draw_subtree_links(canvas, color)
            canvas.create_line(self.center[0], self.center[1], self.right_child.center[0], self.right_child.center[1])

        # Outline the subtree for debugging.
        #canvas.create_rectangle(self.subtree_bounds, fill="", outline="red")

    def draw_subtree_nodes(self, canvas, bg_color, fg_color):
        """ Draw the subtree's nodes."""
        # Draw the node.
        x0 = self.center[0] - BinaryNode.node_radius
        y0 = self.center[1] - BinaryNode.node_radius
        x1 = self.center[0] + BinaryNode.node_radius
        y1 = self.center[1] + BinaryNode.node_radius
        canvas.create_oval(x0, y0, x1, y1, fill=bg_color, outline=fg_color)
        canvas.create_text(self.center, text=self.value)

        # Draw the descendants' nodes.
        if self.left_child != None:
            self.left_child.draw_subtree_nodes(canvas, bg_color, fg_color)
        if self.right_child != None:
            self.right_child.draw_subtree_nodes(canvas, bg_color, fg_color)

    def add_node(self, value):
        """ Add a node to this node's sorted subtree."""
        # See if this value is smaller than ours.
        if value < self.value:
            # The new value is smaller. Add it to the left subtree.
            if self.left_child == None:
                self.left_child = BinaryNode(value)
            else:
                self.left_child.add_node(value)
        else:
            # The new value is not smaller. Add it to the right subtree.
            if self.right_child == None:
                self.right_child = BinaryNode(value)
            else:
                self.right_child.add_node(value)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("sorted_tree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x240")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=2)
        label = tk.Label(frame, text="Value:")
        label.pack(side=tk.LEFT, padx=5, pady=2)
        self.value_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.value_entry.pack(side=tk.LEFT, padx=5, pady=2)
        self.value_entry.insert(tk.END, "10")
        add_button = tk.Button(frame, width=8, text="Add", command=self.add)
        add_button.pack(side=tk.LEFT, padx=5, pady=2)

        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Build the tree's root.
        self.root = BinaryNode(-infinity)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=add_button: add_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def add(self):
        """ Add the value to the tree."""
        value = int(self.value_entry.get())
        self.value_entry.delete(0, tk.END)
        self.value_entry.focus_force()

        self.root.add_node(value)
        self.draw_tree()

    def draw_tree(self):
        """ Draw the tree."""
        self.canvas.delete(tk.ALL)

        # Position the tree.
        if self.root.right_child != None:
            self.root.right_child.position_subtree(10, 10)

            # Draw the links.
            self.root.right_child.draw_subtree_links(self.canvas, "blue")

            # Draw the nodes.
            self.root.right_child.draw_subtree_nodes(self.canvas, "lightblue", "blue")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
