import random
import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox


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

    def wdraw_wcircle(self, wx, wy, wradius, fill, outline):
        """ Draw an oval at the indicated position in world coordinates."""
        x0, y0 = self.w_to_d(wx - wradius, wy - wradius)
        x1, y1 = self.w_to_d(wx + wradius, wy + wradius)
        self.canvas.create_oval(x0, y0, x1, y1, fill=fill, outline=outline)

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
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Variables to manage the queue. (In a real application,
        # it would be better to wrap this with a class.)
        self.queue = [None for i in range(8)]
        self.next = 0
        self.last = 0

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("circular_queue")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x360")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="Item:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.item_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.item_entry.pack(padx=5, pady=2, side=tk.LEFT)
        enqueue_button = tk.Button(frame, width=10, text="Enqueue", command=self.enqueue)
        enqueue_button.pack(padx=5, pady=2, side=tk.LEFT)
        dequeue_button = tk.Button(frame, width=10, text="Dequeue", command=self.dequeue)
        dequeue_button.pack(padx=5, pady=2, side=tk.LEFT)

        self.canvas = tk.Canvas(self.window, width=300, height=300,
            relief=tk.RIDGE, bd=5, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=2, side=tk.TOP)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=enqueue_button: enqueue_button.invoke())) 
        self.window.bind('<Escape>', (lambda e, button=dequeue_button: dequeue_button.invoke())) 

        # Make a font for drawing.
        self.label_font = tk_font.Font(family="Times New Roman", size=12)

        # Draw the initial queue.
        self.draw_queue()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.item_entry.focus_force()
        self.window.mainloop()

    def enqueue(self):
        """ Enqueue an item."""
        try:
            self.enqueue_item(self.item_entry.get())
            self.item_entry.delete(0, tk.END)
            self.item_entry.focus_force()
        except Exception as error:
            messagebox.showinfo("Enqueue Error", str(error))

    def enqueue_item(self, value):
        """ Enqueue an item."""
        # Make sure there's room to add an item.
        new_next = (self.next + 1) % len(self.queue)
        if new_next == self.last:
            raise ValueError("The queue is full.")

        self.queue[self.next] = value
        self.next = new_next
        self.draw_queue()

    def dequeue(self):
        """ Dequeue an item."""
        try:
            self.item_entry.delete(0, tk.END)
            self.item_entry.insert(0, self.dequeue_item())
            self.item_entry.focus_force()
        except Exception as error:
            messagebox.showinfo("Dequeue Error", str(error))

    def dequeue_item(self):
        """ Dequeue an item."""
        # Make sure there's an item to remove.
        if self.next == self.last:
            raise ValueError("The queue is empty.")

        result = self.queue[self.last]
        self.queue[self.last] = ""               # Remove old data to update the picture.
        self.last = (self.last + 1) % len(self.queue)
        self.draw_queue()
        return result

    def draw_queue(self):
        """ Draw the queue."""
        radius1 = 100
        radius2 = 60

        # Create a DrawingCanvas.
        drawing_canvas = DrawingCanvas(self.canvas, -100, -100, 100, 100, 10, True)

        # Draw.
        # Draw the circles.
        drawing_canvas.wdraw_wcircle(0, 0, radius1, "lightgray", "black")
        drawing_canvas.wdraw_wcircle(0, 0, radius2, "white", "black")

        # Draw the dividers.
        theta = 0
        dtheta = 2 * math.pi / len(self.queue)
        for i in range(len(self.queue)):
            x0 = radius1 * math.cos(theta)
            y0 = radius1 * math.sin(theta)
            x1 = radius2 * math.cos(theta)
            y1 = radius2 * math.sin(theta)
            drawing_canvas.wdraw_line(x0, y0, x1, y1, "black", tk.NONE)

            theta += dtheta

        # Draw the letters.
        theta = dtheta / 2
        radius3 = (radius1 + radius2) / 2
        for i in range(len(self.queue)):
            if self.queue[i] != None:
                x0 = radius3 * math.cos(theta)
                y0 = radius3 * math.sin(theta)
                angle = theta * 180 / math.pi - 90
                drawing_canvas.wdraw_rotated_text(x0, y0, f"{self.queue[i]}", angle, "black", self.label_font)

            # Move to the next position.
            theta -= dtheta

        # Draw next and last.
        radius4 = radius2 - 10
        theta = dtheta / 2 - self.next * dtheta
        angle = theta * 180 / math.pi - 90
        x0 = radius4 * math.cos(theta)
        y0 = radius4 * math.sin(theta)
        drawing_canvas.wdraw_rotated_text(x0, y0, "Next", angle, "black", self.label_font)

        radius5 = radius4 - 10
        theta = dtheta / 2 - self.last * dtheta
        angle = theta * 180 / math.pi - 90
        x0 = radius5 * math.cos(theta)
        y0 = radius5 * math.sin(theta)
        drawing_canvas.wdraw_rotated_text(x0, y0, "Last", angle, "black", self.label_font)


if __name__ == '__main__':
    app = App()
