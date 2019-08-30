import tkinter as tk
import math


def sierpinski_carpet(canvas, color, depth, x1, y1, x2, y2):
    """ Draw the carpet."""
    # If this is depth 0, fill the remaining rectangle.
    if depth == 0:
        canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="")
    else:
        # Fill the 8 outside rectangles.
        width = (x2 - x1) / 3
        height = (y2 - y1) / 3
        for row in range(3):
            for col in range(3):
                # Skip the center rectangle.
                if (row != 1) or (col != 1):
                    xa = x1 + col * width
                    ya = y1 + row * height
                    xb = xa + width
                    yb = ya + height
                    sierpinski_carpet(canvas, color, depth - 1, xa, ya, xb, yb)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("sierpinski_carpet")
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

        x1 = margin
        y1 = margin
        x2 = canvas_width - margin
        y2 = canvas_height - margin
        sierpinski_carpet(self.canvas, "red", depth, x1, y1, x2, y2)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
