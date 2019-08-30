import tkinter as tk
import tkinter.font as tk_font
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

        startx = xtic_spacing * int((self.wxmin + xtic_spacing) / xtic_spacing)
        x = startx
        while x < self.wxmax:
            if (abs(x) > 0.01):
                dx0, dy0 = self.w_to_d(x, tic_hgt)
                dx1, dy1 = self.w_to_d(x, -tic_hgt)
                self.canvas.create_line(dx0, dy0, dx1, dy1, fill=color)
                if do_draw_text:
                    self.canvas.create_text(dx1, dy1, text=str(x), fill=color, anchor=tk.N)
            x += xtic_spacing

        starty = ytic_spacing * int((self.wymin + ytic_spacing) / ytic_spacing)
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


def f(x):
    return (x * x * x / 75 - x * x / 4 + x + 10)


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("ch01_ex04")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("570x570")

        # Make a slightly bigger label font.
        self.label_font = tk_font.Font(family="Times New Roman", size=14)

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=550, height=550,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0, bg="white")
        self.canvas.xview("moveto", 5)   # Move out from the border.
        self.canvas.yview("moveto", 5)
        self.canvas.grid(row=1, column=0, columnspan=4, padx=5, pady=5)

        # Make the DrawingCanvas.
        self.drawing_canvas = DrawingCanvas(self.canvas, -1, -1, 21, 21, 10, True)

        # Draw the shapes.
        self.draw_scene()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def draw_scene(self):
        """Draw the scene."""
        self.drawing_canvas.clear()

        # Draw the curves.
        wxmin = self.drawing_canvas.wxmin
        wxmax = self.drawing_canvas.wxmax
        xpix = self.drawing_canvas.xpix
        self.drawing_canvas.wdraw_function(f, "red", wxmin, wxmax, xpix)

        wx0 = wxmin
        wy0 = wx0 / 2 + 8
        wx1 = wxmax
        wy1 = wx1 / 2 + 8
        self.drawing_canvas.wdraw_line(wx0, wy0, wx1, wy1, "blue", "")

        # Label the curves.
        self.drawing_canvas.wdraw_rotated_text(10, 7.5, "y = x^3 / 75 - x^2 / 4 + x + 10", 0, "red", self.label_font)
        self.drawing_canvas.wdraw_rotated_text(9.5, 13.5, "y = x/2 + 8", 26, "blue", self.label_font)

        # Label the points of intersection.
        self.drawing_canvas.wdraw_circle(4.92, 10.46, 5, "", "green")
        self.drawing_canvas.wdraw_circle(15.77, 15.88, 5, "", "green")

        self.drawing_canvas.wdraw_rotated_text(7.5, 10.46, "(4.92, 10.46)", 0, "green", self.label_font)
        self.drawing_canvas.wdraw_rotated_text(18.5, 15.88, "(15.77, 15.88)", 0, "green", self.label_font)
	
        # Draw the axes.
        self.drawing_canvas.wdraw_axes(5, 5, 0.2, 0.2, True, "gray")


if __name__ == '__main__':
    app = App()
