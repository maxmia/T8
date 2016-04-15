#!/usr/bin/python
#  -*- coding: utf-8 -*-
import csv,re

de0=[]
df = "7(903088-903091,90583,906850-906854,906860-906872,906890-906894,906898-906899)"
#print df.split('(')[0]
areasDEFs = (df.split('(')[1]).split(')')[0]
#print areasDEFs
subcodes = areasDEFs.split(',')
for codes in subcodes:

	de0.append(codes.split('-')[0])

print de0

def filldiapason(begin,end):
	array = []
	while begin <= end:
  		array.append(begin)
  		begin = begin + 1
	return array


def _findPatternInInput(input,reg_ex):
	p = re.compile(reg_ex)
	m = p.match(input)
	if m:
		print 'Match found: ', m.group()
		return 1
	else:
		print 'No match'
		return 0
  	

if (_findPatternInInput('7(903088-903091,90583,906850-906854,906860-906872,906890-906894,906898-906899)',r'\d.+[()]')):
	print 'Here'
elif _findPatternInInput('7(903088-903091,90583,906850-906854,906860-906872,906890-906894,906898-906899)',r'\d.+[()]') > 89:
	print 'HH'

_findPatternInInput('79(123)',r'\d.+[()]')

_findPatternInInput('7129',r'\d.+[()]')
_findPatternInInput('7(1-23)',r'\d.+[()]')
_findPatternInInput('7(1-23,32)',r'\d.+[()]')




range0 = [903088, 903089, 903090, 903091]
for r in range0:
	print r


data0 = ['79298(03-12),South Osetia,South Osetia,4.2']
print type(data0)
#for i in data0:

print "-----------------------"
import os,sys

from os import listdir
from os.path import isfile, join
mypath = "/Users/max/Downloads"
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
print onlyfiles


import glob
print glob.glob("*.csv")
#['tele-8.csv','TELE 8 Contact list - Sheet1-2.csv', 'TELE 8 Contact list - Sheet1.csv', 'wstclglb.csv']



def Excel2CSV(ExcelFile, SheetName, CSVFile):
     import xlrd
     import csv
     workbook = xlrd.open_workbook(ExcelFile)
     worksheet = workbook.sheet_by_name(SheetName)
     csvfile = open(CSVFile, 'wb')
     wr = csv.writer(csvfile, quoting=csv.QUOTE_ALL)

     for rownum in xrange(worksheet.nrows):
         wr.writerow(
             list(x.encode('utf-8') if type(x) == type(u'') else x
                  for x in worksheet.row_values(rownum)))

     csvfile.close()




Excel2CSV('EVO004526_RU_Tele8_2015-03-15.xls','EVO -> Tele8','EVO.csv')




for files in glob.glob('/Users/max/Downloads/teletop/*.csv'):
	print files


"""                  
if ( a == b ):
   print "Line 1 - a is equal to b"
else:
   print "Line 1 - a is not equal to b"

if ( a != b ):
   print "Line 2 - a is not equal to b"
else:
   print "Line 2 - a is equal to b"

"""
#print filldiapason(120,128)
#print "I like sublime !"
