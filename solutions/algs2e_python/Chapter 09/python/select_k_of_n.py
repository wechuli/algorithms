import tkinter as tk
import math


def select_k_of_n_with_duplicates(index, selections, items, results):
    """ Generate combinations allowing duplicates."""
    # See if we have made the last assignment.
    if index == len(selections):
        # Add the result to the result list.
        result = ""
        for selection in selections:
            result += items[selection]
        results.append(result)
    else:
        # Get the smallest value we can use for the next selection.
        start = 0
        if index > 0:
            start = selections[index - 1]

        # Make the next assignment.
        for i in range(start, len(items)):
            # Add item i to the selection.
            selections[index] = i

            # Recursively make the other assignments.
            select_k_of_n_with_duplicates(index + 1, selections, items, results)

def select_k_of_n_without_duplicates(index, selections, items, results):
    """ Generate combinations not allowing duplicates."""
    # See if we have made the last assignment.
    if index == len(selections):
        # Add the result to the result list.
        result = ""
        for selection in selections:
            result += items[selection]
        results.append(result)
    else:
        # Get the smallest value we can use for the next selection.
        start = 0
        if index > 0:
            start = selections[index - 1] + 1

        # Make the next assignment.
        for i in range(start, len(items)):
            # Add item i to the selection.
            selections[index] = i

            # Recursively make the other assignments.
            select_k_of_n_without_duplicates(index + 1, selections, items, results)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("select_k_of_n")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x355")

        frame = tk.Frame(self.window)
        frame.pack()
        label = tk.Label(frame, text="Select")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.k_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.k_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.k_entry.insert(tk.END, "3")
        label = tk.Label(frame, text="of")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.n_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.n_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.n_entry.insert(tk.END, "5")
        go_button = tk.Button(frame, text="Go", width=8, command=self.go)
        go_button.pack(padx=(10,5), pady=2, side=tk.LEFT)

        frame = tk.Frame(self.window)
        frame.pack(padx=(0,5), pady=5, fill=tk.BOTH, expand=True)
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.rowconfigure(1, weight=1)

        label = tk.Label(frame, text="With Duplicates")
        label.grid(padx=5, pady=2, row=0, column=0)
        label = tk.Label(frame, text="Without Duplicates")
        label.grid(padx=5, pady=2, row=0, column=1)

        list_frame = tk.Frame(frame)
        list_frame.grid(row=1, column=0, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.with_dups_listbox = tk.Listbox(list_frame)
        self.with_dups_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.with_dups_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.with_dups_listbox.yview)

        list_frame = tk.Frame(frame)
        list_frame.grid(row=1, column=1, sticky=tk.W+tk.E+tk.N+tk.S)
        scrollbar = tk.Scrollbar(list_frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.without_dups_listbox = tk.Listbox(list_frame)
        self.without_dups_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.without_dups_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.without_dups_listbox.yview)

        self.result_with_dups_label = tk.Label(frame, text="")
        self.result_with_dups_label.grid(padx=5, pady=2, row=2, column=0)
        self.result_without_dups_label = tk.Label(frame, text="")
        self.result_without_dups_label.grid(padx=5, pady=2, row=2, column=1)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.k_entry.focus_force()
        self.window.mainloop()

    def go(self):
        """ Draw the Hilbert curve."""
        k = int(self.k_entry.get())
        n = int(self.n_entry.get())

        # Make the list of items.
        asc_a = ord("A")
        items = []
        for i in range(n):
            items.append(chr(asc_a + i))

        selections = [0 for i in range(k)]
        results = []
        select_k_of_n_with_duplicates(0, selections, items, results)
        self.with_dups_listbox.delete(0, tk.END)
        for result in results:
            self.with_dups_listbox.insert(tk.END, result)
        self.result_with_dups_label["text"] = f"{len(results)} permutations"

        selections = [0 for i in range(k)]
        results2 = []
        select_k_of_n_without_duplicates(0, selections, items, results2)
        self.without_dups_listbox.delete(0, tk.END)
        for result in results2:
            self.without_dups_listbox.insert(tk.END, result)
        self.result_without_dups_label["text"] = f"{len(results2)} permutations"


if __name__ == '__main__':
    app = App()

# app.root.destroy()
