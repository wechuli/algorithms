import random
import tkinter as tk


def exponentiate_mod(value, exponent, modulus):
    """ Perform the exponentiation."""
    result = 1
    factor = value
    while exponent != 0:
        if exponent % 2 == 1:
            result = (result * factor) % modulus
        factor = (factor * factor) % modulus
        exponent //= 2
    return result


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("exponentiate_mod")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x100")

        self.window.grid_columnconfigure(4, weight=1)

        label = tk.Label(self.window, text="Value:")
        label.grid(padx=5, pady=5, row=0, column=0)
        self.value_entry = tk.Entry(self.window, width=8, justify=tk.RIGHT)
        self.value_entry.grid(padx=5, pady=5, row=0, column=1)
        self.value_entry.insert(0, "2")
        label = tk.Label(self.window, text="^")
        label.grid(padx=5, pady=5, row=0, column=2)
        self.exponent_entry = tk.Entry(self.window, width=8, justify=tk.RIGHT)
        self.exponent_entry.grid(padx=5, pady=5, row=0, column=3)
        self.exponent_entry.insert(0, "16")
        label = tk.Label(self.window, text="mod")
        label.grid(padx=5, pady=5, row=0, column=3)
        self.modulus_entry = tk.Entry(self.window, width=8, justify=tk.RIGHT)
        self.modulus_entry.grid(padx=5, pady=5, row=0, column=4)
        self.modulus_entry.insert(0, "10")

        evaluate_button = tk.Button(self.window, text="Evaluate", width=8, command=self.evaluate)
        evaluate_button.grid(padx=5, pady=5, row=1, column=0, columnspan=4)

        label = tk.Label(self.window, text="Result:")
        label.grid(padx=5, pady=5, row=3, column=0)
        self.result_entry = tk.Entry(self.window, justify=tk.RIGHT)
        self.result_entry.grid(padx=5, pady=5, row=3, column=1, columnspan=4, sticky=tk.E+tk.W)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=evaluate_button: evaluate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.value_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def evaluate(self):
        """ Evaluate the exponent."""
        value = int(self.value_entry.get())
        exponent = int(self.exponent_entry.get())
        modulus = int(self.modulus_entry.get())
        result = exponentiate_mod(value, exponent, modulus)

        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(0, f"{result}")


if __name__ == '__main__':
    app = App()
