import customtkinter as ctk
from PIL import Image

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode("dark")
        self.title("pomodoro")
        self.geometry('500x350')
        self.resizable(False, False)
        self.iconbitmap('empty.ico')
        self.color = ctk.StringVar(value='#20c997')

        # timer settings
        self.time = 25                   # minutes
        self.totale = self.time * 60     # seconds
        self.remaining = self.totale

        # UI state
        self.running = False
        self.pomodoro_time = ctk.StringVar(value="25:00")
        self.mainapp()
        self.bar = sidebar(self) 
        self.togle = True

    def mainapp(self):
        def fontcustom(size=0, format=None):
            if format == 'bold':
                return ctk.CTkFont('arial', size, format)
            else:
                return ctk.CTkFont('arial', size)

        # Task label
        self.projectlabele = ctk.CTkLabel(
            self,
            text="Task: Study",
            font=fontcustom(30, 'bold'),
            text_color=self.color.get(),
            corner_radius=10
        )
        self.projectlabele.place(relx=0.5, rely=0.15, anchor='center')

        # Timer label
        self.timelabel = ctk.CTkLabel(
            master=self,
            textvariable=self.pomodoro_time,
            font=fontcustom(100, 'bold'),
            text_color=self.color.get()
        )
        self.timelabel.place(relx=0.5, rely=0.45, anchor='center')

        # Buttons
        buttonframe = ctk.CTkFrame(self, fg_color='transparent')

        self.play_button = ctk.CTkButton(
            buttonframe,
            text='Play',
            image=self.images('play-button.png', (15, 15)),
            fg_color=self.color.get(),
            hover_color='#76c2ab',
            compound='left',
            font=fontcustom(20),
            height=40,
            corner_radius=30,
            command=self.toggle_timer,
        )
        self.play_button.pack(side='left', padx=5)

        self.reset_button = ctk.CTkButton(
            buttonframe,
            text='Reset',
            image=self.images('refresh-arrow.png', (15, 15)),
            fg_color=self.color.get(),
            hover_color='#76c2ab',
            compound='left',
            font=fontcustom(20),
            height=40,
            corner_radius=30,
            command=self.reset_timer
        )
        self.reset_button.pack(side='right', padx=5)

        buttonframe.place(relx=0.15, rely=0.8, relwidth=0.7)

        # Settings button
        self.setting = ctk.CTkButton(
            self,
            text='setting',
            font = fontcustom(15,'bold'),
            # image=self.images('settings.png', (20, 20)),
            fg_color='transparent',
            hover_color='gray',
            text_color ='#20c997',
            width=5,
            height=5,
            corner_radius=30,
            cursor='hand2',
            command=lambda: self.sidebarshow()
        )
        self.setting.place(relx=0.88, rely=0.05)

    def images(self, imagename, size=None):
        return ctk.CTkImage(
            light_image=Image.open(f'pomodoroimages/{imagename}'),
            dark_image=Image.open(f'pomodoroimages/{imagename}'),
            size=(50, 50) if size is None else size
        )

    # Toggle between Play and Pause
    def toggle_timer(self):
        if not self.running:
            self.running = True
            self.play_button.configure(
                image=self.images('pause.png', (15, 15)),
                text="Pause"
            )
            self.update_timer()
        else:
            self.running = False
            self.play_button.configure(
                image=self.images('play-button.png', (15, 15)),
                text="Play"
            )
            self.update_timer()

    # Update the timer every second
    def update_timer(self):
        if self.running and self.remaining >= 0:
            minutes = self.remaining // 60
            seconds = self.remaining % 60
            self.pomodoro_time.set(f"{minutes:02}:{seconds:02}")
            self.remaining -= 1
            self.after(1000, self.update_timer)

    # Reset timer
    def reset_timer(self):
        self.running = False
        self.remaining = self.totale
        self.pomodoro_time.set(f"{self.time:02}:00")
        self.play_button.configure(
            image=self.images('play-button.png', (15, 15)),
            text="Play"
        )

    def sidebarshow(self):
        if self.togle:
            self.after(100, self.bar.place(relx=-1, rely=0.05, relwidth=0.84, relheight=0.9))
            self.togle = False
        else:
            self.after(100, self.bar.place(relx=0.03, rely=0.05, relwidth=0.84, relheight=0.9))
            self.togle = True


