import tkinter as tk 
from tkinter import ttk

window =tk.Tk()
window.title('stackes')
window.geometry('600x400')
# create widgets
label1 = ttk.Label(window,text='label1',background='skyblue')
label2 = ttk.Label(window,text='label2',background='pink')
label3 = ttk.Label(window,text='label3',background='tomato')

# buttons 
button1 = ttk.Button(window,text='button1',command=lambda: label1.tkraise())
button2 = ttk.Button(window,text='button2',command=lambda: label2.tkraise())
button3 = ttk.Button(window,text='button3',command=lambda:label3.tkraise())
label1.place(x=80,y=140,width=100,height=100)
label2.place(x=120,y=100,width=120,height=150)
label3.place(x=180,y=100,width=140,height=100)


button1.place(relx=1,rely=1,anchor='se')
button2.place(relx=0.8,rely=1,anchor='se')
button3.place(relx=0.6,rely=1,anchor='se')
window.mainloop()