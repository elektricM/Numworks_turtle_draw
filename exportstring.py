from PIL import Image

# Open the image
img = Image.open('phryge.png')
img = img.convert('RGB')

# Get the dimensions of the image
width, height = img.size

# Dictionary to store colors and their assigned letters
color_letters = {}

# Counter for assigning letters
letter_counter = ord('a')

# Iterate through each pixel in the image
for x in range(width):
    for y in range(height):
        # Get the RGB values of the pixel
        r, g, b = img.getpixel((x, y))
        color = (r, g, b)
        
        # Check if the color is already assigned a letter
        if color not in color_letters:
            # Assign a new letter to the color
            color_letters[color] = chr(letter_counter)
            letter_counter += 1

# Create a string of letters representing colors in the image
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

# Save the string of letters to a file
with open('color_letters.txt', 'w') as file:
    file.write(color_string)

print("Number of colors used in the image:", len(color_letters))
print("Color letters mapping:", color_letters)
print("String of letters representing colors saved to color_letters.txt")