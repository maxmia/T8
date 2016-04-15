#!/usr/bin/python
#  -*- coding: utf-8 -*-
import sys,csv,re,os,random
import xml.etree.ElementTree as ET
from transliterate import slugify
from transliterate import translit, get_available_language_codes
# unix way 
# priceless 

import glob
# glob.glob("*.csv")


def ai_priceless():
	#one,two,tree
	len_def = 8
	rows1 = csv_to_list('/Users/max/Downloads/pr0.csv') 
	rows2 = csv_to_list('/Users/max/Downloads/pr1.csv')
	rows3 =  csv_to_list('/Users/max/Downloads/pr2.csv')
	rowz = csv_to_list('/Users/max/Downloads/pr0.csv') + csv_to_list('/Users/max/Downloads/pr1.csv')+csv_to_list('/Users/max/Downloads/pr2.csv')
	print rowz 
	final_rows = []
	final_price = csv.writer(open('/Users/max/Downloads/FPP0.csv','wb'),delimiter=',') 
	
	#data_new_row_list = [defs,csv_cont[row][1],csv_cont[row][2],round((float(csv_cont[row][3])*0.28 + float(csv_cont[row][3]))/float(rub),4)]
	#print data_new_row_list
	#csv_full.writerow(data_new_row_list) 
		
	final_dict = dict()	
	for row in rowz:
		for data in row:
			if not data in final_rows: 
				final_rows.append(row) 
		#print row
		#defs = row[0]
		#dest = row[1]
		#rate = row[2]
		#if  not row[0] in final_rows:
			#final_dict = dict()
		#final_dict[defs][dest] = rate
		#	Noop() 
	#print final_dict 
	print final_rows 





def _seacrh_index(source,search):
	return source.index(search)



""" 


import csv
rows = csv.reader(open("file.csv", "rb"))
newrows = []
for row in rows:
    if row not in newrows:
        newrows.append(row)
writer = csv.writer(open("file.csv", "wb"))
writer.writerows(newrows)




---------


import csv
def ReadFile (filename = "<csv_file_location>"):
    f = open (filename)
    r = csv.reader (f)
    mentions = dict()
    for line in r:
        user    = line[0]
        product = line[1]
        rate    = float(line[2])
        if not user in mentions:
            mentions[user] = dict()
        mentions[user][product] = rate
    f.close()
    return mentions


"""


def _cyr_to_lat():
	""" """
	csv_en = csv.writer(open('/Users/max/Downloads/RUSTEST.csv','wb'),delimiter=',')
	csv_ru = csv_to_list('/Users/max/Downloads/D00.csv')
        for row in range(len(csv_ru)):
		cr = (csv_ru[row][1]).decode('utf-8')
		#print cr #csv_ru[row][1].encode('utf-8')
                #codeto_lat = slugufy(u'%',csv_ru[row][1])
		#string = "u\'"+ csv_ru[row][1]+"\""
		#print string
		codeto_lat = translit(cr, reversed=True)                
		csv_en.writerow(codeto_lat) 
	       	




def csv_to_list(csv_file, delimiter=','):
    """ 
    Reads in a CSV file and returns the contents as list,
    where every row is stored as a sublist, and each element
    in the sublist represents 1 cell in the table. 
    """
    with open(csv_file, 'rU') as csv_con:
        reader = csv.reader(csv_con, delimiter=delimiter)
        return list(reader)

def _wallgreens_cvs():
	""" read and parse DEFs in brackets X(AAA-BBB,CCC-E,D,...,YYYY) csv file from wstcl"""
	
	os.system("curl \"http://www.cbr.ru/scripts/XML_daily.asp\" > XML_daily.asp")
	tree = ET.parse('XML_daily.asp')
	RUB = tree.findall('./Valute[@ID="R01235"]/Value')[0].text
	rub = RUB.replace(",",".")

	csv_full = csv.writer(open('/Users/max/Downloads/wstcll-full.csv','wb'),delimiter=',')
	csv_cont = csv_to_list('/Users/max/Downloads/wstclglb.csv')
	for row in range(len(csv_cont)):
		defs_parse = _parseDEFs((csv_cont[row][0]).replace(" ", ""))
		for defs in defs_parse:
			if (len(defs) < 9):
				data_new_row_list = [defs,csv_cont[row][1],csv_cont[row][2],round((float(csv_cont[row][3])*0.28 + float(csv_cont[row][3]))/float(rub),4)]
				print data_new_row_list
				csv_full.writerow(data_new_row_list) 
				


