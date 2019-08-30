import tkinter as tk
from tkinter import ttk
import math
import time
import random

def strange(point):
    """ Return the function's value F(x, y)."""
    r2 = (point.x * point.x + point.y * point.y) / 4
    r = math.sqrt(r2)

    theta = math.atan2(point.y, point.x)
    z = 3 * math.exp(-r2) * \
            math.sin(2 * math.pi * r) * \
            math.cos(3 * theta)
    return z

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

    def copy(self):
        return Point2d(self.x, self.y)

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


class Bug:
    def __init__(self, f, location, velocity, max_speed, lock_after):
        self.f = f
        self.location = location
        self.velocity = velocity
        self.max_speed = max_speed
        self.lock_after = lock_after
        self.best_point = location.copy()
        self.best_value = f(location)

        self.is_active = True
        self.moves_since_changed = 0

    def move(self, delta_time, cog_accel, soc_accel, global_best_point, global_best_value):
        """ Move the bug."""
        if not self.is_active:
            return global_best_point, global_best_value

        # Calculate the forces.
        cog_force = (self.best_point - self.location) * random.random() * cog_accel
        soc_force = (global_best_point - self.location) * random.random() * soc_accel

        # Update the velocity.
        self.velocity += (cog_force + soc_force) * delta_time
        if self.velocity.length() > self.max_speed:
            self.velocity.set_length(self.max_speed)

        # Update the position.
        self.location += self.velocity * delta_time

        # See if this gives a new best value.
        value = self.value()
        if value < self.best_value:
            self.best_value = value
            self.best_point = self.location.copy()

            if value < global_best_value:
                global_best_value = value
                global_best_point = self.location.copy()
        else:
            self.moves_since_changed += 1
            self.is_active = (self.moves_since_changed < self.lock_after)

        return global_best_point, global_best_value

    def value(self):
        """ Return the Bug's current value."""
        return self.f(self.location)

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("swarm_minimum")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("520x275")

        # Parameters.
        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.BOTH, expand=True)

        pad_y = 2
        r = 0
        num_bugs_label = tk.Label(frame, text="# Bugs:")
        num_bugs_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.num_bugs_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_bugs_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.num_bugs_entry.insert(tk.END, "100")

        r += 1
        cog_accel_label = tk.Label(frame, text="Cognition Acceleration:")
        cog_accel_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.cog_accel_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.cog_accel_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.cog_accel_entry.insert(tk.END, "2")

        r += 1
        soc_accel_label = tk.Label(frame, text="Social Acceleration:")
        soc_accel_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.soc_accel_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.soc_accel_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.soc_accel_entry.insert(tk.END, "2")

        r += 1
        max_speed_label = tk.Label(frame, text="Max Speed:")
        max_speed_label.grid(row=r, column=0, padx=5, pady=(pad_y, 2), sticky=tk.W)
        self.max_speed_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.max_speed_entry.grid(row=r, column=1, padx=5, pady=(pad_y+20, 2))
        self.max_speed_entry.insert(tk.END, "1")

        r += 1
        lock_after_label = tk.Label(frame, text="Lock After:")
        lock_after_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        self.lock_after_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.lock_after_entry.grid(row=r, column=1, padx=5, pady=pad_y)
        self.lock_after_entry.insert(tk.END, "100")

        r += 1
        self.start_button = tk.Button(frame, text="Start", width=8, command=self.start_click)
        self.start_button.grid(row=r, column=0, columnspan=2, padx=5, pady=pad_y)

        r += 1
        minimum_label = tk.Label(frame, text="Minimum:")
        minimum_label.grid(row=r, column=0, padx=5, pady=pad_y, sticky=tk.W)
        r += 1
        self.minimum_output_label = tk.Label(frame, text="")
        self.minimum_output_label.grid(row=r, column=0, columnspan=2, padx=5, pady=pad_y, sticky=tk.W)

        # The drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", width=256, height=256, borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.LEFT, anchor=tk.NW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.start_button: self.start_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def start_click(self):
        """ Start or stop the simulation."""
        if self.start_button["text"] == "Start":
            self.start()
        else:
            self.stop()

    def start(self):
        """ Make some bugs and start the simulation."""
        # World coordinates.
        self.wxmin = -3.5
        self.wxmax = 3.5
        self.wymin = -3.5
        self.wymax = 3.5

        # Device coordinates.
        self.dxmin = 0
        self.dxmax = self.canvas.winfo_width()
        self.dymin = 0
        self.dymax = self.canvas.winfo_width()
        self.xscale = (self.dxmax - self.dxmin) / (self.wxmax - self.wxmin)
        self.yscale = (self.dymax - self.dymin) / (self.wymax - self.wymin)

        # Make the bugs.
        num_bugs = int(self.num_bugs_entry.get())
        self.cog_accel = float(self.cog_accel_entry.get())
        self.soc_accel = float(self.soc_accel_entry.get())
        max_speed = float(self.max_speed_entry.get())
        lock_after = int(self.lock_after_entry.get())
        self.bugs = []
        for i in range(num_bugs):
            location = Point2d( \
                random.uniform(self.wxmin, self.wxmax), \
                random.uniform(self.wymin, self.wymax))
            velocity = Vector2d( \
                random.uniform(-1, 1), \
                random.uniform(-1, 1))
            self.bugs.append(Bug(strange, location, velocity, max_speed, lock_after))

        # Initialize best_point and best_value.
        self.global_best_point = self.bugs[0].location.copy()
        self.global_best_value = self.bugs[0].value()

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

        # Move the Bugs.
        still_active = False
        for bug in self.bugs:
            self.global_best_point, self.global_best_value = \
                bug.move(delta_time, self.cog_accel, self.soc_accel, \
                    self.global_best_point, self.global_best_value)
            if bug.is_active:
                still_active = True

        # Display the current global minimum.
        self.minimum_output_label["text"] = f"{self.global_best_value}"

        # Redraw.
        self.draw_canvas()

        # If no bugs are active, stop the simulation.
        if not still_active:
            self.stop()
        else:
            self.window.after(20, self.draw_frame)

    # Map world to device coordinates.
    def xy_w_to_d(self, x, y):
        new_x = self.dxmin + (x - self.wxmin) * self.xscale
        new_y = self.dymin + (y - self.wymin) * self.yscale
        return Point2d(new_x, new_y)

    def point_w_to_d(self, point):
        return self.xy_w_to_d(point.x, point.y)

    def draw_canvas(self):
        """ Draw the Bugs."""
        self.canvas.delete(tk.ALL)

        # Draw a checkerboard.
        x = self.wxmin
        while x <= self.wxmax:
            p0 = self.xy_w_to_d(x, self.wymin)
            p1 = self.xy_w_to_d(x, self.wymax)
            self.canvas.create_line(p0.x, p0.y, p1.x, p1.y, fill="gray")
            x += 1
        y = self.wymin
        while y <= self.wymax:
            p0 = self.xy_w_to_d(self.wxmin, y)
            p1 = self.xy_w_to_d(self.wxmax, y)
            self.canvas.create_line(p0.x, p0.y, p1.x, p1.y, fill="gray")
            y += 1

        # Draw the bugs.
        for bug in self.bugs:
            self.draw_bug(bug)

        # Draw the global best point.
        self.draw_circle(self.global_best_point, 5, "blue")

    def draw_bug(self, bug):
        """ Draw a bug."""
        if bug.is_active:
            self.draw_circle(bug.location, 2, "red")
        else:
            self.draw_circle(bug.location, 2, "orange")
        self.draw_circle(bug.best_point, 3, "green")

    def draw_circle(self, point, radius, color):
        """
        Draw a circle at the given point (in world coordinates)
        with the given radius (in device coordinates).
        """
        center = self.point_w_to_d(point)
        self.canvas.create_oval( \
            center.x - radius, center.y - radius, \
            center.x + radius, center.y + radius, \
            fill=color, outline=color)

if __name__ == '__main__':
    app = App()

# app.root.destroy()

