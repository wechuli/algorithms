import random
import tkinter as tk
import tkinter.font as tk_font
import math

BORDER_WIDTH = 3

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with an empty walk.
        self.walk = None

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("triangle_walk")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x360")

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=50, height=50,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        # Parameters.
        parameter_frame = tk.Frame(self.window)
        parameter_frame.pack(padx=5, pady=5, side=tk.BOTTOM)

        step_size_label = tk.Label(parameter_frame, text="Step Size:")
        step_size_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.step_size_entry = tk.Entry(parameter_frame, width=10, justify=tk.RIGHT)
        self.step_size_entry.grid(row=0, column=1, padx=5, pady=2)
        self.step_size_entry.insert(tk.END, "4")

        num_steps_label = tk.Label(parameter_frame, text="# Steps:")
        num_steps_label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.num_steps_entry = tk.Entry(parameter_frame, width=10, justify=tk.RIGHT)
        self.num_steps_entry.grid(row=1, column=1, padx=5, pady=2)
        self.num_steps_entry.insert(tk.END, "10000")

        draw_button = tk.Button(parameter_frame, text="Draw", width=10, command=self.draw_walk)
        draw_button.grid(row=2, column=0, columnspan=2, padx=5, pady=2)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=draw_button: draw_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def draw_walk(self):
        """ Draw a new triangle walk."""
        self.canvas.delete(tk.ALL)
        width = self.canvas.winfo_height()
        height = self.canvas.winfo_width()
        x, y = width // 2, height // 2

        step_size = int(self.step_size_entry.get())
        num_steps = int(self.num_steps_entry.get())

        angle_y = step_size * math.sin(math.pi / 3)
        angle_x = step_size * math.cos(math.pi / 3)

        points = [(x, y)]
        for i in range(0, num_steps):
            direction = random.randint(0, 5)
            if direction == 0:     # Northeast
                y -= angle_y
                x += angle_x
            elif direction == 1:   # East
                x += step_size
            elif direction == 2:   # Southeast
                y += angle_y
                x += angle_x
            elif direction == 3:   # Southwest
                y += angle_y
                x -= angle_x
            elif direction == 4:   # West
                x -= step_size
            else:                  # Northwest
                y -= angle_y
                x -= angle_x
            points.append((x, y))
        self.canvas.create_line(points, fill="red")

if __name__ == '__main__':
    app = App()
