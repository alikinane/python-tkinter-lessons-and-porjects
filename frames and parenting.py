import tkinter as tk 
from tkinter import ttk 
# creat a window  
window = tk.Tk()
window.title('Parenting and frames ')
window.geometry('600x400')
frame = ttk.Frame(window,
                  width=100,
                  height=200,
                  borderwidth=10,
                  relief='groove',

                  )
# now we can start parenting 
frame.pack_propagate(False)
frame.pack()
label = ttk.Label(frame,text="inside of a frame")
label.pack()
button = ttk.Button(frame,text='clickframe')
button.pack()
#start 
window.mainloop()