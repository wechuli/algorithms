import random
import tkinter as tk
import math


class DrawingCanvas():
    """ A canvas drawing manager."""
    def __init__(self, canvas, wxmin, wymin, wxmax, wymax, dmargin, y_is_flipped):
        self.canvas = canvas
        self.wxmin = wxmin
        self.wymin = wymin
        self.wxmax = wxmax
        self.wymax = wymax
        self.dmargin = dmargin
        self.y_is_flipped = y_is_flipped

        self.set_scales()

    def set_scales(self):
        """ Calculate scale parameters for the canvas's current size."""
        self.canvas.update()
        self.dxmin = self.dmargin
        self.dymin = self.dmargin
        self.dxmax = self.canvas.winfo_width() - self.dmargin - 1
        self.dymax = self.canvas.winfo_height() - self.dmargin - 1

        # Flip the Y coordinates to invert the result.
        if self.y_is_flipped:
            self.dymin, self.dymax = self.dymax, self.dymin

        self.xscale = (self.dxmax - self.dxmin) / (self.wxmax - self.wxmin)
        self.yscale = (self.dymax - self.dymin) / (self.wymax - self.wymin)

        # Calculate 1 pixel in world coordinates.
        self.xpix = 1 / self.xscale
        self.ypix = 1 / self.yscale

    def w_to_d(self, wx, wy):
        """Map a point from world to device coordinates."""
        dx = (wx - self.wxmin) * self.xscale + self.dxmin
        dy = (wy - self.wymin) * self.yscale + self.dymin
        return dx, dy

    def clear(self):
        self.canvas.delete(tk.ALL)

    def wdraw_line(self, wx0, wy0, wx1, wy1, color, arrow):
        """ Draw a line in world coordinates."""
        dx0, dy0 = self.w_to_d(wx0, wy0)
        dx1, dy1 = self.w_to_d(wx1, wy1)
        self.canvas.create_line(dx0, dy0, dx1, dy1, fill=color, arrow=arrow)

    def wdraw_axes(self, xtic_spacing, ytic_spacing, tic_hgt, tic_wid, do_draw_text, color):
        """ Draw coordinate axes."""
        self.wdraw_line(self.wxmin, 0, self.wxmax, 0, color, arrow=tk.BOTH)
        self.wdraw_line(0, self.wymin, 0, self.wymax, color, arrow=tk.BOTH)

        startx = xtic_spacing * int((self.wxmin - xtic_spacing) / xtic_spacing)
        x = startx
        while x < self.wxmax:
            if (abs(x) > 0.01):
                dx0, dy0 = self.w_to_d(x, tic_hgt)
                dx1, dy1 = self.w_to_d(x, -tic_hgt)
                self.canvas.create_line(dx0, dy0, dx1, dy1, fill=color)
                if do_draw_text:
                    self.canvas.create_text(dx1, dy1, text=str(x), fill=color, anchor=tk.N)
            x += xtic_spacing

        starty = ytic_spacing * int((self.wymin - ytic_spacing) / ytic_spacing)
        y = starty
        while y < self.wymax:
            if (abs(y) > 0.01):
                dx0, dy0 = self.w_to_d(tic_wid, y)
                dx1, dy1 = self.w_to_d(-tic_wid, y)
                self.canvas.create_line(dx0, dy0, dx1, dy1, fill=color)
                if do_draw_text:
                    self.canvas.create_text(dx1, dy1, text=str(y), fill=color, anchor=tk.E)
            y += ytic_spacing

    def wdraw_polyline(self, wcoords, color):
        """ Draw a connected series of points in world coordinates."""
        dpoints = []
        for i in range(0, len(wcoords), 2):
            dpoints += self.w_to_d(wcoords[i], wcoords[i+1])
        self.canvas.create_line(dpoints, fill=color)

    def wdraw_polygon(self, wcoords, fill, outline):
        """ Draw a polygon in world coordinates."""
        dpoints = []
        for i in range(0, len(wcoords), 2):
            dpoints += self.w_to_d(wcoords[i], wcoords[i+1])
        self.canvas.create_polygon(dpoints, fill=fill, outline=outline)

    def wdraw_rotated_text(self, wx, wy, text, angle, color, font):
        """ Draw a rotated text at the indicated position in world coordinates."""
        dx, dy = self.w_to_d(wx, wy)
        self.canvas.create_text(dx, dy, text=text, angle=angle, fill=color, font=font)

    def wdraw_function(self, func, color, wxmin, wxmax, step_x):
        """ Draw a function."""
        points = []
        x = wxmin
        while x <= wxmax:
            points.append(x)
            points.append(func(x))
            x += step_x
        self.wdraw_polyline(points, color)

    def wdraw_circle(self, wx, wy, dradius, fill, outline):
        """ Draw an oval at the indicated position in world coordinates."""
        dx, dy = self.w_to_d(wx, wy)
        self.canvas.create_oval(dx - dradius, dy - dradius, dx + dradius, dy + dradius, fill=fill, outline=outline)

    def wdraw_oval(self, wx0, wy0, wx1, wy1, fill, outline):
        """ Draw an oval at the indicated position in world coordinates."""
        dx0, dy0 = self.w_to_d(wx0, wy0)
        dx1, dy1 = self.w_to_d(wx1, wy1)
        self.canvas.create_oval(dx0, dy0, dx1, dy1, fill=fill, outline=outline)

    def wdraw_rectangle(self, wx0, wy0, wx1, wy1, fill, outline):
        """ Draw a rectangle at the indicated position in world coordinates."""
        dx0, dy0 = self.w_to_d(wx0, wy0)
        dx1, dy1 = self.w_to_d(wx1, wy1)
        self.canvas.create_rectangle(dx0, dy0, dx1, dy1, fill=fill, outline=outline)


