patternchoisd = None  # global variable to hold choice

def firstpage():
    Font = ctk.CTkFont('Playfair Display', 40)
    ctk.CTkLabel(
        master=firstpageframe,
        text='Choose Pattern',
        font=Font,
        text_color='white'
    ).pack(pady=15)

    combo = ctk.CTkComboBox(
        master=firstpageframe,
        values=['Phones-numbers', 'Emails'],
        variable=combo_variable,
        height=50,
        width=240,
        button_color='black',
        button_hover_color='#121111',
        dropdown_fg_color='black',
        dropdown_hover_color='#121111',
    )
    combo.place(relx=0.5, rely=0.5, anchor='center')

    def confirm_choice():
        global patternchoisd
        choice = combo_variable.get()
        if choice != 'Pattern-type':
            patternchoisd = choice   # store the choice
            print("You chose:", patternchoisd)
            firstpageframe.destroy()
        else:
            print('Please choose a pattern')

    buttonmove = ctk.CTkButton(
        master=firstpageframe,
        text='Confirm',
        height=50,
        width=100,
        fg_color='black',
        hover_color='#121111',
        font=ctk.CTkFont('arial', 15, 'bold'),
        command=confirm_choice
    )
    buttonmove.place(relx=0.5, rely=0.85, anchor='center')
