import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.title('Layouts intr0')
window.geometry('600x400')
lable1  = ttk.Label(text='Label1',background='skyblue')
#lable1.pack(side='left',expand=True,fill='x')
lable2  = ttk.Label(text='Label2',background='pink')
#lable2.pack(side='right')
# the grid methode 
'''window.columnconfigure(0,weight=1)
window.columnconfigure(1,weight=1)
window.columnconfigure(2,weight=1)
window.rowconfigure(0,weight=1)
window.rowconfigure(1,weight=1)
lable1.grid(row=0,column=1,sticky='nswe')
lable2.grid(row=1,column=1,columnspan=2,sticky='nswe')'''
# the place methode 
'''lable1.place(x=300,y=200,height=100,width=100)
lable2.place(x=400,y=200,height=100,width=100)'''
# Now we can place them with relative positions in place 
lable1.place(relx=0.5,rely=0.5,relwidth=1,anchor='se')
window.mainloop()
