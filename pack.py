import tkinter as tk 
from tkinter import ttk 
window = tk.Tk()
window.title('layouts via pack ')
window.geometry('400x600')
label1 = ttk.Label(text='text 1',background='skyblue')
label2 = ttk.Label(text='text 1',background='pink')
label3= ttk.Label(text='text 1',background='tomato')
button = ttk.Button(text='Button')

# packing 
label1.pack(side='top',expand=True,fill='both',padx=10,pady=10) #in default widgets can take all the width of container
label2.pack(side='left',expand=True,fill='both') 
label3.pack(side='top',expand=True,fill='both')
button.pack(side='top',expand=True,fill='both')
window.mainloop()