_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Company_GUI"
_author_ = "Anand"

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from tkinter.messagebox import *
from PIL import Image, ImageTk

""" Provides a GUI interface to input data regarding company data using
Tkinter.
"""


class INPUT:
	def __init__(self):
		self.root = Tk()
		self.root.style = Style()
		self.root.style.theme_names()
		self.root.style.theme_use('vista')
		self.root.style.configure('.', font=('Comic Sans', 10))
		self.root.config(bg='#1234FF')

		self.b = ['', '', '', '', '', '', '']
		self.x1 = StringVar()
		self.x1.set("ENTER")
		self.x2 = StringVar()
		self.x2.set("YEAR")
		self.x3 = StringVar()
		self.x3.set(0)
		self.x4 = StringVar()
		self.x4.set(0)
		self.x5 = StringVar()
		self.x5.set(0)
		self.x6 = StringVar()
		self.x6.set(0)
		self.x7 = StringVar()
		self.x7.set(0)
		self.root.title('COMPANY')
		img = Image.open('background.jpg')
		size = (800, 500)
		img = img.resize(size, Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		self.frame1 = tk.Canvas(self.root, width=1200, height=1000, borderwidth=3, relief='groove')
		self.frame1.create_image(0, 0, image=img, anchor=NW)
		self.frame1.grid(rowspan=2, row=0, column=0, sticky='news', pady=(20, 20))
		self.fun1()
		img1 = Image.open('button.jpg')
		size = (200, 75)
		img1 = img1.resize(size, Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.submitbut = tk.Button(self.frame1, text='SUBMIT', image=img1, background='green', compound=CENTER,
								   foreground='white', font=('Roboto', 16, 'bold'), anchor='center', height=20,
								   width=100, relief='raised')
		self.submitbut.bind('<Button-1>', self.sub)
		self.submitbut.grid(rowspan=1, padx=(5, 5), pady=(5, 5), row=10, column=1, columnspan=2, sticky='news')

		img2 = Image.open('button.jpg')
		size = (200, 75)
		img2 = img2.resize(size, Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		resetbut = tk.Button(self.frame1, command=self.reset, image=img2, text='RESET', compound=CENTER,
							 font=('Roboto', 16, 'bold'), foreground='white', background='green', anchor='center',
							 height=20, width=100, relief='raised')
		resetbut.grid(row=8, sticky='news', column=6, padx=(50, 50), pady=(20, 20), columnspan=3, rowspan=2)
		img3 = Image.open('button.jpg')
		size = (200, 75)
		img3 = img3.resize(size, Image.ANTIALIAS)
		img3 = ImageTk.PhotoImage(img3)
		quitbut = tk.Button(self.frame1, image=img3, text='QUIT', compound=CENTER, font=('Roboto', 16, 'bold'),
							foreground='white', background='green', anchor='center', height=20, width=100,
							relief='raised', command=self.root.destroy)
		quitbut.grid(row=10, sticky='news', column=6, padx=(50, 50), pady=(20, 20), columnspan=3, rowspan=2)
		self.root.mainloop()

	def fun1(self):
		""" Open a Company window and return None. """

		complist = ['Company\nName', 'Academic\nSession',
					'Requirement', 'Criteria\n(> GPA)',
					'live ATKT\nAllowed', 'Dead ATKT\nAllowed', 'Package\n(LPA)']

		self.lab = tk.Label(self.frame1, justify='center', text="Welcome", foreground='yellow', bg='white',
							font=('Bookman Old Style', 14, 'bold'))
		self.lab.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=0, column=0, columnspan=8)

		self.l1 = tk.Label(self.frame1, justify='center', text=complist[0], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2)

		self.e1 = Entry(self.frame1, textvariable=self.x1, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=1, columnspan=4, ipady=5)
		self.e1.bind('<Button-1>', lambda _: self.x1.set(''))

		self.l2 = tk.Label(self.frame1, justify='center', text=complist[1], anchor='center', fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l2.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=5)

		self.menu1 = tk.Menubutton(self.frame1, textvariable=self.x2, background='white', font=('Bahnschrift', 12),
								   foreground='red', width=10)
		menu = Menu(self.menu1)
		self.menu1['menu'] = menu
		# self.menu1['menu'] = self.menu1.menu
		menu.add_radiobutton(label='2016-17', variable=self.x2, value='2016-17')
		menu.add_separator()
		menu.add_radiobutton(label='2017-18', variable=self.x2, value='2017-18')
		menu.add_separator()
		menu.add_radiobutton(label='2018-19', variable=self.x2, value='2018-19')
		menu.add_separator()
		self.menu1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=6, columnspan=3, ipadx=10, ipady=7)

		self.l3 = tk.Label(self.frame1, justify='center', text=complist[2], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l3.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4)

		self.e3 = Entry(self.frame1, textvariable=self.x3, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e3.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=1, columnspan=2, ipady=5)
		self.e3.bind('<Button-1>', lambda _: self.x3.set(''))

		self.l4 = tk.Label(self.frame1, justify='center', text=complist[3], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l4.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=5)

		self.e4 = Entry(self.frame1, textvariable=self.x4, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e4.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=6, columnspan=2, ipady=5)
		self.e4.bind('<Button-1>', lambda _: self.x4.set(''))

		self.l5 = tk.Label(self.frame1, justify='center', text=complist[4], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l5.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6)

		self.e5 = Entry(self.frame1, textvariable=self.x5, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e5.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=1, columnspan=2, ipady=5)
		self.e5.bind('<Button-1>', lambda _: self.x2.set(''))

		self.l6 = tk.Label(self.frame1, justify='center', text=complist[5], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l6.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=5)

		self.e6 = Entry(self.frame1, textvariable=self.x6, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e6.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=6, columnspan=2, ipady=5)
		self.e6.bind('<Button-1>', lambda _: self.x6.set(''))

		self.l7 = tk.Label(self.frame1, justify='center', text=complist[6], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l7.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8)

		self.e7 = Entry(self.frame1, textvariable=self.x7, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e7.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=1, columnspan=2, ipady=5)
		self.e7.bind('<Button-1>', lambda _: self.x7.set(''))

	def sub(self, event):
		if self.x1.get() != "ENTER":
			self.b[0] = self.x1.get()

		if self.x2.get() != "YEAR":
			self.b[6] = self.x2.get()

		if self.x3.get() != '' and int(self.x3.get()) >= 0:
			self.b[1] = self.x3.get()

		if self.x4.get() != '' and float(self.x4.get()) >= 6:
			self.b[2] = self.x4.get()

		if self.x5.get() != '' and int(self.x5.get()) >= 0:
			self.b[3] = self.x5.get()

		if self.x6.get() != '' and int(self.x6.get()) >= 0:
			self.b[4] = self.x6.get()

		if self.x7.get() != '' and float(self.x7.get()) >= 0:
			self.b[5] = self.x7.get()

		if '' in self.b:
			showwarning('Warning', 'Entered information does not match the requirements!')
		else:
			self.root.destroy()

	def reset(self):
		self.x1.set("ENTER")
		self.x2.set("YEAR")
		self.x3.set(0)
		self.x4.set(0)
		self.x5.set(0)
		self.x6.set(0)
		self.x7.set(0)
