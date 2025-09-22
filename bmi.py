import customtkinter as ctk 
class App(ctk.CTk):
	def __init__(self):
		super().__init__(fg_color = '#50BFAB')
		self.geometry('400x400')
		self.columnconfigure(0,weight =1)
		self.rowconfigure((0,1,2,3),weight =1,uniform = 'a')
		self.resizable(False,False)
		self.metricbool = ctk.BooleanVar(value = True)
		self.metricbool.trace('w',self.update_units)
		self.height = ctk.IntVar(value = 140)
		self.height.trace('w',self.bmiconverter)
		self.weight = ctk.DoubleVar(value = 60)
		self.weight.trace('w',self.bmiconverter)
		self.bmi =ctk.StringVar()
		self.bmiconverter()
		Label(self,self.bmi)
		self.weightobject =Weight(self,self.weight,self.metricbool)
		self.heightobject =Height(self,self.height,self.metricbool)
		Units(self,self.metricbool)
		self.bmiconverter()
		self.mainloop()
	def update_units(self,*args):
		self.weightobject.change_weight()
		self.heightobject.change_height(self.height.get())
	def bmiconverter(self,*args):
		heightmeter = self.height.get()/100
		weight = self.weight.get()
		bmi = round(weight/heightmeter**2,2)
		self.bmi.set(bmi)

class Label(ctk.CTkLabel):
	def __init__(self,parent,output):
		Font = ctk.CTkFont('Calibri',150,'bold')
		super().__init__(parent,text = 'output',font = Font,text_color = '#F2F2F2',textvariable = output)
		self.grid(column =0,
			row = 0, 
			rowspan = 2,
			sticky ='nswe'
			)

class Weight(ctk.CTkFrame):
	def __init__(self,parent,kgvar,metricbool):
		super().__init__(parent,fg_color = '#F2F2F2')
		self.weight = kgvar
		self.metricbool = metricbool
		self.grid(column = 0 , row = 2 , sticky = 'nswe',padx = 10,pady = 10)
		self.rowconfigure(0,weight = 1)
		self.columnconfigure(0,weight = 2,uniform = 'b')
		self.columnconfigure(1,weight = 1,uniform = 'b')
		self.columnconfigure(2,weight = 3,uniform = 'b')
		self.columnconfigure(3,weight = 1,uniform  ='b')
		self.columnconfigure(4,weight = 2,uniform ='b')
		Font = ctk.CTkFont('Calibri',26)
		ButtonMinus = ctk.CTkButton(self,text ='-',
			fg_color = '#E8E8E8',
			text_color = 'black',
			hover_color = '#D9D9D9',
			corner_radius=6,font = Font,
			command = lambda: self.change_weight(('minus','large')))
		SmallButtonMinus = ctk.CTkButton(self,text ='-',
			fg_color = '#E8E8E8',text_color = 'black',
			hover_color = '#D9D9D9',
			corner_radius=6,font = Font,
			command = lambda:self.change_weight(('minus','small')))
		self.kgvar_output = ctk.StringVar(value = kgvar.get())
		kgLabel = ctk.CTkLabel(self,text = '76',
			text_color = 'black',
			font = Font,
			textvariable =self.kgvar_output
			)
		ButtonPlus = ctk.CTkButton(self,text ='+',
			fg_color = '#E8E8E8',
			text_color = 'black',
			hover_color = '#D9D9D9',corner_radius=6,font = Font,
			command = lambda:self.change_weight(('plus','small')))
		SmallButtonPlus = ctk.CTkButton(self,text ='+',
			fg_color = '#E8E8E8',
			text_color = 'black',
			hover_color = '#D9D9D9',
			corner_radius=6,font=Font,
			command = lambda:self.change_weight(('plus','large')))

		ButtonMinus.grid(row = 0 , column = 0 , sticky = 'nswe',padx= 8 ,pady =8)
		SmallButtonMinus.grid(row =0 , column = 1 ,padx = 4,pady =8)
		kgLabel.grid(row =0 , column = 2)
		ButtonPlus.grid(row =0 , column = 3 ,padx = 4,pady =8)
		SmallButtonPlus.grid(row =0 , column = 4 , sticky = 'nswe',padx= 8 ,pady =8)
	def change_weight(self,info = None):
		if info:
			if self.metricbool.get():
				amount = 1 if info[1] == 'large' else 0.1
			else :
				amount =0.453592 if info[1] =='large' else 0.453592 /16
				print(amount)
			# print(amount)
			if info[0] =='plus':
				print(self.weight.get())
				self.weight.set(self.weight.get() + amount)
			else :
				self.weight.set((self.weight.get() - amount))
		if self.metricbool.get():
			self.kgvar_output.set(round(self.weight.get(),1))
		else:
			total_pounds = self.weight.get()*2.20462
			print(total_pounds)
			pounds = int(total_pounds)
			onses = (total_pounds - pounds) * 16
			self.kgvar_output.set(f'{pounds}lb{int(onses)}oz')

class Height(ctk.CTkFrame):
	def __init__(self,parent,mvar,metricbool):
		super().__init__(parent,fg_color='#F2F2F2')
		self.height = mvar
		self.metricbool = metricbool
		self.grid(row = 3,column = 0,sticky = 'nswe',padx = 10,pady = 10)
		self.rowconfigure(0,weight =1)
		slider = ctk.CTkSlider(self,
			fg_color = '#D9D9D9',
			progress_color='#50BFAB'
			,button_color = '#50BFAB',
			button_hover_color = '#D9D9D9',
			from_ = 100,
			to  =250,
			variable = mvar,
			command = self.change_height 
			)

		slider.pack(side='left',expand = True,fill ='x',padx = 10)
		Font = ctk.CTkFont('Calibri',26)
		self.output_var = ctk.StringVar()
		labele = ctk.CTkLabel(self,text= '1.85m',font = Font,text_color = 'black',textvariable = self.output_var)
		labele.pack(side = 'left',padx = 20)
		self.change_height(mvar.get())
	def change_height(self,amount):
		if self.metricbool.get():
			height = str(int(amount))
			m = height[0]
			cm = height[1:]
			self.output_var.set(f'{m}.{cm}m')
		else:
			inches = amount/2.54
			feet = inches/12
			self.output_var.set(f"{int(feet)}'{int(inches)}\"")
			

class Units(ctk.CTkLabel):
	def __init__(self,parent,metricbool):
		Font=ctk.CTkFont('Calibri',20,'bold')
		super().__init__(parent,text = 'metric',font = Font,text_color = '#0ba389')
		self.place(relx = 0.97 , rely = 0.05,anchor = 'ne')
		self.metricbool = metricbool
		self.bind('<Button>',self.change_units)
	def change_units(self,event):
		self.metricbool.set(not self.metricbool.get())
		if self.metricbool.get():
			self.configure(text = 'metric')
		else:
			self.configure(text = 'imperial')

if __name__ == '__main__':
	App()
else:
	print('not directly hahhaha')