import random
import tkinter as tk
import math



class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("linear_congruential_generator")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        label = tk.Label(self.window, text="Xn+1 = (A * Xn + B) Mod M")
        label.pack(padx=5, pady=2, side=tk.TOP)

        frame = tk.Frame()
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="A")
        label.grid(padx=5, pady=2, row=0, column=0)
        self.a_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.a_entry.grid(padx=5, pady=2, row=0, column=1)
        self.a_entry.insert(0, "7")
        label = tk.Label(frame, text="B")
        label.grid(padx=5, pady=2, row=1, column=0)
        self.b_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.b_entry.grid(padx=5, pady=2, row=1, column=1)
        self.b_entry.insert(0, "5")
        generate_button = tk.Button(frame, text="Generate", width=10, command=self.generate)
        generate_button.grid(padx=5, pady=2, row=1, column=2)
        label = tk.Label(frame, text="M")
        label.grid(padx=5, pady=2, row=2, column=0)
        self.m_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.m_entry.grid(padx=5, pady=2, row=2, column=1)
        self.m_entry.insert(0, "11")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numbers_listbox = tk.Listbox(frame)
        self.numbers_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.numbers_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.numbers_listbox.yview)

        self.count_label = tk.Label(self.window)
        self.count_label.pack(padx=5, pady=2, side=tk.TOP)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=generate_button: generate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.a_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def generate(self):
        """ Generate numbers."""
        self.numbers_listbox.delete(0, tk.END)

        # Get the parameters.
        a = int(self.a_entry.get())
        b = int(self.b_entry.get())
        m = int(self.m_entry.get())

        # Generate numbers.
        numbers = set()
        txt = ""
        x = 0
        while True:
            # Only display the first 200 numbers in the list box.
            if len(numbers) <= 200:
                self.numbers_listbox.insert(tk.END, x)

            # See if we have generated this number before.
            if x in numbers:
                break

            # Add the number.
            numbers.add(x)

            # Generate the next number.
            x = (a * x + b) % m

        self.count_label["text"] = f"{len(numbers)} values"


if __name__ == '__main__':
    app = App()
