import tkinter as tk
import random


ord_a = ord("A")

def encrypt(pad, start_index, plaintext):
    """ Encrypt."""
    return encrypt_decrypt(pad, start_index, plaintext, False)

def decrypt(pad, start_index, ciphertext):
    """ Decrypt."""
    return encrypt_decrypt(pad, start_index, ciphertext, True)

def encrypt_decrypt(pad, start_index, text, decrypt):
    """ Use the one-time pad to encrypt or decrypt the text. """
    text = text.upper().replace(" ", "")

    # Start at the right entry in the pad.
    i = start_index

    # Make sure we have enough pad left for this message.
    if start_index + len(text) > len(pad):
        raise ValueError("The pad doesn't contain enough unnused characters for this operation.")

    result = ""
    for ch in text:
        ch_num = ord(ch) - ord_a
        pad_num = ord(pad[i]) - ord_a
        if decrypt:
            new_ch = ord_a + (ch_num - pad_num) % 26
        else:
            new_ch = ord_a + (ch_num + pad_num) % 26
        result += chr(new_ch)
        i += 1

    # Return the ciphertext.
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
        self.window.title("one_time_pad")
        self.window.protocol("WM_find_WINDOW", self.kill_callback)
        self.window.geometry("300x310")

        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Pad:")
        label.grid(padx=5, pady=5, row=0, column=0, sticky=tk.W)

        self.pad_text = tk.Text(self.window, wrap=tk.CHAR, height=6, width=10)
        self.pad_text.grid(padx=5, pady=5, row=1, column=0, columnspan=2, sticky=tk.NSEW)

        # Make some fonts.
        self.pad_text.tag_configure("encrypt_font", font=("Courier New", 10), foreground="blue")
        self.pad_text.tag_configure("decrypt_font", font=("Courier New", 10), foreground="blue", background="yellow")
        self.initialize_pad()

        label = tk.Label(self.window, text="Message:")
        label.grid(padx=5, pady=5, row=2, column=0, sticky=tk.W)
        self.message_entry = tk.Entry(self.window, width=30)
        self.message_entry.grid(padx=5, pady=5, row=2, column=1, sticky=tk.EW)
        self.message_entry.insert(tk.END, "This is a secret message")

        encrypt_button = tk.Button(self.window, width=8, text="Encrypt", command=self.encrypt)
        encrypt_button.grid(padx=5, pady=5, row=3, column=0, columnspan=2)

        label = tk.Label(self.window, text="Ciphertext:")
        label.grid(padx=5, pady=5, row=4, column=0, sticky=tk.W)
        self.ciphertext_entry = tk.Entry(self.window, width=30, font="Courier 10")
        self.ciphertext_entry.grid(padx=5, pady=5, row=4, column=1, sticky=tk.EW)

        decrypt_button = tk.Button(self.window, width=8, text="Decrypt", command=self.decrypt)
        decrypt_button.grid(padx=5, pady=5, row=6, column=0, columnspan=2)

        label = tk.Label(self.window, text="Plainttext:")
        label.grid(padx=5, pady=5, row=7, column=0, sticky=tk.W)
        self.plaintext_entry = tk.Entry(self.window, width=30, font="Courier 10")
        self.plaintext_entry.grid(padx=5, pady=5, row=7, column=1, sticky=tk.EW)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=encrypt_button: encrypt_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        encrypt_button.focus_force()
        self.window.mainloop()

    def initialize_pad(self):
        """ Initialize the one-time pad."""
        # Initialize the pad.
        self.pad_string = \
             "GCMURLJYCQAGIZRRHPSSYCEJUEUHVXOSSAZUWBNNHZRKLRRMGJ" + \
             "NEJRKEYCZMQBDFCIOHZWUFCELYKUYDMIBMJKJAQVWUCAXFWMHD" + \
             "DJMJOHBEGLTEDWZIZQWSYOREAADBHFCYMVZDVSXBIFTECRQGAO" + \
             "GFQPEPRIJNEZWBJVSIWWMHTUJTUNCIKXBSYWHWQKLNIJWIIRVG"
        self.num_used_to_encrypt = 0
        self.num_used_to_decrypt = 0

        # Display the pad.
        self.display_pad()

    def display_pad(self):
        """ Display the one-time pad."""
        pos1 = self.num_used_to_decrypt
        pos2 = self.num_used_to_encrypt

        pad_decrypted = self.pad_string[:pos1]
        pad_encrypted = self.pad_string[pos1:pos2]
        pad_remainder = self.pad_string[pos2:]

        self.pad_text.delete("1.0", tk.END)
        self.pad_text.insert(tk.END, pad_decrypted, "decrypt_font")
        self.pad_text.insert(tk.END, pad_encrypted, "encrypt_font")
        self.pad_text.insert(tk.END, pad_remainder)

    def encrypt(self):
        """ Encrypt."""
        message = self.message_entry.get()
        ciphertext = encrypt(self.pad_string, self.num_used_to_encrypt, message)
        self.ciphertext_entry.delete(0, tk.END)
        self.ciphertext_entry.insert(tk.END, to_n_grams(ciphertext))
        self.plaintext_entry.delete(0, tk.END)

        self.num_used_to_encrypt += len(ciphertext)
        self.display_pad()

    def decrypt(self):
        """ Decrypt."""
        message = self.ciphertext_entry.get()
        plaintext = decrypt(self.pad_string, self.num_used_to_decrypt, message)
        self.plaintext_entry.delete(0, tk.END)
        self.plaintext_entry.insert(tk.END, to_n_grams(plaintext))

        self.num_used_to_decrypt += len(plaintext)
        self.display_pad()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
