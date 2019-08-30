import tkinter as tk


class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left_child = None
        self.right_child = None

    def text_display(self, indent):
        """ Return a string containing the subtree's preorder traversal."""
        result = " " * indent + self.name + "\n"
        if self.left_child != None:
            result += self.left_child.text_display(indent + 4)
        if self.right_child != None:
            result += self.right_child.text_display(indent + 4)
        return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("text_display")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("150x200")

        label = tk.Label(self.window, borderwidth=2, relief=tk.SUNKEN)
        label.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

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

        # Display the textual representation.
        label["text"] = root.text_display(0)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        label.focus_force()
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
