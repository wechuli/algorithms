import random
import tkinter as tk


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
        self.window.title("adaptive_grid_integration")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x410")

        self.canvas = tk.Canvas(self.window, width=280, height=280,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Rows/Columns:")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.num_rows_cols_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.num_rows_cols_entry.grid(padx=5, pady=2, row=0, column=1)
        self.num_rows_cols_entry.insert(0, "4")
        integrate_button = tk.Button(frame, text="Integrate", width=10, command=self.integrate)
        integrate_button.grid(padx=5, pady=2, row=0, column=2)

        label = tk.Label(frame, text="Min Box Area:")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.min_box_area_entry = tk.Entry(frame, width=8, justify=tk.RIGHT)
        self.min_box_area_entry.grid(padx=5, pady=2, row=1, column=1)
        self.min_box_area_entry.insert(0, "0.001")
        reset_button = tk.Button(frame, text="Reset", width=10, command=self.reset)
        reset_button.grid(padx=5, pady=2, row=1, column=2)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Area:")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.area_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.area_entry.grid(padx=5, pady=2, row=0, column=1)

        label = tk.Label(frame, text="# Boxes:")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.num_boxes_entry = tk.Entry(frame, width=16, justify=tk.RIGHT)
        self.num_boxes_entry.grid(padx=5, pady=2, row=1, column=1)

        # Make the DrawingCanvas.
        self.wxmin = -5
        self.wymin = -5
        self.wxmax = 5
        self.wymax = 5
        self.drawing_canvas = DrawingCanvas(self.canvas, self.wxmin, self.wymin, self.wxmax, self.wymax, 10, True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=integrate_button: integrate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_rows_cols_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def integrate(self):
        """ Perform the integration."""
        self.draw_background()

        # Get the parameters.
        num_rows = int(self.num_rows_cols_entry.get())
        min_box_area = float(self.min_box_area_entry.get())
        self.num_boxes = 0

        # Start with the full box.
        area = self.integrate_adaptive_grid(self.canvas, self.wxmin, self.wymin, self.wxmax, self.wymax, num_rows, min_box_area)

        self.area_entry.delete(0, tk.END)
        self.area_entry.insert(0, f"{area:,.12}")
        self.num_boxes_entry.delete(0, tk.END)
        self.num_boxes_entry.insert(0, f"{self.num_boxes}")

    def reset(self):
        """ Reset."""
        self.draw_background()

    def draw_background(self):
        """ Make the basic image and reset the area counts."""
        # Reset the area data.
        self.area_entry.delete(0, tk.END)
        self.num_boxes_entry.delete(0, tk.END)

        # Clear the canvas.
        self.drawing_canvas.clear()

        # Fill the shapes.
        self.drawing_canvas.wdraw_oval(-2, -4, 2, 4, "lightblue", "")
        self.drawing_canvas.wdraw_oval(-4, -2, 4, 2, "lightblue", "")
        self.drawing_canvas.wdraw_oval(-1.7, -1.7, 1.7, 1.7, "white", "")
        self.drawing_canvas.wdraw_oval(-3, -1, -1, 1, "white", "")
        self.drawing_canvas.wdraw_oval(1, -1, 3, 1, "white", "")

        # Outline the shapes.
        self.drawing_canvas.wdraw_oval(-2, -4, 2, 4, "", "blue")
        self.drawing_canvas.wdraw_oval(-4, -2, 4, 2, "", "blue")
        self.drawing_canvas.wdraw_oval(-1.7, -1.7, 1.7, 1.7, "", "blue")
        self.drawing_canvas.wdraw_oval(-3, -1, -1, 1, "", "blue")
        self.drawing_canvas.wdraw_oval(1, -1, 3, 1, "", "blue")

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

    def integrate_adaptive_grid(self, canvas, box_xmin, box_ymin, box_xmax, box_ymax, num_rows, min_box_area):
        """ Use an adaptive grid to estimate the area inside this box."""
        self.num_boxes += 1

        # Prepare to divide the box into sub-boxes.
        wid = box_xmax - box_xmin
        hgt = box_ymax - box_ymin
        dx = wid / num_rows
        dy = hgt / num_rows
        xmin = box_xmin

        # See if there are both hits and misses in the box.
        has_hits = False
        has_misses = False
        y = box_ymin
        for row in range(num_rows):
            x = box_xmin
            for col in range(num_rows):
                if self.point_is_in_shape(x, y):
                    has_hits = True
                    if has_misses:
                        break
                else:
                    has_misses = True
                    if has_hits:
                        break
                if (has_hits and has_misses):
                    break
                x += dx
            y += dy

        # If there were no hits, return 0.
        if not has_hits:
            return 0

        # If there were no misses, return the box's area.
        box_area = abs(wid * hgt)
        if not has_misses:
            return box_area

        # See if the box is too small to divide.
        if box_area < min_box_area:
            # Too small. See how many points are in the shape.
            num_hits = 0
            num_misses = 0
            y = box_ymin
            for row in range(num_rows):
                x = box_xmin
                for col in range(num_rows):
                    if self.point_is_in_shape(x, y):
                        num_hits += 1
                    else:
                        num_misses += 1
                    x += dx
                y += dy

            return box_area * num_hits / (num_rows * num_rows)

        # Draw the box.
        self.drawing_canvas.wdraw_rectangle(box_xmin, box_ymin, box_xmax, box_ymax, "", "blue")

        # Divide the box.
        area = 0
        xmin = box_xmin
        y = box_ymin
        for row in range(num_rows):
            x = box_xmin
            for col in range(num_rows):
                area += self.integrate_adaptive_grid(canvas, x, y, x + dx, y + dy, num_rows, min_box_area)
                x += dx
            y += dy

        # Return the result.
        return area


if __name__ == '__main__':
    app = App()
