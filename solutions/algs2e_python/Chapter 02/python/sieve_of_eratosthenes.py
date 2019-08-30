import random
import tkinter as tk
import math



class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("sieve_of_eratosthenes")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Maximum Number:")
        label.pack(padx=5, pady=2, side=tk.LEFT)
        self.max_number_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.max_number_entry.pack(padx=5, pady=2, side=tk.LEFT)
        self.max_number_entry.insert(0, "10000")
        find_primes_button = tk.Button(frame, text="Find Primes", width=10, command=self.do_find_primes)
        find_primes_button.pack(padx=5, pady=2, side=tk.LEFT)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numbers_listbox = tk.Listbox(frame)
        self.numbers_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.numbers_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.numbers_listbox.yview)

        self.count_label = tk.Label(self.window)
        self.count_label.pack(padx=5, pady=2, side=tk.TOP)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=find_primes_button: find_primes_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.max_number_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def do_find_primes(self):
        """ Find prime numbers."""
        self.numbers_listbox.delete(0, tk.END)
        self.count_label["text"] = ""

        # Get the primes.
        max_number = int(self.max_number_entry.get())
        primes = self.find_primes(max_number)

        # Display the results.
        for prime in primes:
            self.numbers_listbox.insert(tk.END, f"{prime}")
        self.count_label["text"] = f"{len(primes)} primes"

    def find_primes(self, max_number):
        """ Find the primes between 2 and max_number (inclusive)."""
        # Allocate an array for the numbers.
        is_composite = [False for i in range(max_number + 1)]
	
        # "Cross out" multiples of 2.
        for i in range(4, max_number + 1, 2):
            is_composite[i] = True

        # "Cross out" multiples of primes found so far.
        next_prime = 3
        stop_at = int(math.sqrt(max_number))
        while next_prime <= stop_at:
            # "Cross out" multiples of this prime.
            for i in range(next_prime * 2, max_number + 1, next_prime):
                is_composite[i] = True

            # Move to the next prime.
            next_prime += 2
            while (next_prime <= max_number) and (is_composite[next_prime]):
                next_prime += 2

        # Copy the primes into a List<long>.
        primes = []
        for i in range(2, max_number + 1):
            if not is_composite[i]:
                primes.append(i)

        # Return the primes.
        return primes


if __name__ == '__main__':
    app = App()
