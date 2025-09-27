import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color ='#171616')
        self.title("pomodoro")
        self.geometry('450x300')
        self.resizable(False,False)
        self.mainapp()
        self.mainloop()

    def mainapp(self):
        def fontcustom(size=0,format=None):
            if format =='bold':
                return ctk.CTkFont('arial', size, format)
            else:
                return ctk.CTkFont('arial', size)
        projectlabele = ctk.CTkLabel(
            self,
            text="Task: Study",
            font=fontcustom(30,'bold'),
            text_color='#20c997',
            corner_radius=10
        )
        projectlabele.place(relx=0.5, rely=0.15, anchor='center')

        timelabel = ctk.CTkLabel(
            master=self,
            text='25:00',
            font=fontcustom(100,'bold'),
            text_color='#20c997'
        )
        timelabel.place(relx=0.5, rely=0.45, anchor='center')
        buttonframe =ctk.CTkFrame(self,fg_color='transparent')
        play_button = ctk.CTkButton(
            buttonframe,
            text='Play',
            image=self.images('play-button.png',(15,15)),
            fg_color='#20c997',
            hover_color='gray',
            compound= 'left',
            font = fontcustom(20),
            height= 40,
            corner_radius= 30,
            
        )
        play_button.pack(side ='left')
        reset_button = ctk.CTkButton(
            buttonframe,
            text='Reset',
            image=self.images('refresh-arrow.png',(15,15)),
            fg_color='#20c997',
            hover_color='gray',
            compound= 'left',
            font = fontcustom(20),
            height= 40,
            corner_radius= 30,
            
        )
        reset_button.pack(side ='right')  
        buttonframe.place(relx =0.15 ,rely = 0.8 ,relwidth =0.7)
        setting = ctk.CTkButton(
            self,
            text='',
            image=self.images('settings.png',(20,20)),
            fg_color='#171616',
            hover_color='#171616',
            width =10,
            corner_radius= 30,
            
        )
        setting.place(relx =0.9,rely = 0.05)
    def images(self,imagename,size =None):
        self.image = ctk.CTkImage(
            light_image=Image.open(f'pomodoroimages/{imagename}'),
            dark_image=Image.open(f'pomodoroimages/{imagename}'),
            size=(50, 50) if size ==None else size
        )
        return self.image
if __name__ == '__main__':
    App()
