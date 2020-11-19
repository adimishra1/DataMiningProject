import pickle 
edu_file = open("Education","rb")
edu_data = pickle.load(edu_file,encoding='utf-8')
# print(edu_data.keys())
YEAR = "2013-14"
CRIME_YEAR = 2014
district =dict()

for districts in edu_data[YEAR].keys():
	tmp = dict()
	val1 = edu_data[YEAR][districts]['Total Schools - Government Primary']
	# print(type(val1))
	tmp['GovPrim'] = val1.astype(int)
	val2 = edu_data[YEAR][districts]['Total Schools - Government Primary with Upper primary']
	tmp['GovPrimUpPrim'] = val2.astype(int)
	val3 = edu_data[YEAR][districts]['Total Schools - Government Upper Primary Only']
	tmp['GovUpPrim'] = val3.astype(int)
	val4 = edu_data[YEAR][districts]['Total Schools - Government Primary with Upper Primary sec and higher sec.']
	tmp['All'] = val4.astype(int)
	val5 = edu_data[YEAR][districts]['Total Schools - Government Upper Primary with sec. and higher sec.']
	tmp['GovUpPrimHS'] = val5.astype(int)
	val6 = edu_data[YEAR][districts]['Total Schools - Government Upper Primary with secondary']
	tmp['GovUpPrimS'] = val6.astype(int)
	val7 = edu_data[YEAR][districts]['Total Schools - Government No Response']
	tmp['GovNR'] = val7.astype(int)
	val8 = edu_data[YEAR][districts]['Total Schools - Government Primary with Upper primary and secondary']
	tmp['GovPrimUpPrimS'] = val8.astype(int)


	dis = districts.strip(" ").lower()
	district[dis]= tmp
print(district)