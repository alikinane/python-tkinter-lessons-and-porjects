import tkinter as tk 
from tkinter import messagebox
from tkinter import ttk
e  
def yes_no():
	message = messagebox.askquestion('yes/no','yes or no')
	print(message)
def creat_window(): 
	extra()
def close_window():
	extra().destroy()

window =  tk.Tk()
window.title('multiple windows')
window.geometry('600x400')
button1 = ttk.Button(window,text = 'open main window',command = creat_window)
button1.pack(expand = True)
button2 = ttk.Button(window,text = 'close main window',command = close_window)
button2.pack(expand = True)
button3 = ttk.Button(window,text = 'creat yes no window ',command = yes_no)
button3.pack(expand = True)
window.mainloop()