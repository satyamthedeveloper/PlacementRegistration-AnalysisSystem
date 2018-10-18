_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "companies_list_analysis"
_author_ = "Satyam"

import pandas as pd
import pdfkit as pdf
def generate_companies_list():
	data = pd.read_csv('./Data/companies_list.csv', header=None)
	header = {0: 'Company Name',
			  1: 'Company Requirement',
			  2: 'Criteria [> GPA]',
			  3: 'Live backlog allowed',
			  4: 'Dead backlog allowed',
			  5: 'Package offered',
			  6: 'Academic Session'}
	data.columns = [header.get(x, x) for x in data.columns]

	path = 'C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe'
	config = pdf.configuration(wkhtmltopdf=path)
	data.to_html('./Output/PlacementCell/html/company_list.html')
	pdf.from_file('./Output/PlacementCell/html/company_list.html', './Output/PlacementCell/pdf/company_list.pdf', configuration=config)

	print('List generated successfully. Go to Output folder..........')
