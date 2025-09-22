import tkinter as tk 
from tkinter import ttk 
window = tk.Tk()
window.geometry('600x400')
window.title("gridlayout")
# labels 
label1 = ttk.Label(text='Label1',background='skyblue')
label2 = ttk.Label(text='Label2',background='purple')
label3 = ttk.Label(text='Label3',background='tomato')
label4 = ttk.Label(text='Label4',background='pink')
# buttons 
button1  = ttk.Button(window,text='button1')
button2  = ttk.Button(window,text='button2')
# input field 
input = ttk.Entry(window)
# colones configure 
window.columnconfigure((0,1,2),weight=1,uniform='a')
window.columnconfigure(3,weight=2,uniform='a')
# rows configure 
window.rowconfigure((0,1,2),weight=1,uniform='a')
window.rowconfigure(3,weight=3,uniform='a')
label1.grid(row=0,column=0)
label2.grid(row=1,column=1,sticky='snwe',rowspan=3)
label3.grid(row=1,column=0,sticky='snwe',columnspan=3,padx=10,pady=10)
label4.grid(row=3,column=3,sticky='se')
button1.grid(row=2,column=2,sticky='snwe')
button2.grid(row=0,column=3,sticky='snwe')
input.grid(row=3,column=3)
window.mainloop()