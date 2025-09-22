import tkinter as tk
from tkinter import ttk

# exercise
# create a scrollbar

class ListFrame(ttk.Frame):
	def __init__(self, parent, text_data, item_height):
		super().__init__(master = parent)
		self.pack(expand = True, fill = 'both')

		# widget data
		self.text_data = text_data
		self.item_number = len(text_data)
		self.list_height = self.item_number * item_height

		# canvas 
		self.canvas = tk.Canvas(self, background = 'red', scrollregion = (0,0,self.winfo_width(),self.list_height))
		self.canvas.pack(expand = True, fill = 'both')
		# display frame
		self.frame = ttk.Frame(self)
		for index , items in enumerate(self.text_data):
			self.creat_widgets(index , items).pack(expand = True , fill = 'both',pady = 5)
		
		self.bind('<Configure>',self.update_size)
		self.canvas.bind_all('<MouseWheel>',lambda event : self.canvas.yview_scroll(-int((event.delta/40 )), "unit"))
		self.scroll = ttk.Scrollbar(self , orient = 'vertical',command= self.canvas.yview)
		self.canvas.configure(yscrollcommand = self.scroll.set)
	def update_size(self,event):
		if self.list_height >=self.winfo_height():
			height = self.list_height
			self.canvas.bind_all('<MouseWheel>',lambda event : self.canvas.yview_scroll(-int((event.delta/40 )), "unit"))
			self.scroll.place(relx = 1 , rely = 0 , relheight = 1 , anchor = 'ne')

		else :
			self.canvas.unbind_all('<MouseWheel>')
			height = self.winfo_height()
			self.scroll.place_forget()
		self.canvas.create_window((0,0),
			window = self.frame,
			width = self.winfo_width(),
			height = height
,			anchor = 'nw'
			)
		print(self.list_height)
	def creat_widgets(self,index , item):
		frame = ttk.Frame(self.frame)
		frame.columnconfigure((0,1,2,3,4),weight = 1 , uniform = 'a')
		frame.rowconfigure(0,weight = 1)
		ttk.Label(frame ,text = f'#{index}').grid(row = 0 , column =0 )
		ttk.Label(frame , text = f'{item[0]}').grid(row = 0 , column =1 )
		ttk.Button(frame , text = f'{item[1]}').grid(row = 0 , column= 2,columnspan = 3 , sticky = 'nswe' )
		return frame
# setup
window = tk.Tk()
window.geometry('500x400')
window.title('Scrolling')

text_list = [('label', 'button'),('thing', 'click'),('third', 'something'),('label1', 'button'),('label2', 'button'),('label3', 'button'),('label4', 'button')]
list_frame = ListFrame(window, text_list, 100)

# run 
window.mainloop()