import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
class App(ctk.CTk):
	def __init__(self,name,size):
		super().__init__()
		# setup main window
		self.title(name)
		self.geometry(size)
		# widgets
		self.menu = Menu(self)
		self.main = Main(self)
		# run 
		self.mainloop()
class Menu(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.place(x=0,y=0,relwidth=0.3,relheight=1)
		self.creat_widgets()
		#Menu layout 

	def creat_widgets(self):
		button1 = ctk.CTkButton(self,text='button11')
		button2 = ctk.CTkButton(self,text='button21')
		button3 = ctk.CTkButton(self,text='button31')
		scale1 = ctk.CTkSlider(self,orientation='vertical')
		scale2 = ctk.CTkSlider(self,orientation='vertical')
		check_frame = ctk.CTkFrame(self,fg_color = 'transparent')
		check1 = ctk.CTkCheckBox(check_frame,text='check1')
		check2 = ctk.CTkCheckBox(check_frame,text='check2')
		entry1 = ctk.CTkEntry(self)
		self.columnconfigure((0,1),weight=1,uniform='a')
		self.rowconfigure((0,1,2,3,4),weight=1,uniform='a')
		button1.grid(row=0,column=0,sticky='nsew',padx = 4 , pady = 4)
		button2.grid(row=0,column=1,sticky='nsew',padx = 4 , pady = 4)
		button3.grid(row=1,column=0,columnspan=2,sticky='nsew',padx = 4 , pady = 4)
		scale1.grid(row=2,column=0,rowspan=2,sticky='ns',pady=5)
		scale2.grid(row=2,column=1,rowspan=2,sticky='ns',pady=5)
		check_frame.grid(row=4,column=0,columnspan=2,sticky='nswe',padx = 2)
		check1.pack(side='left',expand=True)
		check2.pack(side='left',expand=True)
class Main(ctk.CTkFrame):
	def __init__(self,parent):
		super().__init__(parent)
		self.place(relx=0.3,rely=0,relwidth=0.7,relheight=1)
		Main_frames(self,'pink','label','button')
		Main_frames(self,'skyblue','label2','button2')
class Main_frames(ctk.CTkFrame):
		def __init__(self,parent,color,label_text,buton_text):
			super().__init__(parent)
			labele = ctk.CTkLabel(self,text=label_text,fg_color=color)
			button = ctk.CTkButton(self,text=buton_text)
			labele.pack(expand=True,fill='both')
			button.pack(expand=True,fill='both',pady=10)
			self.pack(side='left',expand=True,fill='both',padx=20,pady=20)

App('oopApp',('600x600'))