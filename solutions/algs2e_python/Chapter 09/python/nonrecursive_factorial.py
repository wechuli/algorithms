import tkinter as tk


def factorial(n):
    """ Return n!."""
    # Make a variable to keep track of the returned value.
    # Initialize it to 1 so we can multiply it by returned results.
    # (The result is 1 if we do not enter the loop at all.)
    result = 1

    # Start a loop controlled by the recursion stopping condition.
    while n != 0:
        # Save the result from this "recursive" call.
        result *= n

        # Prepare for "recursion."
        n -= 1

    # Return the accumulated result.
    return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("nonrecursive_factorial")
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
        result = factorial(n)
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(tk.END, f"{result}")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