def _parseDEFs(df):
	DEFs = []
	regex0 = r'\d.+[()]'
 	regex1 = r'\d[()]'

	if (_findPatternInInput(df,regex0) or _findPatternInInput(df,regex1)):
		
		country = df.split('(')[0]
		areasDEFs = (df.split('(')[1]).split(')')[0]
		subcodes = areasDEFs.split(',')
		#print subcodes	
		for s in subcodes:

			range0 = []
			ls = len(s.split('-'))
			if ls == 1:
				DEFs.append(s)
			if ls > 1:
				range0 = filldiapason(int(s.split('-')[0]),int(s.split('-')[1]))
	           	for r in range0:
	           		DEFs.append(r)

		fullDEFs = []
		#print DEFs
		for d in DEFs:
			fullDEFs.append(str(country) + str(d))
		return fullDEFs
	else:
		#print "hjhj"
		DEFs.append(str(df))
    	try:
    		if (_findPatternInInput(DEFs,regex1)):
    			#print 'Here'
    			parseDEF(str(DEFs))
    	except:
    			#print 'AAA'
    			print sys.exc_info()[0]	     
        return DEFs

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
		#print 'Match found: ', m.group()
		return m
	else:
		#print 'No match'
		return 0
"""def _findPatternInInput(input,reg_ex):
	p = re.compile(reg_ex)
	m = p.match(input)
	if m:
		print 'Match found: ', m.group()
	else:
		print 'No match'
  	return m"""




#print filldiapason(1,8)
#print _parseDEFs('7(1-4,10000-10002)')
#print _parseDEFs('77878')
#print _parseDEFs('7(903088-903091,11-13,2222,90583-90585,906850)')
#print filldiapason(903088,903091)



#_cyr_to_lat()
## code _wallgreens_cvs() 


#_priceless()

#'7900' in zip(*list_of_lists)[1]

list_of_lists=[['7900', 'Krakozhiya', '0.023', '23/4+', 'Grey'], ['2200', 'Johndoeland', '0.123', '34/70+', 'White'], ['3300', 'Midlleland', '34.56', '456/0+', 'Dark'], ['5600', 'Atlantida', '0.0001', '0/100+', 'Transparent']]
a = [['7900','Krakozhia Mob','0.02','30/5+','White'],['2200', 'Johndoeland', '0.0123', '34/70+', 'White']]
fl=[['7900', 'Krakozhiya', '0.023', '23/4+', 'Grey'], ['2200', 'Johndoeland', '0.123', '34/70+', 'White'], ['3300', 'Midlleland', '34.56', '456/0+', 'Dark'], ['5600', 'Atlantida', '0.0001', '0/100+', 'Transparent']]

#list_new = map(filter(lambda:list_of_lists[zip(*list_of_lists)[0].index(aa[0])][2] > aa[2])


#map(lambda y: [i for i,z in enumerate(a) if fl[zip(*fl)[0].index(a[0])][2] > a[2], set(a))
#def _normalize_xls_csv_to_parse():
	# function to normalize csv change columns and etc 

def _priceless_RUB():
        #
        len_def = 8
	defs_lists = []
	report = {} 
	report['files']=[]
        #defs_lists = csv_to_list('/Users/max/Downloads/pr0.csv') + csv_to_list('/Users/max/Downloads/pr1.csv')+csv_to_list('/Users/max/Downloads/pr2.csv')
	os.system("curl \"http://www.cbr.ru/scripts/XML_daily.asp\" > XML_daily.asp")
	tree = ET.parse('XML_daily.asp')
	RUB = tree.findall('./Valute[@ID="R01235"]/Value')[0].text
	rub = float(RUB.replace(",","."))
	print rub
	

	for files in glob.glob('/Users/max/Downloads/teletop/*.*'):
		#print files
		report['files'].append(files.split('/')[-1])
		defs_lists = defs_lists + csv_to_list(files)
		#print defs_lists
		#defs_lists = csv_to_list('/Users/max/Downloads/11.csv')+ csv_to_list('/Users/max/Downloads/2.csv') + csv_to_list('/Users/max/Downloads/1.csv')
	#print lambda defs_lists[x]: x in range(len(defs_lists))
	 
	#[['79','Mob rus'],['7911','MTS'],['79','HZZ'],['7911','MTS'],['21','HZZ'],['7911','MTS'],['79','HZZ'],['55','braz']] #csv_to_list('/Users/max/Downloads/pr0.csv') + csv_to_list('/Users/max/Downloads/pr1.csv')+csv_to_list('/Users/max/Downloads/pr2.csv')
        fl = [] # final price
	final_price = csv.writer(open('/Users/max/Downloads/RufixRUB.csv','wb'),delimiter=',')
        #fl.append(defs_lists[0])
	fll = []
	#    0         1           2         3       4
	# ['7900', 'Krakozhiya', '0.023', '23/4+', 'Grey']
	fll.append(defs_lists[0])
	#  squares = map(lambda x: [x], range(3))
	unique_defs = []
	#print range(len(defs_lists))	
	for i in range(len(defs_lists)):
		#print defs_lists[i][2]
		try:
			defs_lists[i][2] = round(_marge_maker(float((defs_lists[i][2]).replace(",", "."))),5)/rub
		except:
			print sys.exc_info()[0]
		fl.append(defs_lists[i])
		if not fl[i][0] in zip(*fll)[0]:
			fll.append(fl[i])
			#print fll[i][0] + '---- ' + fll[zip(*fll)[0].index(fl[i][0])][2]	
		else:
			print "DEF is already exist "+ str(fll[zip(*fll)[0].index(fl[i][0])]) +"----" +  str(fl[i])
			if fll[zip(*fll)[0].index(fl[i][0])][2] < fl[i][2]:
				print "Old is chipper than new one " + str(fl[i][2])
			if fll[zip(*fll)[0].index(fl[i][0])][2] > fl[i][2]:
				print "New is chipper " + str(fl[i][2])
				fll[zip(*fll)[0].index(fl[i][0])][2]=fl[i][2]
				print "Changing rate to new value , now it's = " + str(fll[zip(*fll)[0].index(fl[i][0])][2])				
	

					
	report['counter_str']=len(fll)	
	# hearder 
	fl_logo = open('hdr.txt', 'r')
	hdr = fl_logo.readlines()
	fl_logo.close()	
	final_price.writerow(hdr)
	
	for rows in fll:
		print rows
		final_price.writerow(rows)	


	
	import time
	report['len_file'] = len(report['files'])
	report['time'] = time.strftime('%X %x %Z') #strftime("%a, %d %b %Y %H:%M:%S -5", gmtime())	
	print '-----------------------------------------------'
	print report 
	print '-----------------------------------------------'	 		



