import random
import tkinter as tk
import math

def find_probable_prime(lower_bound, upper_bound, num_trials):
    """ Pick a number that is probably prime between the given bounds."""
    num_tests = 0
    while True:
        num_tests += 1
        number = random.randint(lower_bound, upper_bound)
        if is_prime_fermat(number, num_trials):
            return num_tests, number

def is_prime_fermat(number, num_trials):
    """ Use Fermat's little theorem to see if the number is probably prime."""
    for trial in range(num_trials):
        # Pick a random test number.
        test = random.randint(2, number)

        # Make sure it is relatively prime with number.
        while gcd(test, number) != 1:
            test = random.randint(2, number)

        # Calculate: test ^ (number - 1) mod number.
        result = exponentiate_mod(test, number - 1, number)

        # If this is not -1, then the number is not prime.
        if result != 1:
            return False

    # If we made it this far, the number is probably prime.
    return True

def exponentiate_mod(value, exponent, modulus):
    """ Perform the exponentiation."""
    result = 1
    factor = value
    while exponent != 0:
        if exponent % 2 == 1:
            result = (result * factor) % modulus
        factor = (factor * factor) % modulus
        exponent //= 2
    return result

def gcd(a, b):
    """ Find GCD(a, b)."""
    # GCD(a, b) = GCD(b, a mod b).
    while b != 0:
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
        factors.append(2)
        number //= 2

    # Check odd numbers up to Sqrt(number).
    max_factor = int(math.sqrt(number))
    test_factor = 3
    while test_factor <= max_factor:
        while number % test_factor == 0:
            factors.append(test_factor)
            number //= test_factor

        max_factor = int(math.sqrt(number))
        test_factor += 2

    # If there's anything left of the number, add it.
    if number > 1:
        factors.append(number)

    return factors


class App:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("prime_testing")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("400x120")

        frame = tk.Frame()
        frame.pack(side=tk.TOP, fill=tk.X)
        label = tk.Label(frame, text="Number:")
        label.pack(padx=5, pady=5, side=tk.LEFT)
        self.number_entry = tk.Entry(frame, justify=tk.RIGHT)
        self.number_entry.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=True)
        random_button = tk.Button(frame, text="Random", width=10, command=self.random)
        random_button.pack(padx=5, pady=5, side=tk.LEFT)
        find_prime_button = tk.Button(frame, text="Find Prime", width=10, command=self.find_prime)
        find_prime_button.pack(padx=5, pady=5, side=tk.LEFT)

        frame = tk.Frame()
        frame.pack(side=tk.TOP, fill=tk.X)
        is_prime_button = tk.Button(frame, text="Is Prime?", width=10, command=self.is_prime)
        is_prime_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.is_prime_entry = tk.Entry(frame, width=10, justify=tk.LEFT)
        self.is_prime_entry.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=True)

        frame = tk.Frame()
        frame.pack(side=tk.TOP, fill=tk.X)
        factor_button = tk.Button(frame, text="Factor", width=10, command=self.factor)
        factor_button.pack(padx=5, pady=5, side=tk.LEFT)
        self.factors_entry = tk.Entry(frame, width=10, justify=tk.LEFT)
        self.factors_entry.pack(padx=5, pady=5, side=tk.LEFT, fill=tk.X, expand=True)


        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=random_button: random_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.number_entry.focus_force()
        self.window.mainloop()

    def kill_callback(self):
        self.window.destroy()

    def random(self):
        """ Pick a random number."""
        number = random.randint(0, 1000000000)
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, f"{number}")
        self.is_prime_entry.delete(0, tk.END)
        self.factors_entry.delete(0, tk.END)

    def find_prime(self):
        """ Find a number that is probably prime."""
        # Find a probable prime.
        num_tests, number = find_probable_prime(100000000, 2000000000, 100)
        self.number_entry.delete(0, tk.END)
        self.number_entry.insert(0, f"{number}")
        self.is_prime_entry.delete(0, tk.END)
        self.is_prime_entry.insert(0, f"Found probable prime in {num_tests} attempts.")

        # Factor it.
        self.display_factors()

    def is_prime(self):
        """ See if this number is prime."""
        number = int(self.number_entry.get())
        self.is_prime_entry.delete(0, tk.END)
        if is_prime_fermat(number, 100):
            self.is_prime_entry.insert(0, "Probably prime.")
        else:
            self.is_prime_entry.insert(0, "Not prime.")

    def factor(self):
        """ Factor the number."""
        self.display_factors()

    def display_factors(self):
        # Get the factors.
        number = int(self.number_entry.get())
        factors = prime_factors(number)

        # Display the factors.
        result = "1"
        for factor in factors:
            result += f" x {factor}"
        self.factors_entry.delete(0, tk.END)
        self.factors_entry.insert(0, result)


if __name__ == '__main__':
    app = App()
