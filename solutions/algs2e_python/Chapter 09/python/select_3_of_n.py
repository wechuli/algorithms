import tkinter as tk
import math


def select_3_with_duplicates(items):
    """ Generate selections of 3 items allowing duplicates."""
    results = []
    for i in range(len(items)):
        for j in range(i, len(items)):
            for k in range(j, len(items)):
                results.append(items[i] + items[j] + items[k])
    return results

def select_3_without_duplicates(items):
    """ Generate selections of 3 items without allowing duplicates."""
    results = []
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            for k in range(j + 1, len(items)):
                results.append(items[i] + items[j] + items[k])
    return results


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("select_3_of_n")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x355")

        frame = tk.Frame(self.window)
        frame.pack()
        label = tk.Label(frame, text="Select")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        label = tk.Label(frame, text="3")
        label.pack(padx=5, pady=2, side=tk.LEFT)
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
        self.n_entry.focus_force()
        self.window.mainloop()

    def go(self):
        """ Draw the Hilbert curve."""
        n = int(self.n_entry.get())

        # Make the list of items.
        asc_a = ord("A")
        items = []
        for i in range(n):
            items.append(chr(asc_a + i))

        results = select_3_with_duplicates(items)
        self.with_dups_listbox.delete(0, tk.END)
        for result in results:
            self.with_dups_listbox.insert(tk.END, result)
        self.result_with_dups_label["text"] = f"{len(results)} permutations"

        results2 = select_3_without_duplicates(items)
        self.without_dups_listbox.delete(0, tk.END)
        for result in results2:
            self.without_dups_listbox.insert(tk.END, result)
        self.result_without_dups_label["text"] = f"{len(results2)} permutations"


if __name__ == '__main__':
    app = App()

# app.root.destroy()
