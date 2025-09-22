import tkinter as tk 
from tkinter import ttk
from tkinter import scrolledtext
window = tk.Tk()
'''window.title('Sliders x Progressbar')
window.geometry('600x400')

# Create a variable for the scale and progress bar
scale_output = tk.DoubleVar(value=10.0)

# Label that shows the current value of the scale
Scale_label = ttk.Label(
    window,
    textvariable=scale_output,  # this automatically updates
    font='Arial 25 bold'
)
Scale_label.pack(pady=15)

# Create vertical scale (slider)
scale = ttk.Scale(
    window,
    from_=25,
    to=0,
    length=200,
    orient='vertical',
    variable=scale_output
)
scale.pack()

# Create a progress bar linked to the same variable
progress = ttk.Progressbar(
    window,
    variable=scale_output,
    maximum=25
)
progress.pack()
# create a scrolled text 
scrolled_text = scrolledtext.ScrolledText(window)
print(scrolled_text.get(index1='START',index2='END'))
scrolled_text.pack()'''
# exercise 
# show progress bar

progress_var = tk.DoubleVar() 
lable =ttk.Label(textvariable=progress_var
                 ,font=('arial 20 bold'))
lable.pack()
progress_bar = ttk.Progressbar(window,
                               variable=progress_var,
                               maximum=30
                               )
progress_bar.pack()
progress_bar.start()
# create  a slider 
slider = ttk.Scale(window,
                   from_=0,to=30,
                   length=200,
                   orient='vertical',
                   variable=progress_var)
slider.pack(pady=24)
window.mainloop()
