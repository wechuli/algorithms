import tkinter as tk


""" Initialize the fibonacci_values list."""
fibonacci_values = []
fibonacci_values.append(0)
fibonacci_values.append(1)


def fibonacci(n):
    """ Return the n-th Fibonacci number."""
    # If we have not yet calculated this value, calculate it.
    if len(fibonacci_values) - 1 < n:
        fibonacci_values.append(fibonacci(n - 1) + fibonacci(n - 2))

    # Return the calculated value.
    return fibonacci_values[n]


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("dynamic_fibonacci")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x90")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=(10, 2))
        label = tk.Label(frame, text="N:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.n_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.n_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.n_entry.insert(tk.END, "10")
        calculate_button = tk.Button(frame, text="Calculate", width=8, command=self.calculate)
        calculate_button.pack(padx=5, pady=2, side=tk.LEFT)

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=2, fill=tk.X, expand=True)
        self.result_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.result_entry.pack(padx=5, pady=2, fill=tk.X, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=calculate_button: calculate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.n_entry.focus_force()
        self.window.mainloop()

    def calculate(self):
        """ calculate the problem and draw the chess board."""
        n = int(self.n_entry.get())
        result = fibonacci(n)
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(tk.END, f"{result}")

        # Display the fibonacci values for debugging.
        #print(fibonacci_values)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
