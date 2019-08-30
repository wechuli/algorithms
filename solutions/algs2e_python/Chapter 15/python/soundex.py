import tkinter as tk
from tkinter import ttk
import itertools


def soundex(name):
    """ Return the name's soundex encoding."""
    # Save the first letter.
    first_letter = name[0].upper()

    # Convert to lower case.
    name = name.lower()

    # Remove w and h.
    name = name.replace("w", "")
    name = name.replace("h", "")

    # Encode the letters.
    name = encode_letters(name)

    # Remove adjacent duplicate codes.
    name = remove_adjacent_duplicates(name)

    # Replace the first code with the original letter.
    name = first_letter + name[1:]

    # Remove vowels (after the first letter).
    name = name.replace("0", "")

    # Pad to 4 characters.
    name = (name + "000")[:4]

    return name

def remove_adjacent_duplicates(name):
    """ Remove adjacent duplicate codes."""
    j = 1
    while j < len(name):
        if name[j] == name[j - 1]:
            name = name[:j] + name[j + 1:]
        else:
            j += 1
    return name

def encode_letters(name):
    """ Encode the letters in a string."""
    # Character codes.
    codes = []
    codes.append("aeiouy")    # Vowels map to 0.
    codes.append("bfpv")      # 1
    codes.append("cgjkqsxz")  # 2
    codes.append("dt")        # 3
    codes.append("l")         # 4
    codes.append("mn")        # 5
    codes.append("r")         # 6

    # Encode the letters.
    result = ""
    for ch in name:
        for i in range(len(codes)):
            if ch in codes[i]:
                result += f"{i}"
                break
    return result


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("soundex")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("270x270")

        treeview = ttk.Treeview(self.window, columns=("name", "result", "desired"))
        treeview.pack(padx=5, pady=5, expand=True, fill=tk.BOTH)

        treeview.heading("#0", text="Name")
        treeview.heading("#1", text="Result")
        treeview.heading("#2", text="Desired")
        treeview.column("#0", anchor=tk.E, width=100, stretch=False)
        treeview.column("#1", anchor=tk.E, width=70, stretch=False)
        treeview.column("#2", anchor=tk.E, width=70, stretch=False)

        # Display some test results.
        names = [ "Robert", "Rupert", "Rubin", "Ashcraft", "Ashcroft", "Tymczak", "Pfister", "Honeyman", "Smith", "Smyth", "Smithe", "Smythe" ]
        desired_results = [ "R163", "R163", "R150", "A261", "A261", "T522", "P236", "H555", "S530", "S530", "S530", "S530" ]
        for i in range(len(names)):
            results = (soundex(names[i]), desired_results[i])
            treeview.insert("", tk.END, text=names[i], values=results)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
