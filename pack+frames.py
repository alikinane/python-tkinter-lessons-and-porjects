import tkinter as tk 
from tkinter import ttk 
window = tk.Tk()
window.title('layouts via pack ')
window.geometry('400x600')
#top frame 
top_frame = ttk.Frame(window)
label1 = ttk.Label(top_frame,text='text 1',background='skyblue')
label2 = ttk.Label(top_frame,text='text 2',background='pink')
#middle widget
label3= ttk.Label(text='text 3',background='tomato')
#bottom frame
bottom_frame = ttk.Frame(window) 
label4= ttk.Label(bottom_frame,text='text 4',background='LimeGreen')
button1 = ttk.Button(bottom_frame,text='Button1')
button2 = ttk.Button(bottom_frame,text='Button2')
# bottom_left_frame
buttom_left_frame =ttk.Frame(bottom_frame)
button3 = ttk.Button(buttom_left_frame,text='button3')
button4 = ttk.Button(buttom_left_frame,text='button4')
button5 = ttk.Button(buttom_left_frame,text='button4')
# top layout 
label1.pack(expand=True,fill='both')
label2.pack(expand=True,fill='both')
top_frame.pack(fill='both',expand=True)
# middle layout
label3.pack(expand=True,fill='both')
# bottom layout
button1.pack(side='left',expand=True,fill='both')
label4.pack(side='left',expand=True,fill='both')
button2.pack(side='left',expand=True,fill='both')
bottom_frame.pack(expand=True,fill='both',padx=20,pady=20)
# bottomleft layout
button3.pack(expand=True,fill='both')
button4.pack(expand=True,fill='both')
button5.pack(expand=True,fill='both')
buttom_left_frame.pack(side='left',fill='both',expand=True)
window.mainloop()
