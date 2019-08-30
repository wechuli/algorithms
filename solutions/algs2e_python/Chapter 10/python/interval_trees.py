import tkinter as tk
from tkinter import ttk

class IntervalNode:
    def __init__(self, xmin, xmax):
        self.xmin = xmin
        self.xmax = xmax
        self.xmid = (xmin + xmax) / 2
        self.left_overlap = []
        self.right_overlap = []
        self.left_child = None
        self.right_child = None

    def add_interval(self, interval):
        """ Add a interval to the node."""
        # Find the interval's position.
        if interval.right_point[0] < self.xmid:
            # Left branch.
            if self.left_child == None:
                self.left_child = IntervalNode(self.xmin, self.xmid)
            self.left_child.add_interval(interval)
        elif interval.left_point[0] > self.xmid:
            # Right branch.
            if self.right_child == None:
                self.right_child =  IntervalNode(self.xmid, self.xmax)
            self.right_child.add_interval(interval)
        else:
            # Overlapping.
            # Add to the left interval list in sorted order.
            position = 0
            for seg in self.left_overlap:
                if seg.left_point[0] < interval.left_point[0]:
                    position += 1
            self.left_overlap.insert(position, interval)

            # Add to the right interval list in sorted order.
            position = 0
            for seg in self.right_overlap:
                if seg.right_point[0] > interval.right_point[0]:
                    position += 1
            self.right_overlap.insert(position, interval)

    @staticmethod
    def make_interval_tree(intervals):
        """ Make an interval tree for the given horizontal intervals."""
        # Find the intervals' X coordinate bounds.
        xmin = intervals[0].left_point[0]
        xmax = xmin
        for interval in intervals:
            if interval.left_point[0] < xmin:
                xmin = interval.left_point[0]
            if interval.left_point[0] > xmax:
                xmax = interval.left_point[0]
            if interval.right_point[0] < xmin:
                xmin = interval.right_point[0]
            if interval.right_point[0] > xmax:
                xmax = interval.right_point[0]

        # Add the intervals to a tree.
        root = IntervalNode(xmin, xmax)
        for interval in intervals:
            root.add_interval(interval)

        # Return the tree.
        return root

    def find_overlapping_intervals(self, results, test_x):
        """ Find intervals that overlap the target X value."""
        # Check our overlap intervals.
        if test_x <= self.xmid:
            # Use the left overlap list.
            for seg in self.left_overlap:
                if seg.left_point[0] > test_x:
                    break
                results.append(seg)
        else:
            # Use the right overlap list.
            for seg in self.right_overlap:
                if seg.right_point[0] < test_x:
                    break
                results.append(seg)

        # Check left branch.
        if (test_x < self.xmid) and (self.left_child != None):
            self.left_child.find_overlapping_intervals(results, test_x)
        elif (test_x > self.xmid) and (self.right_child != None):
            self.right_child.find_overlapping_intervals(results, test_x)


class interval:
    """ Represent a horizontal intervals composed of two points."""
    def __init__(self, color, point1, point2):
        self.color = color

        # Save the points in order.
        if point1[0] < point2[0]:
            self.left_point = point1
            self.right_point = point2
        else:
            self.left_point = point2
            self.right_point = point1

    def __str__(self):
        return f"({left_point[0]}, {left_point[1]})--({right_point[0]}, {right_point[1]})"


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # The X coordinate of the test line.
        self.test_x = -1

        # The defined intervals.
        self.intervals = []

        # Variables for drawing new intervals.
        self.drawing_interval = False
        self.new_interval = interval("pink", [0, 0], [0, 0])

        # The interval tree.
        root = None

        # Build the user interface.
        self.window = tk.Tk()
        self.window.title("interval_trees")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        # Button.
        self.build_tree_button = tk.Button(self.window, text="Build Tree", width=10, state=tk.DISABLED, command=self.build_tree)
        self.build_tree_button.pack(padx=5, pady=5, side=tk.BOTTOM)

        # Drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Catch mouse events.
        self.canvas.bind("<Button-1>", self.left_mouse_down)
        self.canvas.bind("<B1-Motion>", self.left_mouse_move)
        self.canvas.bind("<ButtonRelease-1>", self.left_mouse_up)
        self.canvas.bind("<Button-3>", self.right_mouse_down)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def build_tree(self):
        """ Build the interval tree."""
        self.test_x = -1
        self.root = IntervalNode.make_interval_tree(self.intervals)
        self.draw()
        self.build_tree_button["state"] = tk.DISABLED


    def use_interval_tree(self):
        """
        Use the interval tree to see which horizontal
        lines intersect the vertical test line.
        """
        if self.root == None:
            return

        # Reset the colors of all horizontal intervals.
        self.reset_interval_colors()

        # See which intervals intersect the vertical test line.
        hits = []
        self.root.find_overlapping_intervals(hits, self.test_x)
        for interval in hits:
            interval.color = "red"

    def reset_interval_colors(self):
        for seg in self.intervals:
            seg.color="black"

    def left_mouse_down(self, event):
        # Define a new horizontal interval.
        self.drawing_interval = True
        self.new_interval.left_point = [event.x, event.y]
        self.new_interval.right_point = [event.x, event.y]
        self.test_x = -1
        self.root = None
        self.reset_interval_colors()
        self.draw()

    def left_mouse_move(self, event):
        # Continue drawing a new interval.
        if not self.drawing_interval:
            return
        self.new_interval.right_point[0] = event.x
        self.draw()

    def left_mouse_up(self, event):
        """ Stop drawing a new interval."""
        if not self.drawing_interval:
            return
        self.drawing_interval = False
        self.build_tree_button["state"] = tk.NORMAL

        # Don't make zero-length intervals.
        if self.new_interval.left_point[0] == self.new_interval.right_point[0]:
            return

        # Make the new interval.
        self.intervals.append(interval("black", \
            self.new_interval.left_point, \
            self.new_interval.right_point))

        self.draw()

    def right_mouse_down(self, event):
        # Right button. Define the vertical test line.
        if self.root != None:
            self.test_x = event.x

        # Apply the inverval tree if we have one.
        self.use_interval_tree()
        self.draw()

    def draw(self):
        """ Draw the intervals."""
        self.canvas.delete(tk.ALL)

        # Draw existing intervals.
        for seg in self.intervals:
            self.canvas.create_line( \
                seg.left_point[0], seg.left_point[1], \
                seg.right_point[0], seg.right_point[1], \
                fill=seg.color, width=3)

        # Draw the interval in progress (if any).
        if self.drawing_interval:
            self.canvas.create_line( \
                self.new_interval.left_point[0], self.new_interval.left_point[1], \
                self.new_interval.right_point[0], self.new_interval.right_point[1], \
                fill="blue", width=3)

        # Draw the vertical test line.
        if self.test_x >= 0:
            ymax = self.canvas.winfo_height()
            self.canvas.create_line(self.test_x, 0, self.test_x, ymax, fill="green", width=3)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
