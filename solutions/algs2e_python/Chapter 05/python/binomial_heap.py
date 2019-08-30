import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox
from tkinter import ttk
import random

class BinomialNode:
    def __init__(self, new_value):
        # This subtree's order.
        self.order = 0

        # This node's value.
        self.value = new_value

        # References to other nodes.
        self.parent = None
        self.next_sibling = None
        self.first_child = None

    @staticmethod
    def merge_trees(root1, root2):
        """ Merge two binomial trees of the same size."""
        # Ensure that root1 <= root2.
        if root2.value < root1.value:
            # Swap them.
            root1, root2 = root2, root1

        # Make root2 a sub-tree of root1.
        root2.parent = root1
        root2.next_sibling = root1.first_child
        root1.first_child = root2
        root1.next_sibling = None

        # The new tree has one greater order.
        root1.order += 1

        # Return the new root.
        return root1

    def add_to_treeview(self, treeview, parent):
        """ Display the subtree in a TreeView control."""
        # Add our value to the TreeView.
        node = treeview.insert(parent, tk.END, text=str(self), open=True)

        # Recursively add our children to the TreeView.
        child = self.first_child
        while child != None:
            child.add_to_treeview(treeview, node)
            child = child.next_sibling

    def to_list_string(self):
        """ Display a linked list's values."""
        txt = str(self)

        node = self.next_sibling
        while node != None:
            txt += f" -> {str(node)}"
            node = node.next_sibling
        return txt

    def set_order(self):
        """ Set the sub-tree's order."""
        self.order = 0
        if first_child == None:
            return

        # Higher orders.
        child = self.first_child
        while child != None:
            child.set_order()
            if self.order < child.order:
                self.order = child.order
            child = child.next_sibling
        self.order += 1

    def __str__(self):
        return f"(V={self.value}, O={self.order})"

