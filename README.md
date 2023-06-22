![reverse text generator image.png](reverse%20text%20generator%20image.png)

# Reverse Text Generator

The Reverse Text Generator is a simple GUI application, built with Python and the Tkinter library, that reverses the words provided by the user. It provides an easy-to-use interface with a space to enter the text, a display for the reversed output, and buttons to reverse the text and copy the output to the clipboard.

## Features
1. **Text input field**: Where the user can enter the text they want reversed.
2. **Text output field**: Where the reversed text is displayed.
3. **"Reverse" button**: Clicking this button will reverse the order of characters in each word of the entered text.
4. **"Copy Text" button**: This will copy the reversed text to your clipboard, ready to be pasted elsewhere.
5. **Text Count**: This displays the count of non-space characters in the reversed text.

## Prerequisites
The Reverse Text Generator is written in Python, and it requires the following Python packages to function:
- `Tkinter`: A built-in Python package used to create the GUI.
- `pyperclip`: A Python module used for cross-platform clipboard copying and pasting. 

You can install `pyperclip` using pip:
```sh
pip install pyperclip
```

## How to Run
1. Make sure Python and necessary packages are properly installed on your system.
2. Save the provided Python script in a file, for example: `reverse_text_generator.py`.
3. Run the script in a Python environment by executing the following command in the terminal:
```sh
python reverse_text_generator.py
```
4. The application window will appear, and you can start using the Reverse Text Generator.

## Usage
1. Enter the text you want reversed in the "Input" field.
2. Click the "Reverse" button. The reversed text will appear in the "Output" field and the text count will update.
3. If you want to copy the reversed text, click the "Copy Text" button. The reversed text is now in your clipboard and can be pasted elsewhere.

## Note
This is a simple text manipulation application and does not support complex text processing, parsing, or other transformations beyond reversing characters in words.