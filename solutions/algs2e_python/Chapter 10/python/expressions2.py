import tkinter as tk
import math


class Operators:
    Literal = 1
    Plus = 2
    Minus = 3
    Times = 4
    Divide = 5
    Negate = 6
    SquareRoot = 7
    Factorial = 8
    Sine = 9
    Squared = 10


class ExpressionNode:
    def __init__(self, operator, literal_text):
        self.operator = operator
        self.left_operand = None
        self.right_operand = None
        self.literal_text = literal_text

    def evaluate(self):
        """ evaluate the expression."""
        if self.operator == Operators.Literal:
            return float(self.literal_text)
        elif self.operator == Operators.Plus:
            return self.left_operand.evaluate() + self.right_operand.evaluate()
        elif self.operator == Operators.Minus:
            return self.left_operand.evaluate() - self.right_operand.evaluate()
        elif self.operator == Operators.Times:
            return self.left_operand.evaluate() * self.right_operand.evaluate()
        elif self.operator == Operators.Divide:
            return self.left_operand.evaluate() / self.right_operand.evaluate()
        elif self.operator == Operators.Negate:
            return -self.left_operand.evaluate()
        elif self.operator == Operators.SquareRoot:
            return math.sqrt(self.left_operand.evaluate())
        elif self.operator == Operators.Factorial:
            return ExpressionNode.factorial(self.left_operand.evaluate())
        elif self.operator == Operators.Sine:
            return math.sin(math.pi / 180 * self.left_operand.evaluate())
        elif self.operator == Operators.Squared:
            left = self.left_operand.evaluate()
            return left * left

        raise ArithmeticError(f"Unknown operator {self.operator}")

    @staticmethod
    def factorial(n):
        """ Return n!"""
        result = 1
        for i in range(2, int(n) + 1):
            result *= i
        return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("expressions2")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x240")

        label = tk.Label(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Make and evaluate some expressions.
        results = ""

        # Sqrt((36 * 2) / (9 * 32))
        root = ExpressionNode(Operators.SquareRoot, "")
        root.left_operand = ExpressionNode(Operators.Divide, "")
        root.left_operand.left_operand = ExpressionNode(Operators.Times, "")
        root.left_operand.left_operand.left_operand = ExpressionNode(Operators.Literal, "36")
        root.left_operand.left_operand.right_operand = ExpressionNode(Operators.Literal, "2")
        root.left_operand.right_operand = ExpressionNode(Operators.Times, "")
        root.left_operand.right_operand.left_operand = ExpressionNode(Operators.Literal, "9")
        root.left_operand.right_operand.right_operand = ExpressionNode(Operators.Literal, "32")
        results += f"Sqrt((36 * 2) / (9 * 32)) = {root.evaluate()}\n"
        results += f"Check: {math.sqrt((36 * 2) / (9 * 32))}\n\n"

        # 5! / ((5 - 3)! * 3!)
        root = ExpressionNode(Operators.Divide, "")
        # 5!
        root.left_operand = ExpressionNode(Operators.Factorial, "")
        root.left_operand.left_operand = ExpressionNode(Operators.Literal, "5")
        # (5 - 3)! * 3!
        root.right_operand = ExpressionNode(Operators.Times, "")
        root.right_operand.left_operand = ExpressionNode(Operators.Factorial, "")
        root.right_operand.left_operand.left_operand = ExpressionNode(Operators.Minus, "")
        root.right_operand.left_operand.left_operand.left_operand = ExpressionNode(Operators.Literal, "5")
        root.right_operand.left_operand.left_operand.right_operand = ExpressionNode(Operators.Literal, "3")
        # 3!
        root.right_operand.right_operand = ExpressionNode(Operators.Factorial, "")
        root.right_operand.right_operand.left_operand = ExpressionNode(Operators.Literal, "3")
        results += f"5! / (5 - 3)! / 3! = {root.evaluate()}\n"
        result = ExpressionNode.factorial(5) / (ExpressionNode.factorial(5 - 3) * ExpressionNode.factorial(3))
        results += f"Check: {result}\n\n"

        # Sine(45)^2
        root = ExpressionNode(Operators.Squared, "")
        root.left_operand = ExpressionNode(Operators.Sine, "")
        root.left_operand.left_operand = ExpressionNode(Operators.Literal, "45")
        results += f"Sine(45)^2 = {root.evaluate()}\n"
        results += f"Check: {math.pow(math.sin(45 * math.pi / 180), 2)}\n\n"

        label["text"] = results

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()



if __name__ == '__main__':
    app = App()

# app.root.destroy()
