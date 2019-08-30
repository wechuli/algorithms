import random
import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox

BORDER_WIDTH = 3

def FindLinearLeastSquaresFit(points):
    if len(points) < 2:
        raise Exception("A linear least squares fit requires at least two points.")

    # Calculate the S values.
    Sx = 0
    Sxx = 0
    Sxy = 0
    Sy = 0
    for point in points:
        Sx += point[0]
        Sxx += point[0] * point[0]
        Sxy += point[0] * point[1]
        Sy += point[1]
    S1 = len(points)

    m = (Sxy * S1 - Sx * Sy) / (Sxx * S1 - Sx * Sx)
    b = (Sxy * Sx - Sy * Sxx) / (Sx * Sx - S1 * Sxx)
    return m, b

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with no data points.
        self.points = []
        self.solved = False
        self.m = 0
        self.b = 0

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("linear_least_squares")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x378")

        # Canvas.
        self.canvas = tk.Canvas(self.window, width=50, height=50,
            relief=tk.RIDGE, bd=BORDER_WIDTH, highlightthickness=0, bg="white")
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        # Parameters.
        parameter_frame = tk.Frame(self.window)
        parameter_frame.pack(padx=5, pady=5, side=tk.BOTTOM)

        m_label = tk.Label(parameter_frame, text="m:")
        m_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.m_output_label = tk.Label(parameter_frame, text="", width=10, borderwidth=2, relief="groove", anchor=tk.E)
        self.m_output_label.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        b_label = tk.Label(parameter_frame, text="b:")
        b_label.grid(row=0, column=2, padx=5, pady=2, sticky=tk.W)
        self.b_output_label = tk.Label(parameter_frame, text="", width=10, borderwidth=2, relief="groove", anchor=tk.E)
        self.b_output_label.grid(row=0, column=3, padx=5, pady=2, sticky=tk.W+tk.E)

        solve_button = tk.Button(parameter_frame, text="Solve", width=10, command=self.solve)
        solve_button.grid(row=1, column=0, columnspan=2, padx=5, pady=2)
        reset_button = tk.Button(parameter_frame, text="Reset", width=10, command=self.reset)
        reset_button.grid(row=1, column=2, columnspan=2, padx=5, pady=2)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Catch mouse clicks.
        self.canvas.bind("<Button-1>", self.mouse_click)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def mouse_click(self, event):
        self.points.append((event.x, event.y))
        self.solved = False
        self.draw()

    def reset(self):
        self.points = []
        self.solved = False
        self.draw()

    def solve(self):
        """Perform linear least squares."""
        try:
            self.m_output_label["text"] = ""
            self.b_output_label["text"] = ""
            self.solved = False

            self.m, self.b = FindLinearLeastSquaresFit(self.points)

            self.m_output_label["text"] = f"{self.m:.6}"
            self.b_output_label["text"] = f"{self.b:.6}"
            self.solved = True
        except Exception as e:
            messagebox.showinfo("Error", str(e))

        self.draw()

    def draw(self):
        """ Draw the points and least squares fit."""
        self.canvas.delete(tk.ALL)

        # Draw the points.
        radius = 2
        for point in self.points:
            x0 = point[0] - radius
            y0 = point[1] - radius
            x1 = x0 + 2 * radius
            y1 = y0 + 2 * radius
            self.canvas.create_oval(x0, y0, x1, y1, fill="red", outline="red")

        # If we have a solution, draw it.
        if self.solved:
            x0 = 0
            y0 = self.m * x0 + self.b
            x1 = self.canvas.winfo_width()
            y1 = self.m * x1 + self.b
            self.canvas.create_line(x0, y0, x1, y1, fill="blue")

if __name__ == '__main__':
    app = App()
