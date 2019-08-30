import tkinter as tk
from tkinter import ttk

class Rectangle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def right(self):
        return self.x + self.width

    def bottom(self):
        return self.y + self.height


class App:
    def kill_callback(self):
        self.window.destroy()

    def __init__(self):
        # The rectangle and skyline definitions.
        self.ground_y = 0
        self.rectangles = None
        self.skyline = None

        # Build the user interface.
        self.window = tk.Tk()
        self.window.title("skyline_divide_and_conquer")
        self.window.protocol("WM_DELETE_WINDOW", self.kill_callback)
        self.window.geometry("300x300")

        # Parameters.
        params_frame = tk.Frame(self.window)
        params_frame.pack(side=tk.TOP)

        num_rectangles_label = tk.Label(params_frame, text="# Rectangles:")
        num_rectangles_label.grid(row=0, column=0, padx=5, pady=2, sticky=tk.W)
        self.num_rectangles_entry = tk.Entry(params_frame, width=4, justify=tk.RIGHT)
        self.num_rectangles_entry.grid(row=0, column=1, padx=5, pady=2, sticky=tk.W+tk.E)
        self.num_rectangles_entry.insert(tk.END, "10")
        go_button = tk.Button(params_frame, text="Go", width=8, command=self.go)
        go_button.grid(row=0, column=2, padx=5, pady=5)

        # Drawing area.
        self.canvas = tk.Canvas(self.window, bg="white", borderwidth=2, relief=tk.SUNKEN)
        self.canvas.pack(padx=5, pady=5, side=tk.TOP, fill=tk.BOTH, expand=True)

        # Bind some keys.
        self.window.bind('<Return>', (lambda e, button=go_button: go_button.invoke())) 

        # Force focus so Alt+F4 closes this window and not the Python shell.
        self.canvas.focus_force()
        self.window.mainloop()

    def go(self):
        """ Make rectangles and build the skyline."""
        # Make the random rectangles.
        margin = 20
        num_rectangles = int(self.num_rectangles_entry.get())
        xmin = margin
        xmax = self.canvas.winfo_width() - margin
        self.ground_y = self.canvas.winfo_height() - margin
        min_width = 10
        max_width = max(20, (3 * xmax) // num_rectangles)
        min_height = 20
        max_height = 150
        self.rectangles = []

        for i in range(num_rectangles):
            width = random.randint(min_width, max_width)
            x = random.randint(xmin, xmax - width)
            height = random.randint(min_height, max_height)
            y = self.ground_y - height
            self.rectangles.append(Rectangle(x, y, width, height))

        # Make the skyline.
        self.skyline = self.make_skyline(self.rectangles, 0, len(self.rectangles) - 1)

        # Redraw.
        self.draw()

    def draw(self):
        """ Draw the rectangles and skyline."""
        self.canvas.delete(tk.ALL)
        if self.rectangles == None:
            return

        skyline_thickness = 7
        building_thickness = 3

        if self.skyline != None:
            # Convert the key points into a polyline.
            points = []
            skyline_len = len(self.skyline)
            points.append((self.skyline[0][0], self.skyline[skyline_len - 1][1]))
            points.append(self.skyline[0])
            for i in range(1, skyline_len):
                points.append((self.skyline[i][0], self.skyline[i - 1][1]))
                points.append(self.skyline[i])

            # Draw the skyline.
            self.canvas.create_line(points, fill="black", width=skyline_thickness)

            # Draw the rectangles.
            for rect in self.rectangles:
                self.canvas.create_rectangle( \
                    rect.x, rect.y, rect.right(), rect.bottom(),
                    outline="lightgreen", width=building_thickness)

        # Draw the ground.
        x1 = self.canvas.winfo_width()
        y1 = self.canvas.winfo_height()
        self.canvas.create_rectangle( \
            0, self.ground_y, x1, y1, fill="sandybrown")

    def make_skyline(self, rectangles, mini, maxi):
        """ Make the skyline points."""
        # See if we need to process a single rectangle.
        if mini == maxi:
            result = []
            result.append((rectangles[mini].x, rectangles[mini].y))
            result.append((rectangles[mini].right(), rectangles[mini].bottom()))
            return result

        # Process the two halves.
        midi = (mini + maxi) // 2
        skyline1 = self.make_skyline(rectangles, mini, midi)
        skyline2 = self.make_skyline(rectangles, midi + 1, maxi)

        # Merge and return the result.
        return self.merge_skylines(skyline1, skyline2)

    def merge_skylines(self, skyline1, skyline2):
        """ Merge two skylines."""
        results = []

        count1 = len(skyline1)
        count2 = len(skyline2)
        index1 = 0
        index2 = 0
        y1 = skyline1[count1 - 1][1]
        y2 = y1
        current_y = y1
        while (index1 < count1) and (index2 < count2):
            point1 = skyline1[index1]
            point2 = skyline2[index2]
            if point1[0] < point2[0]:
                y1 = point1[1]
                new_y = min(y1, y2)
                if new_y != current_y:
                    current_y = new_y
                    results.append((point1[0], current_y))
                index1 += 1
            elif point2[0] < point1[0]:
                y2 = point2[1]
                new_y = min(y1, y2)
                if new_y != current_y:
                    current_y = new_y
                    results.append((point2[0], current_y))
                index2 += 1
            else:
                y1 = point1[1]
                y2 = point2[1]
                new_y = min(y1, y2)
                if new_y != current_y:
                    current_y = new_y
                    results.append((point1[0], current_y))
                index1 += 1
                index2 += 1

        # Add any remaining points.
        for i in range(index1, count1):
            point1 = skyline1[i]
            if point1[1] != current_y:
                results.append(point1)
                current_y = point1[1]
        for i in range(index2, count2):
            point2 = skyline2[i]
            if point2[1] != current_y:
                results.append(point2)
                current_y = point2[1]

        return results

if __name__ == '__main__':
    app = App()

# app.root.destroy()
