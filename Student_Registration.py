_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Student_Registration"
_author_ = "Satyam"

import csv
import Stud_GUI
from registered_students_list import student_update
from tkinter.messagebox import *
from tkinter import *


def student_gui():
	a = Stud_GUI.INPUT()
	return a.b


def check_file():
	file = open("./Data/registered_students.csv", "a", newline='')
	file.close()


def print_students():
	reader = csv.reader(open("./Data/registered_students.csv", "r"), delimiter=',', quotechar='|',
						quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		print(row)


def student_exist(student):
	reader = csv.reader(open("./Data/registered_students.csv", "r"), delimiter=',', quotechar='|',
						quoting=csv.QUOTE_MINIMAL)
	for row in reader:
		if row == student:
			return True
	return False


def add_student(student):
	if student_exist(student):
		return False

	writer = csv.writer(open("./Data/registered_students.csv", 'a', newline=''), delimiter=',', quotechar='|',
						quoting=csv.QUOTE_MINIMAL)
	writer.writerow(student)
	return True


def runstud(event):
	while True:
		root = Tk()
		exit_input = askyesno('STUDENT REGISTRATION', "Press 'Yes' to register new Student, 'No' to exit : ")
		if not exit_input:
			break
		root.destroy()
		new_student = student_gui()
		check_file()
		add_student(new_student)
		student_update(int(new_student[4]))
