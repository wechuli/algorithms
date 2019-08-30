import tkinter as tk
import random
import math


def distance(point1, point2):
    """ Return the distance between two points."""
    dx = point1[0] - point2[0]
    dy = point1[1] - point2[1]
    return math.sqrt(dx * dx + dy * dy)


def draw_point(canvas, point, radius, bg_color, fg_color):
    """ Draw a point centered at this location."""
    x0 = point[0] - radius
    y0 = point[1] - radius
    x1 = point[0] + radius
    y1 = point[1] + radius
    canvas.create_oval(x0, y0, x1, y1, fill=bg_color, outline=fg_color)


class QuadtreeNode:
    """ The maximum number of points allowed in a quadtree node."""
    max_points = 10

    def __init__(self, xmin, ymin, xmax, ymax):
        # The bounds and middle X and Y values.
        self.xmin = xmin
        self.ymin = ymin
        self.xmax = xmax
        self.ymax = ymax
        self.xmid = (xmin + xmax) / 2
        self.ymid = (ymin + ymax) / 2

        # The points in this quadtree node.
        # This is None if this point has child nodes.
        self.points = []

        # The child quadtree nodes stored in order NW, NE, SW, SE.
        self.children = []

    def add_point(self, new_point):
        """ Add a point to this node."""
        # See if this quadtree node us full.
        if (self.points != None) and (len(self.points) >= QuadtreeNode.max_points):
            # Divide this quadtree node.
            self.children.append(QuadtreeNode(self.xmin, self.ymin, self.xmid, self.ymid)) # NW
            self.children.append(QuadtreeNode(self.xmid, self.ymin, self.xmax, self.ymid)) # NE
            self.children.append(QuadtreeNode(self.xmin, self.ymid, self.xmid, self.ymax)) # SW
            self.children.append(QuadtreeNode(self.xmid, self.ymid, self.xmax, self.ymax)) # SE

            # Move the points into the appropriate subtrees.
            for point in self.points:
                self.add_point_to_child(point)

            # Remove this node's points list.
            self.points = None

        # Add the new point here or in the appropriate subtree.
        if self.points != None:
            self.points.append(new_point)
        else:
            self.add_point_to_child(new_point)

    def add_point_to_child(self, point):
        """ Add a point to the appropriate child subtree."""
        for child in self.children:
            if (point[0] >= child.xmin) and \
               (point[0] <= child.xmax) and \
               (point[1] >= child.ymin) and \
               (point[1] <= child.ymax):
                child.add_point(point)
                break

    def draw_points(self, canvas, bg_color, fg_color, radius):
        """ Draw the points in this quadtree node."""
        # See if this node has children.
        if self.points == None:
            # Make the children draw themselves.
            for child in self.children:
                child.draw_points(canvas, bg_color, fg_color, radius)
        else:
            # Draw the points in this node.
            for point in self.points:
                draw_point(canvas, point, radius, bg_color, fg_color)

    def draw_areas(self, canvas, color):
        """ Draw the quadtree areas."""
        # Draw this quadtree node's area.
        canvas.create_rectangle(self.xmin, self.ymin, self.xmax, self.ymax, fill="", outline=color)

        # Draw the child nodes.
        for child in self.children:
            child.draw_areas(canvas, color)

    def find_point(self, target_point, radius):
        """ Find the specified point."""
        # Make sure the point might intersect this node's area.
        if (target_point[0] + radius < self.xmin) or \
           (target_point[0] - radius > self.xmax) or \
           (target_point[1] + radius < self.ymin) or \
           (target_point[1] - radius > self.ymax):
            return None

        # If we have children, look in them.
        if self.points == None:
            return self.find_point_in_children(target_point, radius)

        # Otherwise, search for the point in this quadtree node.
        return self.find_point_here(target_point, radius)

    def find_point_in_children(self, target_point, radius):
        """ Search the child subtrees for the target_point."""
        for child in self.children:
            point = child.find_point(target_point, radius)
            if point != None:
                return point

        # We didn't find it.
        return None

    def find_point_here(self, target_point, radius):
        """ Search this node's points for the target_point."""
        # The best point we have found so far.
        best_point = None
        best_dist = float("inf")

        # Search the points.
        for test_point in self.points:
            test_dist = distance(target_point, test_point)
            if test_dist < best_dist:
                best_dist = test_dist
                best_point = test_point

        # If the best point is more than radius away
        # from the target point, return None.
        if best_dist > radius:
            return None

        # Otherwise return the best point.
        return best_point


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("quadtree")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("500x400")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5)
        label = tk.Label(frame, text="# Points:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_points_entry = tk.Entry(frame, width=5, justify=tk.RIGHT)
        self.num_points_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_points_entry.insert(tk.END, "1000")

        self.button_is_checked = tk.IntVar()
        self.button_is_checked.trace("w", self.is_checked_changed)
        self.draw_boxes_checkbutton = tk.Checkbutton(frame, text="Show Tree", variable=self.button_is_checked)
        self.draw_boxes_checkbutton.pack(padx=5, pady=2, side=tk.LEFT)
        self.button_is_checked.set(True)

        self.create_button = tk.Button(frame, text="Create", width=8, command=self.create)
        self.create_button.pack(padx=5, pady=2, side=tk.LEFT)

        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)


        # The quadtree's root.
        self.root = None

        # The selected point.
        self.selected_point = None

        # The radius of a drawn point.
        self.radius = 5


        # Catch mouse clicks.
        self.canvas.bind("<Button-1>", self.mouse_click)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.create_button: self.create_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def create(self):
        """ Create the points."""
        # Make the root if we don't have one.
        if self.root == None:
            width = self.canvas.winfo_width()
            height = self.canvas.winfo_height()
            self.root = QuadtreeNode(0, 0, width, height)

        xmin = self.root.xmin + self.radius
        ymin = self.root.ymin + self.radius
        xmax = self.root.xmax - self.radius
        ymax = self.root.ymax - self.radius
        num_points = int(self.num_points_entry.get())
        for i in range(num_points):
            x = random.randint(xmin, xmax)
            y = random.randint(ymin, ymax)
            self.root.add_point((x, y))

        # Redraw.
        self.draw_canvas()

    def is_checked_changed(self, *args):
        """ The user clicked the checkbox. Redraw."""
        self.draw_canvas()

    def draw_canvas(self):
        """ Draw the points."""
        self.canvas.delete(tk.ALL)
        if self.root == None:
            return

        # Draw the points.
        self.root.draw_points(self.canvas, "", "blue", self.radius)

        # If there is a selected point, draw it.
        if self.selected_point != None:
            draw_point(self.canvas, self.selected_point, self.radius, "lightgreen", "green")

        # Draw the node areas.
        if self.button_is_checked.get():
            self.root.draw_areas(self.canvas, "red")

    def mouse_click(self, event):
        """ Select the clicked point."""
        # Find the point closest to the selected point.
        self.selected_point = self.root.find_point((event.x, event.y), self.radius)

        # Redraw.
        self.draw_canvas()


if __name__ == '__main__':
    app = App()

# app.root.destroy()

