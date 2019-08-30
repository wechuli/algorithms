import tkinter as tk
from tkinter import ttk
import math
import time
import random

# Yes, I know pygame can do a better job at this than tkinter.

def draw_oval(canvas, center, radius, color):
    """ Draw a filled circle centered at (x, y)."""
    canvas.create_oval( \
        center.x - radius, center.y - radius, \
        center.x + radius, center.y + radius, \
        fill=color, outline=color)

class Point2d:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """ Add  this point to a point or a vector."""
        return Point2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Subtract two points to get a vector."""
        return Vector2d(self.x - other.x, self.y - other.y)

    def __mul__(self, scale):
        """ Scale this point."""
        return Point2d(self.x * scale, self.y * scale)

    def __truediv__(self, scale):
        """ Scale this point."""
        return Point2d(self.x / scale, self.y / scale)

    def __str__(self):
        return f"({self.x}, {self.y})"

class Vector2d:
    def __init__(self, x, y):
        """
        Initialize from either (x, y) coordinates or
        two points x --> y.
        """
        if isinstance(x, Point2d):
            self.x = y.x - x.x
            self.y = y.y - x.y
        else:
            self.x = x
            self.y = y

    def __add__(self, other):
        """ Add two vectors."""
        return Vector2d(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """ Subtract two vectors."""
        return Vector2d(self.x - other.x, self.y - other.y)

    def __neg__(self):
        """ Return the negation of this vector."""
        return Vector2d(-self.x, -self.y)

    def __mul__(self, scale):
        """ Scale this vector."""
        return Vector2d(self.x * scale, self.y * scale)

    def __truediv__(self, scale):
        """ Scale this vector."""
        return Vector2d(self.x / scale, self.y / scale)

    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def set_length(self, new_length):
        old_length = self.length()
        self.x *= new_length / old_length
        self.y *= new_length / old_length

    def normalize(self):
        self.set_length(1)

    def __str__(self):
        return f"<{self.x}, {self.y}>"


class Boid:
    def __init__(self, position, velocity, max_speed, neighborhood_dist):
        self.position = position
        self.velocity = velocity
        self.max_speed = max_speed
        self.neighborhood_dist = neighborhood_dist

    def move(self, boids, people, target, delta_time, separation_wgt, \
        alignment_wgt, cohesion_wgt, target_wgt, person_wgt):
        """ Move the Boid."""
        num_neighbors = 0
        nbr_center = Point2d(0, 0)
        nbr_separation = Vector2d(0, 0)
        nbr_alignment = Vector2d(0, 0)

        for neighbor in boids:
            # Skip if it's this boid or not a neighbor.
            if neighbor == self:
                continue
            if self.distance(neighbor) > self.neighborhood_dist:
                continue

            num_neighbors += 1

            # Add vectors from the neighbors to this Boid
            # to push away from the neighbors (for separation).
            separationVector = (self.position - neighbor.position)
            nbr_separation += separationVector

            # Add the velocities (for alignment).
            nbr_alignment += neighbor.velocity

            # Add the locations (for cohesion).
            nbr_center += neighbor.position

        # Average the separation components.
        nbr_cohesion = Vector2d(0, 0)
        if num_neighbors > 0:
            nbr_separation /= num_neighbors

            # Average the alignment components.
            nbr_alignment /= num_neighbors

            # Use the average location to calculate the cohesion component.
            nbr_center /= num_neighbors
            nbr_cohesion = nbr_center - self.position

        # Get the vector toward the target.
        target_vector = target - self.position
        target_vector.normalize()

        # Adjust for people.
        num_people = 0
        person_vector = Vector2d(0, 0)
        for person in people:
            if self.distance_to_point(person) < self.neighborhood_dist:
                num_people += 1
                person_vector += (self.position - person)
        if num_people > 0:
            person_vector /= num_people

        # Adjust this Boid.
        self.velocity += \
            nbr_separation * separation_wgt + \
            nbr_alignment * alignment_wgt + \
            nbr_cohesion * cohesion_wgt + \
            target_vector * target_wgt + \
            person_vector * person_wgt
        if self.velocity.length() > self.max_speed:
            self.velocity.set_length(self.max_speed)

        # Update the location.
        self.position += self.velocity * delta_time

    def distance(self, other):
        """ Return the distance to another Boid."""
        v = self.position - other.position
        return v.length()

    def distance_to_point(self, point):
        """ Return the distance to another Boid."""
        v = self.position - point
        return v.length()

    def draw(self, canvas):
        """ Draw the Boid."""
        boid_radius = 2
        draw_oval(canvas, self.position, boid_radius, "black")


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.mouse_location = Point2d(0, 0)

        self.window = tk.Tk()
        self.window.title("boids_classical_people")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("510x390")

        # Parameters.
        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        pad_y = 2
        r = 0
        separation_wgt_label = tk.Label(frame, text="Separation Wgt:")
        separation_wgt_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.separation_wgt_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.separation_wgt_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.separation_wgt_entry.insert(tk.END, "10")

        r += 1
        alignment_wgt_label = tk.Label(frame, text="Alignment Wgt:")
        alignment_wgt_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.alignment_wgt_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.alignment_wgt_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.alignment_wgt_entry.insert(tk.END, "1")

        r += 1
        cohesion_wgt_label = tk.Label(frame, text="Cohesion Wgt:")
        cohesion_wgt_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.cohesion_wgt_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.cohesion_wgt_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.cohesion_wgt_entry.insert(tk.END, "5")

        r += 1
        target_wgt_label = tk.Label(frame, text="Target Wgt:")
        target_wgt_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.target_wgt_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.target_wgt_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.target_wgt_entry.insert(tk.END, "50")

        r += 1
        person_wgt_label = tk.Label(frame, text="Person Wgt:")
        person_wgt_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.person_wgt_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.person_wgt_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.person_wgt_entry.insert(tk.END, "50")

        r += 1
        max_speed_label = tk.Label(frame, text="Max Speed:")
        max_speed_label.grid(row=r, column=0, padx=5, pady=(pad_y+20, 2), sticky=tk.W)
        self.max_speed_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.max_speed_entry.grid(row=r, column=1, padx=5, pady=(pad_y+20, 2))
        self.max_speed_entry.insert(tk.END, "100")

        r += 1
        neighbor_dist_label = tk.Label(frame, text="Neighbor Dist:")
        neighbor_dist_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.neighbor_dist_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.neighbor_dist_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.neighbor_dist_entry.insert(tk.END, "10")

        r += 1
        num_boids_label = tk.Label(frame, text="# Boids:")
        num_boids_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.num_boids_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_boids_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.num_boids_entry.insert(tk.END, "20")

        r += 1
        self.start_button = tk.Button(frame, text="Start", width=8, command=self.start_click)
        self.start_button.grid(row=r, column=0, columnspan=2, padx=5, pady=pad_y)

        # The drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.start_button: self.start_button.invoke())) 

        # Track the mouse position and clicks.
        self.window.bind('<Motion>', self.mouse_move)
        self.canvas.bind("<Button-1>", self.mouse_click)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def mouse_move(self, event):
        self.mouse_location = Point2d(event.x, event.y)

    def mouse_click(self, event):
        self.people.append(Point2d(event.x, event.y))

    def start_click(self):
        """ Start or stop the simulation."""
        if self.start_button["text"] == "Start":
            self.start()
        else:
            self.stop()

    def start(self):
        self.boids = []
        self.people = []
        cx = self.canvas.winfo_width() / 2
        cy = self.canvas.winfo_height() / 2
        num_boids = int(self.num_boids_entry.get())
        max_speed = int(self.max_speed_entry.get())
        neighbor_dist = int(self.neighbor_dist_entry.get())
        for i in range(num_boids):
            location = Point2d( \
                cx + random.randint(-20, 20), \
                cy + random.randint(-20, 20))
            velocity = Vector2d( \
                random.randint(-5, 5), \
                random.randint(-5, 5))
            self.boids.append(Boid(location, velocity, max_speed, neighbor_dist))

        # Save the weights.
        self.separation_wgt = float(self.separation_wgt_entry.get())
        self.alignment_wgt = float(self.alignment_wgt_entry.get())
        self.cohesion_wgt = float(self.cohesion_wgt_entry.get())
        self.target_wgt = float(self.target_wgt_entry.get())
        self.person_wgt = float(self.person_wgt_entry.get())

        # Start the timer.
        self.start_button["text"] = "Stop"
        self.last_time = time.time()
        self.running = True
        self.draw_frame()

    def stop(self):
        self.running = False
        self.start_button["text"] = "Start"

    def draw_frame(self):
        """ Draw a frame of the simulation."""
        if not self.running:
            return

        # Get the elapsed time in seconds.
        now = time.time()
        delta_time = now - self.last_time
        self.last_time = now

        target = self.mouse_location

        # Move the Boids.
        for boid in self.boids:
            boid.move(self.boids, self.people, target, delta_time, \
                self.separation_wgt, self.alignment_wgt, \
                self.cohesion_wgt, self.target_wgt, self.person_wgt)

        # Redraw.
        self.draw_canvas()

        # Repeat.
        self.window.after(20, self.draw_frame)

    def draw_canvas(self):
        """ Draw the Boids."""
        if self.boids == None:
            return
        self.canvas.delete(tk.ALL)

        # Draw the people.
        person_radius = 4
        for person in self.people:
            draw_oval(self.canvas, person, person_radius, "blue")

        # Draw the Boids.
        for boid in self.boids:
            boid.draw(self.canvas)

        # Draw the mouse position.
        mouse_radius = 3
        draw_oval(self.canvas, self.mouse_location, mouse_radius, "red")


if __name__ == '__main__':
    app = App()

# app.root.destroy()

