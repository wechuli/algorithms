import tkinter as tk


def find_inverse(number, modulus):
    for i in range(1, modulus):
        if (i * number) % modulus == 1:
            return i
    return -1


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("multiplicative_inverse")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("265x165")

        label = tk.Label(self.window, text="Number:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)
        self.number_entry = tk.Entry(self.window, width=30)
        self.number_entry.grid(padx=5, pady=5, row=0, column=1)
        self.number_entry.insert(0, "165")

        label = tk.Label(self.window, text="Modulus:")
        label.grid(padx=5, pady=5, row=1, column=0, sticky=tk.W)
        self.modulus_entry = tk.Entry(self.window, width=30)
        self.modulus_entry.grid(padx=5, pady=5, row=1, column=1)
        self.modulus_entry.insert(0, "448")

        calculate_button = tk.Button(self.window, width=8, text="calculate", command=self.calculate)
        calculate_button.grid(padx=5, pady=5, row=2, column=0, columnspan=2)

        label = tk.Label(self.window, text="Inverse:")
        label.grid(padx=5, pady=5, row=3, column=0, sticky=tk.W)
        self.inverse_entry = tk.Entry(self.window, width=30)
        self.inverse_entry.grid(padx=5, pady=5, row=3, column=1)

        label = tk.Label(self.window, text="Verify:")
        label.grid(padx=5, pady=5, row=4, column=0, sticky=tk.W)
        self.verify_entry = tk.Entry(self.window, width=30)
        self.verify_entry.grid(padx=5, pady=5, row=4, column=1)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=calculate_button: calculate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.number_entry.focus_force()
        self.window.mainloop()

    def calculate(self):
        """ Exhaustively find the inverse."""
        number = int(self.number_entry.get())
        modulus = int(self.modulus_entry.get())

        inverse = find_inverse(number, modulus)

        self.inverse_entry.delete(0, tk.END)
        self.inverse_entry.insert(tk.END, f"{inverse}")

        product = (number * inverse) % modulus
        self.verify_entry.delete(0, tk.END)
        self.verify_entry.insert(tk.END, f"{number} * {inverse} = {product} mod {modulus}")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
