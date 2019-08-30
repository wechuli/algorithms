import random
import tkinter as tk
import math


def make_sieve(max_number):
    """ Make a Sieve of Eratosthenes."""
    is_composite = [False for i in range(max_number + 1)]

    # "Cross out" multiples of 2.
    for i in range(4, max_number + 1, 2):
        is_composite[i] = True

    # "Cross out" multiples of primes found so far.
    next_prime = 3
    stop_at = math.sqrt(max_number)
    while next_prime <= stop_at:
        # "Cross out" multiples of this prime.
        for i in range(next_prime * 2, max_number + 1, next_prime):
            is_composite[i] = True

        # Move to the next prime.
        next_prime += 2
        while ((next_prime <= max_number) and (is_composite[next_prime])):
            next_prime += 2

    return is_composite

def is_carmichael(number):
    """ Return true if the number is a Carmichael number."""
    # Check all possible witnesses.
    for i in range(2, number):
        # Only check numbers with GCD(number, 1) = 1.
        if gcd(number, i) == 1:
            # Calculate: i ^ (number-1) mod number.
            result = pow(i, number - 1, number)

            # If we found a Fermat witness,
            # then this is not a Carmichael number.
            if result != 1:
                return False

    # They're all a bunch of liars!
    # This is a Carmichael number.
    return True

def gcd(a, b):
    """ Find GCD(a, b)."""
    # GCD(a, b) = GCD(b, a mod b).
    while (b != 0):
        # Calculate the remainder.
        remainder = a % b

        # Calculate GCD(b, remainder).
        a = b
        b = remainder

    # GCD(a, 0) is a.
    return a

def prime_factors(number):
    """ Return the number's factors."""
    factors = []

    # Pull out factors of 2.
    while number % 2 == 0:
        factors.Add(2)
        number //= 2

    # Check odd numbers up to Sqrt(number).
    max_factor = int(math.sqrt(number))
    test_factor = 3
    while (test_factor <= max_factor):
        while (number % test_factor == 0):
            factors.append(test_factor)
            number //= test_factor

        max_factor = int(math.sqrt(number))
        test_factor += 2

    # If there's anything left of the number, add it.
    if number > 1:
        factors.append(number)

    return factors

def ExponentiateMod(value, exponent, modulus):
    """ Perform the exponentiation."""
    result = 1
    factor = value
    while exponent != 0:
        if (exponent % 2 == 1):
            result = (result * factor) % modulus
        factor = (factor * factor) % modulus
        exponent /= 2

    return result


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("carmichael_numbers")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Maximim Number:")
        label.pack(padx=5, pady=5, side=tk.LEFT)
        self.max_number_entry = tk.Entry(frame, width=10, justify=tk.RIGHT)
        self.max_number_entry.pack(padx=5, pady=5, side=tk.LEFT)
        self.max_number_entry.insert(0, "10000")
        go_button = tk.Button(frame, text="Go", width=10, command=self.go)
        go_button.pack(padx=5, pady=5, side=tk.LEFT)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numbers_listbox = tk.Listbox(frame)
        self.numbers_listbox.pack(padx=5, pady=2, side=tk.TOP, fill=tk.BOTH, expand=True)
        self.numbers_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.numbers_listbox.yview)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP)
        label = tk.Label(frame, text="Count:")
        label.pack(padx=5, pady=5, side=tk.LEFT)
        self.count_label = tk.Label(frame)
        self.count_label.pack(padx=5, pady=5, side=tk.LEFT)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.max_number_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def go(self):
        """ Generate Carmichael numbers."""
        self.window.config(cursor="wait")
        self.window.update()
        self.numbers_listbox.delete(0, tk.END)

        # Get the number of numbers to check.
        max_number = int(self.max_number_entry.get())

        # Make a Sieve of Eratosthenes.
        is_composite = make_sieve(max_number)

        # Check for Carmichael numbers.
        for i in range(3, max_number, 2):
            # Only check non-primes.
            if is_composite[i]:
                # See if i is a Carmichael number.
                if is_carmichael(i):
                    txt = f"{i} = "
                    factors = prime_factors(i)
                    for factor in factors:
                        txt += f"{factor} x "
                    txt = txt[:-3]
                    self.numbers_listbox.insert(tk.END, txt)

        self.count_label["text"] = f"{self.numbers_listbox.size()} Carmichael numbers"
        self.window.config(cursor="")


if __name__ == '__main__':
    app = App()
