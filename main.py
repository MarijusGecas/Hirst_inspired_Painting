import random
from turtle import Turtle, Screen

color_list = [(198, 13, 32), (40, 76, 188), (39, 216, 69), (238, 227, 5), (227, 159, 49), (29, 40, 154), (212, 76, 15), (17, 153, 17), (241, 36, 161), (195, 16, 12), (223, 21, 120), (68, 10, 31), (61, 15, 8), (223, 141, 206), (11, 97, 62), (219, 159, 11), (54, 209, 229), (19, 21, 49), (238, 157, 216), (79, 74, 212), (10, 228, 238), (73, 212, 168), (93, 233, 198), (65, 231, 239), (217, 88, 51)]
tim = Turtle()
screen = Screen()
tim.speed(1000)
number = 0
x = -200
y = -200
# Outer loop for rows (y-coordinate)
for row in range(10):
    x = -200  # Reset x to the start position for each new row
    for column in range(10):
        tim.penup()
        tim.goto(x, y)
        tim.pendown()
        random_color = random.choice(color_list)
        tim.color(f"#{random_color[0]:02x}{random_color[1]:02x}{random_color[2]:02x}")
        tim.dot(20)  # Draw a dot at the current position
        x += 50  # Move right for the next dot

    y += 50  # Move up for the next row

