_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Placement_Analysis"
_author_ = "Satyam"

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tkinter.filedialog import askopenfilenames
from tkinter import *


def bar_graph(company_list, eligible, placed, company_count, label):
	labels = company_list
	sizes1 = eligible
	sizes2 = placed

	index = np.arange(company_count)
	bar_width = 0.5
	rect1 = plt.bar(index, sizes1, bar_width, color='blue')
	rect2 = plt.bar(index, sizes2, bar_width, color='red')
	plt.legend((rect1, rect2), ('Eligible', 'Placed'))
	plt.xlabel(label)
	plt.ylabel('Number of candidates')
	plt.title('Eligible-Placed Bar Graph')
	plt.xticks(index, labels, rotation=90)
	plt.tight_layout()
	plt.show()


def pie_chart(placed, not_placed, company_list):
	labels = ['Placed', 'Not Placed']
	for i in range(0, len(placed)):
		plt.figure(i)
		sizes = [placed[i], not_placed[i]]
		colors = ['darkorange', 'green']
		plt.axis('equal')
		plt.title(company_list[i] + ' Placed Not-Placed Ratio')
		plt.pie(sizes, explode=(0.02, 0), labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=90)
	plt.show()


def scatter_plot(x0, y0, x1, y1):
	plt.scatter(x0, y0, color='red')
	plt.scatter(x1, y1, color='green')
	plt.xlabel('Average GPA')
	plt.ylabel('Average AMCAT Scores')
	plt.show()


def call_selection():
	root1 = Tk()
	filenames = askopenfilenames(title='Choose a file')
	root1.destroy()
	company_count = len(list(filenames))
	eligible_list = []
	placed_list = []
	company_list = []
	dept_eligible_list = []
	dept_placed_list = []
	dept_list = ['COMPUTER', 'IT', 'E&TC', 'MECH', 'CIVIL']
	x_axis_1 = []
	y_axis_1 = []
	x_axis_0 = []
	y_axis_0 = []

	'''
	Extracting Name of companies and count of students from the files,
	selected by the user to perform analysis on.
	'''
	for filename in filenames:
		data = pd.read_csv(filename)
		processed_data = data.iloc[:, [4, 5, -1]]
		scatter_data = data.iloc[:, [11, 12, 13, 16, 17, 18, 19, -1]]
		scatter_data_0 = scatter_data[scatter_data.iloc[:, -1] == 0].dropna()
		scatter_data_1 = scatter_data[scatter_data.iloc[:, -1] == 1].dropna()
		x_axis1 = list(scatter_data_1.iloc[:, [0, 1, 2]].mean(axis=1))
		y_axis1 = list(scatter_data_1.iloc[:, [3, 4, 5, 6]].mean(axis=1))
		x_axis0 = list(scatter_data_0.iloc[:, [0, 1, 2]].mean(axis=1))
		y_axis0 = list(scatter_data_0.iloc[:, [3, 4, 5, 6]].mean(axis=1))
		x_axis_1 = x_axis_1 + x_axis1
		y_axis_1 = y_axis_1 + y_axis1
		x_axis_0 = x_axis_0 + x_axis0
		y_axis_0 = y_axis_0 + y_axis0

		eligible = processed_data.iloc[:, 2]
		eligible_list.append(len(eligible))
		placed = eligible[eligible == 1]
		placed_list.append(len(placed.dropna()))
		while True:
			loc = filename.find('/')
			if loc == -1:
				break
			filename = filename[loc + 1:]
		filename = filename[:-33]
		company_list.append(filename)

		for dept in dept_list:
			dept_data = processed_data[processed_data['Branch'] == str(dept)]
			eligible = dept_data.iloc[:, 2]
			dept_eligible_list.append(len(eligible))
			placed = eligible[eligible == 1]
			dept_placed_list.append(len(placed.dropna()))

	cl = []
	for i in company_list:
		st = ''
		for j in i:
			if j == ' ':
				st = st + '\n'
			else:
				st = st + j
		cl.append(st)

	company_list = cl

	dept_eligible_count = []
	dept_placed_count = []

	for i in range(0, len(dept_list)):
		dept_eligible_count.append(0)
		dept_placed_count.append(0)

	for i in range(0, len(dept_list) * company_count, len(dept_list)):
		for j in range(0, len(dept_list)):
			dept_eligible_count[j] = dept_eligible_count[j] + dept_eligible_list[i + j]
			dept_placed_count[j] = dept_placed_count[j] + dept_placed_list[i + j]

	not_placed_list = []
	for i in range(0, len(placed_list)):
		not_placed_list.append(eligible_list[i] - placed_list[i])

	collection = x_axis_0, y_axis_0, x_axis_1, y_axis_1, placed_list, not_placed_list, company_list, eligible_list, company_count, dept_list, dept_eligible_count, dept_placed_count
	return collection


def scatterchart():
	collection = call_selection()
	x_axis_0, y_axis_0, x_axis_1, y_axis_1, placed_list, not_placed_list, company_list, eligible_list, company_count, dept_list, dept_eligible_count, dept_placed_count = collection
	scatter_plot(x_axis_0, y_axis_0, x_axis_1, y_axis_1)


def piechart():
	collection = call_selection()
	x_axis_0, y_axis_0, x_axis_1, y_axis_1, placed_list, not_placed_list, company_list, eligible_list, company_count, dept_list, dept_eligible_count, dept_placed_count = collection
	pie_chart(placed_list, not_placed_list, company_list)


def compgraph():
	collection = call_selection()
	x_axis_0, y_axis_0, x_axis_1, y_axis_1, placed_list, not_placed_list, company_list, eligible_list, company_count, dept_list, dept_eligible_count, dept_placed_count = collection
	bar_graph(company_list, eligible_list, placed_list, company_count, label='Companies')


def deptgraph():
	collection = call_selection()
	x_axis_0, y_axis_0, x_axis_1, y_axis_1, placed_list, not_placed_list, company_list, eligible_list, company_count, dept_list, dept_eligible_count, dept_placed_count = collection
	bar_graph(dept_list, dept_eligible_count, dept_placed_count, len(dept_list), label='Branch')