class BinomialHeap:
    """ A linked list of child trees."""

    def __init__(self):
        self.root_sentinel = BinomialNode(-1000000)

    def find_root_before_smallest_value(self):
        # Find the root before the one with the smallest value.
        best_prev = self.root_sentinel
        best_value = 1000000

        prev = self.root_sentinel
        while prev.next_sibling != None:
            if prev.next_sibling.value < best_value:
                best_prev = prev
                best_value = prev.next_sibling.value
            prev = prev.next_sibling

        return best_prev

    def find_new_root_position(self, new_root):
        """ Find the node before where this value should go."""
        prev = self.root_sentinel
        while (prev.next_sibling != None) and (prev.next_sibling.order < new_root.order):
            prev = prev.next_sibling
        return prev

    def add_root(self, new_root):
        """ Add a new root in the proper position in the root list."""
        # Find the root before the position
        # where the new one belongs.
        prev = self.find_new_root_position(new_root)

        # Insert the new root after prev.
        new_root.next_sibling = prev.next_sibling
        prev.next_sibling = new_root

    def merge_with_heap(self, heap2):
        """ Merge with another heap."""
        # Merge the heaps' root lists.
        merged_list_sentinel = self.merge_root_lists(self, heap2)

        # Merge roots that have the same order.
        self.merge_roots_with_same_order(merged_list_sentinel)

        # Save the new roots.
        self.root_sentinel = merged_list_sentinel

    def merge_root_lists(self, heap1, heap2):
        """
        Merge the two heaps' roots into one list in ascending order.
        Return the sentinel for the merged list.
        """
        # Make a list to hold the merged roots.
        merged_list_sentinel = BinomialNode(-1000000)
        merged_list_bottom = merged_list_sentinel

        # Remove the root list sentinels.
        heap1.root_sentinel = heap1.root_sentinel.next_sibling
        heap2.root_sentinel = heap2.root_sentinel.next_sibling

        # Merge the two heaps' roots into one list in ascending order.
        while (heap1.root_sentinel != None) and (heap2.root_sentinel != None):
            # See which root has the smaller order.
            move_heap = None
            if heap1.root_sentinel.order <= heap2.root_sentinel.order:
                move_heap = heap1
            else:
                move_heap = heap2

            # Move the selected root.
            move_root = move_heap.root_sentinel
            move_heap.root_sentinel = move_root.next_sibling
            merged_list_bottom.next_sibling = move_root
            merged_list_bottom = move_root
            merged_list_bottom.next_sibling = None

        # Add any remaining roots.
        if heap1.root_sentinel != None:
            merged_list_bottom.next_sibling = heap1.root_sentinel
            heap1.root_sentinel = None
        elif heap2.root_sentinel != None:
            merged_list_bottom.next_sibling = heap2.root_sentinel
            heap2.root_sentinel = None

        # Return the merged list sentinel.
        return merged_list_sentinel

    def merge_roots_with_same_order(self, list_sentinel):
        # Sift through the list and merge roots with the same order.
        prev = list_sentinel
        node = prev.next_sibling
        next = None
        if node != None:
            next = node.next_sibling

        while next != None:
            # See if we need to merge node and next.
            if node.order != next.order:
                # Move to consider the next pair.
                prev = node
                node = next
                next = next.next_sibling
            else:
                # Remove them from the list.
                prev.next_sibling = next.next_sibling

                # Merge node and next.
                node = BinomialNode.merge_trees(node, next)

                # Insert the new root where the old ones were.
                next = prev.next_sibling
                node.next_sibling = next
                prev.next_sibling = node

                # If we have three matches in a row, skip the first one so we can merge
                # the other two in the next round. Otherwise consider node and next
                # again in the next round.
                if (next != None) and (node.order == next.order) and \
                    (next.next_sibling != None) and (node.order == next.next_sibling.order):
                    prev = node
                    node = next
                    next = next.next_sibling

    def enqueue(self, value):
        """ Add a value to the heap."""
        # If this heap is empty, just add the value.
        if self.root_sentinel.next_sibling == None:
            self.root_sentinel.next_sibling = BinomialNode(value)
        else:
            # Make a new heap containing the new value.
            new_heap = BinomialHeap()
            new_heap.enqueue(value)

            # Merge with the new heap.
            self.merge_with_heap(new_heap)

    def dequeue(self):
        """ Remove the smallest value from the heap."""
        if self.root_sentinel.next_sibling == None:
            raise Exception("The heap is empty.")

        # Find the root with the smallest value.
        prev = self.find_root_before_smallest_value()

        # Remove the tree containing the value from our list.
        root = prev.next_sibling
        prev.next_sibling = root.next_sibling

        # Make a new heap containing the
        # removed tree's subtrees.
        new_heap = BinomialHeap()
        subtree = root.first_child
        while (subtree != None):
            # Add this subtree to the top of the new heap's root list.
            next = subtree.next_sibling
            subtree.next_sibling = new_heap.root_sentinel.next_sibling
            new_heap.root_sentinel.next_sibling = subtree
            subtree = next

        # Merge with the new heap.
        self.merge_with_heap(new_heap)

        # Return the removed root's value.
        return root.value

    def add_to_treeview(self, treeview):
        """ Display the heap's trees in a TreeView control."""
        heap_node = treeview.insert("", tk.END, text="Heap", open=True)
        
        # Add our children to the TreeView.
        root = self.root_sentinel.next_sibling
        while root != None:
            root.add_to_treeview(treeview, heap_node)
            root = root.next_sibling

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # The main heap.
        self.the_heap = BinomialHeap()

        self.window = tk.Tk()
        self.window.title("binomial_heap")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("500x200")

        frame1 = tk.Frame(self.window)
        frame1.pack(padx=5, pady=5, side=tk.LEFT, anchor=tk.NW)
        frame2 = tk.Frame(self.window)
        frame2.pack(padx=5, pady=5, side=tk.LEFT, anchor=tk.NW, fill=tk.BOTH, expand=True)

        # Random values.
        label_frame = tk.LabelFrame(frame1, text="Random Values")
        label_frame.pack(padx=5, pady=5)

        min_label = tk.Label(label_frame, text="Minimum:", width=9, anchor=tk.W)
        min_label.grid(row=0, column=0, padx=5, pady=2)
        self.min_entry = tk.Entry(label_frame, width=8, justify=tk.RIGHT)
        self.min_entry.grid(row=0, column=1, padx=5, pady=2)
        self.min_entry.insert(tk.END, "1")

        max_label = tk.Label(label_frame, text="Maximum:", width=9, anchor=tk.W)
        max_label.grid(row=1, column=0, padx=5, pady=2)
        self.max_entry = tk.Entry(label_frame, width=8, justify=tk.RIGHT)
        self.max_entry.grid(row=1, column=1, padx=5, pady=2)
        self.max_entry.insert(tk.END, "100")

        num_values_label = tk.Label(label_frame, text="# Values:", width=9, anchor=tk.W)
        num_values_label.grid(row=2, column=0, padx=5, pady=2)
        self.num_values_entry = tk.Entry(label_frame, width=8, justify=tk.RIGHT)
        self.num_values_entry.grid(row=2, column=1, padx=5, pady=2)
        self.num_values_entry.insert(tk.END, "10")

        add_values_button = tk.Button(label_frame, text="Add Values", width=8, command=self.add_values)
        add_values_button.grid(row=1, column=2, padx=5, pady=2)

        # Enqueue and dequeue.
        enqueue_frame = tk.Frame(frame1)
        enqueue_frame.pack(padx=13, pady=5, side=tk.LEFT)

        value_label = tk.Label(enqueue_frame, text="Value:", width=9, anchor=tk.W)
        value_label.grid(row=0, column=0, padx=5, pady=2)
        self.value_entry = tk.Entry(enqueue_frame, width=8, justify=tk.RIGHT)
        self.value_entry.grid(row=0, column=1, padx=5, pady=2)
        self.value_entry.insert(tk.END, "10")

        enqueue_button = tk.Button(enqueue_frame, text="Enqueue", width=8, command=self.enqueue)
        enqueue_button.grid(row=0, column=2, padx=5, pady=2)

        dequeue_button = tk.Button(enqueue_frame, text="Dequeue", width=8, command=self.dequeue)
        dequeue_button.grid(row=1, column=2, padx=5, pady=2)

        # The Treeview.
        self.treeview = ttk.Treeview(frame2)
        self.treeview.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        scrollbar = ttk.Scrollbar(frame2, orient="vertical", command=self.treeview.yview)
        scrollbar.pack(padx=(0,5), pady=5, side=tk.RIGHT, fill=tk.Y)
        self.treeview.configure(yscrollcommand=scrollbar.set)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=enqueue_button: enqueue_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=dequeue_button: dequeue_button.invoke())) 

        #self.run_test()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def show_heap(self):
        """ Display the heap."""
        self.treeview.delete(*self.treeview.get_children())
        self.the_heap.add_to_treeview(self.treeview)

    def add_values(self):
        """Add random values to the heap."""
        try:
            min = int(self.min_entry.get())
            max = int(self.max_entry.get())
            num_values = int(self.num_values_entry.get())

            for i in range(num_values):
                self.the_heap.enqueue(random.randint(min, max))
        except Exception as e:
            messagebox.showinfo("Error", str(e))

        self.show_heap()

    def enqueue(self):
        """ Add a value to the heap."""
        try:
            value = int(self.value_entry.get())
            self.the_heap.enqueue(value)
        except Exception as e:
            messagebox.showinfo("Error", str(e))

        self.value_entry.delete(0, tk.END)
        self.value_entry.focus()
        self.show_heap()

    def dequeue(self):
        """ Remove the smallest value from the heap."""
        try:
            self.value_entry.delete(0, tk.END)
            self.value_entry.insert(0, f"{self.the_heap.dequeue()}")
        except Exception as e:
            messagebox.showinfo("Error", str(e))

        self.show_heap()

    def run_test(self):
        num_trials = 99
        num_items = 99
        for trial in range(num_trials):
            # Randomize the values 0 through num_items.
            values = [i for i in range(num_items)]
            random.shuffle(values)

            # Add the items to the heap.
            for value in values:
                self.the_heap.enqueue(value)

            # Display the first trial's structure.
            if trial == 0:
                self.show_heap()

            # Pull them off in order.
            for i in range(num_items):
                value = self.the_heap.dequeue()
                assert value == i, f"Dequeued value is {value} but should be {i}."
        messagebox.showinfo("Done", "Done")

if __name__ == '__main__':
    app = App()

# app.root.destroy()
