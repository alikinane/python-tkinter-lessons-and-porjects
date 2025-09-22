import tkinter as tk 
from tkinter import ttk 
window =  tk.Tk()
window.title('measurment of widgets')
window.geometry('800x400')
lable1 = ttk.Label(text='label1',width=100,background='purple')
lable2 = ttk.Label(text='label2',width=100,background='skyblue')
lable1.pack(fill='x')
lable2.pack()
window.mainloop()