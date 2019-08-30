import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import itertools


def is_match(from_state, on_input, new_state, is_accepting, input):
    """ Return true if the state transitions match the input."""
    num_transitions = len(from_state)

    # Begin in the start state 0.
    state = 0

    # Process the input.
    for ch in input:
        # Find the appropriate transition.
        found_transition = False
        for i in range(num_transitions):
            if (from_state[i] == state) and (on_input[i] == ch):
                # This is the correct transition. Apply it.
                state = new_state[i]

                # Process the next input character.
                found_transition = True
                break

        # If we didn't find the transition, do not accept.
        if not found_transition:
            return False

    # See if we finished in an accepting state.
    return is_accepting[state]


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("dfa_match")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("270x220")

        label = tk.Label(self.window, text="State transitions:")
        label.pack(padx=5, pady=5, anchor=tk.W)
        self.transitions_text = tk.Text(self.window, width=1, height=5)
        self.transitions_text.pack(padx=5, pady=5, anchor=tk.W, fill=tk.X)
        transitions = "0\tA\t1\tNo\n1\tA\t2\tNo\n1\tB	1\tNo\n2\t-\t-1\tYes"
        self.transitions_text.insert(tk.END, transitions)

        frame = tk.Frame(self.window)
        frame.pack(anchor=tk.W, fill=tk.X)
        label = tk.Label(frame, text="Input:")
        label.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W)
        self.input_entry = tk.Entry(frame, justify=tk.LEFT)
        self.input_entry.pack(side=tk.LEFT, padx=5, pady=5, anchor=tk.W, fill=tk.X, expand=True)
        self.input_entry.insert(tk.END, "ABBA")

        evaluate_button = tk.Button(self.window, text="Evaluate", width=8, command=self.evaluate)
        evaluate_button.pack(padx=5, pady=5)

        self.result_entry = tk.Entry(self.window, justify=tk.LEFT)
        self.result_entry.pack(padx=5, pady=5, anchor=tk.W, fill=tk.X, expand=True)

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def evaluate(self):
        """ See if the expression matches."""
        self.result_entry.delete(0, tk.END)
        # Load the state transitions.
        from_state = []
        on_input = []
        new_state = []
        is_accepting = {}

        # Get the state transitions.
        all_text = self.transitions_text.get("1.0",'end-1c')
        lines = all_text.split("\n")
        for line in lines:
            if len(line) > 0:
                fields = line.split("\t")
                state = int(fields[0])
                from_state.append(state)
                on_input.append(fields[1])
                new_state.append(int(fields[2]))

                # If we don't know yet whether this state
                # is accepting, save that value now.
                if not state in is_accepting.keys():
                    is_accepting[state] = (fields[3].upper() == "YES")
            num_transitions = len(from_state)

        # Process the input.
        text = self.input_entry.get()
        if is_match(from_state, on_input, new_state, is_accepting, text):
            self.result_entry.insert(0, "Accepting")
        else:
            self.result_entry.insert(0, "Not accepting")


if __name__ == '__main__':
    app = App()

# app.root.destroy()
