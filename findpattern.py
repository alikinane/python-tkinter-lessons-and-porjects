import customtkinter as ctk 
import re
from PIL import Image
import pyperclip
def phones_patterns(text):
    pattern = re.compile(r'''
        (\d{3}|\(\d{3}\))
        (\s|-|\.)?
        (\d{3})
        (\s|-|\.)?
        (\d{4})
        ''', re.VERBOSE)
    matches = pattern.finditer(text)
    matchlist = []
    for match in matches:
        matchlist.append(match.group())
    return matchlist

def emails_patterns(text):
    pattern = re.compile(r'''
        [a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}
    ''', re.VERBOSE)
    matches = pattern.finditer(text)
    matchlist = []
    for match in matches:
        matchlist.append(match.group())
    return matchlist

def customwindow():
    root.geometry('400x600')
    root.title('pattern')
    root.iconbitmap('empty.ico')

def firstpage():
    firstpageframe = ctk.CTkFrame(root)
    firstpageframe.place(relx=0.05, rely=0.2, relwidth=0.9, relheight=0.6)
    Font = ctk.CTkFont('Playfair Display', 40)
    ctk.CTkLabel(
        master=firstpageframe,
        text='Chose Pattern',
        font=Font,
        text_color='white'
    ).pack(pady=15)

    combo_variable = ctk.StringVar(value='Pattern-type')
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

    buttonmove = ctk.CTkButton(
        master=firstpageframe,
        text='Confirm',
        height=50,
        width=100,
        fg_color='black',
        hover_color='#121111',
        font=ctk.CTkFont('arial', 15, 'bold'),
        command=lambda: movepage()
    )
    buttonmove.place(relx=0.5, rely=0.85, anchor='center')

    def movepage():
        global patternchoise
        combo_value = combo_variable.get()
        if combo_value != 'Pattern-type':
            patternchoise = combo_value
            firstpageframe.destroy()
            secondpage()

        else:
            toplevelmessage()

    def toplevelmessage():
        toplevel = ctk.CTkToplevel()
        toplevel.overrideredirect(True)  
        Font = ctk.CTkFont('Helvetica', 18, 'bold')
        ctk.CTkLabel(
            master=toplevel,
            text='chose pattern !',
            text_color='white',
            font=Font,
            fg_color='transparent'
        ).pack(pady=10, padx=20)
        root.eval(f'tk::PlaceWindow {str(toplevel)} center')
        ctk.CTkButton(
            toplevel,
            text='close',
            font=Font,
            command=lambda: [toplevel.destroy()],
            width=100,
            height=30,
            fg_color='black'
        ).pack(pady=10)

def secondpage():
    secondpageframe = ctk.CTkFrame(root)
    secondpageframe.place(relx = 0.05 , rely = 0.05 , relwidth = 0.9,relheight = 0.9)
    Font = ctk.CTkFont('Playfair Display', 30)
    ctk.CTkLabel(
        master=secondpageframe,
        text='Enter your text',
        font=Font,
        text_color='white'
    ).pack(pady=10)
    # input widgets
    inputext = ctk.CTkTextbox(secondpageframe,
        width = 330,
        height = 150,
        )
    inputext.pack(pady = 10)
    input_button = ctk.CTkButton(
        master=secondpageframe,
        text='Generate',
        height=35,
        width=100,
        fg_color='black',
        hover_color='#121111',
        command = lambda: find_pattern(),
        font=ctk.CTkFont('arial', 15, 'bold'),
    )
    input_button.pack()
    # output widgets
    ctk.CTkLabel(
        master=secondpageframe,
        text=f'{patternchoise} results',
        font=Font,
        text_color='white'
    ).pack(pady=10)
    output_text = ctk.CTkTextbox(secondpageframe,
        width = 330,
        height = 150,
        )
    output_text.pack(pady = 10)
    output_button = ctk.CTkButton(
        master=secondpageframe,
        text='Coppy',
        height=35,
        width=100,
        fg_color='black',
        hover_color='#121111',
        command = lambda: coppy(output_text.get('0.0','end-1c')),
        font=ctk.CTkFont('arial', 15, 'bold'),
    )
    output_button.pack()
    # back button
    back = ctk.CTkImage(
                    light_image = Image.open('images/arrow.png'),
                    dark_image = Image.open('images/arrow.png')
                )
    back_button = ctk.CTkButton(
        master=secondpageframe,
        text='',
        image = back,
        width = 20,
        fg_color = 'transparent',
        hover_color = 'white',
        command = lambda:back(),
        font=ctk.CTkFont('arial', 15, 'bold'),
    )
    back_button.place(relx = 0.01 , rely = 0.01)
    # Logic functions 
    def find_pattern():
        # ['Phones-numbers', 'Emails']
        text = inputext.get('0.0','end-1c')
        if text !='':
            output_text.delete('0.0','end')
            if patternchoise == 'Phones-numbers':
                result = phones_patterns(text)
                if result:
                    for number in result:
                        output_text.insert('end',f'{number}\n')
                else:
                    output_text.insert('end','No match founded')
            else:
                result = emails_patterns(text)
                if result:
                    for number in result:
                        output_text.insert('end',f'{number}\n')
                else:
                    output_text.insert('end','No match founded')

        else:
            toplevelmessage()
            
    def toplevelmessage():
                toplevel = ctk.CTkToplevel()
                toplevel.overrideredirect(True)  
                Font = ctk.CTkFont('Helvetica', 18, 'bold')
                ctk.CTkLabel(
                    master=toplevel,
                    text='No text entered!',
                    text_color='white',
                    font=Font,
                    fg_color='transparent'
                ).pack(pady=10, padx=20)
                root.eval(f'tk::PlaceWindow {str(toplevel)} center')
                ctk.CTkButton(
                    toplevel,
                    text='close',
                    font=Font,
                    width=100,
                    height=30,
                    command = lambda:toplevel.destroy(),
                    fg_color='black'
        ).pack(pady=10)

    def coppy(text):
        if text:
            pyperclip.copy(text)
            output_button.configure(text = 'coppied')
            root.after(000,lambda:output_button.configure(text = 'coppy'))
    def back():
        secondpageframe.destroy()
        firstpage()
root = ctk.CTk()
customwindow()
patternchoise = None
firstpage()
root.mainloop()
