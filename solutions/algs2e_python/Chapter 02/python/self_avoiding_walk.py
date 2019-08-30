import random
import tkinter as tk
import tkinter.font as tk_font
import math

BORDER_WIDTH = 3

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with an empty walk.
        self.walk = None

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("self_avoiding_walk")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x360")

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=50, height=50,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        # Parameters.
        parameter_frame = tk.Frame(self.window)
        parameter_frame.pack(padx=5, pady=5, side=tk.BOTTOM)

        width_label = tk.Label(parameter_frame, text="Width:")
        width_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.width_entry = tk.Entry(parameter_frame, width=3, justify=tk.RIGHT)
        self.width_entry.grid(row=0, column=1, padx=5, pady=2)
        self.width_entry.insert(tk.END, "6")

        height_label = tk.Label(parameter_frame, text="Height:")
        height_label.grid(row=0, column=3, padx=5, pady=2, sticky=tk.W)
        self.height_entry = tk.Entry(parameter_frame, width=3, justify=tk.RIGHT)
        self.height_entry.grid(row=0, column=4, padx=5, pady=2)
        self.height_entry.insert(tk.END, "6")

        draw_button = tk.Button(parameter_frame, text="Draw", width=10, command=self.draw_walk)
        draw_button.grid(row=1, column=0, columnspan=4, padx=5, pady=2)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=draw_button: draw_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def draw_walk(self):
        """ Draw a new self avoiding walk."""
        self.canvas.delete(tk.ALL)

        # Get the grid size.
        width = int(self.width_entry.get())
        height = int(self.height_entry.get())

        # Define the grid points.
        canvas_width = self.canvas.winfo_height()
        canvas_height = self.canvas.winfo_width()
        dx = canvas_width / (width + 1)
        dy = canvas_height / (height + 1)
        grid_points = [[None for row in range(height)] for col in range(width)]

        for row in range(height):
            y = (row + 1) * dy
            for col in range(width):
                x = (col + 1) *dx
                grid_points[row][col] = (x, y)

        # Draw the grid points.
        radius = 3
        for row in grid_points:
            for point in row:
                x0 = point[0] - radius
                y0 = point[1] - radius
                x1 = x0 + 2 * radius
                y1 = y0 + 2 * radius
                self.canvas.create_oval(x0, y0, x1, y1, fill="blue", outline="blue")

        # Find the walk.
        walk_points = self.find_walk(width, height)

        # Draw the walk.
        points = []
        for point in walk_points:
            points.append(grid_points[point[1]][point[0]])
        self.canvas.create_line(points, fill="red")

        # Circle the starting point.
        col = walk_points[0][0]
        row = walk_points[0][1]
        point = grid_points[row][col]
        x0 = point[0] - 2 * radius
        y0 = point[1] - 2 * radius
        x1 = x0 + 4 * radius
        y1 = y0 + 4 * radius
        self.canvas.create_oval(x0, y0, x1, y1, outline="red")

    def find_walk(self, width, height):
        """Find a random self-avoiding walk."""
        # Make an array to show where we have been.
        visited = [[False for col in range(width)] for row in range(height)]

        # Start at a random vertex.
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        # Start the walk at (x, y).
        walk = [(x, y)]
        visited[x][y] = True

        # Repeat until we can no longer move.
        while True:
            # Make a list of potential neighbors.
            candidates = []
            candidates.append((x - 1, y))
            candidates.append((x + 1, y))
            candidates.append((x, y - 1))
            candidates.append((x, y + 1))

            # See which neighbors are on the lattice and unvisited.
            neighbors = []
            for point in candidates:
                if ((point[0] >= 0) and (point[0] < width) and \
                    (point[1] >= 0) and (point[1] < height) and \
                    not visited[point[0]][point[1]]):
                        neighbors.append(point)

            # If we have no unvisited neighbors, then we're stuck.
            if len(neighbors) == 0:
                break

            # Pick a random neighbor to visit.
            next = neighbors[random.randint(0, len(neighbors) - 1)]

            # Go there.
            walk.append(next)
            visited[next[0]][next[1]] = True
            x = next[0]
            y = next[1]

        return walk


if __name__ == '__main__':
    app = App()
