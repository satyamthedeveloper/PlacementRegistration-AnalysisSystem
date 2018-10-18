_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Placement_Analysis"
_author_ = "Anand"


from tkinter import *
import tkinter as tk
from tkinter.ttk import *
from tkinter.messagebox import *
from Company_Registration import *
from Student_Registration import *
from Analysis_GUI import *
from PIL import Image, ImageTk
from Placement_Process import *


class INPUT:
        def __init__(self):
                self.root = Tk()
                self.root.config(background='#1234FF')
                self.root.style = Style()
                self.root.style.theme_names()
                self.root.style.theme_use('vista')
                self.x1 = StringVar()
                self.x1.set('Enter Username here')
                self.x2 = StringVar()
                self.x2.set('Enter password here')
                self.names = ['company', 'student', 'placementcell']
                self.codes = ['cmp', 'stu', 'plc']
                img = Image.open('background.jpg')
                size = (1000, 1600)
                img = img.resize(size, Image.ANTIALIAS)
                img = ImageTk.PhotoImage(img)
                self.frame1 = tk.Canvas(self.root, width=1200, height=1000, borderwidth=3, relief='groove')
                self.frame1.create_image(0, 0, image = img, anchor = NW)
                self.frame1.grid(rowspan=2, row=0, column=0, sticky='news', pady=(20, 20))
                self.labels()
                img1 = Image.open('button.jpg')
                size = (320, 75)
                img1 = img1.resize(size, Image.ANTIALIAS)
                img1 = ImageTk.PhotoImage(img1)
                self.submitbut = tk.Button(self.frame1, text='SUBMIT', image = img1, background = 'green',compound = CENTER, foreground = 'white', font = ('Roboto', 16, 'bold'), anchor = 'center', height = 40, width = 100, relief = 'raised')
                self.submitbut.bind('<Button-1>', self.acc)
                self.submitbut.grid(rowspan=3, padx=(20, 20), pady = (20, 20), row=7, column=0, columnspan=2, sticky='news')
                img2 = Image.open('button.jpg')
                size = (150, 75)
                img2 = img2.resize(size, Image.ANTIALIAS)
                img2 = ImageTk.PhotoImage(img2)
                quitbut = tk.Button(self.frame1, image = img2, text = 'QUIT', compound = CENTER, font = ('Roboto', 16, 'bold'), foreground = 'white', background = 'green',anchor = 'center', height = 20, width = 100, relief = 'raised', command = self.root.destroy)
                quitbut.grid(row = 7, sticky = 'news', column = 2, padx = (20, 20), pady = (20, 20), columnspan = 2, rowspan = 3)

                self.root.mainloop()

        def labels(self):
            self.l1 = tk.Label(self.frame1, justify = 'center', text='Authority', fg='#FFFFFF', bg='#FF0000',font = ('Gothic Light', 15, 'bold'))
            self.l1.grid(rowspan=2, padx=(20, 20), pady = (20, 20), row=2)
            self.e1 = Entry(self.frame1, textvariable=self.x1, foreground='red', font = ('Bahnschrift', 15), justify = 'center', width = 30)
            self.e1.grid(rowspan=2, padx=(5, 20), pady=(20, 20), row=2, column=1, columnspan=4, ipady = 5)
            self.e1.bind('<Button-1>', lambda _: self.x1.set(''))

            self.l2 = tk.Label(self.frame1, justify = 'center', text='Password', fg='#FFFFFF', bg='#FF0000',font = ('Gothic Light', 15, 'bold'))
            self.l2.grid(rowspan=2, padx=(20, 20), pady = (20, 20), row=4)
            self.e2 = Entry(self.frame1, textvariable=self.x2, foreground='red', font = ('Bahnschrift', 15), justify = 'center', width = 30)
            self.e2.grid(rowspan=2, padx=(20, 20), pady = (20, 20), row=4, column=1, columnspan=2, ipady = 5)
            self.e2.bind('<Button-1>', lambda _: self.x2.set(''))

        def acc(self, event):
            y = 3
            if self.x1.get() in self.names:
                y = self.names.index(self.x1.get())
        
            if y > 2 or self.codes[y] != self.x2.get():
                showwarning('Incorrect', 'Wrong set of password and username combinations present')
            elif y <= 2 and self.codes[y] == self.x2.get():
                self.root.destroy()
                if y == 0:
                    runcomp(event)
                    self.root = Tk()
                    ans = askyesno('CONFIRM', 'Do you want to start placement process?')
                    self.root.destroy()
                    if ans:
                        runpla(event)
                elif y == 1:
                    #stud reg
                    runstud(event)
                else:
                    #analyis
                    runlys(event)
        
a = INPUT()
