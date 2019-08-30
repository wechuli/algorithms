import tkinter as tk


class ThreadedNode:
    # Class-level drawing parameters.
    node_radius = 20
    x_spacing = 20
    y_spacing = 20

    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.left_thread = None
        self.right_thread = None

    def add_node(self, value):
        """ Add a node to self node's sorted subtree."""
        # See if the new value is smaller than ours.
        if value < self.value:
            # The new value is smaller. Add it to the left subtree.
            if self.left_child != None:
                self.left_child.add_node(value)
            else:
                # Add the new child here.
                child = ThreadedNode(value)
                child.left_thread = self.left_thread
                child.right_thread = self
                self.left_child = child
                self.left_thread = None
        else:
            # The new value is not smaller. Add it to the right subtree.
            if self.right_child != None:
                self.right_child.add_node(value)
            else:
                # Add the new child here.
                child = ThreadedNode(value)
                child.left_thread = self
                child.right_thread = self.right_thread
                self.right_child = child
                self.right_thread = None

    def position_subtree(self, xmin, ymin):
        """ Position the node."""
        # Set ymax to the bottom of self node.
        ymax = ymin + 2 * ThreadedNode.node_radius
        xmax = xmin

        # See if the node has any children.
        if (self.left_child == None) and (self.right_child == None):
            # There are no children. Put the node here.
            xmax += 2 * ThreadedNode.node_radius
            self.subtree_bounds = (xmin, ymin, xmax, ymax)
        else:
            ymax += ThreadedNode.y_spacing

            # Position the left subtree.
            subtree_bottom = ymax

            if self.left_child != None:
                self.left_child.position_subtree(xmax, ymax)

                # Update xmax to allow room for the left subtree.
                xmax = self.left_child.subtree_bounds[2]

                # Update the subtree bottom.
                subtree_bottom = self.left_child.subtree_bounds[3]

            xmax += ThreadedNode.x_spacing

            # Position the right subtree.
            if self.right_child != None:
                self.right_child.position_subtree(xmax, ymax)

                # Update xmax.
                xmax = self.right_child.subtree_bounds[2]

                # Update the subtree bottom.
                if self.right_child.subtree_bounds[3] > subtree_bottom:
                    subtree_bottom = self.right_child.subtree_bounds[3]

            # Position self node centered over the subtrees.
            ymax = subtree_bottom
            self.subtree_bounds = (xmin, ymin, xmax, ymax)

        # Position the node.
        cx = (self.subtree_bounds[0] + self.subtree_bounds[2]) / 2
        cy = ymin + ThreadedNode.node_radius
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
        x0 = self.center[0] - ThreadedNode.node_radius
        y0 = self.center[1] - ThreadedNode.node_radius
        x1 = self.center[0] + ThreadedNode.node_radius
        y1 = self.center[1] + ThreadedNode.node_radius
        canvas.create_oval(x0, y0, x1, y1, fill=bg_color, outline=fg_color)

        text = f"  {self.value:2}\n"
        if self.left_thread == None:
            text += "--"
        else:
            text += f"{self.left_thread.value:2}"
        text += "  "
        if self.right_thread == None:
            text += "--"
        else:
            text += f"{self.right_thread.value:2}"
        canvas.create_text(self.center, text=text)

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
        self.window.title("threaded_tree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("400x300")

        frame = tk.Frame(self.window)
        frame.pack(pady=(5, 0))
        label = tk.Label(frame, text="Value:")
        label.pack(side=tk.LEFT)
        self.value_entry = tk.Entry(frame, width=6, justify=tk.RIGHT)
        self.value_entry.pack(side=tk.LEFT, padx=5, pady=2)
        self.value_entry.insert(tk.END, "20")
        add_button = tk.Button(frame, text="Add", width=8, command=self.add)
        add_button.pack(padx=5, pady=2, side=tk.LEFT)

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.BOTH, expand=True)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(0, weight=1)

        self.canvas = tk.Canvas(frame, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.grid(padx=5, pady=5, row=0, column=0, columnspan=2, sticky=tk.NSEW)

        label = tk.Label(frame, text="Forward:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.forward_label = tk.Label(frame, borderwidth=1, relief=tk.GROOVE)
        self.forward_label.grid(padx=5, pady=2, row=1, column=1, sticky=tk.EW)

        label = tk.Label(frame, text="Backward:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.backward_label = tk.Label(frame, borderwidth=1, relief=tk.GROOVE)
        self.backward_label.grid(padx=5, pady=2, row=2, column=1, sticky=tk.EW)

        # The sentinel root node.
        self.root = None

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=add_button: add_button.invoke())) 

        # Force focus so Alt+F4 closes self window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def add(self):
        """ Add the value to the tree."""
        value = int(self.value_entry.get())

        if self.root != None:
            self.root.add_node(value)
        else:
            self.root = ThreadedNode(value)

        # Display the traversals.
        self.display_traversals()

        # Display the tree.
        self.draw_tree()

        self.value_entry.delete(0, tk.END)
        self.value_entry.focus_force()

    def display_traversals(self):
        # Forward.
        forward = self.get_traversal()
        text = ""
        for node in forward:
            text += f" {node.value}"
        self.forward_label["text"] = text[1:]

        # Backward.
        backward = self.get_backward_traversal()
        text = ""
        for node in backward:
            text += f" {node.value}"
        self.backward_label["text"] = text[1:]

    def get_traversal(self):
        """ Get the forward traversal."""
        traversal = []

        # Start at the root.
        node = self.root

        # Remember whether we got to a node via a branch or thread.
        # Pretend we go to the root via a branch so we go left next.
        via_branch = True

        # Repeat until the traversal is done.
        while node != None:
            # If we got here via a branch, then go
            # down and to the left as far as possible.
            if via_branch:
                while node.left_child != None:
                    node = node.left_child

            # Process this node.
            traversal.append(node)

            # Find the next node to process.
            if node.right_child == None:
                # Use the thread.
                node = node.right_thread
                via_branch = False
            else:
                # Use the right branch.
                node = node.right_child
                via_branch = True
        return traversal

    def get_backward_traversal(self):
        """ Get the backward traversal."""
        traversal = []

        # Start at the root.
        node = self.root

        # Remember whether we got to a node via a branch or thread.
        # Pretend we go to the root via a branch so we go right next.
        via_branch = True

        # Repeat until the traversal is done.
        while node != None:
            # If we got here via a branch, then go
            # down and to the right as far as possible.
            if via_branch:
                while node.right_child != None:
                    node = node.right_child

            # Process this node.
            traversal.append(node)

            # Find the next node to process.
            if node.left_child == None:
                # Use the thread.
                node = node.left_thread
                via_branch = False
            else:
                # Use the right branch.
                node = node.left_child
                via_branch = True
        return traversal

    def draw_tree(self):
        """ Draw the tree."""
        self.canvas.delete(tk.ALL)
        if self.root == None:
            return

        # Position the tree.
        self.root.position_subtree(10, 10)

        # Draw the links.
        self.root.draw_subtree_links(self.canvas, "green")

        # Draw the nodes.
        self.root.draw_subtree_nodes(self.canvas, "white", "blue")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
