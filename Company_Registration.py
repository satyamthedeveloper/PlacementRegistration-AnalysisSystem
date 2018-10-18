_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Company_Registration"
_author_ = "Satyam"

import csv
from companies_list_analysis import generate_companies_list
from shortlist_students import shortlist
import Company_GUI
from tkinter.messagebox import *
from tkinter import *


def company_gui():
	a = Company_GUI.INPUT()
	temp = a.b
	return temp


def check_file():
	file = open("./Data/companies_list.csv", "a", newline='')
	file.close()


def print_companies():
	reader = csv.reader(open("./Data/companies_list.csv", "r"), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		print(row)


def company_exist(company):
	reader = csv.reader(open("./Data/companies_list.csv", "r"), delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		if row == company:
			return True
	return False


def add_company(company):
	if company_exist(company):
		return False

	writer = csv.writer(open("./Data/companies_list.csv", "a", newline=''), delimiter=',', quotechar='|',
						quoting=csv.QUOTE_MINIMAL)
	writer.writerow(company)
	return True


def runcomp(event):
	while True:
		root = Tk()
		exit_input = askyesno('COMPANY REGISTRATION', "Press 'Yes' to register new Company, 'No' to exit : ")
		if not exit_input:
			break
		root.destroy()
		new_company = company_gui()
		check_file()
		add_company(new_company)
		generate_companies_list()
		shortlist(new_company)
		root.mainloop()
