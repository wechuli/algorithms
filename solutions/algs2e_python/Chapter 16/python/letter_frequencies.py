import tkinter as tk


ord_a = ord("A")


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("letter_frequencies")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("320x200")

        self.window.rowconfigure(2, weight=1)
        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Message:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self.window, width=12)
        self.message_entry.grid(padx=5, pady=5, row=0, column=1, sticky=tk.EW)
        self.message_entry.insert(0, "WKLVL VDVHF UHWPH VVDJH")

        evaluate_button = tk.Button(self.window, width=8, text="Evaluate", command=self.evaluate)
        evaluate_button.grid(padx=5, pady=5, row=1, column=0, columnspan=2)

        frame = tk.Frame(self.window)
        frame.grid(row=2, column=0, columnspan=2, sticky=tk.NSEW)

        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox = tk.Listbox(frame)
        self.listbox.pack(fill=tk.BOTH, expand=1)

        # Attach the scrollbar to the listbox.
        self.listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=evaluate_button: evaluate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.message_entry.focus_force()
        self.window.mainloop()

    def evaluate(self):
        """ Calculate the number of occurrances of each letter."""
        message = self.message_entry.get().upper().replace(" ", "")
        occurrences = [0] * 26
        for ch in message:
            ch_num = ord(ch) - ord_a;
            occurrences[ch_num] += 1

        # Display the results.
        self.listbox.delete(0, tk.END)
        items = []
        for i in range(26):
            percent = occurrences[i] / len(message)

            # The offset at the end is the offset if the letter is E.
            offset = (i - 4 + 26) % 26
            letter = chr(i + ord_a)
            txt = f"{percent:6.1%} {letter} {offset}"
            items.append(txt)

        items.sort()
        for item in items:
            self.listbox.insert(tk.END, item)


if __name__ == '__main__':
    app = App()

# app.root.destroy()