def _priceless():
        #
        len_def = 8
	defs_lists = []
	report = {} 
	report['files']=[]
        #defs_lists = csv_to_list('/Users/max/Downloads/pr0.csv') + csv_to_list('/Users/max/Downloads/pr1.csv')+csv_to_list('/Users/max/Downloads/pr2.csv')
	for files in glob.glob('/Users/max/Downloads/teletop/*.*'):
		#print files
		report['files'].append(files.split('/')[-1])
		defs_lists = defs_lists + csv_to_list(files)
		#print defs_lists
		#defs_lists = csv_to_list('/Users/max/Downloads/11.csv')+ csv_to_list('/Users/max/Downloads/2.csv') + csv_to_list('/Users/max/Downloads/1.csv')
	#print lambda defs_lists[x]: x in range(len(defs_lists))
	 
	#[['79','Mob rus'],['7911','MTS'],['79','HZZ'],['7911','MTS'],['21','HZZ'],['7911','MTS'],['79','HZZ'],['55','braz']] #csv_to_list('/Users/max/Downloads/pr0.csv') + csv_to_list('/Users/max/Downloads/pr1.csv')+csv_to_list('/Users/max/Downloads/pr2.csv')
        fl = [] # final price
	final_price = csv.writer(open('/Users/max/Downloads/TELE8-AZ-PREMIUM.csv','wb'),delimiter=',')
        #fl.append(defs_lists[0])
	fll = []
	#    0         1           2         3       4
	# ['7900', 'Krakozhiya', '0.023', '23/4+', 'Grey']
	fll.append(defs_lists[0])
	#  squares = map(lambda x: [x], range(3))
	unique_defs = []
	#print range(len(defs_lists))	
	for i in range(len(defs_lists)):
		print defs_lists[i][2]
		#try:
		defs_lists[i][2] = round(_marge_maker(float((defs_lists[i][2]).replace(",", "."))),5)
		#except:
		#	print sys.exc_info()[0]
		fl.append(defs_lists[i])
		if not fl[i][0] in zip(*fll)[0]:
			fll.append(fl[i])
			#print fll[i][0] + '---- ' + fll[zip(*fll)[0].index(fl[i][0])][2]	
		else:
			print "DEF is already exist "+ str(fll[zip(*fll)[0].index(fl[i][0])]) +"----" +  str(fl[i])
			if fll[zip(*fll)[0].index(fl[i][0])][2] < fl[i][2]:
				print "Old is chipper than new one " + str(fl[i][2])
			if fll[zip(*fll)[0].index(fl[i][0])][2] > fl[i][2]:
				print "New is chipper " + str(fl[i][2])
				fll[zip(*fll)[0].index(fl[i][0])][2]=fl[i][2]
				print "Changing rate to new value , now it's = " + str(fll[zip(*fll)[0].index(fl[i][0])][2])				
	

					
	report['counter_str']=len(fll)	
	# hearder 
	fl_logo = open('hdr.txt', 'r')
	hdr = fl_logo.readlines()
	fl_logo.close()	
	final_price.writerow(hdr)
	
	for rows in fll:
		print rows
		final_price.writerow(rows)	


	
	import time
	report['len_file'] = len(report['files'])
	report['time'] = time.strftime('%X %x %Z') #strftime("%a, %d %b %Y %H:%M:%S -5", gmtime())	
	print '-----------------------------------------------'
	print report 
	print '-----------------------------------------------'	 		


