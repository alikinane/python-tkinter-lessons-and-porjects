import customtkinter as ctk
from todosetting import *
from tkinter import messagebox
import time 
from PIL import Image
import json
class App(ctk.CTk):
    def __init__(self, background=UI_COLORS['background']):
        super().__init__(fg_color=background)

        self.title('To do')
        self.iconbitmap('images/todo.ico')
        self.geometry('400x600')
        self.resizable(False, False)
        self.columnconfigure(0, weight=1)
        self.rowconfigure((0, 1, 2, 3, 4, 5), weight=1, uniform='a')

        # variables :
        self.entry_var = ctk.StringVar(value = ' ')
        self.tasklist = []
        self.index = len(self.tasklist)
        self.task = 0
        self.tasktext  = ctk.StringVar(value = f'0 task(s)')
        self.checktask = 0
        self.checktasktext  = ctk.StringVar(value = f'0 task(s) completed')
        self.checktaskinfo = ctk.StringVar(value = f'{self.tasktext.get()}\n{self.checktasktext.get()}')
        self.widgets()
        self.loadtasks()
        self.mainloop()

    def widgets(self):
        titlefont = ctk.CTkFont('Inter', 30, 'bold')
        holderfont = ctk.CTkFont('Inter', 16)
        seconds = time.time()
        currenttime = time.ctime(seconds)
        listime = currenttime.split(' ')
        date = f'{listime[0]}/{listime[1]}/{listime[4]}'
        Labels(self, 0, 0, titlefont, UI_COLORS['title_text'], f'To do list\n{date}')

        # entry
        TasksEntry(self, holderfont, self.entry_var, self.Addbutton)

        # task box
        self.taskbox = TaskBox(self, 0, 2)
          # cheked task 
        checkedtasks(self,0 ,5,holderfont,UI_COLORS['title_text'],self.checktaskinfo)
    def Addbutton(self, text='newtask',status = False):
        if self.entry_var.get() != '':
            check_variable = ctk.IntVar()
            if status:
                check_variable.set(1)
            task_frame = ctk.CTkFrame(self.taskbox, fg_color="transparent")
            task_frame.pack(fill='x', pady=10, padx=10)
            checkbox = ctk.CTkCheckBox(
                task_frame,
                text=text,
                font=('arial', 20),
                corner_radius=20,
                fg_color='#241B38',
                hover_color='#241B38',
                border_width=3,
                variable=check_variable,
                command=lambda: self.checkcommand(check_variable.get()),
                onvalue=1,
                offvalue=0,
            )
            checkbox.pack(side='left', fill='x', expand=True)
            ctkimage = ctk.CTkImage(
                    light_image = Image.open('images/trash-bin.png'),
                    dark_image = Image.open('images/trash-bin.png')
                )
            del_button = ctk.CTkButton(
                master=task_frame,
                text = '',
                image = ctkimage,
                width = 30,
                corner_radius=50,
                fg_color='transparent',
                hover_color = 'red',
                font=('arial', 20, 'bold'),
                text_color='white',
                command=lambda frame = task_frame:self.deletetasks(frame)   # optional delete function
            )
            del_button.pack(side='right', padx=5)
            self.tasklist.append({
                    'text': text if text != 'newtask' else self.entry_var.get(),
                    'var': check_variable,
                    'checkbox': checkbox,
                    'frame': task_frame
                        })
            self.savetasks()
            self.task +=1
            self.tasktext.set(f'{self.task} task(s)')
            self.checktaskinfo.set(f'{self.tasktext.get()}\n{self.checktasktext.get()}')
        else : 
            messagebox.showerror("error",'No task entered')
    def checkcommand(self,value):
        if value:
            self.checktask +=1
            self.checktasktext.set(f'{self.checktask} task(s) completed')
        else:
            self.statue = 0
            self.checktask -=1
            self.checktasktext.set(f'{self.checktask} task(s) completed')
        self.checktaskinfo.set(f'{self.tasktext.get()}\n{self.checktasktext.get()}')
        self.savetasks()

    def deletetasks(self,frame):
        for task in self.tasklist:
            if  task['frame'] == frame: 
                frame.destroy()
                self.tasklist.remove(task)
                self.savetasks()
                self.task-=1
                self.tasktext.set(f'{self.task} task(s)')
                self.checktaskinfo.set(f'{self.tasktext.get()}\n{self.checktasktext.get()}')
    def savetasks(self):
        taskdata = []
        for data in self.tasklist:
            taskdata.append(
                        {
                            'text':data['text'],
                            'status': bool(data['var'].get())
                        }
                    )
        with open('C:\\Users\\nonoa\\OneDrive\\Desktop\\data.json','w') as f:
            json.dump(taskdata,f,indent = 4)
    def loadtasks(self):
        with open('C:\\Users\\nonoa\\OneDrive\\Desktop\\data.json','r') as f : 
            tasksdata = json.load(f)
            print(tasksdata)
            for task in tasksdata:
                if task['status']:
                    self.checktask +=1
                    self.checktasktext.set(f'{self.checktask} task(s) completed')
                self.checktaskinfo.set(f'{self.tasktext.get()}\n{self.checktasktext.get()}')
                self.Addbutton(task['text'],status = task['status'])
class Labels(ctk.CTkLabel):
    def __init__(self, parent, col, row, font, color, text='text',var = None):
        super().__init__(
            master=parent,
            font=font,
            text_color=color,
            text=text,
            textvariable = var if var else text
        )
        self.grid(column=col, row=row, sticky='ns')

class TasksEntry(ctk.CTkFrame):
    def __init__(self, parent, font, var, func, col=0, row=1):
        super().__init__(
            master=parent,
            fg_color='transparent'
        )
        self.grid(column=col, row=row, sticky='nswe')

        entry = ctk.CTkEntry(
            master=self,
            corner_radius=50,
            fg_color='#4f3f73',
            text_color='#E0D6F6',
            textvariable=var,
            font=font,
            placeholder_text='Enter a task',
        )
        entry.pack(expand=True, fill='both', padx=10)

        Addbutton = ctk.CTkButton(
            master=self,
            text='Add-Task',
            fg_color='#4f3f73',
            hover_color = '#241B38',
            font=font,
            corner_radius=30,
            command=lambda: [func(var.get()), var.set('')]
        )
        Addbutton.pack(expand=True, fill='y', pady=15)

class TaskBox(ctk.CTkScrollableFrame):
    def __init__(self, parent, col, row, background='#4f3f73'):
        super().__init__(
            master=parent,
            fg_color=background,
            corner_radius=20,
        )

        self.grid(
            column=col,
            row=row,
            rowspan=3,
            sticky='nswe',
            padx=30,
            pady=15
        )

class checkedtasks(Labels):
    def __init__(self,parent,col , row , font , color , text='o',var=None):
        super().__init__(
            parent = parent,
            col = col , 
            row = row,
            font =font , 
            color = color,
            text = text,
            var = var
            )
if __name__ == '__main__':
    App()
