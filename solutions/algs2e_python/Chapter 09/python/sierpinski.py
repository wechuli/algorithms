import tkinter as tk
import math


def sierpinski(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw a Sierpinski curve."""
    current_x, current_y = sierp_right(canvas, color, depth, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, dy)
    current_x, current_y = sierp_down(canvas, color, depth, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, dy)
    current_x, current_y = sierp_left(canvas, color, depth, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, -dy)
    current_x, current_y = sierp_up(canvas, color, depth, current_x, current_y, dx, dy)
    current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, -dy)
    return current_x, current_y

def sierp_right(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw right across the top."""
    if depth > 0:
        depth -= 1
        current_x, current_y = sierp_right(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, dy)
        current_x, current_y = sierp_down(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, 2 * dx, 0)
        current_x, current_y = sierp_up(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, -dy)
        current_x, current_y = sierp_right(canvas, color, depth, current_x, current_y, dx, dy)
    return current_x, current_y

def sierp_down(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw down on the right."""
    if depth > 0:
        depth -= 1
        current_x, current_y = sierp_down(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, dy)
        current_x, current_y = sierp_left(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, 0, 2 * dy)
        current_x, current_y = sierp_right(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, dy)
        current_x, current_y = sierp_down(canvas, color, depth, current_x, current_y, dx, dy)
    return current_x, current_y

def sierp_left(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw left across the bottom."""
    if depth > 0:
        depth -= 1
        current_x, current_y = sierp_left(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, -dy)
        current_x, current_y = sierp_up(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, -2 * dx, 0)
        current_x, current_y = sierp_down(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, dy)
        current_x, current_y = sierp_left(canvas, color, depth, current_x, current_y, dx, dy)
    return current_x, current_y

def sierp_up(canvas, color, depth, current_x, current_y, dx, dy):
    """ Draw up along the left."""
    if depth > 0:
        depth -= 1
        current_x, current_y = sierp_up(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, dx, -dy)
        current_x, current_y = sierp_right(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, 0, -2 * dy)
        current_x, current_y = sierp_left(canvas, color, depth, current_x, current_y, dx, dy)
        current_x, current_y = draw_relative(canvas, color, current_x, current_y, -dx, -dy)
        current_x, current_y = sierp_up(canvas, color, depth, current_x, current_y, dx, dy)
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
        self.window.title("sierpinski")
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
        """ Draw the Sierpinski curve."""
        depth = int(self.depth_entry.get())
        self.canvas.delete(tk.ALL)

        margin = 10
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        dx = ((canvas_width - 2 * margin) / (math.pow(2, depth + 2) - 2))
        dy = ((canvas_height - 2 * margin) / (math.pow(2, depth + 2) - 2))
        current_x = margin + dx
        current_y = margin
        sierpinski(self.canvas, "green", depth, current_x, current_y, dx, dy)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
