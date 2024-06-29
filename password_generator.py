import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    n = length_var.get()
    list_of_option = []
    if special_var.get():
        list_of_option.append(special_characters)
    if capital_var.get():
        list_of_option.append(uppercase_alphabets)
    if small_var.get():
        list_of_option.append(lowercase_alphabet)
    if number_var.get():
        list_of_option.append(numbers)

    if not list_of_option:
        messagebox.showerror("Error", "Choose at least one option")
    else:
        password = "".join(random.choice(random.choice(list_of_option)) for _ in range(n))
        password_var.set(password.strip())
        password_text.delete("1.0", tk.END)
        password_text.insert(tk.END, password.strip())

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())
    messagebox.showinfo("Copied", "Password copied to clipboard")

# Lists of characters
lowercase_alphabet = list(string.ascii_lowercase)
uppercase_alphabets = list(string.ascii_uppercase)
numbers = list(string.digits)
special_characters = list(string.punctuation)

# Create the main window
root = tk.Tk()
root.title("Password Generator 🔐")
root.geometry("400x350")

# Title and description
title_label = tk.Label(root, text="Password Generator 🔐", font=("Helvetica", 16))
title_label.pack(pady=10)

desc_label = tk.Label(root, text="Securing you everyday ❤️", font=("Helvetica", 12))
desc_label.pack(pady=5)

# Length of the password
length_label = tk.Label(root, text="Enter the length of the password:")
length_label.pack(pady=5)
length_var = tk.IntVar(value=8)
length_scale = tk.Scale(root, from_=2, to=100, orient="horizontal", variable=length_var)
length_scale.pack(pady=5)

# Checkboxes for options
special_var = tk.BooleanVar()
capital_var = tk.BooleanVar()
small_var = tk.BooleanVar()
number_var = tk.BooleanVar()

special_check = tk.Checkbutton(root, text="Special characters", variable=special_var)
special_check.pack(anchor="w")
capital_check = tk.Checkbutton(root, text="Capital letters", variable=capital_var)
capital_check.pack(anchor="w")
small_check = tk.Checkbutton(root, text="Small letters", variable=small_var)
small_check.pack(anchor="w")
number_check = tk.Checkbutton(root, text="Numbers", variable=number_var)
number_check.pack(anchor="w")

# Button to generate the password
generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=10)

# Display the generated password
password_var = tk.StringVar()
password_text = tk.Text(root, height=5, font=("Helvetica", 12), wrap=tk.WORD)
password_text.pack(pady=5)

# Button to copy the password
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Start the main loop
root.mainloop()
