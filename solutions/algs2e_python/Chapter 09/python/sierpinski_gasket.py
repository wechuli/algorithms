import tkinter as tk
import math


def sierpinski_gasket(canvas, color, depth, p1, p2, p3):
    """ Draw the gasket."""
    # If this is depth 0, fill the remaining rectangle.
    if depth == 0:
        canvas.create_polygon(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1], fill=color, outline="")
    else:
        # Find points on the left, right, and bottom of the triangle.
        lpoint = ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)
        bpoint = ((p2[0] + p3[0]) / 2, (p2[1] + p3[1]) / 2)
        rpoint = ((p3[0] + p1[0]) / 2, (p3[1] + p1[1]) / 2)

        # Draw the triangles at the corners.
        sierpinski_gasket(canvas, color, depth - 1, p1, lpoint, rpoint)
        sierpinski_gasket(canvas, color, depth - 1, lpoint, p2, bpoint)
        sierpinski_gasket(canvas, color, depth - 1, rpoint, bpoint, p3)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("sierpinski_gasket")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x270")

        frame = tk.Frame(self.window)
        frame.pack()

        label = tk.Label(frame, text="Depth:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.depth_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry.insert(tk.END, "4")

        draw_button = tk.Button(frame, text="Draw", width=8, command=self.draw)
        draw_button.pack(padx=(10,5), pady=2, side=tk.LEFT)

        # Canvas.
        self.canvas = tk.Canvas(self.window, bg="white", width=257, height=225, borderwidth=2, relief="groove")
        self.canvas.pack()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=draw_button: draw_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.depth_entry.focus_force()
        self.window.mainloop()

    def draw(self):
        """ Draw the Sierpinski curve."""
        depth = int(self.depth_entry.get())
        self.canvas.delete(tk.ALL)

        margin = 10
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()

        p1 = (canvas_width / 2, margin)
        p2 = (margin, canvas_height - margin)
        p3 = (canvas_width - margin, canvas_height - margin)
        sierpinski_gasket(self.canvas, "red", depth, p1, p2, p3)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
