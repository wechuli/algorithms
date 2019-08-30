import tkinter as tk
import math


def hilbert(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw the Hilbert curve."""
    if depth > 0:
        current_x, current_y = hilbert(canvas, color, depth - 1, current_x, current_y, dy, dx)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, dy)
    if depth > 0:
        current_x, current_y = hilbert(canvas, color, depth - 1, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, dy, dx)
    if depth > 0:
        current_x, current_y = hilbert(canvas, color, depth - 1, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, -dy)
    if depth > 0:
        current_x, current_y = hilbert(canvas, color, depth - 1, current_x, current_y, -dy, -dx)
    return current_x, current_y

def draw_relative(canvas, color, current_x, current_y, dx, dy):
    """ Draw starting at the indicated point and return the new point."""
    new_x = current_x + dx
    new_y = current_y + dy
    canvas.create_line(current_x, current_y, new_x, new_y, fill=color)
    return new_x, new_y


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("hilbert")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x355")

        frame = tk.Frame(self.window)
        frame.pack()

        label = tk.Label(frame, text="Depth:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.depth_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry.insert(tk.END, "3")

        draw_button = tk.Button(frame, text="Draw", width=8, command=self.draw)
        draw_button.pack(padx=(10,5), pady=2, side=tk.LEFT)

        # Canvas.
        self.canvas = tk.Canvas(self.window, bg="white", width=300, height=300, borderwidth=2, relief="groove")
        self.canvas.pack()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=draw_button: draw_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.depth_entry.focus_force()
        self.window.mainloop()

    def draw(self):
        """ Draw the Hilbert curve."""
        depth = int(self.depth_entry.get())
        self.canvas.delete(tk.ALL)

        margin = 10
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = (canvas_width - 2 * margin) / (math.pow(2, depth + 1) - 1)
        hilbert(self.canvas, "blue", depth, margin, margin, dx, 0)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
