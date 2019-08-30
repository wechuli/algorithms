import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import itertools


def evaluate_expression(expression):
    """ Recursively evaluate the expression."""
    # Find the operator.
    count = 0
    for i in range(len(expression)):
        if expression[i] == "(":
            count += 1
        elif expression[i] == ")":
            count -= 1
            if count < 0:
                raise ValueError(f"Unexpected ) at position {i} in {expression}")
        elif count == 0:
            # Look for an operator.
            ch = expression[i]
            if (ch == "+") or (ch == "-") or (ch == "*") or (ch == "/"):
                # Get the operands.
                operand1 = expression[0:i]
                operand2 = expression[i + 1:]

                # Evaluate the operands.
                value1 = evaluate_expression(operand1)
                value2 = evaluate_expression(operand2)

                # Combine the operands and return the result.
                if ch == "+":
                    result = value1 + value2
                elif ch == "-":
                    result = value1 - value2
                elif ch == "*":
                    result = value1 * value2
                elif ch == "/":
                    result = value1 / value2
                else:
                    raise ValueError(f"Unknown operator {ch}")
                return result

    # If we get here, we did not find an operator.
    # See if this is (expression).
    if (expression[0] == "(") and (matching_paren_index(expression, 0) == len(expression) - 1):
        # Remove the parentheses.
        operand = expression[1:len(expression) - 1]
        return evaluate_expression(operand)

    # See if this is -expression.
    if expression[0] == "-":
        # Remove the -.
        operand = expression[1:]
        return not evaluate_expression(operand)

    # This must be a literal value.
    return float(expression)

def matching_paren_index(expression, open_paren_index):
    """ Return the index of the parenthesis matching the one in the indicated position."""
    count = 1
    for i in range(open_paren_index + 1, len(expression)):
        if expression[i] == "(":
            count += 1
        elif expression[i] == ")":
            count -= 1
        if count == 0:
            return i
        if count < 0:
            return -1
    return -1


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("evaluate_expression")
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
        """ Evaluate the expression."""
        result = evaluate_expression(self.expression_entry.get())
        self.result_entry.delete(0, tk.END)
        self.result_entry.insert(tk.END, str(result))


if __name__ == '__main__':
    app = App()

# app.root.destroy()
