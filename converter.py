import ttkbootstrap as ttk
import tkinter as tk 

def submit():
    try:
        # Get the string from entry, convert to float
        x = float(entry.get())
        y = x * 1.60934
        text_variable.set(f"{y:.2f} kilometres")
    except ValueError:
        text_variable.set("Invalid input")

# Main window with ttkbootstrap and dark theme
window = ttk.Window(themename="darkly")  # "darkly" is a dark theme

window.title("Miles to Kilometres")
window.geometry("300x150")

# Title label
title_label = ttk.Label(window, text="Miles to Kilometres", font="Arial 15 bold")
title_label.pack(pady=5)

# Input frame
input_form = ttk.Frame(window)

entry = ttk.Entry(input_form)
button = ttk.Button(input_form, text="Convert", command=submit)

entry.pack(side="left", padx=10)
button.pack(side="left")
input_form.pack(pady=5)

# Output
text_variable = ttk.StringVar()
output_label = ttk.Label(window, font="Arial 15 bold", textvariable=text_variable)
output_label.pack(pady=10)

# Start GUI
window.mainloop()
