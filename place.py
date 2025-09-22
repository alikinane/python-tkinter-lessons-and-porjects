import tkinter  as tk 
from tkinter import ttk

window = tk.Tk()
window.title('place methode')
window.geometry("400x600")
'''label1 = ttk.Label(window,text='Label1',background='skyblue')
label2 = ttk.Label(window,text='Label2',background='pink')
label3 = ttk.Label(window,text='Label3',background='tomato')
button = ttk.Button(window,text='button')
label1.place(x=300,y=100,width=100,height=200)
label2.place(relx=0.2,rely=0.1,relwidth=0.4,relheight=0.5)
label3.place(x = 80, y = 60, width= 160, height =300 )
button.place(relx=1,rely=1,anchor='se') #  we changed the anchor to the bottom left so we can see the widget '''
# exercise 
ex_label = ttk.Label(window,text='Label',background='purple')
ex_label.place(relx=0.5,rely=0.5,relwidth=0.5,height=200,anchor='center')
window.mainloop()