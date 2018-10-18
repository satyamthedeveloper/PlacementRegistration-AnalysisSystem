_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Placement_Process"
_author_ = "Satyam"

import pandas as pd
from tkinter.filedialog import askopenfilename
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.messagebox import *


def runpla(event):
	filename = askopenfilename()
	'''
        img = Image.open('background.jpg')
        size = (1000, 1600)
        img = img.resize(size, Image.ANTIALIAS)
        img = ImageTk.PhotoImage(img)
        '''
	data = pd.read_csv(filename)
	list1 = data.columns.tolist()
	list1 = list1[2:]
	str1 = ''
	for i in range(len(list1)):
		str1 = str1 + list1[i] + ':\n'

	placed = []
	i = 0
	for i in range(0, data.shape[0]):
		list2 = data.iloc[i].tolist()
		list2 = list2[2:]

		str1 = ''
		for i in range(len(list2)):
			str1 = str1 + str(list1[i]) + ': ' + str(list2[i]) + '\n'
		root = Tk()
		root.geometry('300x500+400+200')
		root.title('PLACEMENT')
		root.config(background='#1234FF')
		root.style = Style()
		root.style.theme_names()
		root.style.theme_use('vista')
		root.style.configure('.', font=('Verdana', 10))
		msg = tk.Message(root, text=str1, font=('Bahnschrift', 14), fg='#FFFFFF', bg='#123456', width=400, aspect=100)
		msg.grid(row=1, column=1)
		root1 = Tk()
		placed_val = int(askyesno('SUBMIT', 'Do you wanna place the student?'))
		root1.destroy()
		root.destroy()
		if not placed_val:
			root = Tk()
			exit1 = int(askyesno('CONFIRM', 'Do you wanna QUIT'))
			root.destroy()
			if exit1:
				break
		else:
			placed.append(placed_val)

	if (i == len(list2)):
		data['Placed'] = placed
		data.to_csv(filename, sep=',')
