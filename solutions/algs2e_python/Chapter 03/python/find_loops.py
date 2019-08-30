import tkinter as tk
import re
from tkinter import messagebox

class ValueCell:
    def __init__(self, value, next):
         self.value = value
         self.next = next

    def contains_loop(self):
        """ Return True if the list contains a loop."""
        # Lists with 0 or 1 items don't contain loops.
        if (self.next == None) or (self.next.next == None):
            return False

        slow_cell = self.next
        fast_cell = slow_cell.next

        # Start the cells running.
        while True:
            if slow_cell == fast_cell:
                return True
            slow_cell = slow_cell.next

            fast_cell = fast_cell.next
            if fast_cell.next == None:
                return False
            fast_cell = fast_cell.next
            if fast_cell.next == None:
                return False

    def break_loop(self):
        """
        If this list after this cell contains a loop,
        break it so we have a normal list.
        """
        if not self.contains_loop():
             return

        slow_cell = self.next
        fast_cell = slow_cell.next

        # Start the cells running and see where they meet.
        while True:
            if slow_cell == fast_cell:
                break
            slow_cell = slow_cell.next
            fast_cell = fast_cell.next.next

        # Start slow_cell again at the beginning and
        # run the two at the same speed until their Next
        # cells are the same.
        slow_cell = self
        while slow_cell.next != fast_cell.next:
            slow_cell = slow_cell.next
            fast_cell = fast_cell.next

        # At this point, slow_cell.next is the first cell in the
        # loop and lastCell.next is the last cell in the loop.
        fast_cell.next = None


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("find_loops")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("200x350")

        frame = tk.Frame(self.window)
        frame.pack(padx=10, pady=2)

        label = tk.Label(frame, text="Original List")
        label.grid(row=0, column=0, padx=5, pady=2)
        label = tk.Label(frame, text="Fixed List")
        label.grid(row=0, column=1, padx=5, pady=2)

        self.listbox1 = tk.Listbox(frame, width=8, height=17)
        self.listbox1.grid(row=1, column=0, padx=5, pady=5)
        self.listbox2 = tk.Listbox(frame, width=8, height=17)
        self.listbox2.grid(row=1, column=1, padx=5, pady=5)

        self.status1_label = tk.Label(frame)
        self.status1_label.grid(row=2, column=0, padx=5, pady=2)
        self.status2_label = tk.Label(frame)
        self.status2_label.grid(row=2, column=1, padx=5, pady=2)

        # Test.
        self.test()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def test(self):
        """ Make a list that contains a loop and test it."""
        # Make and display the original values.
        self.build_list()
        self.display_list(self.listbox1)

        if self.top_cell.contains_loop():
            self.status1_label["text"] ="Loop"
        else:
            self.status1_label["text"] ="No loop"

        # Break the loop and redisplay the values.
        self.top_cell.break_loop()
        self.display_list(self.listbox2)

        if self.top_cell.contains_loop():
            self.status2_label["text"] = "Loop"
        else:
            self.status2_label["text"] = "No loop"

    def build_list(self):
        """ Make a list that contains a loop."""
        # Make some cells.
        # The number of cells in the list.
        num_cells = 7

        # The cell to which the last cell connects.
        loop_cell = 2

        cells = [None for i in range(num_cells)]
        for i in range(num_cells):
            cells[i] = ValueCell(i, None)
            cells[i].Value = i + 1

        # Link the cells.
        for i in range(num_cells - 1):
            cells[i].next = cells[i + 1]

        # Make the loop.
        cells[num_cells - 1].next = cells[loop_cell]

        # Prepare the sentinel.
        self.top_cell = ValueCell("<sentinel>", cells[0])

    def display_list(self, listbox):
        """ Display the list in the indicated ListBox."""
        # The maximum number of cells we will list.
        max_cells = 14

        # Display the list.
        listbox.delete(0, tk.END)
        cell_num = 0
        cell = self.top_cell.next
        while cell != None:
            listbox.insert(tk.END, cell.value)

            # Stop after a while.
            cell_num += 1
            if cell_num > max_cells:
                listbox.insert(tk.END, "...")
                break
            cell = cell.next


if __name__ == '__main__':
    app = App()

# app.root.destroy()
