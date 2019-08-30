import tkinter as tk


def encrypt(plaintext, num_columns):
    """ Use a row/column transposition to encrypt the message."""
    # Calculate the number of rows.
    num_rows = int(1 + (len(plaintext) - 1) / num_columns)

    # Pad the string if necessary to make it fit the rectangle evenly.
    if num_rows * num_columns != len(plaintext):
        plaintext += "X" * (num_rows * num_columns - len(plaintext))

    # Construct the encrypted string.
    result = ""
    for col in range(num_columns):
        index = col
        for row in range(num_rows):
            result += plaintext[index]
            index += num_columns

    return result

def decrypt(ciphertext, num_columns):
    """ Use a row/column transposition to encrypt the message."""
    num_rows = int(len(ciphertext) / num_columns)
    return encrypt(ciphertext, num_rows)

def to_n_grams(message):
    """ Break the text into 5-character chunks."""
    # Pad the message in case its length isn't a multiple of 5.
    message += "     "

    # Create the 5-character chunks.
    result = ""
    for i in range(0, len(message) - 5, 5):
        result += message[i: i + 5] + " "

    # Remove trailing spaces.
    return result.rstrip()


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("row_column_transposition")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("320x200")

        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Message:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self.window, width=12)
        self.message_entry.grid(padx=5, pady=5, row=0, column=1, sticky=tk.EW)
        self.message_entry.insert(0, "THIS IS A SECRET MESSAGE")

        label = tk.Label(self.window, text="# Columns:")
        label.grid(padx=5, pady=5, row=1, column=0, sticky=tk.W)
        self.num_columns_entry = tk.Entry(self.window, width=12)
        self.num_columns_entry.grid(padx=5, pady=5, row=1, column=1, sticky=tk.W)
        self.num_columns_entry.insert(0, "5")

        encrypt_button = tk.Button(self.window, width=8, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(padx=5, pady=5, row=2, column=0, columnspan=2)

        label = tk.Label(self.window, text="Ciphertext:")
        label.grid(padx=5, pady=5, row=3, column=0, sticky=tk.W)
        self.ciphertext_entry = tk.Entry(self.window, width=12)
        self.ciphertext_entry.grid(padx=5, pady=5, row=3, column=1, sticky=tk.EW)

        decrypt_button = tk.Button(self.window, width=8, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(padx=5, pady=5, row=4, column=0, columnspan=2)

        label = tk.Label(self.window, text="Plaintext:")
        label.grid(padx=5, pady=5, row=5, column=0, sticky=tk.W)
        self.plaintext_entry = tk.Entry(self.window, width=12)
        self.plaintext_entry.grid(padx=5, pady=5, row=5, column=1, sticky=tk.EW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=encrypt_button: encrypt_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.message_entry.focus_force()
        self.window.mainloop()

    def encrypt(self):
        """ Encrypt."""
        message = self.message_entry.get().upper().replace(" ", "")
        num_columns = int(self.num_columns_entry.get())
        ciphertext = encrypt(message, num_columns)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(tk.END, to_n_grams(ciphertext))
        self.plaintext_entry.delete(0, tk.END)

    def decrypt(self):
        """ Encrypt."""
        ciphertext = self.ciphertext_entry.get().upper().replace(" ", "")
        num_columns = int(self.num_columns_entry.get())
        plaintext = decrypt(ciphertext, num_columns)
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(tk.END, to_n_grams(plaintext))


if __name__ == '__main__':
    app = App()

# app.root.destroy()
