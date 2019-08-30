import tkinter as tk
from tkinter import ttk
import itertools


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("ch01_ex02")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("565x160")

        # Operations the program can execute in various lengths of time.
        second = 1000000
        minute = second * 60
        hour = minute * 60
        day = hour * 24
        week = day * 7
        year = day * 365.25

        self.treeview = ttk.Treeview(self.window)
        self.treeview.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)
        minwidth = self.treeview.column('#0', option='minwidth')
        self.treeview.column('#0', width=minwidth)
        self.treeview["columns"] = ("Time", "log N", "Sqrt(N)", "N", "N^2", "2^N", "N!")
        self.treeview.heading("Time", text="Time")
        self.treeview.heading("log N", text="log N")
        self.treeview.heading("Sqrt(N)", text="Sqrt(N)")
        self.treeview.heading("N", text="N")
        self.treeview.heading("N^2", text="N^2")
        self.treeview.heading("2^N", text="2^N")
        self.treeview.heading("N!", text="N!")
        self.treeview.column("Time", width=75)
        self.treeview.column("log N", width=75)
        self.treeview.column("Sqrt(N)", width=75)
        self.treeview.column("N", width=75)
        self.treeview.column("N^2", width=75)
        self.treeview.column("2^N", width=75)
        self.treeview.column("N!", width=75)
        self.add_row("Second", second)
        self.add_row("Minute", minute)
        self.add_row("Hour", hour)
        self.add_row("Day", day)
        self.add_row("Week", week)
        self.add_row("Year", year)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.treeview.focus_force()
        self.window.mainloop()

    def add_row(self, name, steps):
        values = [name]
        try:
            values.append(math.pow(2, steps))          # Log N
        except:
            values.append("Infinity")
        values.append(f"{steps * steps:.1g}")               # Sqrt(N)
        values.append(f"{steps:.1g}")               # N
        values.append(f"{int(math.sqrt(steps)):,}")            # N^2
        values.append(f"{int(math.log(steps, 2))}")          # 2^N
        values.append(f"{self.inverse_factorial(steps)}")    # N!
        self.treeview.insert("", tk.END, values=values)

    def inverse_factorial(self, value):
        i = 1
        while True:
            if self.factorial(i) > value:
                return i - 1
            i += 1

    def factorial(self, n):
        result = 1
        for i in range(2, n):
            result *= i
        return result


if __name__ == '__main__':
    app = App()
