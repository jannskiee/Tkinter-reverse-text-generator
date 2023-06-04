import pyperclip
from tkinter import *


def update_count_text():
    text = user_text.get("1.0", END)
    text = text.rstrip("\n")
    text = text.replace(" ", "")
    text_count_label.configure(text=f"Text Count: {len(text)}")


def reverse_text():
    text = user_text.get("1.0", END)
    words = text.split()
    reversed_words = [word[::-1] for word in words if word.strip()]
    reversed_text = " ".join(reversed_words)
    output_text.configure(state='normal')
    output_text.delete("1.0", END)
    output_text.insert(END, reversed_text)
    output_text.configure(state='disabled')
    update_count_text()


def copy_text():
    pyperclip.copy(output_text.get("1.0", END))


window = Tk()
window.title("Reverse Text Generator")
window.geometry("515x700")
window.resizable(width=False, height=False)

input_label = Label(text="Input:", font=("Courier", 15, "normal"))
input_label.grid(column=1, row=1, padx=10, pady=10, sticky="N")

user_text = Text(window, height=15, width=60)
user_text.focus()
user_text.grid(column=1, row=2, padx=15, pady=15)

output_label = Label(text="Output:", font=("Courier", 15, "normal"))
output_label.grid(column=1, row=3, padx=10, pady=10)

output_text = Text(window, height=15, width=60, state='disabled')
output_text.grid(column=1, row=4, padx=15, pady=15)

text_count_label = Label(text="Text Count:", font=("Courier", 10, "normal"))
text_count_label.grid(column=1, row=5, padx=10, pady=10, sticky="W")

reverse_button = Button(text="Reverse", font=("Courier", 10, "normal"), command=reverse_text)
reverse_button.grid(column=1, row=5, padx=10, pady=10, sticky="N")

copy_button = Button(text="Copy Text", font=("Courier", 10, "normal"), command=copy_text)
copy_button.grid(column=1, row=5, padx=10, pady=10, sticky="E")

window.mainloop()
