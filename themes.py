import tkinter as tk 
from tkinter import ttk 
import tkinter as tk
from tkinter import ttk
class App(tk.Tk):
	def __init__(self,name,size):
		super().__init__()
		# setup main window
		self.title(name)
		self.geometry(size)
		# theme 
		self.tk.call('source','Azure/azure.tcl')
		self.tk.call('set_theme','dark')
		# widgets
		self.menu = Menu(self)
		self.main = Main(self)
		# run 
		self.mainloop()
class Menu(ttk.Frame):
	def __init__(self,parent):
		super().__init__(parent)
		self.place(x=0,y=0,relwidth=0.3,relheight=1)
		self.creat_widgets()
		#Menu layout 

	def creat_widgets(self):
		button1 = ttk.Button(self,text='button11')
		button2 = ttk.Button(self,text='button21')
		button3 = ttk.Button(self,text='button31')
		scale1 = ttk.Scale(self,orient='vertical')
		scale2 = ttk.Scale(self,orient='vertical')
		check_frame = ttk.Frame(self)
		check1 = ttk.Checkbutton(check_frame,text='check1')
		check2 = ttk.Checkbutton(check_frame,text='check2')
		entry1 = ttk.Entry(self)
		self.columnconfigure((0,1),weight=1,uniform='a')
		self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
		button1.grid(row=0,column=0,sticky='nsew',padx = 4 , pady = 4)
		button2.grid(row=0,column=1,sticky='nsew',padx = 4,pady = 4)
		button3.grid(row=1,column=0,columnspan=2,sticky='nsew',pady = 4,padx = 4)
		scale1.grid(row=2,column=0,rowspan=2,sticky='ns',pady=5)
		scale2.grid(row=2,column=1,rowspan=2,sticky='ns',pady=5)
		check_frame.grid(row=4,column=0,columnspan=2,sticky='nswe')
		check1.pack(side='left',expand=True)
		check2.pack(side='left',expand=True)
class Main(ttk.Frame):
	def __init__(self,parent):
		super().__init__(parent)
		self.place(relx=0.3,rely=0,relwidth=0.7,relheight=1)
		Main_frames(self,'pink','label','button')
		Main_frames(self,'skyblue','label2','button2')
class Main_frames(ttk.Frame):
		def __init__(self,parent,color,label_text,buton_text):
			super().__init__(parent)
			labele = ttk.Label(self,text=label_text,background=color)
			button = ttk.Button(self,text=buton_text)
			labele.pack(expand=True,fill='both')
			button.pack(expand=True,fill='both',pady=10)
			self.pack(side='left',expand=True,fill='both',padx=20,pady=20)

App('oopApp',('600x600'))