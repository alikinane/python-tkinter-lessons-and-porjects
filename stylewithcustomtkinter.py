import customtkinter as ctk
window = ctk.CTk()
window.title('customtkinter')
window.geometry('400x300')
# creating some widgets 
label =ctk.CTkLabel(master = window ,
 text = 'label',
 fg_color = 'red',
 corner_radius = 20,
 width = 50,
 height = 20
)
label.pack()
switch = ctk.CTkSwitch(window,
	progress_color = 'blue')
switch.pack()
window.mainloop()