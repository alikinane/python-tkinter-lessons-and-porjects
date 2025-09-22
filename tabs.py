import tkinter as tk 
from tkinter import ttk

Window = tk.Tk()
Window.title('taps')
Window.geometry('600x400')
#create tap holder 
notebook = ttk.Notebook(Window)
tab1 = ttk.Frame(notebook)
label1 = ttk.Label(tab1,text='this is y')
label1.pack()
button1 = ttk.Button(tab1,text='buttony')
button1.pack()
tab2 = ttk.Frame(notebook)
label2 = ttk.Label(tab2,text='this is x')
label2.pack()
button2 = ttk.Button(tab2,text='buttonx')
button2.pack()
notebook.add(tab1,text='tab1')
notebook.add(tab2,text='tab2'
'') 
notebook.pack()
Window.mainloop()