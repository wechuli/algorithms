import tkinter as tk

class Cell:
    """Store an item for a linked list."""
    def __init__(self, value, prev, next):
        self.value = value
        self.count = 0

        self.prev = prev
        if prev != None:
            prev.next = self

        self.next = next
        if next != None:
            next.prev = self

    def remove(self):
        """Remove the cell from the list."""
        self.prev.next = self.next
        if self.next != None:
            self.next.prev = self.prev

    def insert(self, prev, after_cell):
        """Insert the cell betweeen two others."""
        prev.next = self
        self.next = after_cell

        if after_cell != None:
            after_cell.prev = self
        self.prev = prev

    def __str__(self):
        return f"{self.value}"

class OrganizingList:
    """Base class for self-organizing lists."""
    def __init__(self):
        # Give the lists a sentinel.
        self.sentinel = Cell(-1, None, None)        

    def __str__(self):
        """ Return the list's values."""
        result = ""
        cell = self.sentinel.next
        while cell != None:
            result += " " + str(cell)
            cell = cell.next
        return result[1:]

    def expected_search(self, probs):
        """
        Return the expected search length for
        the values with the given probabilities.
        """
        total = 0
        num_steps = 0
        cell = self.sentinel.next
        while cell != None:
            num_steps += 1
            total += num_steps * probs[cell.value]
            cell = cell.next
        return total

    def add(self, value):
        """Add an item at the beginning of the list after the sentinel."""
        cell = Cell(value, self.sentinel, self.sentinel.next)

    def rearrange(self, cell):
        """Rearrange the list appropriately."""
        pass

    def find(self, value):
        """
        Find an item, move it appropriately, and
        return the number of steps it took.
        """
        num_steps = 1
        cell = self.sentinel.next
        while (cell != None) and (cell.value != value):
            num_steps += 1
            cell = cell.next

        # Rearrange the list appropriately.
        assert cell != None, f"Could not find item {value}."
        if cell != None:
            self.rearrange(cell)

        return num_steps

    def swap_cells(self, cell1, cell2):
        """Swap two cells."""
        cell1.remove()
        cell1.insert(cell2, cell2.next)

class MtfList(OrganizingList):
    """
    A linked list that moves the most
    recently accessed value to the front.
    """

    def rearrange(self, cell):
        """Move the found cell to the front of the list."""
        # Don't bother if the cell is already at the front.
        if cell == self.sentinel.next:
            return

        # Remove the cell from its current position.
        cell.remove()

        # Move the cell to the front.
        cell.insert(self.sentinel, self.sentinel.next)

class SwapList(OrganizingList):
    """
    A linked list that swaps the most recently
    found item with the item before it.
    """

    def rearrange(self, cell):
        """Swap the found cell with the cell before it."""
        # Don't bother if the cell is already at the front.
        if cell == self.sentinel.next:
            return

        self.swap_cells(cell.prev, cell)

