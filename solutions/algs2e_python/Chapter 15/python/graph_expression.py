from enum import Enum
import tkinter as tk
import math


class OperatorTypes(Enum):
    none = 0
    literal = 1
    variable = 2
    plus = 3
    minus = 4
    times = 5
    divide = 6
    sine = 7


class ExpressionNode:
    def __init__(self, expression):
        """ The constructor parses the expression and initializes the object."""
        self.operator_type = OperatorTypes.none
        self.left_child = None
        self.right_child = None
        self.literal_value = -1000000

        self.parse(expression)

    def parse(self, expression):
        """ Find the operator."""
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
                    operand1 = expression[:i]
                    operand2 = expression[i + 1:]
    
                    # Parse the operands.
                    self.left_child = ExpressionNode(operand1)
                    self.right_child = ExpressionNode(operand2)
    
                    # Remember the operator.
                    if ch == "+":
                        self.operator_type = OperatorTypes.plus
                    elif ch == "-":
                        self.operator_type = OperatorTypes.minus
                    elif ch == "*":
                        self.operator_type = OperatorTypes.times
                    elif ch == "/":
                        self.operator_type = OperatorTypes.divide
                    else:
                        raise ValueError(f"Unknown operator {ch}")
    
                    # We're done initializing this object.
                    return
    
        # If we get here, we did not find an operator.
        # This must be:
        #      (expression)
        #      Sine(expression)
        #      X
        #      A literal.
        if (expression[0] == "(") and (matching_paren_index(expression, 0) == len(expression) - 1):
            # This is (expression).
            # Remove the parentheses.
            self.parse(expression[1:len(expression) - 1])
        elif expression.upper() == "X":
            # This is X.
            self.operator_type = OperatorTypes.variable
        elif (expression.upper()[:5] == "SINE(") and (matching_paren_index(expression, 4) == len(expression) - 1):
            # This is Sine(expression).
            self.operator_type = OperatorTypes.sine

            expression = expression[5:len(expression) - 1]
            self.left_child = ExpressionNode(expression)
        else:
            # This is a literal.
            self.operator_type = OperatorTypes.literal
            self.literal_value = float(expression)

    def evaluate(self, x):
        """ Return the value of the expression for the indicated value of x."""
        if self.operator_type == OperatorTypes.literal:
            return self.literal_value
        elif self.operator_type == OperatorTypes.variable:
            return x
        elif self.operator_type == OperatorTypes.plus:
            return self.left_child.evaluate(x) + self.right_child.evaluate(x)
        elif self.operator_type == OperatorTypes.minus:
            return self.left_child.evaluate(x) - self.right_child.evaluate(x)
        elif self.operator_type == OperatorTypes.times:
            return self.left_child.evaluate(x) * self.right_child.evaluate(x)
        elif self.operator_type == OperatorTypes.divide:
            return self.left_child.evaluate(x) / self.right_child.evaluate(x)
        elif self.operator_type == OperatorTypes.sine:
            return math.sin(self.left_child.evaluate(x))
        else:
            raise ValueError("Unknown operator in evaluate method")


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
        self.window = tk.Tk()
        self.window.title("graph_expression")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x375")

        frame = tk.Frame(self.window)
        frame.pack(fill=tk.X)

        label = tk.Label(frame, text="Expression:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.expression_entry = tk.Entry(frame)
        self.expression_entry.pack(padx=5, pady=2, side=tk.LEFT, fill=tk.X, expand=True)
        self.expression_entry.insert(tk.END, "(Sine(X/10)*50)+100")

        graph_button = tk.Button(self.window, text="Graph", width=8, command=self.graph)
        graph_button.pack(padx=(10,5), pady=2)

        # Canvas.
        self.canvas = tk.Canvas(self.window, bg="white", width=300, height=300, borderwidth=2, relief="groove")
        self.canvas.pack()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=graph_button: graph_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.expression_entry.focus_force()
        self.window.mainloop()

    def graph(self):
        """ Graph the expression."""
        # Build the parse tree.
        root = ExpressionNode(self.expression_entry.get())

        # Evaluate to get the points.
        curve_points = []
        for x in range(self.canvas.winfo_width()):
            y = root.evaluate(x)
            curve_points += (x, y)

        # Draw.
        self.canvas.delete(tk.ALL)
        self.canvas.create_line(curve_points, fill="red")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
