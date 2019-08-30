import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import itertools


def is_well_formed(expression):
    """ Verify that the expression's parenthesis are properly nested."""
    count = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            count += 1
        elif expression[i] == ")":
            count -= 1

        if count < 0:
            return False

    if count == 0:
        return True
    return False


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("parenthesis_matching")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("270x100")

        self.window.grid_columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Expression:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.expression_entry = tk.Entry(self.window, width=1)
        self.expression_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        self.expression_entry.insert(tk.END, "(8*3)+(20/(7-3))")

        evaluate_button = tk.Button(self.window, text="Evaluate", width=8, command=self.evaluate)
        evaluate_button.grid(row=1, column=0, columnspan=2, padx=5, pady=5)

        label = tk.Label(self.window, text="Result:")
        label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
        self.result_entry = tk.Entry(self.window, width=1)
        self.result_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.EW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=evaluate_button: evaluate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.expression_entry.focus_force()
        self.window.mainloop()

    def evaluate(self):
        """ Make sure the expression is well-formed."""
        self.result_entry.delete(0, tk.END)

        if is_well_formed(self.expression_entry.get()):
            self.result_entry.insert(tk.END, "Parentheses match")
        else:
            self.result_entry.insert(tk.END, "Parentheses don't match")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
