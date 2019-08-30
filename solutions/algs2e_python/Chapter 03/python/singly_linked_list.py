import tkinter as tk

class PersonCell:
    def __init__(self, name, next):
        self.name = name
        self.next = next

    def insert_after(self, new_name):
        """ Insert a cell after this one."""
        new_cell = PersonCell(new_name, self.next)
        self.next = new_cell

    def insert_after_name(self, new_name, after_name):
        """ Insert a cell after the indicated one."""
        # Find the target cell.
        after_cell = self.find_cell(after_name)

        # Insert the new name after the one we found.
        after_cell.insert_after(new_name)

    def delete_after(self):
        """ Delete the cell after this one."""
        cell = self.next
        if cell == None:
            return
        self.next = cell.next

    def delete(self, 	name):
        """ Delete the indicated cell."""
        # Find the cell before the one to delete.
        cell = self.find_cell_before(name)

        # Delete the target cell.
        cell.delete_after()

    def find_cell(self, name):
        """ Return the indicated cell."""
        cell = self
        while cell != None:
            if cell.name == name:
                return cell
            cell = cell.next
        return None

    def find_cell_before(self, name):
        """ Return the cell before the indicated one."""
        cell = self
        while cell != None:
            if cell.next.name == name:
                return cell
            cell = cell.next
        return None


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("singly_linked_list")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x300")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)

        label = tk.Label(frame, text="Name:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.name_entry = tk.Entry(frame, width=12)
        self.name_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        add_to_top_button = tk.Button(frame, width=12, text="Add To Top", command=self.add_to_top)
        add_to_top_button.grid(padx=5, pady=2, row=0, column=2)
        button = tk.Button(frame, width=12, text="Delete", command=self.delete)
        button.grid(padx=5, pady=2, row=0, column=3)

        label = tk.Label(frame, text="After:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.after_entry = tk.Entry(frame, width=12)
        self.after_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        button = tk.Button(frame, width=12, text="Add After", command=self.add_after)
        button.grid(padx=5, pady=2, row=1, column=2)

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=2, fill=tk.BOTH, expand=True)

        # Make an empty list.
        self.top_sentinel = PersonCell("<sentinel>", None)
        self.display_list()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=add_to_top_button: add_to_top_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.name_entry.focus_force()
        self.window.mainloop()

    def add_to_top(self):
        """ Add the new name to the top of the list."""
        self.top_sentinel.insert_after(self.name_entry.get())
        self.name_entry.delete(0, tk.END)
        self.name_entry.focus_force()
        self.display_list()

    def delete(self):
        """ Delete the indicated cell."""
        self.top_sentinel.delete(self.name_entry.get())
        self.name_entry.delete(0, tk.END)
        self.name_entry.focus_force()
        self.display_list()

    def add_after(self):
        """ Add the new name after the indicated name."""
        self.top_sentinel.insert_after_name(self.name_entry.get(), self.after_entry.get())
        self.name_entry.delete(0, tk.END)
        self.name_entry.focus_force()

        self.display_list()

    def display_list(self):
        """ Display the people in the list."""
        self.listbox.delete(0, tk.END)

        cell = self.top_sentinel
        while cell != None:
            self.listbox.insert(tk.END, cell.name)
            cell = cell.next


if __name__ == '__main__':
    app = App()

# app.root.destroy()
