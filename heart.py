import math  # Import the math module for mathematical functions.
from turtle import *  # Import everything from the turtle module for working with the turtle.

def hearta(k):
    return 15 * math.sin(k) ** 3  # Define the hearta function to calculate the first part of the heart's coordinates.

def heartb(k):
    return 12 * math.cos(k) - 5 * math.cos(2 * k) - 2 * math.cos(3 * k) - math.cos(4 * k)  # Define the heartb function to calculate the second part of the heart's coordinates.

speed(0)  # Set the turtle's maximum speed (no delay between steps).
bgcolor("black")  # Set the background color to black.
hideturtle()  # Hide the turtle (so it's not visible in the initial position).
penup()  # Lift the pen (the turtle won't draw while moving).
goto(hearta(0) * 20, heartb(0) * 20)  # Move the turtle to the initial position of the heart.
pendown()  # Lower the pen (the turtle will draw while moving).
color("#f73487")  # Set the drawing color to pink.

for i in range(6000):  # Start a loop for drawing the heart. It will run 6000 times.
    goto(hearta(i) * 20, heartb(i) * 20)  # Move the turtle to the next position of the heart.
    # You can add changes to the turtle's color or other effects here if needed.

done()  # Finish the program after drawing the heart.

