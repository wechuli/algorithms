import random
import tkinter as tk
import math
import tkinter.font as tk_font


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

    def wdraw_polyline(self, wcoords, color, width):
        """ Draw a connected series of points in world coordinates."""
        dpoints = []
        for i in range(0, len(wcoords), 2):
            dpoints += self.w_to_d(wcoords[i], wcoords[i+1])
        self.canvas.create_line(dpoints, fill=color, width=width)

    def wdraw_polygon(self, wcoords, fill, outline):
        """ Draw a polygon in world coordinates."""
        dpoints = []
        for i in range(0, len(wcoords), 2):
            dpoints += self.w_to_d(wcoords[i], wcoords[i+1])
        self.canvas.create_polygon(dpoints, fill=fill, outline=outline)

    def wdraw_rotated_text(self, wx, wy, text, angle, color, font, anchor):
        """ Draw a rotated text at the indicated position in world coordinates."""
        dx, dy = self.w_to_d(wx, wy)
        self.canvas.create_text(dx, dy, text=text, angle=angle, fill=color, font=font, anchor=anchor)

    def wdraw_function(self, func, color, wxmin, wxmax, step_x, width):
        """ Draw a function."""
        points = []
        x = wxmin
        while x <= wxmax:
            points.append(x)
            points.append(func(x))
            x += step_x
        self.wdraw_polyline(points, color, width)

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
        self.window.title("two_dice_rolls")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("600x350")

        frame = tk.Frame()
        frame.pack(side=tk.TOP, fill=tk.X)
        label = tk.Label(frame, text="# Trials:")
        label.pack(padx=5, pady=5, side=tk.LEFT)
        self.num_trials_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.num_trials_entry.pack(padx=5, pady=5, side=tk.LEFT)
        self.num_trials_entry.insert(0, 100)
        roll_button = tk.Button(frame, text="Roll", width=10, command=self.roll)
        roll_button.pack(padx=5, pady=5, side=tk.LEFT)

        self.canvas = tk.Canvas(self.window, width=280, height=280,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=roll_button: roll_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_trials_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def roll(self):
        """ Simulate rolling two dice."""
        # Make a list to hold value counts.
        # The value counts[i] represents rolls of i.
        counts = [0 for i in range(13)]

        # Roll.
        num_trials = int(self.num_trials_entry.get())
        for i in range(num_trials):
            result = random.randint(1, 6) + random.randint(1, 6)
            counts[result] += 1

        # The expected percentages.
        expected = \
        [ \
            0, 0, 1 / 36, 2 / 36, 3 / 36, 4 / 36, 5 / 36, \
            6 / 36, 5 / 36, 4 / 36, 3 / 36, 2 / 36, 1 / 36 \
        ]

        # Make the DrawingCanvas.
        wxmin = 2
        wymin = 0
        wxmax = 13
        wymax = max(max(counts), num_trials * max(expected))
        drawing_canvas = DrawingCanvas(self.canvas, wxmin, wymin, wxmax, wymax, 10, True)
        drawing_canvas.clear()

        # Make a label font.
        label_font = tk_font.Font(family="Times New Roman", size=10)

        # Display the results.
        for x in range(2, 13):
            drawing_canvas.wdraw_rectangle(x, 0, x + 1, counts[x], "lightblue", "blue")

            percent = 100 * counts[x] / num_trials
            expected_percent = 100 * expected[x]
            error = 100 * (expected_percent - percent) / expected_percent
            text = f"{percent:.2f}\n{expected_percent:.2f}\n{error:.2f}%"
            drawing_canvas.wdraw_rotated_text(x + 0.5, counts[x], text, 0, "red", label_font, tk.N)



        # Scale the expected percentages for the number of rolls.
        expected = [i * num_trials for i in expected]

        # Draw the expected results.
        points = []
        points.append(2)
        points.append(0)
        for x in range(2, 13):
            points.append(x)
            points.append(expected[x])
            points.append(x + 1)
            points.append(expected[x])
        points.append(13)
        points.append(0)
        drawing_canvas.wdraw_polyline(points, "red", 3)


if __name__ == '__main__':
    app = App()
