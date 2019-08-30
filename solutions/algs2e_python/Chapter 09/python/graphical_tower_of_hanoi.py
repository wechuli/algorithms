import tkinter as tk
import math
import time


# Drawing constants.
milliseconds = 10      # Tick speed.
pixels_per_frame = 4
y_margin = 10
x_margin = 10
peg_width = 10
disk_height = 10
min_disk_width = 30
disk_width_difference = 20
platform_height = 20

# The minimum and maximum Y coordinate for the pegs.
peg_ymin = 0
peg_ymax = 0

class MyStack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def __getitem__(self, index):
        # Peek at a value.
        return self.items[index]

    def __setitem__(self, index, value):
        # Set a value.
        self.items[index] = value

class DiskMove:
    """Represents moving the top disk from from_peg to to_peg."""
    def __init__(self, from_peg, to_peg):
        self.from_peg = from_peg
        self.to_peg = to_peg

    def make_move_points(self, pegs, peg_xs):
        """Calculate the disk's movement points and return the disk."""
        # Remove the disk from from_peg.
        disk = pegs[self.from_peg].pop()

        # Starting point.
        disk.points.append((disk.x, disk.y))

        # Move up.
        disk.points.append((disk.x, peg_ymin - disk_height))

        # Move above to_peg.
        disk.points.append((peg_xs[self.to_peg], peg_ymin - disk_height))

        # Move down onto to_peg.
        y = peg_ymax - disk_height * pegs[self.to_peg].size()
        disk.points.append((peg_xs[self.to_peg], y))

        # Add the disk to to_peg.
        pegs[self.to_peg].push(disk)

        return disk

class Disk:
    def __init__(self, canvas, rectangle, x, y):
        self.canvas = canvas
        self.rectangle = rectangle
        self.x = x
        self.y = y
        self.points = []

    def move(self, canvas):
        """
        Move towards the next point in the Points list.
        Return True if we have more moving to do.
        """
        # Do nothing if there are no points.
        if len(self.points) == 0:
            return False

        # Get the direction of movement.
        dx = self.points[0][0] - self.x
        dy = self.points[0][1] - self.y
        distance = math.sqrt(dx * dx + dy * dy)
        if distance < pixels_per_frame:
            # Remove the point from the points list.
            del self.points[0]
        else:
            # Move towards the point.
            dx = dx / distance * pixels_per_frame
            dy = dy / distance * pixels_per_frame

        # Move to the new location.
        canvas.move(self.rectangle, dx, dy)
        self.x += dx
        self.y += dy

        return len(self.points) > 0

