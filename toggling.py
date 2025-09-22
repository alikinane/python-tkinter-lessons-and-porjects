import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.geometry('600x400')
'''
def toggle ():
    global lable_visible
    if lable_visible:
        labele.place_forget()
        lable_visible = 0
    else:
        labele.place(relx=0.5,rely=0.5,anchor='center')
        lable_visible = 1        
toggle_button = ttk.Button(window,text='togle',command=toggle)
toggle_button.place(x=50,y=50)
lable_visible= 1
labele =ttk.Label(window,text='Toggle me')
labele.place(relx=0.5,rely=0.5,anchor='center')'''
def toggle():
    labele.pack_forget()

labele =ttk.Label(window,text='Toggle me')
labele.pack(expand=True)
toggle_button = ttk.Button(window,text='togle',command=toggle)
toggle_button.pack(side='bottom')
window.mainloop()