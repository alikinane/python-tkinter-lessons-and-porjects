import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
# Create window
window = tk.Tk()
window.title('Paint App')
window.geometry('600x400')

# Canvas
canvas = tk.Canvas(window, bg='white')
canvas.pack(fill=tk.BOTH, expand=True)

# Initial brush size
brush_size = 2

# Draw function
def paint(event):
    global brush_size
    canvas.create_oval(
        event.x - brush_size // 2,
        event.y - brush_size // 2,
        event.x + brush_size // 2,
        event.y + brush_size // 2,
        fill='black',
        outline='black'
    )

# Control functions
def add_width():
    global brush_size
    brush_size += 2

def reset_width():
    global brush_size
    brush_size = 2

def clear():
    canvas.delete('all')

def reduce():
    global brush_size
    if brush_size >0 :
        brush_size -=2 
    else:
        messagebox.showwarning("Notice","width is at minumum")

# Bind paint
canvas.bind('<Motion>', paint)

# Create button frame
button_frame = ttk.Frame(window)
button_frame.pack(pady=5)

# Add buttons to the frame side by side
ttk.Button(button_frame, text="Add Width", command=add_width).pack(side='left', padx=5)
ttk.Button(button_frame, text="Reset Width", command=reset_width).pack(side='left', padx=5)
ttk.Button(button_frame, text="Clear Canvas", command=clear).pack(side='left', padx=5)
ttk.Button(button_frame, text="Reduce with ", command=reduce).pack(side='left', padx=5)

# Run the app
window.mainloop()