def integrate_rectangle(function, xmin, xmax, intervals):
    """ Integrate by using the rectangle rule."""
    dx = (xmax - xmin) / intervals
    total = 0

    # Perform the integration.
    x = xmin
    for interval in range(intervals):
        # Add the area in the rectangle for this slice.
        total += dx * function(x)

        # Move to the next slice.
        x += dx

    return total


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("rectangle_rule")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("400x460")

        label = tk.Label(self.window, text="y = 1 + x + Sin(2 * x)")
        label.pack(padx=5, pady=2, side=tk.TOP)

        self.canvas = tk.Canvas(self.window, width=280, height=280,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP, fill=tk.X)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="X:")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.xmin_entry = tk.Entry(frame, width=5, justify=tk.RIGHT)
        self.xmin_entry.grid(padx=5, pady=2, row=0, column=1)
        self.xmin_entry.insert(0, "0")
        label = tk.Label(frame, text="to")
        label.grid(padx=5, pady=2, row=0, column=2)
        self.xmax_entry = tk.Entry(frame, width=5, justify=tk.RIGHT)
        self.xmax_entry.grid(padx=5, pady=2, row=0, column=3)
        self.xmax_entry.insert(0, "5")

        label = tk.Label(frame, text="# Intervals:")
        label.grid(padx=5, pady=2, row=1, column=0, columnspan=3)
        self.intervals_entry = tk.Entry(frame, width=5, justify=tk.RIGHT)
        self.intervals_entry.grid(padx=5, pady=2, row=1, column=3)
        self.intervals_entry.insert(0, "10")

        integrate_button = tk.Button(self.window, text="Integrate", width=10, command=self.integrate)
        integrate_button.pack(padx=5, pady=2, side=tk.TOP)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Est. Area:")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.est_area_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.est_area_entry.grid(padx=5, pady=2, row=0, column=1)

        label = tk.Label(frame, text="True Area:")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.true_area_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.true_area_entry.grid(padx=5, pady=2, row=1, column=1)
        label = tk.Label(frame, text="% Err:")
        label.grid(padx=5, pady=2, row=1, column=2)
        self.pct_error_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.pct_error_entry.grid(padx=5, pady=2, row=1, column=3)

        # Make the DrawingCanvas.
        self.wxmin = -1
        self.wymin = -1
        self.wxmax = 7
        self.wymax = 7
        self.drawing_canvas = DrawingCanvas(self.canvas, self.wxmin, self.wymin, self.wxmax, self.wymax, 0, True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=integrate_button: integrate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.xmin_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def integrate(self):
        """ Perform the integration."""
        # Get parameters.
        xmin = float(self.xmin_entry.get())
        xmax = float(self.xmax_entry.get())

        intervals = int(self.intervals_entry.get())

        # Integrate.
        est_area = integrate_rectangle(self.f, xmin, xmax, intervals)
        self.est_area_entry.delete(0, tk.END)
        self.est_area_entry.insert(0, f"{est_area:,.12}")

        # Display the true area and percent error.
        true_area = self.anti_derivative_f(xmax) - self.anti_derivative_f(xmin)
        self.true_area_entry.delete(0, tk.END)
        self.true_area_entry.insert(0, f"{true_area:,.12}")

        pct_error = 100 * (est_area - true_area) / true_area
        self.pct_error_entry.delete(0, tk.END)
        self.pct_error_entry.insert(0, f"{pct_error:,.4}%")

        # Draw the graph.
        self.draw_graph()

    def f(self, x):
        """ The function we will integrate."""
        return 1 + x + math.sin(2.0 * x)

    def anti_derivative_f(self, x):
        """ The anti-derivative of the function."""
        return x + x * x / 2.0 - math.cos(2.0 * x) / 2.0

    def draw_graph(self):
        """ Draw the graph. (This is for visualization and isn't part of the algorithm.)"""
        """ Make the basic image and reset the area counts."""
        self.drawing_canvas.clear()

        # Get parameters.
        xmin = float(self.xmin_entry.get())
        xmax = float(self.xmax_entry.get())

        intervals = int(self.intervals_entry.get())

        # Fill and draw the rectangles.
        self.draw_rectangles(self.f, xmin, xmax, intervals, "lightblue", "blue")

        # Draw axes.
        self.drawing_canvas.wdraw_axes(1, 1, 0.1, 0.1, True, "red")

        # Draw the function.
        xpix = self.drawing_canvas.xpix
        self.drawing_canvas.wdraw_function(self.f, "green", self.wxmin, self.wxmax, xpix)

    def draw_rectangles(self, function, xmin, xmax, intervals, fill, outline):
        """ Draw the integration trapezoids."""
        dx = (xmax - xmin) / intervals

        # Perform the integration.
        x = xmin
        for interval in range(intervals):
            # Draw this slice.
            y = function(x)
            self.drawing_canvas.wdraw_rectangle(x, 0, x + dx, y, fill, outline)

            # Move to the next slice.
            x += dx


if __name__ == '__main__':
    app = App()
