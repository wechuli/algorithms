import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import itertools


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("string_search")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("270x300")

        self.window.grid_rowconfigure(3, weight=1)
        self.window.grid_columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Text:")
        label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
        self.text_entry = tk.Entry(self.window, width=1)
        self.text_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        self.text_entry.insert(tk.END, "abba daba abadabracadabra")

        label = tk.Label(self.window, text="Target:")
        label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
        self.target_entry = tk.Entry(self.window, width=1)
        self.target_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        self.target_entry.insert(tk.END, "cadabra")

        evaluate_button = tk.Button(self.window, text="Evaluate", width=8, command=self.evaluate)
        evaluate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.result_text = tk.Text(self.window)
        self.result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=evaluate_button: evaluate_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.text_entry.focus_force()
        self.window.mainloop()

    def evaluate(self):
        """ Search for the target."""
        text = self.text_entry.get()
        target = self.target_entry.get()
        location = self.find_target(text, target)

        if location < 0:
            self.text_entry.select_range(0, 0)
        else:
            self.text_entry.select_range(location, location + len(target))
        self.text_entry.focus_force()


    def find_target(self, text, target):
        """
        Find the first instance of the target string.
        Use a pre-calculated shift array.
        """
        self.result_text.delete("1.0", tk.END)
        trace = text + "\n"

        target_len = len(target)
        text_len = len(text)

        # Pre-calculate the shifts.
        shift = [[0 for c in range(target_len)] for r in range(256)]
        for ch in range(256):
            for i in range(target_len):
                # Fill in the shift if we see ch at position i.
                # Assume ch doesn't appear to the left in the target.
                shift[ch][i] = target_len

                # See if ch actually appears to the left in the target.
                for j in range(i - 1, -1, -1):
                    if target[j] == chr(ch):
                        shift[ch][i] = i - j
                        break

        # Examine the string.
        text_pos = target_len - 1
        while text_pos < text_len:
            if text_pos > target_len:
                trace += " " * (text_pos - target_len + 1)
            trace += target + "\n"

            matches = True
            for j in range(target_len):
                target_end = target_len - 1

                # See if the corresponding characters match.
                if text[text_pos - j] != target[target_end - j]:
                    # They don't match.
                    matches = False

                    # Get the character that didn't match.
                    bad_char = text[text_pos - j]

                    # Shift.
                    target_pos = target_len - j - 1
                    text_pos += shift[ord(bad_char)][target_pos]
                    break

            # If we had a match, return the starting point of the match.
            if matches:
                self.result_text.insert(tk.END, trace)
                return text_pos - target_len + 1

        # If we get here, there is no match.
        self.result_text.insert(tk.END, trace)
        return -1

    def find_target1(self, text, target):
        """
        Find the first instance of the target string.
        Calculate the shift on the fly.
        """
        self.result_text.delete("1.0", tk.END)
        trace = text + "\n"

        target_len = len(target)
        text_len = len(text)

        # Examine the string.
        text_pos = target_len - 1
        while text_pos < text_len:
            if text_pos > target_len:
                trace += " " * (text_pos - target_len + 1)
            trace += target + "\n"

            matches = True
            for j in range(target_len):
                target_end = target_len - 1

                # See if the corresponding characters match.
                if text[text_pos - j] != target[target_end - j]:
                    # They don't match.
                    matches = False

                    # Get the character that didn't match.
                    bad_char = text[text_pos - j]

                    # Find the next occurrance of bad_char to the left in the target.
                    # See how many characters we need to shift.
                    offset = target_len
                    for shift in range(1, target_len - j):
                        if target[target_end - j - shift] == bad_char:
                            offset = shift
                            break

                    # Shift.
                    text_pos += offset
                    break

            # If we had a match, return the starting point of the match.
            if matches:
                self.result_text.insert(tk.END, trace)
                return text_pos - target_len + 1

        # If we get here, there is no match.
        self.result_text.insert(tk.END, trace)
        return -1


if __name__ == '__main__':
    app = App()

# app.root.destroy()
