import tkinter as tk

class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left_child = None
        self.right_child = None

    def traverse_preorder(self):
        """ Return a string containing the subtree's preorder traversal."""
        result = self.name
        if self.left_child != None:
            result += " " + self.left_child.traverse_preorder()
        if self.right_child != None:
            result += " " + self.right_child.traverse_preorder()
        return result

    def traverse_inorder(self):
        """ Return a string containing the subtree's inorder traversal."""
        result = ""
        if self.left_child != None:
            result += self.left_child.traverse_inorder() + " "
        result += self.name
        if self.right_child != None:
            result += " " + self.right_child.traverse_inorder()
        return result

    def traverse_postorder(self):
        """ Return a string containing the subtree's postorder traversal."""
        result = ""
        if self.left_child != None:
            result += self.left_child.traverse_postorder() + " "
        if self.right_child != None:
            result += self.right_child.traverse_postorder() + " "
        result += self.name
        return result

    def traverse_depth_first(self):
        """ Return a string containing the subtree's depth-first traversal."""
        result = ""

        # Place this node in a queue.
        children = []
        children.append(self)

        # Process the queue until it's empty.
        while len(children) > 0:
            # Get the next node in the queue.
            node = children.pop(0)

            # Process the node.
            result += " " + node.name

            # Add the node's children to the queue.
            if node.left_child != None:
                children.append(node.left_child)
            if node.right_child != None:
                children.append(node.right_child)

        # Remove the initial space.
        return result[1:]


class App:
    def __init__(self):
        """ Build a tree and display its traversals."""
        # Build the tree.
        root = BinaryNode("E")
        nodeA = BinaryNode("A")
        nodeB = BinaryNode("B")
        nodeC = BinaryNode("C")
        nodeD = BinaryNode("D")
        nodeF = BinaryNode("F")
        nodeG = BinaryNode("G")
        nodeH = BinaryNode("H")
        nodeI = BinaryNode("I")
        nodeJ = BinaryNode("J")
        root.left_child = nodeB
        root.right_child = nodeF
        nodeB.left_child = nodeA
        nodeB.right_child = nodeD
        nodeD.left_child = nodeC
        nodeF.right_child = nodeI
        nodeI.left_child = nodeG
        nodeI.right_child = nodeJ
        nodeG.right_child = nodeH

        # Display the traversals.
        print(f"Preorder:    {root.traverse_preorder()}")
        print(f"Inorder:     {root.traverse_inorder()}")
        print(f"Postorder:   {root.traverse_postorder()}")
        print(f"Depth First: {root.traverse_depth_first()}")
        print()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
