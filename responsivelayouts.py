import tkinter as tk 
from tkinter import ttk 
class App(tk.Tk):
	def __init__(self,title,size):
		super().__init__()
		self.title(title)
		self.geometry(size)
		self.frame = ttk.Frame(self)
		self.frame.pack(expand = True,fill='both')
		# creat object that have all size size logic
		Size(self,{300:self.small_layouts,600:self.medium_layouts})
		# run  

	def small_layouts(self):
		self.frame.pack_forget()
		self.frame = ttk.Frame(self)
		ttk.Label(self.frame, text = 'Label 1', background = 'red').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame, text = 'Label 2', background = 'green').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame, text = 'Label 3', background = 'blue').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame, text = 'Label 4', background = 'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		self.frame.pack(expand = True,fill='both')

	def medium_layouts(self):
		self.frame.pack_forget() 
		self.frame = ttk.Frame(self)
		self.frame1 = ttk.Frame(self.frame)
		self.frame2 = ttk.Frame(self.frame)
		ttk.Label(self.frame1, text = 'Label 1', background = 'red').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame1, text = 'Label 2', background = 'green').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame2, text = 'Label 3', background = 'blue').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		ttk.Label(self.frame2, text = 'Label 4', background = 'yellow').pack(expand = True, fill = 'both', padx = 10, pady = 5)
		self.frame.pack(expand = True,fill='both')
		self.frame1.pack(side = 'left',expand = True,fill='both')
		self.frame2.pack(side = 'left',expand = True,fill='both')

class Size: 
	def __init__(self,window,dic):
		self.window = window 
		self.dic = dic
		self.current_minsize = None
		self.window.bind('<Configure>',self.check_size)
		self.window.update()
		height = self.window.winfo_height()
		width = list(dic)[0]
		self.window.minsize(width,height)
	def check_size(self, event): 
		if event.widget == self.window:
			window_width = event.width
			checked_size = None
			for min_width in self.dic:
				delta = window_width - min_width
				if delta>=0:
					checked_size = min_width

			if checked_size != self.current_minsize:

				self.current_minsize = checked_size
				self.dic[self.current_minsize]()
App('responsive','400x400').mainloop()