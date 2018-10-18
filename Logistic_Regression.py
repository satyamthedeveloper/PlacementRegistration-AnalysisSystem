_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Logistic Regression"
_author_ = "Satyam"

import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
# import Stud_GUI
from tkinter import *
from tkinter.messagebox import *
from tkinter.ttk import *
from PIL import Image, ImageTk


def logireg(b):
	data = pd.read_csv('./Data/Concatenated/data.csv', sep=',')

	col_names = ['Branch', 'SSC %age', 'HSC %age', 'FE GPA', 'SE GPA', 'TE GPA', 'Live Backlog', 'Dead Backlog',
				 'AMCAT Eng', 'AMCAT Logic', 'AMCAT Quant', 'AMCAT Tech', 'Certification', 'Co-circular', 'Sports',
				 'Extras', 'Placed']
	selected_data = data.loc[:, col_names]

	X = selected_data.iloc[:, :-1]
	y = selected_data.iloc[:, -1]

	label_dic = {}

	for column in X.columns:
		if X[column].dtype == 'object':
			le = LabelEncoder()
			X[column] = le.fit_transform(X[column].fillna('0'))
			label_dic[column] = dict(zip(le.classes_, le.transform(le.classes_)))

	X, y = shuffle(X, y)
	x_train, x_test, y_train, y_test = train_test_split(X, y, train_size=0.8, test_size=0.2)

	clf = LogisticRegression()
	clf.fit(x_train, y_train)
	y_pred = clf.predict(x_test)
	accuracy = accuracy_score(y_test, y_pred)

	# a = Stud_GUI.INPUT()

	new_data = b
	new_pred = []
	new_pred.append(new_data[2])
	temp_list = list(new_data[i] for i in range(7, 22))
	for x in temp_list:
		new_pred.append(x)
	if new_pred[-1] == 'NA':
		new_pred[-1] = 'N.A.'
	new_pred = pd.DataFrame(new_pred)
	new_pred.iloc[0] = new_pred.iloc[0].map(label_dic['Branch'])
	new_pred.iloc[-1] = new_pred.iloc[-1].map(label_dic['Extras'])
	new_pred = new_pred.T
	new_pred.fillna(0)
	# print(new_pred)
	# print(label_dic)
	pred = int(clf.predict(new_pred))
	prediction = ''
	if pred == 1:
		prediction = 'Hey {}.\nThere is high chances that you will be placed.\nAll the Best !!!'.format(new_data[0])
	else:
		prediction = "Sorry {}!\nStatistic predicts low chance of getting placed.\nBut, don't loose hope. Keep trying.\nAll the Best !!!".format(
			new_data[0])
	print('\n\n\n\n')
	showinfo('PLACEMENT PREDICTOR', prediction)
	sh = showwarning('IMPORTANT NOTE',
					 'The system predicting your result has an accuracy of {:.2f}%. You may not have a just prediction'.format(
						 accuracy * 100))
