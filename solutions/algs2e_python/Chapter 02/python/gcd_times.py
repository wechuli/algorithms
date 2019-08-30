import random
import tkinter as tk


def log_x(x):
    return math.log(x, 2)


def gcd(a, b):
    """ Find GCD(a, b)."""
    # GCD(a, b) = GCD(b, a mod b).
    while b != 0:
        # Calculate the remainder.
        remainder = a % b

        # Calculate GCD(b, remainder).
        a = b
        b = remainder

    # GCD(a, 0) is a.
    return a

def lcm(a, b):
    """ Find LCM(a, b)."""
    # LCM(a, b) = a * b * GCD(a, b).
    return a * (b // gcd(a, b))

def gcd_steps(a, b):
    """ Return the number of steps needed to calculate GCD(a, b)."""
    # GCD(a, b) = GCD(b, a mod b).
    steps = 0
    while b != 0:
        steps += 1

        # Calculate the remainder.
        remainder = a % b

        # Calculate GCD(b, remainder).
        a = b
        b = remainder

    # GCD(a, 0) is a.
    #return a
    return steps


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

    def wdraw_connect_points(self, wpoints, color):
        """ Draw a connected series of points in world coordinates."""
        dpoints = []
        for point in wpoints:
            dpoints += self.w_to_d(point[0], point[1])
        self.canvas.create_line(dpoints, fill=color)

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
        self.window.title("gcd_times")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("570x300")

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Largest #:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.max_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.max_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.max_entry.insert(0, "100000000")
        label = tk.Label(frame, text="# Trials:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_trials_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_trials_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_trials_entry.insert(0, "10000")

        go_button = tk.Button(frame, text="Go", width=8, command=self.go)
        go_button.pack(padx=5, pady=2)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        self.ymax_label = tk.Label(frame, text="Y1", width=3)
        self.ymax_label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.N)
        self.canvas = tk.Canvas(frame, width=500, height=200,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.grid(padx=5, pady=2, row=0, column=1, rowspan=2, sticky=tk.W+tk.E)
        self.ymin_label = tk.Label(frame, text="Y2", width=3)
        self.ymin_label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.S)
        self.xmin_label = tk.Label(frame, text="X1", width=16, anchor=tk.W)
        self.xmin_label.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)
        self.xmax_label = tk.Label(frame, text="X2", width=16, anchor=tk.E)
        self.xmax_label.grid(padx=5, pady=2, row=2, column=1, sticky=tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.max_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def go(self):
        # Perform the trials.
        num_trials = int(self.num_trials_entry.get())
        coords = []
        max_num = int(self.max_entry.get())
        for i in range(num_trials):
            a = random.randint(1, max_num)
            b = random.randint(1, max_num)
            steps = gcd_steps(a, b)
            coords.append(((a + b) / 2, steps))

        # Sort the results.
        coords.sort()

        # Make the DrawingCanvas.
        self.wxmin = int(min(coords, key=lambda pair: pair[0])[0])
        self.wxmax = int(max(coords, key=lambda pair: pair[0])[0])
        self.wymin = int(min(coords, key=lambda pair: pair[1])[1])
        self.wymax = int(max(coords, key=lambda pair: pair[1])[1])
        self.drawing_canvas = DrawingCanvas(self.canvas, self.wxmin, self.wymin, self.wxmax, self.wymax, 10, True)

        # Graph the results.
        self.drawing_canvas.wdraw_connect_points(coords, "blue")

        # Draw y = log(x).
        xpix = self.drawing_canvas.xpix
        self.drawing_canvas.wdraw_function(log_x, "black", self.wxmin, self.wxmax, xpix)


if __name__ == '__main__':
    app = App()
