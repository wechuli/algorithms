import tkinter as tk


class Operators:
    Literal = 1
    Plus = 2
    Minus = 3
    Times = 4
    Divide = 5
    Negate = 6


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

        raise ArithmeticError(f"Unknown operator {self.operator}")


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("expressions")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("250x240")

        label = tk.Label(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        label.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Make and evaluate some expressions.
        results = ""

        # (15 / 3) + (24 / 6)
        root = ExpressionNode(Operators.Plus, None)
        left_oper = ExpressionNode(Operators.Divide, None)
        left_oper.left_operand = ExpressionNode(Operators.Literal, "15")
        left_oper.right_operand = ExpressionNode(Operators.Literal, "3")
        right_oper = ExpressionNode(Operators.Divide, None)
        right_oper.left_operand = ExpressionNode(Operators.Literal, "24")
        right_oper.right_operand = ExpressionNode(Operators.Literal, "6")
        root.left_operand = left_oper
        root.right_operand = right_oper
        results += f"(15 / 3) + (24 / 6) = {root.evaluate()}\n"
        results += f"Check: {(15 / 3) + (24 / 6)}\n\n"

        # 8 * 12 - 14 * 32
        root = ExpressionNode(Operators.Minus, None)
        left_oper = ExpressionNode(Operators.Times, None)
        left_oper.left_operand = ExpressionNode(Operators.Literal, "8")
        left_oper.right_operand = ExpressionNode(Operators.Literal, "12")
        right_oper = ExpressionNode(Operators.Times, None)
        right_oper.left_operand = ExpressionNode(Operators.Literal, "14")
        right_oper.right_operand = ExpressionNode(Operators.Literal, "32")
        root.left_operand = left_oper
        root.right_operand = right_oper
        results += f"8 * 12 - 14 * 32 = {root.evaluate()}\n"
        results += f"Check: {8 * 12 - 14 * 32}\n\n"

        # 1 / 2 + 1 / 4 + 1 / 20
        root = ExpressionNode(Operators.Plus, None)
        # 1 / 2
        left_oper = ExpressionNode(Operators.Divide, None)
        left_oper.left_operand = ExpressionNode(Operators.Literal, "1")
        left_oper.right_operand = ExpressionNode(Operators.Literal, "2")
        root.left_operand = left_oper

        # 1 / 4
        root.right_operand = ExpressionNode(Operators.Plus, None)
        left_oper = ExpressionNode(Operators.Divide, None)
        left_oper.left_operand = ExpressionNode(Operators.Literal, "1")
        left_oper.right_operand = ExpressionNode(Operators.Literal, "4")
        root.right_operand.left_operand = left_oper

        # 1 / 20
        right_oper = ExpressionNode(Operators.Divide, None)
        right_oper.left_operand = ExpressionNode(Operators.Literal, "1")
        right_oper.right_operand = ExpressionNode(Operators.Literal, "20")
        root.right_operand.right_operand = right_oper
        results += f"1 / 2 + 1 / 4 + 1 / 20 = {root.evaluate()}\n"
        results += f"Check: {1 / 2 + 1 / 4 + 1 / 20}\n\n"

        label["text"] = results

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()



if __name__ == '__main__':
    app = App()

# app.root.destroy()
