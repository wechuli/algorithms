import tkinter as tk
import math


def tower_of_hanoi(from_peg, to_peg, other_peg, num_disks):
    """
    Move the top num_disks disks from peg from_peg to peg to_peg
    using other_peg to hold disks temporarily as needed.
    """
    result = ""

    # Recursively move the top n - 1 disks from from_peg to other_peg.
    if num_disks > 1:
        result += tower_of_hanoi(from_peg, other_peg, to_peg, num_disks - 1)

    # Move the last disk from from_peg to to_peg.
    if num_disks > 1:
        result += " "
    result += from_peg + "->" + to_peg

    # Recursively move the top n - 1 disks back from other_peg to to_peg.
    if num_disks > 1:
        result += " " + tower_of_hanoi(other_peg, to_peg, from_peg, num_disks - 1)

    return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tower_of_hanoi")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("280x270")

        frame = tk.Frame(self.window)
        frame.pack()

        label = tk.Label(frame, text="# Disks:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_disks_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.num_disks_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.num_disks_entry.insert(tk.END, "4")

        solve_button = tk.Button(frame, text="Solve", width=8, command=self.solve)
        solve_button.pack(padx=(10,5), pady=2, side=tk.LEFT)

        self.result_text = tk.Text(self.window, borderwidth=2, relief="groove")
        self.result_text.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=solve_button: solve_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_disks_entry.focus_force()
        self.window.mainloop()

    def solve(self):
        """ Solve the Tower of Hanoi problem."""
        num_disks = int(self.num_disks_entry.get())
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, tower_of_hanoi("A", "B", "C", num_disks))


if __name__ == '__main__':
    app = App()

# app.root.destroy()
