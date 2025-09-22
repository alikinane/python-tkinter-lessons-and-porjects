import customtkinter as ctk
import random
from ttkbootstrap.dialogs import Messagebox
from PIL import Image
class App(ctk.CTk):
    def __init__(self):
        super().__init__(fg_color='#2C3E50')
        self.title('X/O')
        self.geometry("600x700")
        self.resizable(False, False)
        self.buttons = {}
        self.mode =ctk.StringVar(value ='')
        self.current_player =ctk.StringVar(value ='X')
        self.start_menu()
        self.mainloop()
    def start_menu(self):
        self.frame = ctk.CTkFrame(self, fg_color='#3b64b3')
        self.frame.place(relx=0.2, rely=0.2, relwidth=0.6, relheight=0.6)

        Font = ctk.CTkFont(family='Helvetica', size=30, weight="bold")
        ctk.CTkLabel(self.frame, text='Choose Game Mode', font=Font, text_color='white').pack(pady=20)

        # Create a container frame for buttons
        button_frame = ctk.CTkFrame(self.frame, fg_color='#3b64b3', corner_radius=0)
        button_frame.pack(pady=20, fill='x', expand=True)
        pvpimage = ctk.CTkImage(
                    light_image = Image.open('images/pvp.png'),
                    dark_image = Image.open('images/pvp.png')
                )
        robotimage = ctk.CTkImage(
                    light_image = Image.open('images/artificial-intelligence.png'),
                    dark_image = Image.open('images/artificial-intelligence.png')
                )

        # PvP Button
        Font = ctk.CTkFont('arial',20,'bold')
        pvpbutton = ctk.CTkButton(button_frame, 
            text='vs player', fg_color='white', 
            text_color='black', width=150, 
            height=80,image =pvpimage,
            font =Font,compound = 'top'
            ,hover_color = '#c8d1e3'
            ,cursor ='hand2',
            command = lambda : self.mode_choice('pvp')
            )
        pvpbutton.pack(side='left', expand=True, padx=10)

        # Robot Button
        robotbutton = ctk.CTkButton(button_frame, text='vs robot', 
            fg_color='white', text_color='black', width=150, height=80,image =robotimage,
            font =Font,compound ='top',
            hover_color = '#c8d1e3',
            cursor ='hand2',
            command = lambda : self.mode_choice('robot')

            )
        robotbutton.pack(side='left', expand=True, padx=10)
    def mode_choice(self,mode):
        self.mode.set(mode)
        self.frame.destroy()
        self.widgets()
    def widgets(self):
        Font = ctk.CTkFont('Arial',20,'bold')
        text_mode =ctk.CTkLabel(self,text = f'Mode\n{self.mode.get()}',text_color ='white',font =Font)
        text_mode.place(relx =0.5 ,rely = 0.05,anchor = 'center')
        self.quit = ctk.CTkButton(self,
            text = 'Quit',
            fg_color = 'white',
            font= Font,
            hover_color = '#c8d1e3'
            ,cursor ='hand2',
            text_color = 'black',
            command = lambda:self.destroy())
        self.quit.place(relx = 0.35,rely = 0.95,anchor ='center')
        self.back = ctk.CTkButton(self,
            text = 'Back',
            fg_color = 'white',
            font= Font,
            hover_color = '#c8d1e3'
            ,cursor ='hand2',
            text_color = 'black',
            command = lambda:[self.mainframe.destroy(),self.start_menu(),self.quit.destroy(),self.back.destroy(),text_mode.destroy(),self.buttons.clear()])
        self.back.place(relx = 0.65,rely = 0.95,anchor ='center')
        self.mainframe = MainFrame(self, '#3471ad')
        for r in range(3):
            for c in range(3):
                button = ctk.CTkButton(
                    self.mainframe,
                    text=' ',
                    corner_radius=0,
                    fg_color='white',
                    font=ctk.CTkFont(family="Arial", size=50, weight="bold"),
                    command=lambda r=r, c=c: self.on_click(r, c)
                )
                button.grid(row=r, column=c, sticky='nswe', padx=5, pady=5)
                self.buttons[(r, c)] = button

    def on_click(self, r, c):
        btn = self.buttons[(r, c)]
        if btn.cget("text") != ' ':
            return
        if self.mode.get() =='pvp':
            btn.configure(text=self.current_player.get(),text_color='#75b9f0' if self.current_player.get() == "X" else '#f07a75')
            self.current_player.set('O') if self.current_player.get() == 'X' else self.current_player.set('X')
            result = self.wincheck()
            if result == "Tie":
                self.toplevel(result)
                self.current_player.set('X')
                return
            if result == "X":
                self.toplevel(result)
                self.current_player.set('X')
                return
            if result == "O":
                self.toplevel(result)
                return
        else:
            btn.configure(text='X',text_color='#75b9f0')
            result = self.wincheck()
            if result == "Tie":
                self.toplevel(result)
                self.current_player.set('X')
                return
            if result == "X":
                self.toplevel(result)
                self.current_player.set('X')
                return  
            self.after(400, self.robot_turn)


    def robot_turn(self):
        empty_cells = [pos for pos, button in self.buttons.items() if button.cget('text') == ' ']
        if empty_cells:
            current_cell = random.choice(empty_cells)
            btn = self.buttons[current_cell]
            btn.configure(text="O", text_color='#f07a75')

            result = self.wincheck()
            if result == "Tie":
                self.toplevel(result)
                return
            if result == "O":
                self.toplevel(result)
                return
    def toplevel(self,result):
        if result =='X':
            text = 'Player X won'
        elif result == 'O':
            text = 'Player O won'
        else:
            text = 'it is a tie'
        toplevel = ctk.CTkToplevel()
        toplevel.overrideredirect(True)  # hides title bar (including X and -)
        Font = ctk.CTkFont('Helvetica',18,'bold')
        ctk.CTkLabel(master=toplevel,text = text,text_color = 'white',font = Font ,fg_color = 'transparent').pack(pady =10,padx =20)
        self.eval(f'tk::PlaceWindow {str(toplevel)} center')
        ctk.CTkButton(toplevel,
            text = 'close',
            font = Font ,
            command = lambda : [toplevel.destroy()],
            width = 100,
            height = 30,
            fg_color = '#2C3E50'
            ).pack(pady = 10)
    def wincheck(self):
        combos = [
            [(0, 0), (0, 1), (0, 2)],
            [(1, 0), (1, 1), (1, 2)],
            [(2, 0), (2, 1), (2, 2)],
            [(0, 0), (1, 0), (2, 0)],
            [(0, 1), (1, 1), (2, 1)],
            [(0, 2), (1, 2), (2, 2)],
            [(0, 0), (1, 1), (2, 2)],
            [(0, 2), (1, 1), (2, 0)]
        ]
        for combo in combos:
            win_moves = [self.buttons[pos].cget("text") for pos in combo]
            buttons = [self.buttons[pos] for pos in combo]
            if win_moves[0] != ' ' and win_moves.count(win_moves[0]) == 3:
                for btn in buttons:
                    btn.configure(fg_color='#2ff757')
                return win_moves[0]   # "X" or "O"

        # Tie check
        if not any(button.cget('text') == ' ' for button in self.buttons.values()):
            return "Tie"

        return None  # game continues

    def reset_board(self):
        for pos, button in self.buttons.items():
            button.configure(text=' ', fg_color='white',text_color = 'black')  # no text_color reset
        self.update_idletasks()  # force redraw

class MainFrame(ctk.CTkFrame):
    def __init__(self, parent, color):
        super().__init__(master=parent, fg_color=color, corner_radius=0)
        self.columnconfigure((0, 1, 2), weight=1, uniform='a')
        self.rowconfigure((0, 1, 2), weight=1, uniform='a')
        self.pack(expand=True, fill='both', pady=90, padx=80)


if __name__ == '__main__':
    App()
