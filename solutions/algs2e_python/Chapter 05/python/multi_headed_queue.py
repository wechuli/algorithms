import tkinter as tk
import random


class Customer:
    def __init__(self, id, create_time):
       self.id = id
       self.create_time = create_time
       self.finished_time = -1


class App:
    """The tkinter GUI interface."""
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # Set up tkinter.
        self.window = tk.Tk()
        self.window.title("multi_headed_queue")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        frame = tk.LabelFrame(self.window, text="Parameters", padx=5, pady=5)
        frame.pack(side=tk.TOP)

        label = tk.Label(frame, text="# Tellers:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.num_tellers_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.num_tellers_entry.grid(padx=5, pady=2, row=0, column=1)
        self.num_tellers_entry.insert(0, "2")

        label = tk.Label(frame, text="Arrivals:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.min_arrival_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.min_arrival_entry.grid(padx=5, pady=2, row=1, column=1)
        self.min_arrival_entry.insert(0, "1")
        label = tk.Label(frame, text="to")
        label.grid(padx=5, pady=2, row=1, column=2, sticky=tk.W)
        self.max_arrival_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.max_arrival_entry.grid(padx=5, pady=2, row=1, column=3)
        self.max_arrival_entry.insert(0, "3")
        label = tk.Label(frame, text="minutes")
        label.grid(padx=5, pady=2, row=1, column=4, sticky=tk.W)

        label = tk.Label(frame, text="Duration:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.min_duration_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.min_duration_entry.grid(padx=5, pady=2, row=2, column=1)
        self.min_duration_entry.insert(0, "2")
        label = tk.Label(frame, text="to")
        label.grid(padx=5, pady=2, row=2, column=2, sticky=tk.W)
        self.max_duration_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.max_duration_entry.grid(padx=5, pady=2, row=2, column=3)
        self.max_duration_entry.insert(0, "7")
        label = tk.Label(frame, text="minutes")
        label.grid(padx=5, pady=2, row=2, column=4, sticky=tk.W)

        label = tk.Label(frame, text="Speed:")
        label.grid(padx=5, pady=2, row=3, column=0, sticky=tk.W)
        self.steps_per_second_entry = tk.Entry(frame, width=4, justify=tk.RIGHT)
        self.steps_per_second_entry.grid(padx=5, pady=2, row=3, column=1)
        self.steps_per_second_entry.insert(0, "5")
        label = tk.Label(frame, text="steps per second")
        label.grid(padx=5, pady=2, row=3, column=2, columnspan=3, sticky=tk.W)

        self.start_button = tk.Button(self.window, width=10, text="Start", command=self.start)
        self.start_button.pack(padx=5, pady=4, side=tk.TOP)

        frame = tk.Frame(self.window)
        frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
        frame.rowconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)

        label = tk.Label(frame, text="Queue:")
        label.grid(padx=5, pady=2, row=0, column=0, sticky=tk.W)
        self.queue_text = tk.Text(frame)
        self.queue_text.config(state=tk.NORMAL)
        self.queue_text.grid(padx=5, pady=5, row=0, column=1, sticky=tk.NSEW)

        label = tk.Label(frame, text="Tellers:")
        label.grid(padx=5, pady=2, row=1, column=0, sticky=tk.W)
        self.tellers_entry = tk.Entry(frame)
        self.tellers_entry.grid(padx=5, pady=5, row=1, column=1, sticky=tk.NSEW)

        label = tk.Label(frame, text="Time:")
        label.grid(padx=5, pady=2, row=2, column=0, sticky=tk.W)
        self.time_entry = tk.Entry(frame, width=20)
        self.time_entry.grid(padx=5, pady=2, row=2, column=1, sticky=tk.W)

        label = tk.Label(frame, text="Wait:")
        label.grid(padx=5, pady=2, row=3, column=0, sticky=tk.W)
        self.average_wait_entry = tk.Entry(frame, width=20)
        self.average_wait_entry.grid(padx=5, pady=(2, 10), row=3, column=1, sticky=tk.W)

        # Display the items.
        self.time = 0
        self.num_served = 0
        self.teller_serving = []
        self.customer_queue = []
        self.show_customers()

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=self.start_button: self.start_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.num_tellers_entry.focus_force()
        self.window.mainloop()

    def start(self):
        """ Start or stop the simulation."""
        if self.start_button["text"] == "Start":
            self.start_simulation()
        else:
            self.stop_simulation()

    def start_simulation(self):
        """ Start the simulation."""
        self.num_tellers = int(self.num_tellers_entry.get())
        self.min_arrival = int(self.min_arrival_entry.get())
        self.max_arrival = int(self.max_arrival_entry.get())
        self.min_duration = int(self.min_duration_entry.get())
        self.max_duration = int(self.max_duration_entry.get())

        self.teller_serving = [None for customer in range(self.num_tellers)]
        self.customer_queue = []

        self.num_served = 0
        self.total_wait_time = 0
        self.next_id = 1

        self.time = 0
        self.next_arrival_time = 1

        # Display the current situation.
        self.show_customers()

        # Start the simulation timer.
        self.start_button["text"] = "Stop"
        self.delay = int(1000 / int(self.steps_per_second_entry.get()))
        self.window.after(self.delay, self.tick)

    def tick(self):
        """ A minute has passed."""
        self.time += 1

        # See if we need to create a new customer.
        if self.next_arrival_time <= self.time:
            # Create a customer.
            customer = Customer(self.next_id, self.time)
            self.next_id += 1

            # Add the customer to the queue.
            self.customer_queue.append(customer)

            # See when to add the next customer.
            self.next_arrival_time = self.time + random.randint(self.min_arrival, self.min_arrival)

        # Process the tellers.
        for i in range(self.num_tellers):
            # If this teller is serving someone, see if that customer is done.
            if (self.teller_serving[i] != None) and (self.teller_serving[i].finished_time <= self.time):
                self.teller_serving[i] = None

            # If this teller is available, move a customer here.
            if (self.teller_serving[i] == None) and (len(self.customer_queue) > 0):
                # This teller isn't busy. Move a customer here.
                customer = self.customer_queue.pop(0)    # Dequeue the customer
                self.teller_serving[i] = customer

                # Set the customer's finish time.
                customer.finished_time = self.time + random.randint(self.min_duration, self.max_duration)

                # Record the customer's wait time.
                self.total_wait_time += self.time - customer.create_time
                self.num_served += 1

        # Display the new situation.
        self.show_customers()

        # Queue the next tick.
        if self.start_button["text"] == "Stop":
            self.window.after(self.delay, self.tick)

    def stop_simulation(self):
        """ Stop the simulation."""
        self.start_button["text"] = "Start"

    def show_customers(self):
        """ Show the current situation."""
        # Show the customers in the queue.
        txt = ""
        for customer in self.customer_queue:
            txt += f"{customer.id} "
        self.queue_text.delete(1.0, tk.END)
        self.queue_text.insert(1.0, txt)

        # Show the customers being served.
        txt = ""
        for customer in self.teller_serving:
            if customer == None:
                txt += "-- "
            else:
                txt += f"{customer.id} "
        self.tellers_entry.delete(0, tk.END)
        self.tellers_entry.insert(0, txt)

        # Show elapsed time.
        hours = self.time // 60
        mins = self.time - hours * 60
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, f"{hours:2d} hours, {mins:2d} mins")

        # Show the average wait time.
        self.average_wait_entry.delete(0, tk.END)
        if self.num_served > 0:
            elapsed = self.total_wait_time / self.num_served
            mins = int(elapsed)
            secs = (elapsed - mins) * 60
            self.average_wait_entry.insert(0, f"{mins} mins, {secs:.2f} secs")


if __name__ == '__main__':
    app = App()
