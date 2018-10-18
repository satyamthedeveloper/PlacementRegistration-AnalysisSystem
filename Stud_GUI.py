_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Stud_GUI"
_author_ = "Anand"

from tkinter import *
from tkinter.ttk import *
import tkinter as tk
from Logistic_Regression import *
from tkinter.messagebox import *
from PIL import Image, ImageTk

""" Provides a GUI interface to input data regarding company data using
Tkinter.
"""


class INPUT:
	def __init__(self):
		self.root = Tk()
		self.root.config(background='#1234FF')
		self.root.style = Style()
		self.root.style.theme_names()
		self.root.style.theme_use('vista')
		self.root.style.configure('.', font=('Verdana', 10))
		self.b = ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']
		self.x1 = StringVar()
		self.x1.set("String")
		self.x2 = StringVar()
		self.x2.set("String")
		self.x3 = StringVar()
		self.x3.set("String")
		self.x4 = StringVar()
		self.x4.set("String")
		self.x5 = StringVar()
		self.x5.set('YEAR')
		self.x6 = StringVar()
		self.x6.set("ENTER")
		self.x7 = StringVar()
		self.x7.set('10-digit number')
		self.x8 = StringVar()
		self.x8.set("Numeric")
		self.x9 = StringVar()
		self.x9.set("Numeric")
		self.x10 = StringVar()
		self.x10.set("Numeric")
		self.x11 = StringVar()
		self.x11.set("Numeric")
		self.x12 = StringVar()
		self.x12.set("Numeric")
		self.x13 = StringVar()
		self.x13.set('Numeric')
		self.x14 = StringVar()
		self.x14.set('Numeric')
		self.x15 = StringVar()
		self.x15.set('Numeric')
		self.x16 = StringVar()
		self.x16.set('Numeric')
		self.x17 = StringVar()
		self.x17.set('Numeric')
		self.x18 = StringVar()
		self.x18.set("String")
		self.x19 = StringVar()
		self.x19.set('Out of 100')
		self.x20 = StringVar()
		self.x20.set('Out of 100')
		self.x21 = StringVar()
		self.x21.set('Out of 100')
		self.x22 = StringVar()
		self.x22.set('Out of 100')
		img = Image.open('background.jpg')
		size = (1000, 1600)
		img = img.resize(size, Image.ANTIALIAS)
		img = ImageTk.PhotoImage(img)
		self.frame1 = tk.Canvas(self.root, width=1200, height=1000, borderwidth=3, relief='groove')
		self.frame1.create_image(0, 0, image=img, anchor=NW)
		self.frame1.grid(rowspan=2, row=0, column=0, sticky='news', pady=(20, 20))
		self.root.title(
			'                                                                                                                                                STUDENT                                                                ')
		# self.root.wm_iconbitmap(bitmap = 'reset.png')
		self.fun1()
		img1 = Image.open('button.jpg')
		size = (200, 75)
		img1 = img1.resize(size, Image.ANTIALIAS)
		img1 = ImageTk.PhotoImage(img1)
		self.submitbut = tk.Button(self.frame1, text='SUBMIT', image=img1, background='green', compound=CENTER,
								   foreground='white', font=('Roboto', 16, 'bold'), anchor='center', height=20,
								   width=100, relief='raised')
		self.submitbut.bind('<Button-1>', self.sub)
		self.submitbut.grid(rowspan=3, padx=(10, 10), pady=(10, 10), row=10, column=11, columnspan=2, sticky='news')
		img2 = Image.open('button.jpg')
		size = (200, 75)
		img2 = img2.resize(size, Image.ANTIALIAS)
		img2 = ImageTk.PhotoImage(img2)
		resetbut = tk.Button(self.frame1, command=self.reset, image=img2, text='RESET', compound=CENTER,
							 font=('Roboto', 16, 'bold'), foreground='white', background='green', anchor='center',
							 height=20, width=100, relief='raised')
		resetbut.grid(row=14, sticky='news', column=11, padx=(50, 50), pady=(20, 20), columnspan=2, rowspan=3)
		img3 = Image.open('button.jpg')
		size = (200, 75)
		img3 = img3.resize(size, Image.ANTIALIAS)
		img3 = ImageTk.PhotoImage(img3)
		quitbut = tk.Button(self.frame1, image=img3, text='QUIT', compound=CENTER, font=('Roboto', 16, 'bold'),
							foreground='white', background='green', anchor='center', height=20, width=100,
							relief='raised', command=self.root.destroy)
		quitbut.grid(row=16, sticky='news', column=11, padx=(50, 50), pady=(20, 20), columnspan=2, rowspan=3)
		self.root.mainloop()

	def fun1(self):
		""" Open a Student window and return None. """
		studlist = ['STUDENT\n NAME', 'COLLEGE\n  NAME', 'BRANCH', 'CLASS',
					'PASSING\n  YEAR', 'EMAIL_ID', 'MOBILE\nNUMBER', 'SSC %',
					'HSC %', 'FIRST YEAR\nCGPA', 'SECOND YEAR\nCGPA', 'THIRD YEAR\nCGPA', 'LIVE_ATKT', 'DEAD_ATKT',
					'CERTIFICATES', 'CO-CURRICULARS', 'SPORTS', 'EXTRAS', 'ENGLISH',
					'LOGICAL\nABILITY', 'QUANTITATIVE\nANALYSIS', 'TECHNICAL']

		self.lab = tk.Label(self.frame1, justify='center', text="Personal and Academic\nInformation",
							foreground='yellow', bg='white', font=('Bookman Old Style', 14, 'bold'))
		self.lab.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=0, column=0, columnspan=8)

		self.l1 = tk.Label(self.frame1, justify='center', text=studlist[0], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2)

		self.e1 = Entry(self.frame1, textvariable=self.x1, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=1, columnspan=4, ipady=5)
		self.e1.bind('<Button-1>', lambda _: self.x1.set(''))

		self.l2 = tk.Label(self.frame1, justify='center', text=studlist[4], anchor='center', fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l2.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=5)

		self.menu1 = tk.Menubutton(self.frame1, textvariable=self.x5, background='white', font=('Bahnschrift', 12),
								   foreground='red', width=10)
		menu = Menu(self.menu1)
		self.menu1['menu'] = menu
		menu.add_radiobutton(label=2018, variable=self.x5, value=2018)
		menu.add_separator()
		menu.add_radiobutton(label=2019, variable=self.x5, value=2019)
		menu.add_separator()
		menu.add_radiobutton(label=2020, variable=self.x5, value=2020)
		menu.add_separator()
		self.menu1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=6, columnspan=3, ipadx=10, ipady=7)

		self.l3 = tk.Label(self.frame1, justify='center', text=studlist[2], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l3.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4)

		self.e3 = Entry(self.frame1, textvariable=self.x3, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e3.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=1, columnspan=2, ipady=5)
		self.e3.bind('<Button-1>', lambda _: self.x3.set(''))

		self.l4 = tk.Label(self.frame1, justify='center', text=studlist[3], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l4.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=5)

		self.e4 = Entry(self.frame1, textvariable=self.x4, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e4.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=6, columnspan=2, ipady=5)
		self.e4.bind('<Button-1>', lambda _: self.x4.set(''))

		self.l5 = tk.Label(self.frame1, justify='center', text=studlist[1], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l5.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6)

		self.e5 = Entry(self.frame1, textvariable=self.x2, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e5.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=1, columnspan=2, ipady=5)
		self.e5.bind('<Button-1>', lambda _: self.x2.set(''))

		self.l6 = tk.Label(self.frame1, justify='center', text=studlist[5], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l6.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=5)

		self.e6 = Entry(self.frame1, textvariable=self.x6, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e6.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=6, columnspan=2, ipady=5)
		self.e6.bind('<Button-1>', lambda _: self.x6.set(''))

		self.l7 = tk.Label(self.frame1, justify='center', text=studlist[6], fg='#FFFFFF', bg='#FF0000',
						   font=('Gothic Light', 10, 'bold'))
		self.l7.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8)

		self.e7 = Entry(self.frame1, textvariable=self.x7, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e7.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=1, columnspan=2, ipady=5)
		self.e7.bind('<Button-1>', lambda _: self.x7.set(''))

		self.l8 = tk.Label(self.frame1, justify='center', text=studlist[7], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l8.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=5)

		self.e8 = Entry(self.frame1, textvariable=self.x8, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e8.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=6, columnspan=2, ipady=5)
		self.e8.bind('<Button-1>', lambda _: self.x8.set(''))

		self.l9 = tk.Label(self.frame1, justify='center', text=studlist[8], fg='#FF0000', bg='#FFFFFF',
						   font=('Gothic Light', 10, 'bold'))
		self.l9.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=10)

		self.e9 = Entry(self.frame1, textvariable=self.x9, foreground='grey', font=('Bahnschrift', 12),
						justify='center')
		self.e9.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=10, column=1, columnspan=2, ipady=5)
		self.e9.bind('<Button-1>', lambda _: self.x9.set(''))

		self.l10 = tk.Label(self.frame1, justify='center', text=studlist[9], fg='#FFFFFF', bg='#FF0000',
							font=('Gothic Light', 10, 'bold'))
		self.l10.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=10, column=5)

		self.e10 = Entry(self.frame1, textvariable=self.x10, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e10.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=10, column=6, columnspan=2, ipady=5)
		self.e10.bind('<Button-1>', lambda _: self.x10.set(''))

		self.l11 = tk.Label(self.frame1, justify='center', text=studlist[10], fg='#FFFFFF', bg='#FF0000',
							font=('Gothic Light', 10, 'bold'))
		self.l11.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=12)

		self.e11 = Entry(self.frame1, textvariable=self.x11, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e11.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=12, column=1, columnspan=2, ipady=5)
		self.e11.bind('<Button-1>', lambda _: self.x11.set(''))

		self.l12 = tk.Label(self.frame1, justify='center', text=studlist[11], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l12.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=12, column=5)

		self.e12 = Entry(self.frame1, textvariable=self.x12, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e12.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=12, column=6, columnspan=2, ipady=5)
		self.e12.bind('<Button-1>', lambda _: self.x12.set(''))

		self.l13 = tk.Label(self.frame1, justify='center', text=studlist[12], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l13.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=14)

		self.e13 = Entry(self.frame1, textvariable=self.x13, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e13.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=14, column=1, columnspan=2, ipady=5)
		self.e13.bind('<Button-1>', lambda _: self.x13.set(''))

		self.l14 = tk.Label(self.frame1, justify='center', text=studlist[13], fg='#FFFFFF', bg='#FF0F0F',
							font=('Gothic Light', 10, 'bold'))
		self.l14.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=14, column=4, columnspan=2, ipady=5)

		self.e14 = Entry(self.frame1, textvariable=self.x14, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e14.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=14, column=6, columnspan=2, ipady=5)
		self.e14.bind('<Button-1>', lambda _: self.x14.set(''))

		self.l15 = tk.Label(self.frame1, justify='center', text=studlist[14], fg='#FFFFFF', bg='#FF0F0F',
							font=('Gothic Light', 10, 'bold'))
		self.l15.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=16, column=0)

		self.e15 = Entry(self.frame1, textvariable=self.x15, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e15.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=16, column=1, columnspan=2, ipady=5)
		self.e15.bind('<Button-1>', lambda _: self.x15.set(''))

		self.l16 = tk.Label(self.frame1, justify='center', text=studlist[15], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l16.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=16, column=5)

		self.e16 = Entry(self.frame1, textvariable=self.x16, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e16.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=16, column=6, columnspan=2, ipady=5)
		self.e16.bind('<Button-1>', lambda _: self.x16.set(''))

		self.l17 = tk.Label(self.frame1, justify='center', text=studlist[16], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l17.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=18, column=0)

		self.e17 = Entry(self.frame1, textvariable=self.x17, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e17.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=18, column=1, columnspan=2, ipady=5)
		self.e17.bind('<Button-1>', lambda _: self.x17.set(''))

		self.l18 = tk.Label(self.frame1, justify='center', text=studlist[17], fg='#FFFFFF', bg='#FF0F0F',
							font=('Gothic Light', 10, 'bold'))
		self.l18.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=18, column=5)

		self.e18 = Entry(self.frame1, textvariable=self.x18, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e18.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=18, column=6, columnspan=2, ipady=5)
		self.e18.bind('<Button-1>', lambda _: self.x18.set(''))

		self.lab1 = tk.Label(self.frame1, justify='center', text='Amcat Information', foreground='yellow', bg='white',
							 font=('Bookman Old Style', 14, 'bold'))
		self.lab1.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=0, column=11, columnspan=2)

		self.l19 = tk.Label(self.frame1, justify='center', text=studlist[18], fg='#FFFFFF', bg='#FF0F0F',
							font=('Gothic Light', 10, 'bold'))
		self.l19.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=11)

		self.e19 = Entry(self.frame1, textvariable=self.x19, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e19.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=2, column=12, columnspan=2, ipady=5)
		self.e19.bind('<Button-1>', lambda _: self.x19.set(''))

		self.l20 = tk.Label(self.frame1, justify='center', text=studlist[19], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l20.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=11)

		self.e20 = Entry(self.frame1, textvariable=self.x20, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e20.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=4, column=12, columnspan=2, ipady=5)
		self.e20.bind('<Button-1>', lambda _: self.x20.set(''))

		self.l21 = tk.Label(self.frame1, justify='center', text=studlist[20], fg='#FFFFFF', bg='#FF0000',
							font=('Gothic Light', 10, 'bold'))
		self.l21.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=11)

		self.e21 = Entry(self.frame1, textvariable=self.x21, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e21.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=6, column=12, columnspan=2, ipady=5)
		self.e21.bind('<Button-1>', lambda _: self.x21.set(''))

		self.l22 = tk.Label(self.frame1, justify='center', text=studlist[21], fg='#FF0000', bg='#FFFFFF',
							font=('Gothic Light', 10, 'bold'))
		self.l22.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=11)

		self.e22 = Entry(self.frame1, textvariable=self.x22, foreground='grey', font=('Bahnschrift', 12),
						 justify='center')
		self.e22.grid(rowspan=2, padx=(10, 10), pady=(10, 10), row=8, column=12, columnspan=2, ipady=5)
		self.e22.bind('<Button-1>', lambda _: self.x22.set(''))

	def sub(self, event):
		x = False
		if self.x1.get() != "String" and not any(c.isdigit() for c in self.x1.get()):
			self.b[0] = self.x1.get().upper()

		if self.x2.get() != "String" and not any(c.isdigit() for c in self.x2.get()):
			self.b[1] = self.x2.get().upper()

		if self.x3.get() != "String" and not any(c.isdigit() for c in self.x3.get()):
			self.b[2] = self.x3.get().upper()

		if self.x4.get() != "String" and not any(c.isdigit() for c in self.x4.get()):
			self.b[3] = self.x4.get().upper()

		if self.x5.get() != 'YEAR':
			self.b[4] = self.x5.get()

		if self.x6.get() != "ENTER":
			self.b[5] = self.x6.get().upper()

		if self.x7.get() != '10-digit number' and not any(c.isalpha() for c in self.x7.get()):
			self.b[6] = self.x7.get()

		if self.x8.get() != "Numeric" and not any(c.isalpha() for c in self.x8.get()) and float(
				self.x8.get()) >= 0 and float(self.x8.get()) <= 100:
			self.b[7] = self.x8.get().upper()

		if self.x9.get() != "Numeric" and not any(c.isalpha() for c in self.x9.get()) and float(
				self.x9.get()) >= 0 and float(self.x9.get()) <= 100:
			self.b[8] = self.x9.get().upper()

		if self.x10.get() != "Numeric" and not any(c.isalpha() for c in self.x10.get()) and float(
				self.x10.get()) >= 6.5 and float(self.x10.get()) <= 10:
			self.b[9] = self.x10.get().upper()

		if self.x11.get() != "Numeric" and not any(c.isalpha() for c in self.x11.get()) and float(
				self.x11.get()) >= 6.5 and float(self.x11.get()) <= 10:
			self.b[10] = self.x11.get().upper()

		if self.x12.get() != "Numeric" and not any(c.isalpha() for c in self.x12.get()) and float(
				self.x12.get()) >= 6.5 and float(self.x12.get()) <= 10:
			self.b[11] = self.x12.get().upper()

		if self.x13.get() != "Numeric" and self.x13.get() != '' and not any(c.isalpha() for c in self.x13.get()):
			self.b[12] = self.x13.get()

		if self.x14.get() != "Numeric" and self.x14.get() != '' and not any(c.isalpha() for c in self.x14.get()):
			self.b[13] = self.x14.get()

		if self.x15.get() != "Numeric" and self.x15.get() != '':
			self.b[18] = self.x15.get().upper()

		if self.x16.get() != "Numeric" and self.x14.get() != '':
			self.b[19] = self.x16.get().upper()

		if self.x17.get() != "Numeric" and self.x14.get() != '':
			self.b[20] = self.x17.get().upper()

		if self.x18.get() != "String":
			self.b[21] = self.x18.get().upper()

		if self.x19.get() != 'Out of 100' and self.x19.get() != '' and not any(
				c.isalpha() for c in self.x19.get()) and float(self.x19.get()) >= 0 and float(self.x19.get()) <= 100:
			self.b[14] = self.x19.get()

		if self.x20.get() != 'Out of 100' and self.x20.get() != '' and not any(
				c.isalpha() for c in self.x20.get()) and float(self.x20.get()) >= 0 and float(self.x20.get()) <= 100:
			self.b[15] = self.x20.get()

		if self.x21.get() != 'Out of 100' and self.x21.get() != '' and not any(
				c.isalpha() for c in self.x21.get()) and float(self.x21.get()) >= 0 and float(self.x21.get()) <= 100:
			self.b[16] = self.x21.get()

		if self.x22.get() != 'Out of 100' and self.x22.get() != '' and not any(
				c.isalpha() for c in self.x22.get()) and float(self.x22.get()) >= 0 and float(self.x22.get()) <= 100:
			self.b[17] = self.x22.get()

		if '' not in self.b:
			x = askyesno('Confirm', 'Click on "Yes" to predict outcome or click on "No" to QUIT')
			if x:
				logireg(self.b)

			self.root.destroy()

		else:
			showwarning('Warning', 'Entered information does not match the requirements!')

	def reset(self):
		self.x1.set("String")
		self.x2.set("String")
		self.x3.set("String")
		self.x4.set("String")
		self.x5.set('YEAR')
		self.x6.set("ENTER")
		self.x7.set('10-digit number')
		self.x8.set("Numeric")
		self.x9.set("Numeric")
		self.x10.set("Numeric")
		self.x11.set("Numeric")
		self.x12.set("Numeric")
		self.x13.set('Numeric')
		self.x14.set('Numeric')
		self.x15.set('Numeric')
		self.x16.set('Numeric')
		self.x17.set('Numeric')
		self.x18.set("String")
		self.x19.set('Out of 100')
		self.x20.set('Out of 100')
		self.x21.set('Out of 100')
		self.x22.set('Out of 100')
