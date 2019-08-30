import tkinter as tk


ord_a = ord("A")


def encrypt(plaintext, key):
    """ Use a column transformation to encrypt the message."""
    return encrypt_decrypt(plaintext, key, False)

def decrypt(ciphertext, key):
    """ Use a column transformation to decrypt the message."""
    return encrypt_decrypt(ciphertext, key, True)

def encrypt_decrypt(plaintext, key, decrypt):
    """ Use a Vigenere cihper to encrypt or decrypt the message."""
    # Convert the key into an array of offsets.
    offset = []
    if decrypt:
        for i in range(len(key)):
            offset.append(26 - (ord(key[i]) - ord_a))
    else:
        for i in range(len(key)):
            offset.append(ord(key[i]) - ord_a)

    # Process the message.
    result = ""
    for i in range(len(plaintext)):
        j = i % len(key)
        ch_num = ord(plaintext[i]) - ord_a
        ch_num = (ch_num + offset[j]) % 26
        result += chr(ch_num + ord_a)

    return result

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
        self.window.title("vigenere_cipher")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("320x200")

        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Message:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self.window, width=12)
        self.message_entry.grid(padx=5, pady=5, row=0, column=1, sticky=tk.EW)
        self.message_entry.insert(0, "THIS IS A SECRET MESSAGE")

        label = tk.Label(self.window, text="Key:")
        label.grid(padx=5, pady=5, row=1, column=0, sticky=tk.W)
        self.key_entry = tk.Entry(self.window, width=12)
        self.key_entry.grid(padx=5, pady=5, row=1, column=1, sticky=tk.W)
        self.key_entry.insert(0, "ZEBRAS")

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
        """ Use a column transformation to encrypt the message."""
        message = self.message_entry.get().upper().replace(" ", "")
        key = self.key_entry.get()
        ciphertext = encrypt(message, key)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(tk.END, to_n_grams(ciphertext))
        self.plaintext_entry.delete(0, tk.END)

    def decrypt(self):
        """ Use a column transformation to decrypt the message."""
        ciphertext = self.ciphertext_entry.get().upper().replace(" ", "")
        key = self.key_entry.get()
        plaintext = decrypt(ciphertext, key)
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(tk.END, to_n_grams(plaintext))


if __name__ == '__main__':
    app = App()

# app.root.destroy()
