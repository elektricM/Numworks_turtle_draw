# NumWorks Calculator Turtle Art Project

This project allows you to draw pictures on the NumWorks calculator using the Turtle graphics library. The project involves converting an image into a sequence of turtle commands based on color mappings.

## Requirements

- Python 3.x
- NumWorks Calculator
- PIL (Pillow) library
- Turtle graphics library

## Setup

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/your-username/numworks-turtle-art.git
   cd numworks-turtle-art
   ```

2. **Install Dependencies:**

   Make sure you have Python 3.x installed. Then, install the required libraries using pip:

   ```bash
   pip install Pillow
   ```

   The `turtle` library is usually included with Python by default.

## Usage

### 1. Prepare Your Image

- Place your desired image (e.g., `phryge.png`) in the project directory.

### 2. Generate Color Letters

Run the following script to generate the color mapping (`color_letters.txt`) from your image:

```bash
python exportstring.py
```

This script will create a mapping of colors to letters and save them in `color_letters.txt`.

### 3. Draw on NumWorks Calculator

1. Transfer `color_letters.txt` to your NumWorks calculator.
2. Open the `turtle_drawing.py` script on your calculator.

### 4. Run the Turtle Drawing

On your NumWorks calculator, execute the `turtle_drawing.py` script. This script will interpret the color letters from `color_letters.txt` and draw the corresponding image using turtle graphics.

## Additional Notes

- Ensure the image you use (`phryge.png` in the example) is appropriately sized for the NumWorks calculator screen dimensions (`320x240`).

---