class sidebar(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        self.parent = parent
        super().__init__(master=self.parent)
        self.place(relx=0.03, rely=0.05, relwidth=0.84, relheight=0.9)

        ctk.CTkLabel(
            self,
            text='Edit Theme',
            font=ctk.CTkFont('Helvetica', 30, 'bold')
        ).pack(pady=10)

        self.tasknamevar = ctk.StringVar()
        self.edits('Task-name :', self.tasknamevar)

        self.durationvar = ctk.StringVar()
        self.edits('Duration   :', self.durationvar)

        self.bgvar = ctk.StringVar()
        self.edits('bg-color  :', self.bgvar)

        self.widgetcolorvar = ctk.StringVar()
        self.edits('widget-bg:', self.widgetcolorvar)
        self.text_colorvar = ctk.StringVar()
        self.edits('text-color:',self.text_colorvar)
        # Save button
        ctk.CTkButton(
            self,
            text='Save',
            font=ctk.CTkFont('arial', 15, 'bold'),
            fg_color='#20c997',
            corner_radius=5,
            hover_color ='#20a990',
            text_color ='white',
            height = 20,
            width=50,
            command = lambda:self.save()
        ).pack(pady=10)

    def edits(self, text, var):
        frame = ctk.CTkFrame(self)
        frame.pack(expand=True, fill='both', pady=10, padx=10)

        ctk.CTkLabel(
            frame,
            text=text,
            font=ctk.CTkFont('arial', 20, 'bold'),
            text_color='#20c997'
        ).pack(side='left', fill='both', expand=True)

        ctk.CTkEntry(
            frame,
            text_color='white',
            textvariable=var,
            corner_radius=10,
            placeholder_text='(Optional)',
            placeholder_text_color='black'
        ).pack(side='right', expand=True, fill='both')

    def save(self):
        self.togle = False
        self.notification()

        # Background color
        if self.checkcolor(self.bgvar.get()):
            self.parent.configure(fg_color=self.bgvar.get())

        # Widget colors
        if self.checkcolor(self.widgetcolorvar.get()):
            color = self.widgetcolorvar.get()
            self.parent.projectlabele.configure(text_color=color)
            self.parent.timelabel.configure(text_color=color)
            self.parent.reset_button.configure(fg_color=color, hover_color=color)
            self.parent.play_button.configure(fg_color=color, hover_color=color)
            self.parent.setting.configure(text_color =color)
            
        # Task name
        if len(self.tasknamevar.get()) <= 15:
            self.parent.projectlabele.configure(text=f'Task: {self.tasknamevar.get()}')
        elif len(self.tasknamevar.get()) <= 25:
            self.parent.projectlabele.configure(text=f'Task:\n{self.tasknamevar.get()}')

        # Duration (update timer)
        if self.durationvar.get().isdecimal():
            minutes = int(self.durationvar.get())
            self.parent.time = minutes
            self.parent.totale = minutes * 60
            self.parent.remaining = self.parent.totale
            self.parent.pomodoro_time.set(f"{minutes:02}:00")
        if self.checkcolor(self.text_colorvar.get()):
            color = self.text_colorvar.get()
            self.parent.play_button.configure(text_color =color)
            self.parent.reset_button.configure(text_color =color)
        # Close sidebar
        self.after(100, self.place(relx=-1, rely=0.05, relwidth=0.84, relheight=0.9))
    def checkcolor(self, color):
        try:
            self.parent.winfo_rgb(color)  # use parent window to validate
            return True
        except:
            print('Invalid color')
            return False

    def notification(self):
        text = '"  Current modification \nwill be applied only \nif they are valid!  "'
        toplevel = ctk.CTkToplevel(fg_color = '#0F1C24')
        toplevel.wm_attributes("-transparentcolor", "#0F1C24")
        toplevel.overrideredirect(True)  # hides title bar (including X and -)
        topframe = ctk.CTkFrame(toplevel, fg_color='#0F1C2E', corner_radius=20)
        Font = ctk.CTkFont('Helvetica', 16, 'bold')
        ctk.CTkLabel(
            master=topframe,
            text=text,
            text_color='white',
            font=Font,
            fg_color='transparent',
            image=self.parent.images('information.png',(30,30)),
            compound='top'
        ).pack(pady=10, padx=20)
        self.parent.eval(f'tk::PlaceWindow {str(toplevel)} center')
        ctk.CTkButton(
            topframe,
            text='close',
            font=Font,
            command=lambda: toplevel.destroy(),
            width=100,
            height=30,
            fg_color='#20c997'
        ).pack(pady=10)
        topframe.pack(expand=True, fill='both')


if __name__ == '__main__':
    app = App()
    app.mainloop()
