import random
import string
import tkinter as tk
from tkinter import scrolledtext

def generate_code():
    valid_chars = ''.join(set(string.ascii_uppercase + string.digits) - set('AEIOULS015'))
    return '-'.join(''.join(random.choice(valid_chars) for _ in range(5)) for _ in range(5))

def generate_codes(n):
    return [generate_code() for _ in range(n)]

def display_codes():
    codes = generate_codes(10)
    text_area.delete(1.0, tk.END)
    for code in codes:
        text_area.insert(tk.END, code + '\n')

# Create the main window
root = tk.Tk()
root.title("Code Generator")

# Create a button to generate codes
generate_button = tk.Button(root, text="Generate Codes", command=display_codes)
generate_button.pack(pady=10)

# Create a scrolled text area to display the codes
text_area = scrolledtext.ScrolledText(root, width=40, height=10)
text_area.pack(pady=10)

# Run the application
root.mainloop()
