import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os
import pyperclip

def resize_and_reduce_colors(image_path, num_colors):
    # Open the image
    img = Image.open(image_path)
    
    # Determine the aspect ratio of the image
    width, height = img.size
    aspect_ratio = width / height
    
    # Calculate the desired width and height for resizing
    target_height = 240
    target_width = int(target_height * aspect_ratio)
    
    # Resize the image while preserving aspect ratio
    img = img.resize((target_width, target_height))
    
    # Calculate the cropping dimensions
    if target_width > 320:
        crop_width = (target_width - 320) / 2
        img = img.crop((crop_width, 0, target_width - crop_width, target_height))
    elif target_height > 240:
        crop_height = (target_height - 240) / 2
        img = img.crop((0, crop_height, target_width, target_height - crop_height))
    
    # Reduce the image to the selected number of colors
    reduced_img = img.quantize(colors=num_colors)
    
    return reduced_img

def generate_turtle_script(image_path, num_colors):
    img = resize_and_reduce_colors(image_path, num_colors)
    img = img.convert('RGB')

    width, height = img.size

    color_letters = {}
    letter_counter = ord('a')

    for x in range(width):
        for y in range(height):
            r, g, b = img.getpixel((x, y))
            color = (r, g, b)
            if color not in color_letters:
                color_letters[color] = chr(letter_counter)
                letter_counter += 1

    color_string = ''
    for y in range(height):
        x = 0
        while x < width:
            color_count = 1
            while x + color_count < width and img.getpixel((x + color_count, y)) == img.getpixel((x, y)):
                color_count += 1
            if color_count > 1:
                color_string += str(color_count) + color_letters[img.getpixel((x, y))]
                x += color_count
            else:
                color_string += color_letters[img.getpixel((x, y))]
                x += 1

    color_letters_mapping_str = '{\n'
    for color, letter in color_letters.items():
        color_letters_mapping_str += f"    '{letter}': {list(color)},\n"
    color_letters_mapping_str += '}'

    turtle_script = f'''
from turtle import *

# Color letters mapping from the provided dictionary
color_letters_mapping = {color_letters_mapping_str}

width, height = {width}, {height}

speed(0)
penup()
hideturtle()

x, y = -width/2, height/2
goto(x, y)

color_string = '{color_string}'
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
    colort = color_letters_mapping[char]
    i += 1
    
    # Set turtle color
    color(colort[0], colort[1], colort[2])
    
    # Move turtle and draw line
    pendown()
    goto(x + count, y)
    penup()
    
    # Update x position for the next segment
    x += count
    
    # Check if x exceeds half of the width
    if x >= width/2:
        # Move to the next row
        y -= 1
        x = -width/2
        goto(x, y)
'''

    return turtle_script, len(color_letters)

def save_script(turtle_script):
    save_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python files", "*.py")])
    if save_path:
        with open(save_path, 'w', encoding='utf-8') as file:
            file.write(turtle_script)
        messagebox.showinfo("Success", f"File saved as {os.path.basename(save_path)}")

def copy_to_clipboard(turtle_script):
    pyperclip.copy(turtle_script)
    messagebox.showinfo("Success", "Script copied to clipboard")

def select_image():
    image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if image_path:
        num_colors = color_slider.get()
        turtle_script, _ = generate_turtle_script(image_path, num_colors)
        colors_label.config(text=f"Selected number of colors: {num_colors}")
        save_button.config(state=tk.NORMAL, command=lambda: save_script(turtle_script))
        copy_button.config(state=tk.NORMAL, command=lambda: copy_to_clipboard(turtle_script))

root = tk.Tk()
root.title("Image to Turtle Drawing Script")

select_button = tk.Button(root, text="Select Image", command=select_image)
select_button.pack(pady=10)

colors_label = tk.Label(root, text="Selected number of colors: 10")
colors_label.pack(pady=10)

color_slider = tk.Scale(root, from_=5, to=50, orient=tk.HORIZONTAL, label="Number of Colors", length=200)
color_slider.set(10)
color_slider.pack(pady=10)

save_button = tk.Button(root, text="Save Python Script", state=tk.DISABLED)
save_button.pack(pady=10)

copy_button = tk.Button(root, text="Copy to Clipboard", state=tk.DISABLED)
copy_button.pack(pady=10)

root.mainloop()
