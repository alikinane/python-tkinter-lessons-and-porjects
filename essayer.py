import customtkinter as ctk 

root = ctk.CTk(fg_color = '#0F1C2E')
root.geometry('300x400')
root.resizable(False,False)
# search bar and button
frame1 = ctk.CTkFrame(root,fg_color ='transparent',corner_radius = 0)
# frame widgets 
smallentry = ctk.CTkEntry(
        frame1,
        corner_radius = 20,
        height=35,
        # textvariable=self.entry_var,
        fg_color='transparent',
        placeholder_text='⌕ search a city '
    )
smallentry.pack(fill = 'x',padx = 20,pady = 5)
smallsearchbutton = ctk.CTkButton(
            frame1,
            corner_radius=20,
            text='search',
            width=60,
            height=35,
            font = ctk.CTkFont('arial',12,'bold'),
            cursor = 'hand2',
            fg_color='#4459ad',
            # command = lambda : self.get_weather()
    )
smallsearchbutton.pack(pady = 10)
frame1.pack(fill = 'x')
frame2 = ctk.CTkFrame(root,fg_color ='transparent',corner_radius = 0)
# degree
ctk.CTkLabel(
            frame1,
            text = '25 C',
            # textvariable=self.degree_var,
            font=ctk.CTkFont('Helvetica', 70, 'bold')
        ).pack(pady=10)
icon_image = ctk.CTkImage(
            light_image=Image.open(f'images/meteoapp/.png'),
            dark_image=Image.open(f'images/meteoapp/clouds.png'),
            size=(100, 100)
)
icon = icon_image
icon_label =ctk.CTkLabel(
            frame1,
            text='',
            image=icon
        )
icon_label.pack(pady=10)
frame2.pack(fill = 'x')
root.mainloop()