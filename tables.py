import tkinter as tk 
from tkinter import ttk 
from random import choice
# lists of names
first_names = ["Liam", "Emma", "Noah", "Olivia", "Elijah", "Ava", "James", "Sophia", "Benjamin", "Isabella"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Martinez", "Taylor"]
# create a window 
window = tk.Tk()
table = ttk.Treeview(window,
                     columns=('first','second','third'),
                     show='headings'
                     )
table.pack(fill='both',expand=True)
table.heading('first',text='firstName')
table.heading('second',text='lastName')
table.heading('third',text='Email')
# insert values
for i in range(10):
    x = choice(first_names)
    y = choice(last_names)
    table.insert(parent='',
                 index=0,
            
                 values=(x,y,i))     # '' meand it's attached primarely to the main table
# function output all selected elments 
def selected (event):
    for i in table.selection():
        x = table.item(i)
        print(x['values'])
table.insert(parent='',index=0,values=('xx','yy','zz'))# it would get in top frocing the precednt element to get down 
table.insert(parent='',index=tk.END,values=('last','last','last'))
def delete (event):
    for i in table.selection():
        table.delete(i)
table.bind('<<TreeviewSelect>>',selected)
#Delete items
table.bind('<Delete>',delete)
# run our window 
window.mainloop()