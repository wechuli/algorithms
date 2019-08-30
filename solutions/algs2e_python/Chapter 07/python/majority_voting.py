import tkinter as tk


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("majority_voting")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("275x320")

        frame1 = tk.Frame(self.window)
        frame1.pack(side=tk.TOP, fill=tk.X)
        label = tk.Label(frame1, text="Outcomes:")
        label.pack(side=tk.LEFT)
        self.outcomes_entry = tk.Entry(frame1, width=8)
        self.outcomes_entry.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=1)
        self.outcomes_entry.insert(tk.END, "A B B A B B C C C B B")

        self.find_button = tk.Button(self.window, width=12, text="Find Majority", command=self.find_majority_click)
        self.find_button.pack(padx=5, pady=5, side=tk.TOP)

        self.steps_list = tk.Listbox(self.window)
        self.steps_list.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=1)

        frame2 = tk.Frame(self.window)
        frame2.pack(side=tk.TOP)
        label = tk.Label(frame2, text="Majority:")
        label.pack(side=tk.LEFT)
        self.majority_entry = tk.Entry(frame2, width=8)
        self.majority_entry.pack(padx=5, pady=5, side=tk.LEFT)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.find_button: self.find_button.invoke()))

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def find_majority_click(self):
        """ Find the majority outcome."""
        self.steps_list.delete(0, tk.END)

        # Break the outcome list into elements.
        outcomes = self.outcomes_entry.get().split()

        # Perform the Boyer-Moore algorithm.
        majority = ""
        counter = 0
        for outcome in outcomes:
            if counter == 0:
                majority = outcome
                counter = 1
            elif outcome == majority:
                counter += 1
            else:
                counter -= 1

            # Display the current step.
            self.steps_list.insert(tk.END, f"{outcome}: {majority} {counter}")

        # Display the result.
        self.majority_entry.delete(0, tk.END)
        self.majority_entry.insert(0, majority)


if __name__ == '__main__':
    app = App()

# app.root.destroy()

