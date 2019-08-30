import tkinter as tk


class Planet:
    def __init__(self, name, distance_to_sun, mass, diameter):
        self.name = name
        self.distance_to_sun = distance_to_sun
        self.mass = mass
        self.diameter = diameter

        self.next_distance = None
        self.next_mass = None
        self.next_diameter = None


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        self.window = tk.Tk()
        self.window.title("planet_list")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("330x300")

        frame = tk.Frame(self.window)
        frame.pack(padx=5, pady=5, fill=tk.X)
        self.sort_choice = tk.IntVar()
        radiobutton = tk.Radiobutton(frame, text="Distance to Sun", variable=self.sort_choice, value=0, command=self.make_list)
        radiobutton.pack(padx=10, pady=2, side=tk.LEFT)
        radiobutton = tk.Radiobutton(frame, text="Mass", variable=self.sort_choice, value=1, command=self.make_list)
        radiobutton.pack(padx=10, pady=2, side=tk.LEFT)
        radiobutton = tk.Radiobutton(frame, text="Diameter", variable=self.sort_choice, value=2, command=self.make_list)
        radiobutton.pack(padx=10, pady=2, side=tk.LEFT)

        self.listbox = tk.Listbox(self.window)
        self.listbox.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)

        # Make the planet objects.
        planets = [
            Planet("Mercury", 0.39, 0.06, 0.382),
            Planet("Venus", 0.72, 0.82, 0.949),
            Planet("Earth", 1, 1, 1),
            Planet("Mars", 1.52, 0.11, 0.532),
            Planet("Jupiter", 5.20, 317.8, 11.209),
            Planet("Saturn", 9.54, 95.2, 9.449),
            Planet("Uranus", 19.22, 14.6, 4.007),
            Planet("Neptune", 30.06, 17.2, 3.883),
        ]

        # Create the threads.
        self.sentinel = Planet("<sentinel>", 0, 0, 0)
        for planet in planets:
            self.add_planet_to_list(self.sentinel, planet)

        # Display the first list.
        self.make_list()

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.window.focus_force()
        self.window.mainloop()

    def make_list(self):
        """ Display the planets ordered by the selected thread."""
        self.listbox.delete(0, tk.END)
        choice = self.sort_choice.get()

        if choice == 0:
            planet = self.sentinel.next_distance
            while planet != None:
                self.listbox.insert(tk.END, planet.name)
                planet = planet.next_distance
        elif choice == 1:
            planet = self.sentinel.next_mass
            while planet != None:
                self.listbox.insert(tk.END, planet.name)
                planet = planet.next_mass
        else:
            planet = self.sentinel.next_diameter
            while planet != None:
                self.listbox.insert(tk.END, planet.name)
                planet = planet.next_diameter

    def add_planet_to_list(self, sentinel, planet):
        """ Add a Planet to the linked list."""
        # Add the planet to the next_distance thread.
        after_me = sentinel
        while (after_me.next_distance != None) and \
              (after_me.next_distance.distance_to_sun < planet.distance_to_sun):
            after_me = after_me.next_distance
        planet.next_distance = after_me.next_distance
        after_me.next_distance = planet

        # Add the planet to the next_mass thread.
        after_me = sentinel
        while (after_me.next_mass != None) and \
              (after_me.next_mass.mass < planet.mass):
            after_me = after_me.next_mass
        planet.next_mass = after_me.next_mass
        after_me.next_mass = planet

        # Add the planet to the next_diameter thread.
        after_me = sentinel
        while (after_me.next_diameter != None) and \
              (after_me.next_diameter.diameter < planet.diameter):
            after_me = after_me.next_diameter
        planet.next_diameter = after_me.next_diameter
        after_me.next_diameter = planet


if __name__ == '__main__':
    app = App()

# app.root.destroy()
