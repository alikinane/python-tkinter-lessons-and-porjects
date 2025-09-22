import tkinter as tk 
from tkinter import ttk 

# start 
window = tk.Tk()
# window configurations
window.title('Shapes')
window.geometry('600x400')
# our canva inside of window 
canvas = tk.Canvas(window,bg='white')
canvas.pack()
# create a rectangle 
canvas.create_rectangle((50,20,100,200),fill='red',width=5,dash=(1,2),outline='green')
# create a line 
canvas.create_line((0,0,600,400),fill='black')
# create a circle 
canvas.create_oval(50,50,100,100,fill='gray')
# create a polygone
canvas.create_polygon(0,0,100,200,300,50)
# create a circle 
canvas.create_oval(50,50,100,100,fill='gray')
# creat an ark
canvas.create_arc((50,50,100,100),fill = 'red')
# creat a text 
canvas.create_text((109,109),text='Im ali ',fill='green',width=10)
# display a w diget inside of a canva 
canvas.create_window((200,200),window=ttk.Label(text='Hello canvas '))
#run 
window.mainloop()