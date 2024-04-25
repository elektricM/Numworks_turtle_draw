from turtle import *
import time

# Color letters mapping from the provided dictionary
color_letters_mapping = {
    'a': [38, 31, 29],
    'b': [142, 34, 14],
    'c': [114, 89, 28],
    'd': [92, 83, 72],
    'e': [158, 138, 113],
    'f': [231, 112, 68],
    'g': [230, 66, 55],
    'h': [230, 177, 89],
    'i': [238, 202, 147],
    'j': [187, 22, 23]
}

width, height = 320, 240
screen = Screen()
screen.setup(width, height)
screen.tracer(0)

t = Turtle()
t.speed(0)
t.penup()
t.hideturtle()

x, y = -width/2, height/2
t.goto(x, y)

with open('color_letters.txt', 'r') as file:
    color_string = file.read()

# Draw based on color string
i = 0
while i < len(color_string):
    char = color_string[i]
    count = 0
    
    # Accumulate digits to determine the length of line
    while char.isdigit():
        count = count * 10 + int(char)
        i += 1
        char = color_string[i]
    
    if count == 0:
        count = 1
    
    # Get color RGB values
    color = color_letters_mapping[char]
    i += 1
    
    # Set turtle color
    t.color(color[0] / 255, color[1] / 255, color[2] / 255)
    
    # Move turtle and draw line
    t.pendown()
    t.goto(x + count, y)
    t.penup()
    
    # Update x position for the next segment
    x += count
    
    # Check if x exceeds half of the width
    if x >= width/2:
        # Move to the next row
        y -= 1
        x = -width/2
        t.goto(x, y)
        screen.update()

# Keep the window open for a while
time.sleep(10)
