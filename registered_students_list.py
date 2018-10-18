_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "registered_students_list"
_author_ = "Satyam"

import pandas as pd
import pdfkit as pdf


def student_update(passing_year):
	data = pd.read_csv('./Data/registered_students.csv', header=None)
	header = {0: 'Student Name',
			  1: 'College Name',
			  2: 'Branch',
			  3: 'Division',
			  4: 'Passing Year',
			  5: 'Email-id',
			  6: 'Mobile Number',
			  7: 'SSC %age',
			  8: 'HSC %age',
			  9: 'FE GPA',
			  10: 'SE GPA',
			  11: 'TE GPA',
			  12: 'Live Backlog',
			  13: 'Dead Backlog',
			  14: 'AMCAT English',
			  15: 'AMCAT Logic',
			  16: 'AMCAT Quantitative',
			  17: 'AMCAT Technical',
			  18: 'Certifications',
			  19: 'Co-circular Activities',
			  20: 'Sports Certificates',
			  21: 'Extras'}
	data.columns = [header.get(x, x) for x in data.columns]

	data = data[data['Passing Year'] == passing_year]
	all_student = data.iloc[:, [0, 1, 2, 3, 5, 6]]

	path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
	config = pdf.configuration(wkhtmltopdf=path)

	data.to_html('./Output/PlacementCell/html/' + str(passing_year) + '_students_all_details.html')
	pdf.from_file('./Output/PlacementCell/html/' + str(passing_year) + '_students_all_details.html',
				  './Output/PlacementCell/pdf/' + str(passing_year) + '_students_all_details.pdf', configuration=config)

	all_student.to_html('./Output/PlacementCell/html/' + str(passing_year) + '_all_students_contact.html')
	pdf.from_file('./Output/PlacementCell/html/' + str(passing_year) + '_all_students_contact.html',
				  './Output/PlacementCell/pdf/' + str(passing_year) + '_all_students_contact.pdf', configuration=config)

	print('List generated successfully. Go to Output folder..........')
