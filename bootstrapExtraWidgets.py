import ttkbootstrap as ttk
from ttkbootstrap.scrolled import ScrolledFrame
import tkinter as tk 
import customtkinter as ctk
from ttkbootstrap.tooltip import ToolTip
from ttkbootstrap.widgets import DateEntry
from ttkbootstrap.widgets import Floodgauge
from ttkbootstrap.widgets import Meter
n = 1
def addtask():
    global n
    ctk.CTkCheckBox(sf, text=f"{n} {var.get()}",corner_radius = 20,border_width = 2,
        font = ('arial' , 15),).pack(anchor='nw' , pady = 4)
    n+=1

app = ttk.Window(themename = 'darkly')
var = tk.StringVar(value = 'enter a task')
label= ttk.Label(app,
    text = 'Enter a new task',
    bootstyle = 'success',
    font = ('arial' ,15)).pack(pady = 8)
entry = ctk.CTkEntry(app,textvariable = var,corner_radius = 20,width = 200,border_width = 1).pack()
calendar = DateEntry(app , width = 25)
calendar.pack(pady = 10)
pvar = tk.IntVar(value =50)
progress = ttk.Floodgauge(app,
    variable = pvar,
    bootstyle = 'danger',
    mask = 'progress {}%')
progress.pack()
metter = ttk.Meter(app,
    amounttotal = 100,
    interactive = True)
metter.pack()
sf = ScrolledFrame(app, autohide=True)
sf.pack(fill='both', expand=True, padx=10, pady=10)

button = ttk.Button(app,text = 'add task',bootstyle = 'success',command = addtask)
button.pack()
ToolTip(button, text="This is a new task ", bootstyle=('success', 'INVERSE'))
app.mainloop()