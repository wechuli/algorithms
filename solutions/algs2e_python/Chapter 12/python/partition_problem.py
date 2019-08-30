import sys
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random
import math
import time


def set_text(entry, text):
    """ Set an Entry widget's text."""
    entry.delete(0, tk.END)
    entry.insert(tk.END, text)

class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.x0 = 0
        self.y0 = 0
        self.tree_links = []
        self.walls = []

        # Make the widgets.
        self.window = tk.Tk()
        self.window.title("partition_problem")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("445x450")
        self.window.rowconfigure(0, weight=1)

        # Weights area.
        frame1 = tk.LabelFrame(self.window, text="Weights")
        frame1.grid(padx=10, pady=5, row=0, column=0)
        self.weights_text = tk.Text(frame1, width=10)
        self.weights_text.pack(side=tk.LEFT, expand=True, fill=tk.BOTH)
        scrollbar = tk.Scrollbar(frame1, command=self.weights_text.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.weights_text.configure(yscrollcommand=scrollbar.set)

        # Random Weights area.
        frame2 = tk.LabelFrame(self.window, text="Random Weights")
        frame2.grid(padx=10, pady=5, row=0, column=1, sticky=tk.NSEW)
        label = tk.Label(frame2, text="# Weights:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_weights_entry = tk.Entry(frame2, width=8, justify=tk.RIGHT)
        self.num_weights_entry.grid(padx=5, pady=2, row=0, column=1, sticky=tk.W)
        self.num_weights_entry.insert(tk.END, "15")
        label = tk.Label(frame2, text="Between:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.min_entry = tk.Entry(frame2, width=8, justify=tk.RIGHT)
        self.min_entry.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        self.min_entry.insert(tk.END, "30")
        label = tk.Label(frame2, text="and")
        label.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        self.max_entry = tk.Entry(frame2, width=8, justify=tk.RIGHT)
        self.max_entry.grid(padx=5, pady=2, row=1, column=3, sticky=tk.W)
        self.max_entry.insert(tk.END, "50")
        build_button = tk.Button(frame2, text="Build", width=8, command=self.build)
        build_button.grid(padx=5, pady=5, row=2, column=0, columnspan=4)

        # Algorithms.
        frame3 = tk.LabelFrame(self.window, text="Algorithms")
        frame3.grid(padx=10, pady=(5, 10), row=1, column=0, columnspan=2, sticky=tk.NSEW)
        self.shortcircuit = BooleanVar()
        checkbox = tk.Checkbutton(frame3, text="Allow Short Circuit", variable=self.shortcircuit)
        checkbox.grid(padx=5, pady=2, row=0, column=0)
        label = tk.Label(frame3, text="Nodes Visited")
        label.grid(padx=5, pady=2, row=1, column=1, sticky=tk.W)
        label = tk.Label(frame3, text="Time (sec)")
        label.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        label = tk.Label(frame3, text="Difference")
        label.grid(padx=5, pady=2, row=1, column=3, sticky=tk.W)

        ex_button = tk.Button(frame3, text="Exhaustive", width=20, command=self.exhaustive_search)
        ex_button.grid(padx=5, pady=2, row=2, column=0)
        self.ex_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.ex_nodes_label.grid(padx=5, pady=2, row=2, column=1)
        self.ex_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.ex_time_label.grid(padx=5, pady=2, row=2, column=2)
        self.ex_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.ex_diff_label.grid(padx=5, pady=2, row=2, column=3)

        rnd_button = tk.Button(frame3, text="Random", width=20, command=self.random)
        rnd_button.grid(padx=5, pady=2, row=3, column=0)
        self.rnd_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.rnd_nodes_label.grid(padx=5, pady=2, row=3, column=1)
        self.rnd_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.rnd_time_label.grid(padx=5, pady=2, row=3, column=2)
        self.rnd_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.rnd_diff_label.grid(padx=5, pady=2, row=3, column=3)

        imp_button = tk.Button(frame3, text="Improvements", width=20, command=self.improvements)
        imp_button.grid(padx=5, pady=2, row=4, column=0)
        self.imp_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.imp_nodes_label.grid(padx=5, pady=2, row=4, column=1)
        self.imp_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.imp_time_label.grid(padx=5, pady=2, row=4, column=2)
        self.imp_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.imp_diff_label.grid(padx=5, pady=2, row=4, column=3)

        hill_button = tk.Button(frame3, text="Hill Climbing", width=20, command=self.hill_climbing)
        hill_button.grid(padx=5, pady=2, row=5, column=0)
        self.hill_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.hill_nodes_label.grid(padx=5, pady=2, row=5, column=1)
        self.hill_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.hill_time_label.grid(padx=5, pady=2, row=5, column=2)
        self.hill_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.hill_diff_label.grid(padx=5, pady=2, row=5, column=3)

        shill_button = tk.Button(frame3, text="Sorted Hill Climbing", width=20, command=self.sorted_hill_climbing)
        shill_button.grid(padx=5, pady=2, row=6, column=0)
        self.shill_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.shill_nodes_label.grid(padx=5, pady=2, row=6, column=1)
        self.shill_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.shill_time_label.grid(padx=5, pady=2, row=6, column=2)
        self.shill_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.shill_diff_label.grid(padx=5, pady=2, row=6, column=3)

        bb_button = tk.Button(frame3, text="Branch and Bound", width=20, command=self.branch_and_bound)
        bb_button.grid(padx=5, pady=2, row=7, column=0)
        self.bb_nodes_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.bb_nodes_label.grid(padx=5, pady=2, row=7, column=1)
        self.bb_time_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.bb_time_label.grid(padx=5, pady=2, row=7, column=2)
        self.bb_diff_label = tk.Label(frame3, width=10, borderwidth=2, relief=tk.SUNKEN, anchor=tk.E)
        self.bb_diff_label.grid(padx=5, pady=2, row=7, column=3)

        self.tree_size_label = tk.Label(frame3)
        self.tree_size_label.grid(padx=5, pady=2, row=8, column=0, sticky=tk.W)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=build_button: build_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def build(self):
        """ Generate weights."""
        # Get the parameters.
        min = int(self.min_entry.get())
        max = int(self.max_entry.get())
        num_weights = int(self.num_weights_entry.get())

        # Make the weights.
        txt = ""
        for i in range(num_weights):
            txt += f"\n{random.randint(min, max)}"
        txt = txt[1:]
        self.weights_text.delete(1.0, tk.END)
        self.weights_text.insert(tk.END, txt)

    """ Helper Routines """

    def read_weights(self):
        """ Load the weights before running an algorithm."""
        # Read the weights.
        txt = self.weights_text.get(1.0, END)
        weight_strings = txt.split("\n")

        # Reset the solution.
        self.weights = []
        for weight_string in weight_strings:
            try:
                self.weights.append(int(weight_string))
            except:
                continue
        self.num_weights = len(self.weights)

        self.best_assigned_to = [-1 for i in range(self.num_weights)]
        self.best_total_weight = [-1, -1]

        self.test_assigned_to = [-1 for i in range(self.num_weights)]
        self.test_total_weight = [-1, -1]

        self.tree_size_label["text"] = f"Tree size: {int(math.pow(2, self.num_weights + 1)):,} nodes"

    def clear_results(self, nodes_visited_label, time_label, difference_label):
        """ Blank the results for an algorithm."""
        # Reset the test and best solutions.
        self.reset_solutions()

        # Clear previous results.
        nodes_visited_label["text"] = ""
        time_label["text"] = ""
        difference_label["text"] = ""
        self.window.update()

    def report_results(self, nodes_visited_label, time_label, difference_label, elapsed_time):
        """ Report the results for an algorithm."""
        nodes_visited_label["text"] = f"{self.num_nodes_visited:,}"
        time_label["text"] = f"{elapsed_time:.4f}"
        difference = abs(self.best_total_weight[0] - self.best_total_weight[1])
        difference_label["text"] = f"{difference}"

        # Debugging: Display assignments.
        print("Assignments:")
        for i in range(self.num_weights):
            print(f"{self.best_assigned_to[i]}", end=" ")
        print()

        txt = ["", ""]
        for i in range(self.num_weights):
            txt[self.best_assigned_to[i]] += f" + {self.weights[i]}"
        if len(txt[0]) > 0:
            txt[0] = txt[0][3:]
        if len(txt[1]) > 0:
            txt[1] = txt[1][3:]
        print(f"Weights(0): {txt[0]} = {self.best_total_weight[0]}")
        print(f"Weights(1): {txt[1]} = {self.best_total_weight[1]}")
        print()

    def reset_solutions(self):
        """ Reset the best and test solutions."""
        # Reset assigned_to weights.
        for i in range(self.num_weights):
            self.best_assigned_to[i] = -1
            self.test_assigned_to[i] = -1

        # Reset totals.
        self.best_total_weight[0] = 0
        self.best_total_weight[1] = 0
        self.test_total_weight[0] = 0
        self.test_total_weight[1] = 0

        # Reset difference and nodes visited.
        self.best_difference = 1000000000
        self.num_nodes_visited = 0

    def check_for_improvement(self):
        """ If the test solution is an improvement, update the best solution."""
        test_difference = abs(self.test_total_weight[0] - self.test_total_weight[1])
        if self.best_difference > test_difference:
            # This is an improvement, Save it.
            self.best_difference = test_difference
            for i in range(self.num_weights):
                self.best_assigned_to[i] = self.test_assigned_to[i]
            self.best_total_weight[0] = self.test_total_weight[0]
            self.best_total_weight[1] = self.test_total_weight[1]

    def short_circuit(self):
        """ Return True if we have an optimal solution."""
        # Return true if:
        #   - We are allowed to short-circuit.
        #   - We have assigned weights.
        #   - The totals are equal.
        return (self.shortcircuit.get() and
            (self.best_total_weight[0] > 0) and
            (self.best_total_weight[0] == self.best_total_weight[1]))

    """ End Helper Routines """

    """ Exhaustive Search """

    def exhaustive_search(self):
        # Get ready to run the algorithm.
        self.read_weights()
        if self.num_weights > 20:
            num_nodes = Math.Pow(2, self.num_weights + 1) - 2
            if not messagebox.askyesno("Continue?", f"Warning: This tree contains {num_nodes} nodes.\n\nDo you want to continue?"):
                return

        self.clear_results(self.ex_nodes_label, self.ex_time_label, self.ex_diff_label)
        start_time = time.time()

        # Run the algorithm.
        # Assign the first weight.
        self.exhaustive_assign_weight(0)

        elapsed_time = time.time() - start_time
        self.report_results(self.ex_nodes_label, self.ex_time_label, self.ex_diff_label, elapsed_time)

    def exhaustive_assign_weight(self, next_index):
        """ Assign weight number next_index and then recursively assign the other weights."""
        # Short-circuit.
        if self.short_circuit():
            return

        self.num_nodes_visited += 1

        # See if we have assigned all weights.
        if next_index >= self.num_weights:
            # We have assigned all weights.
            # See if the test solution is an improvement.
            self.check_for_improvement()
        else:
            # We have not assigned all weights.

            # Assign the weight to group 0.
            self.test_assigned_to[next_index] = 0
            self.test_total_weight[0] += self.weights[next_index]
            self.exhaustive_assign_weight(next_index + 1)  # Recurse.
            self.test_total_weight[0] -= self.weights[next_index]

            # Assign the weight to group 1.
            self.test_assigned_to[next_index] = 1
            self.test_total_weight[1] += self.weights[next_index]
            self.exhaustive_assign_weight(next_index + 1)  # Recurse.
            self.test_total_weight[1] -= self.weights[next_index]

    """ End Exhaustive Search """

    """ Random Search """

    def random(self):
        """ Perform random trials."""
        # Calculate the number of trials.
        num_trials = int(3 * math.pow(self.num_weights, 3))

        # Get ready to run the algorithm.
        self.read_weights()
        self.clear_results(self.rnd_nodes_label, self.rnd_time_label, self.rnd_diff_label)

        start_time = time.time()

        # Perform the trials.
        for trial in range(num_trials):
            self.num_nodes_visited += self.num_weights

            # Reset the test totals.
            self.test_total_weight[0] = 0
            self.test_total_weight[1] = 0

            # Make random assignments.
            for i in range(self.num_weights):
                # Pick the group.
                group = random.randint(0, 1)

                # Assign the weight.
                self.test_assigned_to[i] = group
                self.test_total_weight[group] += self.weights[i]

            # See if the test solution is an improvement.
            self.check_for_improvement()

            # Short-circuit.
            if self.short_circuit():
                break

        elapsed_time = time.time() - start_time
        self.report_results(self.rnd_nodes_label, self.rnd_time_label, self.rnd_diff_label, elapsed_time)

    """ End Random Search """

    """ Random Improvements """

    def improvements(self):
        """ Make random trials with improvements."""
        # Get the number of trials.
        num_trials = int(math.pow(self.num_weights, 3))

        # Get ready to run the algorithm.
        self.read_weights()
        self.clear_results(self.imp_nodes_label, self.imp_time_label, self.imp_diff_label)
        start_time = time.time()

        # Perform the trials.
        for trial in range(1, num_trials + 1):
            self.num_nodes_visited += self.num_weights

            # Reset the test totals.
            self.test_total_weight[0] = 0
            self.test_total_weight[1] = 0

            # Make random assignments.
            for i in range(self.num_weights):
                # Pick the group.
                group = random.randint(0, 1)

                # Assign the weight.
                self.test_assigned_to[i] = group
                self.test_total_weight[group] += self.weights[i]

            # Get the current difference.
            test_difference = abs(self.test_total_weight[0] - self.test_total_weight[1])

            # Try to make improvements.
            num_without_improvement = 0
            while num_without_improvement < self.num_weights:
                # Pick a random weight to move.
                i = random.randint(0, self.num_weights - 1)
                group = self.test_assigned_to[i]
                new_difference = abs(
                    (self.test_total_weight[group] - self.weights[i]) -
                    (self.test_total_weight[1 - group] + self.weights[i]))
                if test_difference > new_difference:
                    test_difference = new_difference
                    self.test_total_weight[group] -= self.weights[i]
                    self.test_total_weight[1 - group] += self.weights[i]
                    self.test_assigned_to[i] = 1 - group
                    num_without_improvement = 0
                else:
                    num_without_improvement += 1

                self.num_nodes_visited += 1

            # See if the improved test solution is an improvement.
            self.check_for_improvement()

            # Short-circuit.
            if self.short_circuit():
                break

        elapsed_time = time.time() - start_time
        self.report_results(self.imp_nodes_label, self.imp_time_label, self.imp_diff_label, elapsed_time)

    """ End Random Improvements """

    """ Hill Climbing """

    def hill_climbing(self):
        """ Add weights to the group with the smaller current total."""
        # Get ready to run the algorithm.
        self.read_weights()
        self.clear_results(self.hill_nodes_label, self.hill_time_label, self.hill_diff_label)
        start_time = time.time()

        # Make the assignments.
        for i in range(self.num_weights):
            # See which group has the smaller total.
            group = 1
            if self.best_total_weight[0] < self.best_total_weight[1]:
                group = 0

            self.best_assigned_to[i] = group
            self.best_total_weight[group] += self.weights[i]

        self.best_difference = abs(self.best_total_weight[0] - self.best_total_weight[1])
        self.num_nodes_visited = self.num_weights

        elapsed_time = time.time() - start_time
        self.report_results(self.hill_nodes_label, self.hill_time_label, self.hill_diff_label, elapsed_time)

    """ End Hill Climbing """

    """ Sorted Hill Climbing """

    def sorted_hill_climbing(self):
        """
        Sort the weights and then add them in order of decreasing
        weight to the group with the smaller current total.
        """
        # Get ready to run the algorithm.
        self.read_weights()
        self.clear_results(self.shill_nodes_label, self.shill_time_label, self.shill_diff_label)
        start_time = time.time()

        # Sort the weights in descending order.
        self.weights.sort(reverse=True)

        # Make the assignments.
        for i in range(0, self.num_weights):
            # See which group has the smaller total.
            group = 1
            if self.best_total_weight[0] < self.best_total_weight[1]:
                group = 0

            self.best_assigned_to[i] = group
            self.best_total_weight[group] += self.weights[i]

        """ @
        # Sort the weights.
        self.weights.sort()

        # Make the assignments.
        for i in range(self.num_weights - 1, -1, -1):
            # See which group has the smaller total.
            group = 1
            if self.best_total_weight[0] < self.best_total_weight[1]:
                group = 0

            self.best_assigned_to[i] = group
            self.best_total_weight[group] += self.weights[i]
        @ """

        self.best_difference = abs(self.best_total_weight[0] - self.best_total_weight[1])
        self.num_ndes_visited = self.num_weights

        elapsed_time = time.time() - start_time
        self.report_results(self.shill_nodes_label, self.shill_time_label, self.shill_diff_label, elapsed_time)

    """ End Sorted Hill Climbing """

    """ Branch and Bound """

    def branch_and_bound(self):
        """ Branch and bound."""
        # Get ready to run the algorithm.
        self.read_weights()
        if self.num_weights > 20:
            num_nodes = math.pow(2, self.num_weights + 1) - 2
            if not messagebox.askyesno("Continue?", f"Warning: This tree contains {num_nodes} nodes.\n\nDo you want to continue?"):
                return

        self.clear_results(self.bb_nodes_label, self.bb_time_label, self.bb_diff_label)
        start_time = time.time()

        # Calculate the total weight available.
        total_weight = sum(self.weights)

        # Assign the first weight.
        self.branch_and_bound_assign_weight(0, total_weight)

        elapsed_time = time.time() - start_time
        self.report_results(self.bb_nodes_label, self.bb_time_label, self.bb_diff_label, elapsed_time)

    def branch_and_bound_assign_weight(self, next_index, total_unassigned):
        """
        Assign weight number next_index and
        then recursively assign the other weights.
        Use branch and bound.
        """
        # Short-circuit.
        if self.short_circuit():
            return

        self.num_nodes_visited += 1

        # See if we have assigned all weights.
        if next_index >= self.num_weights:
            # We have assigned all weights.
            # If we get here, this *is* an improvement.
            self.check_for_improvement()
        else:
            # We have not assigned all weights.

            # See if we can improve on the best solution.
            # If the current difference is so big that
            # all of the remaining weights cannot reduce
            # it below the best difference, then there#s no hope.
            test_difference = abs(self.test_total_weight[0] - self.test_total_weight[1])
            if test_difference - total_unassigned > self.best_difference:
                return

            total_unassigned -= self.weights[next_index]

            # Assign the weight to group 0.
            self.test_assigned_to[next_index] = 0
            self.test_total_weight[0] += self.weights[next_index]
            self.branch_and_bound_assign_weight(next_index + 1, total_unassigned)  # Recurse.
            self.test_total_weight[0] -= self.weights[next_index]

            # Assign the weight to group 1.
            self.test_assigned_to[next_index] = 1
            self.test_total_weight[1] += self.weights[next_index]
            self.branch_and_bound_assign_weight(next_index + 1, total_unassigned)  # Recurse.
            self.test_total_weight[1] -= self.weights[next_index]

    """ End Branch and Bound """


if __name__ == '__main__':
    app = App()

# app.root.destroy()

