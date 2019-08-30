import random
import tkinter as tk


def gcd(a, b):
    """ Find GCD(a, b)."""
    # GCD(a, b) = GCD(b, a mod b).
    while b != 0:
        # Calculate the remainder.
        remainder = a % b

        # Calculate GCD(b, remainder).
        a = b
        b = remainder

    # GCD(a, 0) is a.
    return a

def lcm(a, b):
    """ Find LCM(a, b)."""
    # LCM(a, b) = a * b * GCD(a, b).
    return a * (b // gcd(a, b))


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("gcd")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x150")

        label = tk.Label(self.window, text="Numbers:")
        label.grid(padx=5, pady=5, row=0, column=0)
        self.a_entry = tk.Entry(self.window, width=16, justify=tk.RIGHT)
        self.a_entry.grid(padx=5, pady=5, row=0, column=1)
        self.a_entry.insert(0, "60")
        self.b_entry = tk.Entry(self.window, width=16, justify=tk.RIGHT)
        self.b_entry.grid(padx=5, pady=5, row=0, column=2)
        self.b_entry.insert(0, "45")

        find_gcd_button = tk.Button(self.window, text="Find GCD", width=10, command=self.find_gcd)
        find_gcd_button.grid(padx=5, pady=5, row=1, column=0, columnspan=3)

        label = tk.Label(self.window, text="GCD:")
        label.grid(padx=5, pady=5, row=2, column=0)
        self.gcd_entry = tk.Entry(self.window, width=16, justify=tk.RIGHT)
        self.gcd_entry.grid(padx=5, pady=5, row=2, column=1)

        label = tk.Label(self.window, text="LCM:")
        label.grid(padx=5, pady=5, row=3, column=0)
        self.lcm_entry = tk.Entry(self.window, width=16, justify=tk.RIGHT)
        self.lcm_entry.grid(padx=5, pady=5, row=3, column=1)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=find_gcd_button: find_gcd_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.a_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def find_gcd(self):
        """ Evaluate the exponent."""
        a = int(self.a_entry.get())
        b = int(self.b_entry.get())

        gcd_ab = gcd(a, b)
        self.gcd_entry.delete(0, tk.END)
        self.gcd_entry.insert(0, f"{gcd_ab}")

        lcm_ab = lcm(a, b)
        self.lcm_entry.delete(0, tk.END)
        self.lcm_entry.insert(0, f"{lcm_ab}")


if __name__ == '__main__':
    app = App()
