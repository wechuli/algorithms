import tkinter as tk
from tkinter import messagebox


ord_a = ord("A")


class TrieNode:
    def __init__(self):
        self.remaining_key = ""
        self.value = None
        self.children = None
	
    def add_value(self, new_key, new_value):
        """ Add a value to this node's subtrie."""
        # If the remaining new key is not blank and matches
        # the remaining node key, place the value here.
        if (len(new_key) > 0) and (new_key == self.remaining_key):
            self.value = new_value
            return

        # If the remaining new key is blank and
        # so is the remaining node key, place the value here.
        if (len(new_key) == 0) and (len(self.remaining_key) == 0):
            self.value = new_value
            return

        # If the new key is blank but the node's remaining key isn't blank,
        # move the node's remaining key into a child and place the value here.
        if (len(new_key) == 0) and (len(self.remaining_key) > 0):
            # This must be a leaf node so give it children.
            self.children = [None for i in range(26)]
            index = ord(self.remaining_key[0]) - ord_a
            self.children[index] = TrieNode()
            self.children[index].remaining_key = self.remaining_key[1:]
            self.children[index].value = self.value
            self.remaining_key = ""
            self.value = new_value
            return

        # We need a child node.
        if self.children == None:
            # Make the children.
            self.children = [None for i in range(26)]

            # See if we have a remaining key.
            if len(self.remaining_key) > 0:
                # Move this into the appropriate child.
                index = ord(self.remaining_key[0]) - ord_a
                self.children[index] = TrieNode()
                self.children[index].remaining_key = self.remaining_key[1:]
                self.children[index].value = self.value
                self.remaining_key = ""
                self.value = None

        # Search the appropriate subtrie.
        index = ord(new_key[0]) - ord_a
        if self.children[index] == None:
            # This child doesn't exist. Make it and
            # let it represent the rest of the new key.
            self.children[index] = TrieNode()
            self.children[index].remaining_key = new_key[1:]
            self.children[index].value = new_value
            return

        # Search the appropriate subtrie.
        self.children[index].add_value(new_key[1:], new_value)

    def find_value(self, target_key):
        """ Find a value in this node's subtrie."""
        # If the remaining key matches the
        # remaining node key, return this node's value.
        if target_key == self.remaining_key:
            return self.value

        # Search the appropriate child.
        if self.children == None:
            return None
        index = ord(target_key[0]) - ord_a
        if self.children[index] == None:
            return None
        return self.children[index].find_value(target_key[1:])

    def __str__(self):
        """ Return a textual representation of this subtrie."""
        return self.make_string('-', 0)

    def make_string(self, letter, indent):
        """
        Return a textual representation for this subtrie.
        Variable letter is this node's letter. 
        """
        # Start with our value.
        result = " " * indent
        result += letter
        if len(self.remaining_key) > 0:
            result += f" -> {self.remaining_key}"
        if self.value != None:
            result += f" ({self.value})"
        result += "\n"

        # Add the child values if we have any.
        if self.children != None:
            for i in range(26):
                if self.children[i] != None:
                    ch = chr(ord_a + i)
                    result += self.children[i].make_string(ch, indent + 2)
        return result

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("trie")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")
        self.window.rowconfigure(2, weight=1)
        self.window.columnconfigure(1, weight=1)

        label = tk.Label(self.window, text="Key (text):")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.key_entry = tk.Entry(self.window)
        self.key_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W+tk.E)
        self.key_entry.insert(tk.END, "AARDVARK")
        add_button = tk.Button(self.window, text="Add", width=8, command=self.add)
        add_button.grid(padx=5, pady=2, row=0, column=2, sticky=tk.W+tk.E)

        label = tk.Label(self.window, text="Value (number):")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.value_entry = tk.Entry(self.window)
        self.value_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W+tk.E)
        self.value_entry.insert(tk.END, "80")
        find_button = tk.Button(self.window, text="Find", width=8, command=self.find)
        find_button.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W+tk.E)

        self.trie_label = tk.Label(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN, justify=tk.LEFT, anchor=tk.NW)
        self.trie_label.grid(padx=5, pady=5, row=2, column=0, columnspan=3, sticky=tk.NSEW)

        # The root of the trie.
        self.root = TrieNode()

        """ Uncomment to create a test tree. """
        self.root.add_value("APPLE", "10")
        self.root.add_value("APP", "20")
        self.root.add_value("APE", "30")
        self.root.add_value("BAN", "40")
        self.root.add_value("BANANA", "50")
        self.root.add_value("BEAR", "60")
        self.root.add_value("BANSHEE", "70")
        """ """
        self.trie_label["text"] = f"{self.root}"

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=add_button: add_button.invoke())) 

        # Force focus so Alt+F4 closes self window and not the Python shell.
        self.key_entry.focus_force()
        self.window.mainloop()

    def add(self):
        """ Add the value to the trie."""
        key = self.key_entry.get().upper()
        if len(key) == 0:
            messagebox.showinfo("Missing Key", "The key must not be blank.")
            self.key_entry.focus_force()
            return

        value = self.value_entry.get().upper()
        if len(value) == 0:
            messagebox.showinfo("Missing Value", "The value must not be blank.")
            self.value_entry.focus_force()
            return

        self.root.add_value(key, value)

        self.trie_label["text"] = f"{self.root}"
        self.key_entry.delete(0, tk.END)
        self.value_entry.delete(0, tk.END)
        self.key_entry.focus_force()

    def find(self):
        """ Find a value in the trie."""
        key = self.key_entry.get().upper()
        if len(key) == 0:
            messagebox.showinfo("Missing Key", "The key must not be blank.")
            self.key_entry.focus_force()
            return

        value = self.root.find_value(key)

        self.value_entry.delete(0, tk.END)
        self.value_entry.insert(tk.END, value)
        self.key_entry.focus_force()


if __name__ == '__main__':
    app = App()

# app.root.destroy()
