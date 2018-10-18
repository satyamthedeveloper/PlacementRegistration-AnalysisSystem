_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "shortlist_students"
_author_ = "Satyam"

import pandas as pd
import pdfkit


def shortlist_passing_out_year(old_data, session):
	year = int(session[:2] + session[5:])
	return old_data[old_data['Passing Year'] == year]


def shortlist_gpa(old_data, gpa):
	return old_data[(old_data['FE GPA'] + old_data['SE GPA'] + old_data['TE GPA']) / 3 >= gpa]


def shortlist_live_backlog(old_data, live):
	return old_data[old_data['Live Backlog'] <= live]


def shortlist_dead_backlog(old_data, dead):
	return old_data[old_data['Dead Backlog'] <= dead]


def shortlist(company_criteria):
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

	data = shortlist_passing_out_year(data, company_criteria[-1])
	data = shortlist_gpa(data, float(company_criteria[2]))
	data = shortlist_live_backlog(data, int(company_criteria[3]))
	data = shortlist_dead_backlog(data, int(company_criteria[4]))

	path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
	config = pdfkit.configuration(wkhtmltopdf=path)

	data.to_html(
		'./Output/Companies/html/' + company_criteria[0] + 'eligible_students_' + company_criteria[-1] + '.html')
	pdfkit.from_file(
		'./Output/Companies/html/' + company_criteria[0] + 'eligible_students_' + company_criteria[-1] + '.html',
		'./Output/Companies/pdf/' + company_criteria[0] + 'eligible_students_' + company_criteria[-1] + '.pdf',
		configuration=config)

	data.to_csv(
		'Data/Shortlisted_Data/' + company_criteria[0] + "_" + company_criteria[-1] + "_shortlisted_students.csv",
		sep=",", encoding='utf-8')

	print('Eligible Candidates List Generated... Please Check Output Folder')