class CountList(OrganizingList):
    """
    A linked list that moves found items up
    in the list until their counts are ordered.
    """

    def __init__(self):
        """Initialize the sentinel's count."""
        super().__init__()
        self.sentinel.count = 100000000000

    def rearrange(self, cell):
        """
        Swap the found cell with the cell
        before it until the counts are ordered.
        """
        # Increment the count.
        cell.count += 1

        # Swap the cell up as long as its count is
        # greater than the count of the cell before it.
        while cell.count > cell.prev.count:
            self.swap_cells(cell.prev, cell)


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("self_organizing_lists")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("380x230")

        frame1 = tk.Frame(self.window)
        frame1.pack(pady=(5,0))

        num_values_label = tk.Label(frame1, text="# Values:")
        num_values_label.grid(row=0, column=0, padx=5, pady=2)
        self.num_values_entry = tk.Entry(frame1, width=8, justify=tk.RIGHT)
        self.num_values_entry.grid(row=0, column=1, padx=5, pady=2)
        self.num_values_entry.insert(tk.END, "100")

        probs_label = tk.Label(frame1, text="Probabilities:", justify=tk.LEFT)
        probs_label.grid(row=0, column=2, padx=5, pady=2)

        num_searches_label = tk.Label(frame1, text="# Searches:")
        num_searches_label.grid(row=1, column=0, padx=5, pady=2)
        self.num_searches_entry = tk.Entry(frame1, width=8, justify=tk.RIGHT)
        self.num_searches_entry.grid(row=1, column=1, padx=5, pady=2)
        self.num_searches_entry.insert(tk.END, "10000")

        self.prob_type = tk.IntVar()
        self.prob_type.set(0)
        equal_button = tk.Radiobutton(frame1, text="Equal", variable=self.prob_type, value=0)
        equal_button.grid(row=1, column=2, padx=5, pady=2)
        linear_button = tk.Radiobutton(frame1, text="Linear", variable=self.prob_type, value=1)
        linear_button.grid(row=1, column=3, padx=5, pady=2)
        quadratic_button = tk.Radiobutton(frame1, text="Quadratic", variable=self.prob_type, value=2)
        quadratic_button.grid(row=1, column=4, padx=5, pady=2)

        go_button = tk.Button(self.window, text="Go", width=8, command=self.go)
        go_button.pack(pady=5)

        frame2 = tk.Frame(self.window)
        frame2.pack()

        steps_label = tk.Label(frame2, text="Steps", width=11)
        steps_label.grid(row=0, column=1, padx=5, pady=2)
        ave_steps_label = tk.Label(frame2, text="Ave Steps", width=11)
        ave_steps_label.grid(row=0, column=2, padx=5, pady=2)
        expected_steps_label = tk.Label(frame2, text="Expected Steps", width=11)
        expected_steps_label.grid(row=0, column=3, padx=5, pady=2)

        none_label = tk.Label(frame2, text="None List:", justify=tk.LEFT)
        none_label.grid(row=1, column=0, padx=5, pady=2)
        self.none_steps_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.none_steps_label.grid(row=1, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.none_ave_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.none_ave_label.grid(row=1, column=2, padx=5, pady=2, sticky=tk.W+tk.E)
        self.none_expected_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.none_expected_label.grid(row=1, column=3, padx=5, pady=2, sticky=tk.W+tk.E)

        mtf_label = tk.Label(frame2, text="MTF List:", justify=tk.LEFT)
        mtf_label.grid(row=2, column=0, padx=5, pady=2)
        self.mtf_steps_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.mtf_steps_label.grid(row=2, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.mtf_ave_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.mtf_ave_label.grid(row=2, column=2, padx=5, pady=2, sticky=tk.W+tk.E)
        self.mtf_expected_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.mtf_expected_label.grid(row=2, column=3, padx=5, pady=2, sticky=tk.W+tk.E)

        swap_label = tk.Label(frame2, text="Swap List:", justify=tk.LEFT)
        swap_label.grid(row=3, column=0, padx=5, pady=2)
        self.swap_steps_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.swap_steps_label.grid(row=3, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.swap_ave_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.swap_ave_label.grid(row=3, column=2, padx=5, pady=2, sticky=tk.W+tk.E)
        self.swap_expected_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.swap_expected_label.grid(row=3, column=3, padx=5, pady=2, sticky=tk.W+tk.E)

        count_label = tk.Label(frame2, text="Count List:", justify=tk.LEFT)
        count_label.grid(row=4, column=0, padx=5, pady=2)
        self.count_steps_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.count_steps_label.grid(row=4, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.count_ave_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.count_ave_label.grid(row=4, column=2, padx=5, pady=2, sticky=tk.W+tk.E)
        self.count_expected_label = tk.Label(frame2, borderwidth=2, relief="groove", justify=tk.RIGHT)
        self.count_expected_label.grid(row=4, column=3, padx=5, pady=2, sticky=tk.W+tk.E)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def go(self):
        """Prepare the lists and run the searches."""
        self.none_steps_label["text"] = ""
        self.none_ave_label["text"] = ""
        self.none_expected_label["text"] = ""
        self.mtf_steps_label["text"] = ""
        self.mtf_ave_label["text"] = ""
        self.mtf_expected_label["text"] = ""
        self.swap_steps_label["text"] = ""
        self.swap_ave_label["text"] = ""
        self.swap_expected_label["text"] = ""
        self.count_steps_label["text"] = ""
        self.count_ave_label["text"] = ""
        self.count_expected_label["text"] = ""

        # Build the probabilities.
        num_values = int(self.num_values_entry.get())
        if self.prob_type.get() == 0:
            probs = equal_probs(num_values)
        elif self.prob_type.get() == 1:
            probs = linear_probs(num_values)
        else:
            probs = quadratic_probs(num_values)
        assert abs(sum(probs) - 1) < 0.001, "Probabilities do not add up to 1.0"

        # Build the lists.
        none_list = OrganizingList()
        mtf_list = MtfList()
        swap_list = SwapList()
        count_list = CountList()
        for i in range(num_values - 1, -1, -1):
            none_list.add(i)
            mtf_list.add(i)
            swap_list.add(i)
            count_list.add(i)

        # Perform the searches.
        none_steps = 0
        mtf_steps = 0
        swap_steps = 0
        count_steps = 0
        num_searches = int(self.num_searches_entry.get())
        for i in range(num_searches):
            value = pick_value(num_values, probs)
            none_steps += none_list.find(value)
            mtf_steps += mtf_list.find(value)
            swap_steps += swap_list.find(value)
            count_steps += count_list.find(value)

        # Display the results.
        self.none_steps_label["text"] = f"{none_steps}"
        self.none_ave_label["text"] = f"{none_steps / num_searches:.2f}"
        self.none_expected_label["text"] = f"{none_list.expected_search(probs):.2f}"

        self.mtf_steps_label["text"] = f"{mtf_steps}"
        self.mtf_ave_label["text"] = f"{mtf_steps / num_searches:.2f}"
        self.mtf_expected_label["text"] = f"{mtf_list.expected_search(probs):.2f}"

        self.swap_steps_label["text"] = f"{swap_steps}"
        self.swap_ave_label["text"] = f"{swap_steps / num_searches:.2f}"
        self.swap_expected_label["text"] = f"{swap_list.expected_search(probs):.2f}"

        self.count_steps_label["text"] = f"{count_steps}"
        self.count_ave_label["text"] = f"{count_steps / num_searches:.2f}"
        self.count_expected_label["text"] = f"{count_list.expected_search(probs):.2f}"


def equal_probs(num_values):
    """Make an array of equal probabilities."""
    prob = 1.0 / num_values
    probs = [prob for i in range(num_values)]
    return probs

def linear_probs(num_values):
    """Make an array containing linearly increasing probabilities."""
    total = num_values * (num_values - 1) / 2.0
    probs = [i / total for i in range(num_values)]
    return probs

def quadratic_probs(num_values):
    """Make an array containing quadratically increasing probabilities."""
    total = (num_values - 1) * num_values * (2 * (num_values - 1) + 1) / 6.0
    probs = [i * i / total for i in range(num_values)]
    return probs

def pick_value(num_values, probs):
    """Pick a value with the given probabilities."""
    prob = random.random()
    for i in range(num_values):
        prob -= probs[i]
        if prob <= 0:
            return i
    assert false, "Error picking a random value."

if __name__ == '__main__':
    app = App()

# app.root.destroy()
