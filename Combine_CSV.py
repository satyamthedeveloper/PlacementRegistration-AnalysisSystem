_project_ = "PRAS (Placement Registration and Analytics System)"
_file_ = "Combine_CSV"
_author_ = "Satyam"

import os
import glob
import pandas


def concatenate(indir='./Data/Shortlisted_Data', outfile='E:\Projects\PRAS (Placement Registration and Analytics System)\Data\Concatenated\data.csv'):
	os.chdir(indir)
	fileList = glob.glob('*.csv')
	dfList = []
	colnames = ['Unnamed', 'Unnamed', 'Student Name', 'College Name', 'Branch', 'Division', 'Passing Year', 'Email-id',
				'Mobile Number', 'SSC %age', 'HSC %age', 'FE GPA', 'SE GPA', 'TE GPA', 'Live Backlog', 'Dead Backlog',
				'AMCAT Eng', 'AMCAT Logic', 'AMCAT Quant', 'AMCAT Tech', 'Certification', 'Co-circular', 'Sports',
				'Extras', 'Placed']
	for filename in fileList:
		print(filename)
		df = pandas.read_csv(filename)
		dfList.append(df)
	concatDf = pandas.concat(dfList, axis=0)
	concatDf.columns = colnames
	concatDf.to_csv(outfile, index=None)

concatenate()