class App:
    def __init__(self):
        self.items = []

        self.window = tk.Tk()
        self.window.title("graphical_tower_of_hanoi")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("420x185")

        # Inputs.
        input_frame = tk.Frame(self.window)
        input_frame.pack()
        num_disks_label = tk.Label(input_frame, text="# Disks:", padx=5, pady=5)
        num_disks_label.pack(side=tk.LEFT, pady=5)
        self.num_disks_entry = tk.Entry(input_frame, width=3, justify=tk.RIGHT)
        self.num_disks_entry.pack(side=tk.LEFT, pady=5)
        self.num_disks_entry.insert(tk.END, "4")
        solve_button = tk.Button(input_frame, text="Solve", width=10, command=self.solve)
        solve_button.pack(padx=(30,5), pady=5)

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=390, height=120,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0)
        self.canvas.pack(padx=5, pady=5)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_disks_entry.focus_force()
        self.window.mainloop()

    def solve(self):
        """Solve it and start the animation."""
        # Prepare the objects for the scene.
        num_disks = int(self.num_disks_entry.get())
        self.prepare_scene(num_disks)

        # Create the moves.
        self.moves = []
        self.tower_of_hanoi(self.moves, 0, 1, 2, num_disks)

        # Start the movement timer.
        self.moving_disk = None
        self.tick()

    def prepare_scene(self, num_disks):
        global peg_ymax
        global peg_ymin

        self.canvas.delete(tk.ALL)
        # Calculate the size of the largest disk.
        max_disk_width = min_disk_width + num_disks * disk_width_difference

        # Resize the canvas.
        peg_height = disk_height * (num_disks + 1)
        canvas_width = 3 * max_disk_width + 6 * x_margin
        canvas_height = peg_height + platform_height + 5 * x_margin
        self.canvas.config(width=canvas_width, height=canvas_height)

        # Create the platform.
        platform_xmin = x_margin
        platform_xmax = canvas_width - x_margin
        platform_ymax = canvas_height - y_margin
        platform_ymin = platform_ymax - platform_height
        platform = self.canvas.create_rectangle(
            platform_xmin, platform_ymin, platform_xmax, platform_ymax,
            fill="brown", outline="black")

        # peg_xs holds the X coordinates of the peg centers.
        self.peg_xs = []

        # Create the pegs.
        self.pegs = [MyStack() for i in range(3)]
        peg_height = disk_height * (num_disks + 2)
        peg_ymax = platform_ymin
        peg_ymin = peg_ymax - peg_height
        peg_x = platform_xmin + x_margin + max_disk_width / 2
        for i in range(3):
            self.peg_xs.append(peg_x)
            peg_xmin = peg_x - peg_width / 2
            peg_xmax = peg_xmin + peg_width
            peg_rectangle = self.canvas.create_rectangle(
                peg_xmin, peg_ymin, peg_xmax, peg_ymax,
                fill="lightgreen", outline="green")
            peg_x += max_disk_width + x_margin

        # Create the disks.
        disk_width = max_disk_width
        disk_ymax = platform_ymin
        disk_ymin = disk_ymax - disk_height
        for i in range(num_disks, 0, -1):
            # Make disk i's rectangle.
            disk_xmin = self.peg_xs[0] - disk_width / 2
            disk_xmax = disk_xmin + disk_width
            disk_rectangle = self.canvas.create_rectangle(
                disk_xmin, disk_ymin, disk_xmax, disk_ymax,
                fill="lightblue", outline="blue")

            # Make a Disk object and add it to the first peg.
            disk_x = self.peg_xs[0]
            disk = Disk(self.canvas, disk_rectangle, disk_x, disk_ymax)
            self.pegs[0].push(disk)

            # Prepare for the next disk.
            disk_ymin -= disk_height
            disk_ymax -= disk_height
            disk_width -= disk_width_difference

    def tower_of_hanoi(self, moves, from_peg, to_peg, other_peg, num_disks):
        """
        Move the top num_disks disks from from_peg to to_peg
        using other_peg to hold disks temporarily as needed.
        """
        # Recursively move the top n - 1 disks from from_peg to other_peg.
        if num_disks > 1:
            self.tower_of_hanoi(moves, from_peg, other_peg, to_peg, num_disks - 1)

        # Move the last disk from from_peg to to_peg.
        moves.append(DiskMove(from_peg, to_peg))

        # Recursively move the top n - 1 disks back from other_peg to to_peg.
        if num_disks > 1:
            self.tower_of_hanoi(moves, other_peg, to_peg, from_peg, num_disks - 1)

    def tick(self):
        """Move disks and redraw."""
        # If a disk is currently moving, move it some more.
        if self.moving_disk is not None:
            if not self.moving_disk.move(self.canvas):
                # This disk is done moving.
                self.moving_disk = None

        # If no disk is currently moving, start the next one.
        if self.moving_disk is None:
            if len(self.moves) > 0:
                disk_move = self.moves.pop(0)
                self.moving_disk = disk_move.make_move_points(self.pegs, self.peg_xs)

        # If a disk is moving, continue.
        if self.moving_disk is not None:
            self.window.after(milliseconds, self.tick)

    def kill_callback(self):
        self.window.destroy()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
