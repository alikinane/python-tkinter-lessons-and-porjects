import ttkbootstrap as ttk
import tkinter as tk 
x = ttk.Window(themename = 'darkly')
x.geometry('400x300')
button1 = ttk.Button(text = 'button11', bootstyle = ('success','outline'))
button1.pack(expand = True)
button2 = ttk.Button(text = 'button2',bootstyle = 'secondary')
button2.pack(expand = True)
button3 = ttk.Button(text = 'button3',bootstyle = 'warning')
button3.pack(expand = True)

x.mainloop()