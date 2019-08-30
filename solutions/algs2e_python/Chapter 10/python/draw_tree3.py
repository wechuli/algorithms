import tkinter as tk


class NAryNode:
    # Class-level drawing parameters.
    node_radius = 10
    x_spacing = 20
    y_spacing = 20

    def __init__(self, name):
        self.name = name
        self.children = []

        # Drawing parameters.
        self.center = (0, 0)
        self.subtree_bounds = (
            self.center[0] - NAryNode.node_radius, 
            self.center[1] - NAryNode.node_radius, 
            self.center[0] + NAryNode.node_radius, 
            self.center[1] + NAryNode.node_radius)

    def position_subtree(self, xmin, ymin):
        """ Position the node."""
        # Set ymax to the bottom of this node.
        ymax = ymin + 2 * NAryNode.node_radius
        xmax = xmin

        # See if the node has any children.
        if len(self.children) == 0:
            # There are no children. Put the node here.
            xmax += 2 * NAryNode.node_radius
            self.subtree_bounds = (xmin, ymin, xmax, ymax)
        else:
            ymax += NAryNode.y_spacing

            # Position the child subtrees.
            subtree_bottom = ymax
            for i in range(len(self.children)):
                # Position this child subtree.
                child = self.children[i]
                child.position_subtree(xmax, ymax)

                # Update xmax to allow room for the subtree.
                xmax = child.subtree_bounds[2]

                # Update the subtree bottom.
                if child.subtree_bounds[3] > subtree_bottom:
                    subtree_bottom = child.subtree_bounds[3]

                # If this is not the last child, add horizontal
                # space before the next child subtree.
                if i < len(self.children) - 1:
                    xmax += NAryNode.x_spacing

            # Position this node centered over the subtrees.
            ymax = subtree_bottom
            self.subtree_bounds = (xmin, ymin, xmax, ymax)

        # Position the node.
        cx = (self.subtree_bounds[0] + self.subtree_bounds[2]) / 2
        cy = ymin + NAryNode.node_radius
        self.center = (cx, cy)

    def draw_subtree_links(self, canvas, color):
        """ Draw the subtree's links."""
        for child in self.children:
            child.draw_subtree_links(canvas, color)
            canvas.create_line(self.center[0], self.center[1], child.center[0], child.center[1])

        # Outline the subtree for debugging.
        #canvas.create_rectangle(self.subtree_bounds, fill="", outline="red")

    def draw_subtree_nodes(self, canvas, bg_color, fg_color):
        """ Draw the subtree's nodes."""
        # Draw the node.
        x0 = self.center[0] - NAryNode.node_radius
        y0 = self.center[1] - NAryNode.node_radius
        x1 = self.center[0] + NAryNode.node_radius
        y1 = self.center[1] + NAryNode.node_radius
        canvas.create_oval(x0, y0, x1, y1, fill=bg_color, outline=fg_color)
        canvas.create_text(self.center, text=self.name)

        # Draw the descendants' nodes.
        for child in self.children:
            child.draw_subtree_nodes(canvas, bg_color, fg_color)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("draw_tree2")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("270x240")

        canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Build the tree.
        root = NAryNode("E")
        node_a = NAryNode("A")
        node_b = NAryNode("B")
        node_c = NAryNode("C")
        node_d = NAryNode("D")
        node_f = NAryNode("F")
        node_g = NAryNode("G")
        node_h = NAryNode("H")
        node_i = NAryNode("I")
        node_j = NAryNode("J")
        node_k = NAryNode("K")
        node_l = NAryNode("L")
        node_m = NAryNode("M")
        root.children.append(node_b)
        root.children.append(node_f)
        node_b.children.append(node_a)
        node_b.children.append(node_d)
        node_d.children.append(node_c)
        node_f.children.append(node_i)
        node_i.children.append(node_g)
        node_i.children.append(node_j)
        node_g.children.append(node_h)
        node_i.children.append(node_k)
        node_k.children.append(node_l)
        node_k.children.append(node_m)

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
