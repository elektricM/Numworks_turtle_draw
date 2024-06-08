# NumWorks Calculator Turtle Drawing Project

[![License](https://img.shields.io/github/license/elektricM/Numworks_turtle_draw)](

- [English](README.md)
- [Français](README.fr.md)

This project allows you to draw pictures on the NumWorks calculator using the Turtle graphics library. The project involves converting an image into a sequence of turtle commands based on color mappings.

## Usage

### Option 1: Using the GUI Executable

1. **Download the GUI Executable**:

   Download the latest release from the [releases page](https://github.com/elektricM/Numworks_turtle_draw/releases).

2. **Run the Executable**:

   Run the executable and follow the instructions in the GUI to select your image and generate the Python script for the NumWorks calculator.

### Option 2: Running Manually with Python

## Requirements

- Python 3.x
- NumWorks Calculator
- PIL (Pillow) library
- Turtle graphics library
- Tkinter (for the GUI version)
- pyperclip (for clipboard functionality)

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/elektricM/Numworks_turtle_draw.git
   cd Numworks-turtle-draw
   ```

2. **Install Dependencies:**

   Make sure you have Python 3.x installed. Then, install the required libraries using pip:

   ```bash
   pip install pillow
   pip install pyperclip
   pip install turtle
   pip install tk
   ```

## Usage

## Option 1: Using the GUI Script

- Use the `automatic_gui.py` script to generate the color mapping and Python script for the NumWorks calculator using the GUI.

## Option 2: Running Manually with Python

### 1. Prepare Your Image

- Place your desired image (e.g., `example.png`) in the project directory.

### 2. Generate Color Letters

Run the following script to generate the color mapping (`color_letters.txt`) from your image:

```bash
python exportstring.py
```

This script will create a mapping of colors to letters and save them in `color_letters.txt`.

### 3. Draw on NumWorks Calculator

1. copy the contents of `color_letters.txt` and the colors in the table to `code_numworks.py` on your calculator.
2. export this to the calculator using the Numworks online tool.

3. If you want to draw this on the pc instead use the `tortue.py` file and run it with python. (make sure to copy the colors into the table in the file python first)

### 4. Run the Turtle Drawing

On your NumWorks calculator, execute the `turtle_drawing.py` script. This script will interpret the color letters from `color_letters.txt` and draw the corresponding image using turtle graphics.

## Additional Notes

- Ensure the image you use (`example.png` in the example) is appropriately sized for the NumWorks calculator screen dimensions (`320x240`) and doesn't have too many colors.

---
