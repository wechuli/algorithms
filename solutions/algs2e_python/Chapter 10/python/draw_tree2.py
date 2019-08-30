import tkinter as tk


class BinaryNode:
    # Class-level drawing parameters.
    node_radius = 10
    x_spacing = 20
    y_spacing = 20

    def __init__(self, name):
        self.name = name
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
        canvas.create_text(self.center, text=self.name)

        # Draw the descendants' nodes.
        if self.left_child != None:
            self.left_child.draw_subtree_nodes(canvas, bg_color, fg_color)
        if self.right_child != None:
            self.right_child.draw_subtree_nodes(canvas, bg_color, fg_color)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("draw_tree2")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x240")

        canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Build the tree.
        root = BinaryNode("E")
        node_a = BinaryNode("A")
        node_b = BinaryNode("B")
        node_c = BinaryNode("C")
        node_d = BinaryNode("D")
        node_f = BinaryNode("F")
        node_g = BinaryNode("G")
        node_h = BinaryNode("H")
        node_i = BinaryNode("I")
        node_j = BinaryNode("J")
        root.left_child = node_b
        root.right_child = node_f
        node_b.left_child = node_a
        node_b.right_child = node_d
        node_d.left_child = node_c
        node_f.right_child = node_i
        node_i.left_child = node_g
        node_i.right_child = node_j
        node_g.right_child = node_h

        # Position the tree.
        root.position_subtree(10, 10)

        # Draw the links.
        root.draw_subtree_links(canvas, "green")

        # Draw the nodes.
        root.draw_subtree_nodes(canvas, "white", "blue")

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
