import random
import tkinter as tk


BORDER_WIDTH = 5

# The area of interest.
WXMIN = -5
WYMIN = -5
WXMAX = 5
WYMAX = 5

def map_canvas(canvas, xmin, ymin, xmax, ymax, margin):
    """Define parameters to map from world coordinates onto the canvas."""
    global wxmin
    global wymin
    global wxmax
    global wymax
    global wwid
    global whgt
    global dxmin
    global dymin
    global dxmax
    global dymax
    global xscale
    global yscale

    wxmin = xmin
    wymin = ymin
    wxmax = xmax
    wymax = ymax
    wwid = xmax - xmin
    whgt = ymax - ymin

    canvas.update()
    dxmin = 0
    dymin = 0
    dxmax = canvas.winfo_width() - 2 * margin - 1
    dymax = canvas.winfo_height() - 2 * margin - 1

    # Flip the Y coordinates to invert the result.
    temp = dymin
    dymin = dymax
    dymax = temp

    xscale = (dxmax - dxmin) / (xmax - xmin)
    yscale = (dymax - dymin) / (ymax - ymin)

def w_to_d(point):
    """Map a point from world to device coordinates."""
    global wxmin
    global wymin
    global dxmin
    global dymin
    global xscale
    global yscale
    x = (point[0] - wxmin) * xscale + dxmin
    y = (point[1] - wymin) * yscale + dymin
    return (x, y)

def wdraw_point(canvas, x0, y0, color):
    p0 = w_to_d((x0, y0))
    canvas.create_oval(p0[0], p0[1], p0[0] + 1, p0[1] + 1, fill=color, outline="")

def wdraw_oval(canvas, x0, y0, x1, y1, bg_color, fg_color):
    p0 = w_to_d((x0, y0))
    p1 = w_to_d((x1, y1))
    canvas.create_oval(p0[0], p0[1], p1[0], p1[1], fill=bg_color, outline=fg_color)

def wdraw_rectangle(canvas, x0, y0, x1, y1, bg_color, fg_color):
    p0 = w_to_d((x0, y0))
    p1 = w_to_d((x1, y1))
    canvas.create_rectangle(p0[0], p0[1], p1[0], p1[1], fill=bg_color, outline=fg_color)


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("monte_carlo_integration")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x380")

        self.canvas = tk.Canvas(self.window, width=280, height=280,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Points:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_points_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_points_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_points_entry.insert(0, "1000")
        integrate_button = tk.Button(frame, text="Integrate", width=10, command=self.integrate)
        integrate_button.pack(padx=5, pady=2, side=tk.LEFT)
        reset_button = tk.Button(frame, text="Reset", width=10, command=self.reset)
        reset_button.pack(padx=5, pady=2, side=tk.LEFT)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Area:")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.area_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.area_entry.grid(padx=5, pady=2, row=0, column=1)
        label = tk.Label(frame, text="Total points:")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.total_points_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.total_points_entry.grid(padx=5, pady=2, row=1, column=1)

        # Make some counters.
        self.num_hits = 0
        self.num_misses = 0
        self.total_points = 0

        # Display the initial image.
        self.make_image()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=integrate_button: integrate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_points_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def reset(self):
        """ Reset the counters."""
        self.num_hits = 0
        self.num_misses = 0
        self.total_points = 0

        self.make_image()

    def integrate(self):
        """ Perform the integration."""
        global wxmin
        global wymin
        global wxmax
        global wymax

        # Get the parameters.
        num_points = int(self.num_points_entry.get())
        for i in range(num_points):
            # Pick a random point within the area of interest.
            x = wxmin + random.random() * wwid
            y = wymin + random.random() * whgt

            # See if it's in the shape.
            if self.point_is_in_shape(x, y):
                wdraw_point(self.canvas, x, y, "blue")
                self.num_hits += 1
            else:
                wdraw_point(self.canvas, x, y, "red")
                self.num_misses += 1

        # Calculate the area.
        self.total_points += num_points
        area = wwid * -whgt * self.num_hits / self.total_points
        self.area_entry.delete(0, tk.END)
        self.area_entry.insert(0, f"{area:,.12}")
        self.total_points_entry.delete(0, tk.END)
        self.total_points_entry.insert(0, f"{self.total_points}")

    def make_image(self):
        """ Make the basic image and reset the area counts."""
        map_canvas(self.canvas, WXMIN, WYMIN, WXMAX, WYMAX, BORDER_WIDTH)

        # Reset the area data.
        self.area_entry.delete(0, tk.END)
        self.total_points_entry.delete(0, tk.END)

        # Clear the canvas.
        self.canvas.delete(tk.ALL)

        # Fill the shapes.
        wdraw_oval(self.canvas, -2, -4, 2, 4, "lightblue", "")
        wdraw_oval(self.canvas, -4, -2, 4, 2, "lightblue", "")
        wdraw_oval(self.canvas, -1.7, -1.7, 1.7, 1.7, "white", "")
        wdraw_oval(self.canvas, -3, -1, -1, 1, "white", "")
        wdraw_oval(self.canvas, 1, -1, 3, 1, "white", "")

        # Outline the shapes.
        wdraw_oval(self.canvas, -2, -4, 2, 4, "", "blue")
        wdraw_oval(self.canvas, -4, -2, 4, 2, "", "blue")
        wdraw_oval(self.canvas, -1.7, -1.7, 1.7, 1.7, "", "blue")
        wdraw_oval(self.canvas, -3, -1, -1, 1, "", "blue")
        wdraw_oval(self.canvas, 1, -1, 3, 1, "", "blue")

    def point_is_in_shape(self, x, y):
        """ Return True if the point is inside the shape."""
        # See if it is inside all of the ellipses.
        if ((x * x / 4.0 + y * y / 16.0 > 1.0) and (x * x / 16.0 + y * y / 4.0 > 1.0)):
            return False

        # See if it is inside any circle.
        if (x * x + y * y < 1.7 * 1.7):
            return False
        if ((x + 2) * (x + 2) + y * y < 1):
            return False
        if ((x - 2) * (x - 2) + y * y < 1):
            return False
        return True


if __name__ == '__main__':
    app = App()
