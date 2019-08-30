import tkinter as tk


def encrypt(plaintext, col_key, row_key):
    """ Use a column transformation to encrypt the message."""
    return encrypt_decrypt(plaintext, col_key, row_key, False)

def decrypt(ciphertext, col_key, row_key):
    """ Use a column transformation to decrypt the message."""
    return encrypt_decrypt(ciphertext, col_key, row_key, True)

def encrypt_decrypt(plaintext, col_key, row_key, decrypt):
    """ Use a column transformation to encrypt or decrypt the message."""
    # Calculate the number of rows.
    num_columns = len(col_key)
    num_rows = int(1 + (len(plaintext) - 1) / num_columns)

    # Pad the string if necessary to make it fit the rectangle evenly.
    if num_rows * num_columns != len(plaintext):
        plaintext += "X" * (num_rows * num_columns - len(plaintext))

    # Make the key mappings.
    forward_col_mapping, inverse_col_mapping = make_key_mapping(col_key)
    forward_row_mapping, inverse_row_mapping = make_key_mapping(row_key)
    if decrypt:
        col_mapping = forward_col_mapping
        row_mapping = forward_row_mapping
    else:
        col_mapping = inverse_col_mapping
        row_mapping = inverse_row_mapping

    # Construct the encrypted/decrypted string.
    result = ""
    for row in range(num_rows):
        # Read this row in permuted order.
        for col in range(num_columns):
            index = row_mapping[row] * num_columns + col_mapping[col]
            result += plaintext[index]

    return result

def make_key_mapping(key):
    """ Make a mapping for this key."""
    # Sort the characters.
    chars = list(key)
    chars.sort()
    sorted_key = "".join(chars)

    # Make the mapping.
    mapping = []
    for i in range(len(key)):
        mapping.append(sorted_key.index(key[i]))

    # Make the inverse mapping.
    inverse_mapping = [0 for i in range(len(key))]
    for i in range(len(key)):
        inverse_mapping[mapping[i]] = i

    return mapping, inverse_mapping

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
        self.window.title("swap_rows_and_columns")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("320x230")

        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Message:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self.window, width=12)
        self.message_entry.grid(padx=5, pady=5, row=0, column=1, sticky=tk.EW)
        self.message_entry.insert(0, "THIS IS A SECRET MESSAGE")

        label = tk.Label(self.window, text="Key 1:")
        label.grid(padx=5, pady=5, row=1, column=0, sticky=tk.W)
        self.key1_entry = tk.Entry(self.window, width=12)
        self.key1_entry.grid(padx=5, pady=5, row=1, column=1, sticky=tk.W)
        self.key1_entry.insert(0, "CARTS")

        label = tk.Label(self.window, text="Key 2:")
        label.grid(padx=5, pady=5, row=2, column=0, sticky=tk.W)
        self.key2_entry = tk.Entry(self.window, width=12)
        self.key2_entry.grid(padx=5, pady=5, row=2, column=1, sticky=tk.W)
        self.key2_entry.insert(0, "FISH")

        encrypt_button = tk.Button(self.window, width=8, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(padx=5, pady=5, row=3, column=0, columnspan=2)

        label = tk.Label(self.window, text="Ciphertext:")
        label.grid(padx=5, pady=5, row=4, column=0, sticky=tk.W)
        self.ciphertext_entry = tk.Entry(self.window, width=12)
        self.ciphertext_entry.grid(padx=5, pady=5, row=4, column=1, sticky=tk.EW)

        decrypt_button = tk.Button(self.window, width=8, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(padx=5, pady=5, row=5, column=0, columnspan=2)

        label = tk.Label(self.window, text="Plaintext:")
        label.grid(padx=5, pady=5, row=6, column=0, sticky=tk.W)
        self.plaintext_entry = tk.Entry(self.window, width=12)
        self.plaintext_entry.grid(padx=5, pady=5, row=6, column=1, sticky=tk.EW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=encrypt_button: encrypt_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.message_entry.focus_force()
        self.window.mainloop()

    def encrypt(self):
        """ Use a column transformation to encrypt the message."""
        message = self.message_entry.get().upper().replace(" ", "")
        col_key = self.key1_entry.get()
        row_key = self.key2_entry.get()
        ciphertext = encrypt(message, col_key, row_key)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(tk.END, to_n_grams(ciphertext))
        self.plaintext_entry.delete(0, tk.END)

    def decrypt(self):
        """ Use a column transformation to decrypt the message."""
        ciphertext = self.ciphertext_entry.get().upper().replace(" ", "")
        col_key = self.key1_entry.get()
        row_key = self.key2_entry.get()
        plaintext = decrypt(ciphertext, col_key, row_key)
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(tk.END, to_n_grams(plaintext))


if __name__ == '__main__':
    app = App()

# app.root.destroy()
