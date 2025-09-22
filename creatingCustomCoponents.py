import tkinter as tk 
from tkinter import ttk
# class approach
class segements(ttk.Frame):
	def __init__(self ,parent, label_text , button_text , background):
		super().__init__(parent)
		self.rowconfigure(0 , weight = 1)
		self.columnconfigure((0,1,2) , weight = 1 , uniform = 'a')
		ttk.Label(self,text = label_text , background = background).grid(row =0 , column = 0,sticky='nswe')
		ttk.Button(self,text = button_text).grid(row = 0 , column = 1 , sticky = 'nswe')
		# from function 
		container(self,'button').grid(row=0 , column = 2 , sticky = 'nswe')
		self.pack(expand=True,fill='both')
		print('working ')


#exercise function 
def container(parent,button_name):
	frame = ttk.Frame(parent)
	ttk.Entry(frame).pack(expand = True, fill = 'both')
	ttk.Button(frame,text= button_name).pack(expand = True, fill = 'both')
	return frame
# functioanl approch
# def segment(parent ,label_text , button_text,color):
# 	frame = ttk.Frame(parent)
# 	frame.rowconfigure(0 , weight = 1)
# 	frame.columnconfigure((0,1,2) , weight = 1 , uniform = 'a')
# 	ttk.Label(frame,text = label_text , background = color).grid(row =0 , column = 0,sticky='nswe')
# 	ttk.Button(frame,text = button_text).grid(row = 0 , column = 1 , sticky = 'nswe')
# 	return frame
window = tk.Tk()
window.title('compenentes')
window.geometry('600x600')
# set them as objects
segements(window,'text1','button1','pink')
segements(window,'text2','button2','skyblue')
segements(window,'text3','button3','purple')
segements(window,'text4','button4','gray')
segements(window,'text5','button5','LimeGreen')
#sets them as functions 
# segment(window,'text1','button1','pink').pack(expand = True , fill = 'both' , pady = 10)
# segment(window,'text2','button2','skyblue').pack(expand = True , fill = 'both' , pady = 10)
# segment(window,'text3','button3','purple').pack(expand = True , fill = 'both' , pady = 10)
# segment(window,'text4','button4','gray').pack(expand = True , fill = 'both' , pady = 10)
# x =segment(window,'text5','button5','LimeGreen')
# x.pack(expand = True , fill = 'both' , pady = 10)
window.mainloop()