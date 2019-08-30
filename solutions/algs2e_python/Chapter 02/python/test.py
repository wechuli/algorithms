import random
import tkinter as tk
import tkinter.font as tk_font

BORDER_WIDTH = 3

def extended_gcd(a, b):
    """Perform the extended GCD algorithm."""
    # Setup.
    r = b
    prev_r = a

    x = 0
    prev_x = 1

    y = 1
    prev_y = 0

    # Run the algorithm.
    print()
    while True:
        # See if we're done.
        new_r = prev_r % r
        if new_r == 0:
            return r, x, y

        # Update s and t.
        q = prev_r // r
        new_x = prev_x - q * x
        prev_x, x = x, new_x

        new_y = prev_y - q * y
        prev_y, y = y, new_y

        # Update r.
        prev_r, r = r, new_r

        print(f"q: {q}, r: {r}, x: {x}, y: {y}")

class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Start with an empty walk.
        self.walk = None

        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("extended_gcd")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("370x180")

        # Parameters.
        parameter_frame = tk.Frame(self.window)
        parameter_frame.pack(padx=5, pady=5, side=tk.TOP)

        a_label = tk.Label(parameter_frame, text="A:")
        a_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.a_entry = tk.Entry(parameter_frame, width=30, justify=tk.RIGHT)
        self.a_entry.grid(row=0, column=1, padx=5, pady=2)
        self.a_entry.insert(tk.END, "210")

        b_label = tk.Label(parameter_frame, text="B:")
        b_label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.b_entry = tk.Entry(parameter_frame, width=30, justify=tk.RIGHT)
        self.b_entry.grid(row=1, column=1, padx=5, pady=2)
        self.b_entry.insert(tk.END, "154")

        gcd_label = tk.Label(parameter_frame, text="GCD:")
        gcd_label.grid(row=2, column=0, padx=5, pady=(15,2), sticky=tk.W)
        self.gcd_output_label = tk.Label(parameter_frame, text="", borderwidth=2, relief="groove", anchor=tk.E)
        self.gcd_output_label.grid(row=2, column=1, padx=5, pady=(15,2), sticky=tk.W+tk.E)

        lcm_label = tk.Label(parameter_frame, text="LCM:")
        lcm_label.grid(row=3, column=0, padx=5, pady=2, sticky=tk.W)
        self.lcm_output_label = tk.Label(parameter_frame, text="", borderwidth=2, relief="groove", anchor=tk.E)
        self.lcm_output_label.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        bezout_label = tk.Label(parameter_frame, text="Bézout:")
        bezout_label.grid(row=4, column=0, padx=5, pady=2, sticky=tk.W)
        self.bezout_output_label = tk.Label(parameter_frame, text="", borderwidth=2, relief="groove", anchor=tk.E)
        self.bezout_output_label.grid(row=4, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        verify_label = tk.Label(parameter_frame, text="Verify:")
        verify_label.grid(row=5, column=0, padx=5, pady=2, sticky=tk.W)
        self.verify_output_label = tk.Label(parameter_frame, text="", borderwidth=2, relief="groove", anchor=tk.E)
        self.verify_output_label.grid(row=5, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        solve_button = tk.Button(parameter_frame, text="Solve", width=10, command=self.solve)
        solve_button.grid(row=0, column=2, padx=(15,5), pady=2)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def solve(self):
        """Calculate the GCD, LCM, and Bezout, and verify the result."""
        a = int(self.a_entry.get())
        b = int(self.b_entry.get())

        gcd, x, y = extended_gcd(a, b)
        self.gcd_output_label["text"] = f"{gcd}"
        lcm = a * (b // gcd)
        self.lcm_output_label["text"] = f"{lcm}"
        self.bezout_output_label["text"] = f"{a} * {x} + {b} * {y} = {gcd}"
        self.verify_output_label["text"] = f"{a * x + b * y == gcd}"


if __name__ == '__main__':
    app = App()