def _top():
	""" top writes N unique defs < 5 length of each country DEFS """
	MAXTOP = 81
	fpp = csv_to_list('/Users/max/Downloads/FPP.csv')
	top_file = csv.writer(open('/Users/max/Downloads/TOP.csv','wb'),delimiter=',')
	shrt_defs = []
	def_final_range = []
	for row  in range(len(fpp)):	
		if len(fpp[row][0]) <= 5:
			shrt_defs.append(fpp[row])
	ddc = {}
	defs = ['1','2','3','4','5','6','7','8','9']
	for d in defs:
		ddc[d]=[]
		for j in shrt_defs:
			if j[0][0]== d:
				ddc[d].append(j)	
	top = 0 
	vec_ddc = {}
	
	for i in ddc:
		vec_ddc[i] = len(ddc[i])
		top = top + vec_ddc[i]
	#vec_ddc = {'1': 110, '3': 150, '2': 30, '5': 0, '4': 10, '7': 174, '6': 0, '9': 1, '8': 0}
	while top > MAXTOP + 1:
		new_top =0 
		for v in vec_ddc:
			new_top  = new_top + vec_ddc[v]
			if vec_ddc[v] > 10:
				vec_ddc[v]=vec_ddc[v]-1	
		top = new_top
	
	tpi_def = {}  # final array of defs 
	for d in vec_ddc:
		if vec_ddc[d] < 9:
			tpi_def[d] = [ x for x in range(vec_ddc[d])] # PEP 289 - Generator Expressions 	
		if vec_ddc[d] > 9:
			print vec_ddc[d]
			a = random.sample(range(0,vec_ddc[d]),vec_ddc[d])
			tpi_def[d] = [ x for x in a]        # random.sample(range(0,vec_ddc[d]),vec_ddc[d])


	
	
	for d in tpi_def:
		for n in tpi_def[d]:
			ddc[d][n].append(_asr_acd_rangen())
			ddc[d][n].append('GREY / 2015')
			top_file.writerow(ddc[d][n])
	print '------  T E L E T O P ---------------------'		
	print 'Report TOP generated'

	
		

	"""




        
        for  in range(len(defs_lists)):
		#print defs_lists[i]
		if  not fl[i][0] in zip(*defs_lists)[0]:
			print 'Here'
			fl.append(defs_lists[i])
               # 	for data in row:
               #         if not data in final_rows:
               #                 final_rows.append(row)
                #print row
                #defs = row[0]
                #dest = row[1]
                #rate = row[2]
                #if  not row[0] in final_rows:
                        #final_dict = dict()
                #final_dict[defs][dest] = rate
                #       Noop() 
        #print final_dict 
        	print fl

	"""

#price = [0.042,0.099, 0.0001 ,103, 0.034, 0.1, 0.45, 0.0003, 0.027]
#for pr in price:
#	print _marge_maker(pr)



def _asr_acd_rangen():
	""" ASR / ACD 23/6+ 59/8+ 97/7+ """
	a = str(random.sample(range(27,81),1)[0]) + '/' + str(random.sample(range(4,22),1)[0]) + '+'
	return a
		

def list_duplicates(seq):	
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
  # turn the set into a list (as requested)
  return list( seen_twice )

import random
a = random.sample(range(1, 1000), 999)
print list_duplicates(a) # yields [1, 2, 5]
	
a = [1,2,3,4,5,6,7,8,8,8,8,8,8,8,8,89,9,9,9000,0,0,0,0]# random.sample(range(1, 1000), 999)
print list_duplicates(a) # yields [1, 2, 5]
	
	
def _marge_maker(price):
	
	if price < 0.0001:
		Pr = price*0.3 + price
		return Pr
	if  (0.0001 <= price < 0.001 ):
		return (price*0.15 + price)
	if  0.001 <= price < 0.09 :
		return (price*0.10 + price)
	if  (0.01 <= price < 0.1 ):
		return (price*0.7 + price)
	if  0.1 <= price < 1 :
		return (price*0.05 + price)
	if  1 <= price < 10 :
		return (price*0.03 + price)
	if  10 <= price < 100 :
		return (price*0.02 + price)	
	if price > 100:
		return (price*0.01 +price)




_priceless()

#_priceless_RUB()
#_top()
#os.system('more TOP.csv')

