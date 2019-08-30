
import tkinter as tk
import tkinter.font as tk_font
from tkinter import messagebox
from tkinter import ttk
import random

def find_optimal_cuts(length, values, optimal_values = None, optimal_cuts = None):
    """ Find optimal cuts. Return the total value and cuts."""
    # If optimal_values and optimal_cuts are null, initialize them.
    if optimal_values == None:
        optimal_values = [0 for i in range(length + 1)]
        optimal_cuts = [None for i in range(length + 1)]

    # See if we already know length's optimal cut.
    if optimal_cuts[length] != None:
        return optimal_values[length], optimal_cuts[length]

    # Assume we make no cuts.
    best_value = values[length]
    best_cuts = [length]

    # Try possible single cuts.
    for i in range(1, length // 2 + 1):
        # Try pieces with lengths i and length - i.
        value1, cuts1 = find_optimal_cuts(i, values, optimal_values, optimal_cuts)
        value2, cuts2 = find_optimal_cuts(length - i, values, optimal_values, optimal_cuts)

        # See if this is an improvement.
        if value1 + value2 > best_value:
            best_value = value1 + value2
            best_cuts = cuts1 + cuts2

    # Save the optimal value and cuts.
    optimal_values[length] = best_value
    optimal_cuts[length] = best_cuts

    return best_value, best_cuts

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("dynamic_rod_cutting")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("350x160")

        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        frame.grid_columnconfigure(1, weight=1)

        values_label = tk.Label(frame, text="Values:")
        values_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.values_entry = tk.Entry(frame)
        self.values_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.values_entry.insert(tk.END, "1 5 8 9 10 17 17 20 25 26 31 32 35 39 40 44 46 48 55 58 60 63 67 70 72")
        cut_button = tk.Button(frame, text="Cut", width=8, command=self.cut)
        cut_button.grid(row=0, column=2, padx=5, pady=2)

        length_label = tk.Label(frame, text="Length:", anchor=tk.W)
        length_label.grid(row=1, column=0, padx=5, pady=2, sticky=tk.W)
        self.length_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.length_entry.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W)
        self.length_entry.insert(tk.END, "10")

        spacer_label = tk.Label(frame, text="", anchor=tk.W)
        spacer_label.grid(row=2, column=0, padx=5, pady=2, sticky=tk.W)

        cuts_label = tk.Label(frame, text="Cuts:", anchor=tk.W)
        cuts_label.grid(row=3, column=0, padx=5, pady=2, sticky=tk.W)
        self.cuts_entry = tk.Entry(frame)
        self.cuts_entry.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        best_values_label = tk.Label(frame, text="Values:", anchor=tk.W)
        best_values_label.grid(row=4, column=0, padx=5, pady=2, sticky=tk.W)
        self.best_values_entry = tk.Entry(frame)
        self.best_values_entry.grid(row=4, column=1, padx=5, pady=2, sticky=tk.W+tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=cut_button: cut_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.values_entry.focus_force()
        self.window.mainloop()

    def cut(self):
        """ Find optimal cuts."""
        self.cuts_entry.delete(0, 'end')
        self.best_values_entry.delete(0, 'end')

        # Read the values.
        fields = self.values_entry.get().split(" ")
        values = [0]
        for i in range(0, len(fields)):
            values.append(int(fields[i]))
        length = int(self.length_entry.get())

        # Expand the values list up to values[length].
        for i in range(len(values), length +1):
            values.append(0)

        # Find the cuts.
        best_value, best_cuts = find_optimal_cuts(length, values)

        # Display the cuts.
        cuts_list = map(str, best_cuts)
        self.cuts_entry.insert(tk.END, " + ".join(cuts_list))

        # Display the cut values.
        cut_values = [values[cut] for cut in best_cuts]
        values_list = map(str, cut_values)
        values_text = " + ".join(values_list) + " = " + str(sum(cut_values))
        self.best_values_entry.insert(tk.END, values_text)

if __name__ == '__main__':
    app = App()

# app.root.destroy()
