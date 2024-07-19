# Lab 9 -- Display Chart

We will build a GUI to display a set of values. You will display the values using both a line chart and a bar chart on the same app. You will implement the following:

1. In the constructor create a list of 20 values from your generator class in **Lab Assignment 6**. This will not change for the life of the application.

2. In the initUI() method do the following:
    - Add the code that will create the three widgets at the top of the window as shown in the screenshot below.
    - Call the method below that will draw the rectangles and lines as shown in the screenshot.
    - Wire-up the button to read the input from the textbox and call the method in step 3 with the appropriate arguments.

3. Define a method that takes the start values (the list of values is available as a class attribute) and will draw the six rectangles and the lines.

![](media/image1.png)

![](media/image2.png)

![](media/image3.png)

## Requirements

1. You will use the same quantity that you selected in the previous lab (from temperature, humidity, barometric pressure, customers at a mall, or just with an alternate descriptor).
2. Design and build a GUI application class that will model a display for your sensor reasonably well.
3. You must provide an Entry (Textbox) and a button to read the value and call the method to draw the rectangles and lines.
4. There are marks for aesthetics.

See the appendix of the previous week lab for some code sample and possible directions to explore.

### Rubrics

| **Class** | 4/4 |
|-----------|-----|
| **unitUI Method** | 3/3 |
| **Button Handler** | 2/2 |
| **Draw rectangle** | 6/6 |
| **Gui** | 2/2 |
| **Aesthetics** | 3/3 |
| **Total** | **20/20** |

## Appendix

Because you will be drawing multiple rectangles and lines on your canvas, you will have to "clear the output". There are two suggested techniques:

1. Remove the canvas from your Tkinter app. So, to draw you will have to create a new canvas and re-draw your rectangles etc. This is not a bad option, but if you must redraw axis and other embellishments, it might be too expensive.  
   Code to remove a canvas widget:

   ```python
   self.canvas = Canvas(«host_container»)  # reference to the canvas
   «host_container».delete(self.canvas)
   ```

2. A slightly more efficient approach is to remove all the items in the canvas.  
   Code to remove the items:

   ```python
   self.canvas = Canvas(«host_container»)  # reference to the canvas
   self.canvas.delete('all')  # clears the canvas
   ```

3. Another option is to remove just the temporary items. This is more efficient but slightly little more complicated.  
   Code to remove the items:

   ```python
   self.items = []  # this will store all temp items
   self.canvas = Canvas(«host_container»)  # reference to the canvas
   self.items.append(self.canvas.create_text(«left», «top», text='some text'))  # add a temp item
   self.items.append(self.canvas.create_line(«left», «top», «right», «bottom»))  # add another temp item
   for item in self.items:
       self.canvas.delete(item)  # remove each item
   self.items = []  # re-initialize the temp storage
   ```
