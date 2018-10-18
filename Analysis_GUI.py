_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Analysis_GUI"
_author_ = "Anand"


from tkinter import *
import tkinter as tk
from tkinter.ttk import *
import Placement_Analysis as PA
from PIL import Image, ImageTk

def runlys(event):
    root = Tk()
    root.title('ANALYSIS')
    root.style = Style()
    root.style.theme_use('vista')
    root.style.configure('.',font = ('Verdana', 10))
    root.wm_iconbitmap(bitmap = "Button.jpg")
    root.geometry('365x510+500+100')
    img = Image.open('background.jpg')
    size = (365,510)
    img = img.resize(size, Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    can = Canvas(root, borderwidth=3, relief='groove')
    can.create_image(0, 0, image = img, anchor = 'nw')
    can.grid(sticky = 'news', columnspan = 20, rowspan = 12, row = 0)
    img1 = Image.open('Button.jpg')
    size = (320, 60)
    img1 = img1.resize(size, Image.ANTIALIAS)
    img1 = ImageTk.PhotoImage(img1)

    cgbut = tk.Button(can, text='Company - Wise\nAnalysis', compound = CENTER, fg = 'white', bg = 'green',anchor = 'center', height = 50, width = 300, relief = 'raised', command=PA.compgraph, font = ('Bahnschrift', 16, 'bold'), image = img1, justify = 'center')
    cgbut.grid(row = 0, sticky = 'news', column = 0, padx = (20, 20), pady = (20, 20), columnspan = 7, rowspan = 3, ipady = 5, ipadx = 10)

    bgbut = tk.Button(can, text='Department - Wise\nAnalysis', compound = CENTER, fg = 'white', bg = 'green',anchor = 'center', height = 50, width = 300, relief = 'raised', command=PA.deptgraph, font = ('Bahnschrift', 16, 'bold'),image = img1)
    bgbut.grid(row=4, sticky = 'news', column = 0, padx = (20, 20), pady = (20, 20), columnspan = 7, rowspan = 3, ipady = 5, ipadx = 10)

    sp = tk.Button(can, text='Scatterplot', compound = CENTER, fg = 'white', bg = 'green',anchor = 'center', height = 50, width = 300, relief = 'raised', command=PA.scatterchart, font = ('Bahnschrift', 16, 'bold'),image = img1)
    sp.grid(row=8, sticky = 'news', column = 0, padx = (20, 20), pady = (20, 20), columnspan = 7, rowspan = 3, ipady = 5, ipadx = 10)

    pc = tk.Button(can, text='Pie chart', compound = CENTER, fg = 'white', bg = 'green',anchor = 'center', height = 50, width = 300, relief = 'raised', command=PA.piechart, font = ('Bahnschrift', 16, 'bold'),image = img1)
    pc.grid(row=12, sticky = 'news', column = 0, padx = (20, 20), pady = (20, 20), columnspan = 7, rowspan = 3, ipady = 5, ipadx = 10)
    
    quitbut = tk.Button(can, image = img1, text = 'QUIT', compound = CENTER, fg = 'white', bg = 'green',anchor = 'center', relief = 'raised', command = root.destroy, font = ('Bahnschrift', 16, 'bold'), height = 30, width = 70)
    quitbut.grid(row = 16, sticky = 'news', column = 2, padx = (20, 20), pady = (20, 20), columnspan = 3, rowspan = 3, ipady = 5, ipadx = 10)
   
    root.mainloop()
