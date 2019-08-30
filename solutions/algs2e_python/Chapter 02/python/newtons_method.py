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

        start_x = xtic_spacing * int((self.wxmin - xtic_spacing) / xtic_spacing)
        x = start_x
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


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("newtons_method")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("550x460")

        self.canvas = tk.Canvas(self.window, width=500, height=300,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Zeros:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.zero0_label = tk.Label(frame)
        self.zero0_label.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.zero1_label= tk.Label(frame)
        self.zero1_label.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        self.zero2_label = tk.Label(frame)
        self.zero2_label.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)

        # Make the DrawingCanvas.
        self.wxmin = -0.5
        self.wymin = -1.5
        self.wxmax = 4.5
        self.wymax = 1.5
        self.drawing_canvas = DrawingCanvas(self.canvas, self.wxmin, self.wymin, self.wxmax, self.wymax, 0, True)

        # Find the zeros.
        self.draw_graph()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def draw_graph(self):
        """ Draw the graph and zeros."""
        # Axes.
        self.drawing_canvas.wdraw_axes(1, 1, 0.1, 0.1, True, "gray")

        # Curve.
        xpix = self.drawing_canvas.xpix
        self.drawing_canvas.wdraw_function(self.f, "black", self.wxmin, self.wxmax, xpix)

        # Find the zeros.
        x0 = self.find_zero(0.3)
        self.zero0_label["text"] = f"({x0:.2f}, {self.f(x0):.2f})"

        x1 = self.find_zero(1)
        self.zero1_label["text"] = f"({x1:.2f}, {self.f(x1):.2f})"

        x2 = self.find_zero(3)
        self.zero2_label["text"] = f"({x2:.2f}, {self.f(x2):.2f})"


    def f(self, x):
        """ F(x)."""
        return x * x * x / 5 - x * x + x

    def df_dx(self, x):
        """ dF/dx."""
        return (3 * x * x - 10 * x + 5) / 5

    def find_zero(self, start_x):
        """ Use Newton's Method to find a zero from this starting point."""
        max_error = 1e-6
        x = start_x
        for i in range(100):
            # Calculate and plot this point.
            y = self.f(x)
            self.drawing_canvas.wdraw_circle(x, y, 4, "", "green")
            print(f"({x}, {y})")

            # If we have a small enough error, stop.
            if abs(y) < max_error:
                break

            # Update x.
            x -= y / self.df_dx(x)

        print()
        return x


if __name__ == '__main__':
    app = App()
