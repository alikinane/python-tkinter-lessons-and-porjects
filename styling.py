import tkinter as tk 
from tkinter import ttk 

window = tk.Tk()
window.geometry('400x300')
window.title("styling")

style = ttk.Style()
# style.theme_use('winnative')
# print(style.theme_names())
style.configure('TButton' , foreground = 'green') # like that for all buttons
# style.configure('new.TButton' , foreground = 'green',background = 'green',font = ('Jokerman',20)) # here our style name is newT.. and we can use everywhere 
style.map('new.TButton',foreground = [('pressed','red'),('disabled','yellow')],
	background = [('pressed' , 'blue'),('active' ,'pink')])
label = ttk.Label(window,text =
 'this is a text',
	background = 'red',
	foreground = 'white',
	font = ('Jokerman' , 20 )
	)
button = ttk.Button(window,text = 'button')
label.pack()
button.pack()
# exercise : add a frame with width and height and give it a pink background color 
#style 
# style = ttk.Style()
# style.configure('new.Txx',background = 'pink')
# frame = ttk.Frame(window,style = 'new.Txx')
# frame.place(x = 0 , y = 0 , height = 50 , width = 50)
window.mainloop()