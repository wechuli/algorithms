import tkinter as tk
import math


def draw_koch(canvas, color, depth, theta, pt1, angle, length):
    if depth == 0:
        pt2 = (
            pt1[0] + length * math.cos(angle),
            pt1[1] + length * math.sin(angle))
        canvas.create_line(pt1[0], pt1[1], pt2[0], pt2[1], fill=color)
    else:
        new_length = length / 2.0 / (1.0 + math.cos(theta))

        pt2 = (pt1[0] + new_length * math.cos(angle),
               pt1[1] + new_length * math.sin(angle))

        theta1 = angle - theta
        theta2 = angle + theta
        pt3 = (pt2[0] + new_length * math.cos(theta1),
               pt2[1] + new_length * math.sin(theta1))

        pt4 = (pt3[0] + new_length * math.cos(theta2),
               pt3[1] + new_length * math.sin(theta2))

        draw_koch(canvas, color, depth - 1, theta, pt1, angle, new_length)
        draw_koch(canvas, color, depth - 1, theta, pt2, theta1, new_length)
        draw_koch(canvas, color, depth - 1, theta, pt3, theta2, new_length)
        draw_koch(canvas, color, depth - 1, theta, pt4, angle, new_length)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("angle_snowflake")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("350x350")

        frame = tk.Frame(self.window)
        frame.pack()

        label = tk.Label(frame, text="Depth:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.depth_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.depth_entry.insert(tk.END, "3")

        label = tk.Label(frame, text="Angle:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.angle_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.angle_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.angle_entry.insert(tk.END, "80")

        draw_button = tk.Button(frame, text="Draw", width=8, command=self.draw)
        draw_button.pack(padx=(10,5), pady=2, side=tk.LEFT)

        # Canvas.
        frame = tk.Frame(self.window, borderwidth=2, relief="groove")
        frame.pack(padx=5, pady=(0,5), side=tk.TOP, fill=tk.BOTH, expand=True)
        self.canvas = tk.Canvas(frame, bg="white")
        self.canvas.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=draw_button: draw_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.depth_entry.focus_force()
        self.window.mainloop()

    def draw(self):
        """ Draw the snowflake."""
        depth = int(self.depth_entry.get())
        theta = float(self.angle_entry.get())
        theta *= math.pi / 180.0

        self.canvas.delete(tk.ALL)

        # Figure out where to put the corners.
        margin = 10
        canvas_width = self.canvas.winfo_width()
        canvas_height = self.canvas.winfo_height()
        area_width = canvas_width - 2 * margin
        area_height = canvas_height - 2 * margin

        radius = min(area_height, area_width) / 2

        cx = canvas_width / 2
        cy = canvas_height / 2 

        angle120 = 120 * math.pi / 180
        angle240 = 240 * math.pi / 180
        alpha = (90 + 120) * math.pi / 180
        pt1 = (cx + radius * math.cos(alpha), cy + radius * math.sin(alpha))
        alpha += angle120
        pt2 = (cx + radius * math.cos(alpha), cy + radius * math.sin(alpha))
        alpha += angle120
        pt3 = (cx + radius * math.cos(alpha), cy + radius * math.sin(alpha))

        """ Draw the points and radius for debugging.
        self.canvas.create_oval(cx - radius,  cy - radius, cx + radius,  cy + radius)
        r = 4
        self.canvas.create_oval(pt1[0] - r, pt1[1] - r, pt1[0] + r, pt1[1] + r, fill="red", outline="red")
        self.canvas.create_oval(pt2[0] - r, pt2[1] - r, pt2[0] + r, pt2[1] + r, fill="green", outline="green")
        self.canvas.create_oval(pt3[0] - r, pt3[1] - r, pt3[0] + r, pt3[1] + r, fill="blue", outline="blue")
        self.canvas.create_oval(cx - r, cy - r, cx + r, cy + r, fill="yellow", outline="blue")
        """

        # Draw the sides.
        color = "blue"
        triangle_width = 2 * radius * math.sqrt(3) / 2
        draw_koch(self.canvas, color, depth, theta, pt1, 0, triangle_width)
        draw_koch(self.canvas, color, depth, theta, pt2, angle120, triangle_width)
        draw_koch(self.canvas, color, depth, theta, pt3, angle240, triangle_width)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
