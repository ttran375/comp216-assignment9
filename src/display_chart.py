import tkinter as tk
from tkinter import ttk
from data_generator import DataGenerator


class LineChartApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.canvas_temp_width = 600
        self.canvas_temp_height = 300

        self.canvas_width = 800
        self.canvas_height = 300

        self.my_pointer = None
        self.x_dist = 60
        self.y_dist = 5
        self.bar_width = self.x_dist - 6

        self.low_value = 18
        self.high_value = 27
        self.normal_range = [20, 25]
        # Set up the main window
        self.title("Line Chart App")
        self.geometry("800x600")

        # Create a frame for the input and update button
        self.input_frame = ttk.Frame(self)
        self.input_frame.pack(pady=10)

        # Label and entry for new value input
        self.entry_label = ttk.Label(self.input_frame, text="Data range:")
        self.entry_label.grid(row=0, column=0, padx=5)

        self.value_entry = ttk.Entry(self.input_frame)
        self.value_entry.grid(row=0, column=1, padx=5)

        # Button to update the chart with the new value
        self.update_button = ttk.Button(self.input_frame, text="Go", command=self.draw_chart)
        self.update_button.grid(row=0, column=2, padx=5)

        # Canvas for drawing the line chart
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height, bg='white')
        self.canvas.pack(pady=10)

        # Initialize the list of values and draw the initial chart
        self.values = []
        self.values2 = []
        self.dataset = DataGenerator(20).getTemperatureSensorDataset(-10, 40)
        self.draw_chart()

    def draw_chart(self):
        """
        Draw the line chart on the canvas.
        This function clears the canvas and redraws the chart with the current values.
        """
        my_range_start = int(self.value_entry.get()) if self.value_entry.get().isdecimal() else 0
        data_range = [my_range_start, my_range_start + 5]

        self.canvas.delete("all")

        # Draw the X and Y axes
        self.canvas.create_line(50, 280, 550, 280, arrow=tk.LAST)  # X axis
        self.canvas.create_line(50, 280, 50, 10, arrow=tk.LAST)    # Y axis

        # Labels for the X and Y axes
        self.canvas.create_text(550, 290, text="Time (s)", anchor=tk.W)
        self.canvas.create_text(15, 50, text="Temperature (°C)", anchor=tk.E, angle=90)
        self.canvas.create_text(400, 5, text=f"Data range: {data_range[0]}-{data_range[1]}", anchor=tk.N)

        # Draw the numerical values on the X axis
        for i in range(0, 7, 1):
            x = 50 + (i * self.x_dist)
            self.canvas.create_text(x, 288, text=f"{i}", anchor=tk.N)

        # Draw the numerical values on the Y axis
        for i in range(-10, 41, 10):
            y = 280 - (i + 10) * self.y_dist
            self.canvas.create_text(40, y, text=f"{i}", anchor=tk.E)

        # Draw bars and lines
        self.values2 = []
        for i in self.dataset[data_range[0]:data_range[1] + 1]:
            self.values2.append(i)
            
            # Draw bar
            self.rect_top_left = [(50 - self.bar_width / 2) + len(self.values2) * self.x_dist, 280 - (i + 10) * self.y_dist]
            self.rect_bottom_right = [(50 + self.bar_width / 2) + len(self.values2) * self.x_dist, 280]
            self.canvas.create_rectangle(
                self.rect_top_left[0], self.rect_top_left[1],  # top left
                self.rect_bottom_right[0], self.rect_bottom_right[1],  # bottom right
                outline='', fill='#1f1')

            # Draw line
            if len(self.values2) > 1:
                pre_point = [50 + (len(self.values2) - 1) * self.x_dist, 280 - (self.values2[-2] + 10) * self.y_dist]
                new_point = [50 + len(self.values2) * self.x_dist, 280 - (i + 10) * self.y_dist]
                self.canvas.create_line(new_point[0], new_point[1], pre_point[0], pre_point[1], fill='blue', width=2)

    def update_chart(self):
        """
        Update the chart with a new value.
        This function replaces the last value in the list with a new value provided by the user.
        """
        try:
            new_value = int(self.value_entry.get())
            self.values.append(new_value)  # Update the last value in the list

            new_point = [50 + len(self.values) * self.x_dist, 280 - (new_value + 10) * self.y_dist]

            self.canvas.create_oval(new_point[0] - 3, new_point[1] - 3, new_point[0] + 3, new_point[1] + 3, fill='red')
            self.canvas.create_text(new_point[0], new_point[1] - 10, text=str(new_value), fill='black')

            if len(self.values) > 1:
                pre_point = [50 + (len(self.values) - 1) * self.x_dist, 280 - (self.values[-2] + 10) * self.y_dist]
                self.canvas.create_line(new_point[0], new_point[1], pre_point[0], pre_point[1], fill='blue', width=2)

            self.draw_temp_pointer(new_value)

        except ValueError:
            print("Please enter a valid integer")

    def draw_temperature(self):
        """
        Draw the line chart on the canvas.
        This function clears the canvas and redraws the chart with the current values.
        """

        width = 30
        start_point = [700, 10]
        start_point2 = [start_point[0] + width, start_point[1]]

        cir_top_left = [start_point[0], self.canvas_height - start_point[1] - width]
        cir_bottom_right = [start_point2[0], self.canvas_height - start_point[1]]

        self.temp_start_y = cir_bottom_right[1] - (width / 2)

        self.canvas.create_oval(cir_top_left[0], cir_top_left[1],  # top left
                                start_point2[0], cir_bottom_right[1],  # bottom right
                                outline='#f11', fill='#1f1')

        self.canvas.create_line(cir_top_left[0] - 2, start_point[1], cir_top_left[0] - 2, self.temp_start_y)  # X axis

        self.rect_top_left = [cir_top_left[0] + 5, start_point[1]]
        self.rect_bottom_right = [cir_bottom_right[0] - 5, cir_bottom_right[1] - 20]
        self.canvas.create_rectangle(
            self.rect_top_left[0], self.rect_top_left[1],  # top left
            self.rect_bottom_right[0], self.rect_bottom_right[1],  # bottom right
            outline='', fill='#1f1')

        for i in range(0, 100, 10):
            y = self.temp_start_y - (i * 3)
            self.canvas.create_text(start_point[0] - 5, y, text=f"{i}", anchor=tk.E)

    def draw_temp_pointer(self, i):
        if self.my_pointer is not None:
            self.canvas.delete(self.my_pointer)

        new_point = self.temp_start_y - (i * 3)

        new_rect_top_left = [self.rect_top_left[0], new_point]
        new_rect_bottom_right = [self.rect_bottom_right[0], new_point + (5 * 3)]
        self.my_pointer = self.canvas.create_rectangle(
            new_rect_top_left[0], new_rect_top_left[1],  # top left
            new_rect_bottom_right[0], new_rect_bottom_right[1],  # bottom right
            outline='', fill='#87cefa')


if __name__ == "__main__":
    app = LineChartApp()
    app.mainloop()
