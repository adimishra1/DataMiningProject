from getDistrictCode import *
import pickle



set_of_final_keys = ["TotalPopulation","SexRation","LiteracyRate","MaleLiteracyRate","FemaleLiteracyRate",
"TotalSchoolE","GovtSchoolE","PrvtSchoolE","TeacherGovtE","TeacherPrvtE","WithElectricityE",
"WithComputerE","WithRoadsE","NumberOfClassroomE", "TotalUniformIncentives", "TotalTextBookIncentives"]
s1 = set(set_of_final_keys)
set_of_special_keys = ["P","PU","PUS","PUSH","U","US","USH"]
s2 = set(set_of_special_keys)

final_keys = dict()

final_keys["Basic data from Census 2011 Total Population(in 1000's)"] = "TotalPopulation"
final_keys["Basic data from Census 2011 Sex Ratio"] = "SexRation"
final_keys["Basic data from Census 2011 Literacy Rate"] = "LiteracyRate"
final_keys["Basic data from Census 2011 Female Literacy Rate"] = "MaleLiteracyRate"
final_keys["Basic data from Census 2011 Male Literacy Rate" ] = "FemaleLiteracyRate"
final_keys["Schools By Category Primary Only"] = "TotalSchoolE_P"
final_keys["Schools By Category Primary with Upper Primary"] = "TotalSchoolE_PU"
final_keys["Schools By Category Primary with upper Primary Sec"] = "TotalSchoolE_PUS"
final_keys["Schools By Category Primary with upper Primary Sec/H.Sec"] = "TotalSchoolE_PUSH"
final_keys["Schools By Category Upper Primary Only"] = "TotalSchoolE_U"
final_keys["Schools By Category Upper Primary with  Sec."] = "TotalSchoolE_US"
final_keys["Schools By Category Upper Primary with Sec./H.Sec"] = "TotalSchoolE_USH"
# final_keys["Schools By Category Total"] = "TotalSchoolE_T"


final_keys["Schools by Category: Government Primary Only"] = "GovtSchoolE_P"
final_keys["Schools by Category: Government Primary with Upper Primary"] = "GovtSchoolE_PU"
final_keys["Schools by Category: Government Primary with upper Primary Sec"] = "GovtSchoolE_PUS"
final_keys["Schools by Category: Government Primary with upper Primary Sec/H.Sec"] = "GovtSchoolE_PUSH"
final_keys["Schools by Category: Government Upper Primary Only"] = "GovtSchoolE_U"
final_keys["Schools by Category: Government Upper Primary with Sec."] = "GovtSchoolE_US"
final_keys["Schools by Category: Government Upper Primary with Sec./H.Sec"] = "GovtSchoolE_USH"
final_keys["Schools by Category: Government Total"] = "GovtSchoolE_T"



final_keys["Schools by Category: Private Primary Only"] = "PrvtSchoolE_P"
final_keys["Schools by Category: Private Primary with Upper Primary"] = "PrvtSchoolE_PU"
final_keys["Schools by Category: Private Primary with upper Primary Sec"] = "PrvtSchoolE_PUS"
final_keys["Schools by Category: Private Primary with upper Primary Sec/H.Sec"] = "PrvtSchoolE_PUSH"
final_keys["Schools by Category: Private Upper Primary Only"] = "PrvtSchoolE_U"
final_keys["Schools by Category: Private Upper Primary with Sec."] = "PrvtSchoolE_US"
final_keys["Schools by Category: Private Upper Primary with Sec./H.Sec"] = "PrvtSchoolE_USH"
# final_keys["Schools by Category: Private Total"] = "PrvtSchoolE_T"



final_keys["Teachers by School Category (Government) Primary Only"] = "TeacherGovtE_P"
final_keys["Teachers by School Category (Government) Primary with Upper Primary"] = "TeacherGovtE_PU"
final_keys["Teachers by School Category (Government) Primary with upper Primary Sec"] = "TeacherGovtE_PUS"
final_keys["Teachers by School Category (Government) Primary with upper Primary Sec/H.Sec"] = "TeacherGovtE_PUSH"
final_keys["Teachers by School Category (Government) Upper Primary Only"] = "TeacherGovtE_U"
final_keys["Teachers by School Category (Government) Upper Primary with Sec."] = "TeacherGovtE_US"
final_keys["Teachers by School Category (Government) Upper Primary with Sec./H.Sec"] = "TeacherGovtE_USH"
final_keys["Teachers by School Category (Government) Total"] = "TeacherGovtE_T"



final_keys["Teachers by School Category (Private) Primary Only"] = "TeacherPrvtE_P"
final_keys["Teachers by School Category (Private) Primary with Upper Primary"] = "TeacherPrvtE_PU"
final_keys["Teachers by School Category (Private) Primary with upper Primary Sec"] = "TeacherPrvtE_PUS"
final_keys["Teachers by School Category (Private) Primary with upper Primary Sec/H.Sec"] = "TeacherPrvtE_PUSH"
final_keys["Teachers by School Category (Private) Upper Primary Only"] = "TeacherPrvtE_U"
final_keys["Teachers by School Category (Private) Upper Primary with Sec."] = "TeacherPrvtE_US"
final_keys["Teachers by School Category (Private) Upper Primary with Sec./H.Sec"] = "TeacherPrvtE_USH"
# final_keys["Teachers by School Category (Private) Total"] = "TeacherPrvtE_T"




final_keys["Schools with Electricity Primary Only"] = "WithElectricityE_P"
final_keys["Schools with Electricity Primary with Upper Primary"] = "WithElectricityE_PU"
final_keys["Schools with Electricity Primary with upper Primary Sec"] = "WithElectricityE_PUS"
final_keys["Schools with Electricity Primary with upper Primary Sec/H.Sec"] = "WithElectricityE_PUSH"
final_keys["Schools with Electricity Upper Primary Only"] = "WithElectricityE_U"
final_keys["Schools with Electricity Upper Primary with Sec."] = "WithElectricityE_US"
final_keys["Schools with Electricity Upper Primary with Sec./H.Sec"] = "WithElectricityE_USH"
# final_keys["Schools with Electricity Total"] = "WithElectricityE_T"




final_keys["Schools with Computer Primary Only"] = "WithComputerE_P"
final_keys["Schools with Computer Primary with Upper Primary"] = "WithComputerE_PU"
final_keys["Schools with Computer Primary with upper Primary Sec"] = "WithComputerE_PUS"
final_keys["Schools with Computer Primary with upper Primary Sec/H.Sec"] = "WithComputerE_PUSH"
final_keys["Schools with Computer Upper Primary Only"] = "WithComputerE_U"
final_keys["Schools with Computer Upper Primary with Sec."] = "WithComputerE_US"
final_keys["Schools with Computer Upper Primary with Sec./H.Sec"] = "WithComputerE_USH"
# final_keys["Schools with Computer Total"] = "WithComputerE_T"




final_keys["Schools Approachable by All Weather Road Primary Only"] = "WithRoadsE_P"
final_keys["Schools Approachable by All Weather Road Primary with Upper Primary"] = "WithRoadsE_PU"
final_keys["Schools Approachable by All Weather Road Primary with upper Primary Sec"] = "WithRoadsE_PUS"
final_keys["Schools Approachable by All Weather Road Primary with upper Primary Sec/H.Sec"] = "WithRoadsE_PUSH"
final_keys["Schools Approachable by All Weather Road Upper Primary Only"] = "WithRoadsE_U"
final_keys["Schools Approachable by All Weather Road Upper Primary with Sec."] = "WithRoadsE_US"
final_keys["Schools Approachable by All Weather Road Upper Primary with Sec./H.Sec"] = "WithRoadsE_USH"
# final_keys["Schools Approachable by All Weather Road Total"] = "WithRoadsE_T"






final_keys["Total Classrooms Primary Only"] = "NumberOfClassroomE_P"
final_keys["Total Classrooms Primary with Upper Primary"] = "NumberOfClassroomE_PU"
final_keys["Total Classrooms Primary with upper Primary Sec"] = "NumberOfClassroomE_PUS"
final_keys["Total Classrooms Primary with upper Primary Sec/H.Sec"] = "NumberOfClassroomE_PUSH"
final_keys["Total Classrooms Upper Primary Only"] = "NumberOfClassroomE_U"
final_keys["Total Classrooms Upper Primary with Sec."] = "NumberOfClassroomE_US"
final_keys["Total Classrooms Upper Primary with Sec./H.Sec"] = "NumberOfClassroomE_USH"
# final_keys["Total Classrooms Total"] = "NumberOfClassroomE_T"




final_keys["Total Poulation"] = "TotalPopulation"
final_keys["Sexratio"] = "SexRation"
final_keys["Overall Literacy"] = "LiteracyRate"
# final_keys["Female Literacy"] = "MaleLiteracyRate"
final_keys["Female Literacy" ] = "FemaleLiteracyRate"
# final_keys[""] = "TotalSchoolE_P"
# final_keys[""] = "TotalSchoolE_PU"
# final_keys[""] = "TotalSchoolE_PUS"
# final_keys[""] = "TotalSchoolE_PUSH"
# final_keys[""] = "TotalSchoolE_U"
# final_keys[""] = "TotalSchoolE_US"
# final_keys[""] = "TotalSchoolE_USH"
# final_keys[""] = "TotalSchoolE_T"


final_keys["Total Schools - Government Primary"] = "GovtSchoolE_P"
final_keys["Total Schools - Government Primary with Upper primary"] = "GovtSchoolE_PU"
final_keys["Total Schools - Government Primary with Upper primary and secondary"] = "GovtSchoolE_PUS"
final_keys["Total Schools - Government Primary with Upper Primary sec and higher sec."] = "GovtSchoolE_PUSH"
final_keys["Total Schools - Government Upper Primary Only"] = "GovtSchoolE_U"
final_keys["Total Schools - Government Upper Primary with secondary"] = "GovtSchoolE_US"
final_keys["Total Schools - Government Upper Primary with sec. and higher sec."] = "GovtSchoolE_USH"
# final_keys[""] = "GovtSchoolE_T"



final_keys["Total Schools - Private Primary"] = "PrvtSchoolE_P"
final_keys["Total Schools - Private Primary with Upper primary"] = "PrvtSchoolE_PU"
final_keys["Total Schools - Private Primary with Upper primary and secondary"] = "PrvtSchoolE_PUS"
final_keys["Total Schools - Private Primary with Upper Primary sec/higher sec."] = "PrvtSchoolE_PUSH"
final_keys["Total Schools - Private Upper Primary Only"] = "PrvtSchoolE_U"
final_keys["Total Schools - Private Upper Primary with secondary"] = "PrvtSchoolE_US"
final_keys["Total Schools - Private Upper Primary with sec./higher sec."] = "PrvtSchoolE_USH"
# final_keys[""] = "GovtSchoolE_T"




final_keys["Enrolment by medium of instructions Teachers in Government Schools Primary"] = "TeacherGovtE_P"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Primary with Upper primary"] = "TeacherGovtE_PU"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Primary with Upper primary sec"] = "TeacherGovtE_PUS"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Primary with Upper Primary sec and higher sec."] = "TeacherGovtE_PUSH"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Upper Primary Only"] = "TeacherGovtE_U"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Upper Primary sec"] = "TeacherGovtE_US"
final_keys["Enrolment by medium of instructions Teachers in Government Schools Upper Primary with sec. and higher sec."] = "TeacherGovtE_USH"
# final_keys[""] = "GovtSchoolE_T"





final_keys["Enrolment by medium of instructions Teachers in Private Schools Primary"] = "TeacherPrvtE_P"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Primary with Upper primary"] = "TeacherPrvtE_PU"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Primary with Upper Primary sec"] = "TeacherPrvtE_PUS"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Primary with Upper Primary sec and higher sec."] = "TeacherPrvtE_PUSH"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Upper Primary Only"] = "TeacherPrvtE_U"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Upper Primary sec"] = "TeacherPrvtE_US"
final_keys["Enrolment by medium of instructions Teachers in Private Schools Upper Primary with sec. and higher sec."] = "TeacherPrvtE_USH"
# final_keys[""] = "GovtSchoolE_T"


final_keys["Incentive Type Number of Schools with Electricity Primary"] = "WithElectricityE_P"
final_keys["Incentive Type Number of Schools with Electricity Primary with Upper primary"] = "WithElectricityE_PU"
final_keys["Incentive Type Number of Schools with Electricity Primary with Upper primary and secondary"] = "WithElectricityE_PUS"
final_keys["Incentive Type Number of Schools with Electricity Primary with Upper Primary sec./higher sec."] = "WithElectricityE_PUSH"
final_keys["Incentive Type Number of Schools with Electricity Upper Primary Only"] = "WithElectricityE_U"
final_keys["Incentive Type Number of Schools with Electricity Upper Primary with secondary"] = "WithElectricityE_US"
final_keys["Incentive Type Number of Schools with Electricity Upper Primary with sec./higher sec."] = "WithElectricityE_USH"
# final_keys[""] = "GovtSchoolE_T"





final_keys["Incentive Type Number of Schools with Computer Primary"] = "WithComputerE_P"
final_keys["Incentive Type Number of Schools with Computer Primary with Upper primary"] = "WithComputerE_PU"
final_keys["Incentive Type Number of Schools with Computer Primary with Upper primary and secondary"] = "WithComputerE_PUS"
final_keys["Incentive Type Number of Schools with Computer Primary with Upper Primary sec./higher sec."] = "WithComputerE_PUSH"
final_keys["Incentive Type Number of Schools with Computer Upper Primary Only"] = "WithComputerE_U"
final_keys["Incentive Type Number of Schools with Computer Upper Primary with secondary"] = "WithComputerE_US"
final_keys["Incentive Type Number of Schools with Computer Upper Primary with sec./higher sec."] = "WithComputerE_USH"
# final_keys[""] = "GovtSchoolE_T"




final_keys["Incentive Type Number of Schools approachable by all weather  roads Primary"] = "WithRoadsE_P"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Primary with Upper primary"] = "WithRoadsE_PU"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Primary with Upper primary and secondary"] = "WithRoadsE_PUS"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Primary with Upper Primary sec./higher sec."] = "WithRoadsE_PUSH"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Upper Primary Only"] = "WithRoadsE_U"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Upper Primary with secondary"] = "WithRoadsE_US"
final_keys["Incentive Type Number of Schools approachable by all weather  roads Upper Primary with sec./higher sec."] = "WithRoadsE_USH"
# final_keys[""] = "GovtSchoolE_T"





final_keys["Total Classrooms Primary"] = "NumberOfClassroomE_P"
final_keys["Total Classrooms Primary with Upper primary"] = "NumberOfClassroomE_PU"
final_keys["Total Classrooms Primary with Upper primary and secondary"] = "NumberOfClassroomE_PUS"
final_keys["Total Classrooms Primary with Upper Primary sec./higher sec."] = "NumberOfClassroomE_PUSH"
final_keys["Total Classrooms Upper Primary Only"] = "NumberOfClassroomE_U"
final_keys["Total Classrooms Upper Primary with secondary"] = "NumberOfClassroomE_US"
final_keys["Total Classrooms Upper Primary with sec./higher sec."] = "NumberOfClassroomE_USH"
# final_keys[""] = "GovtSchoolE_T"




def strC(s1):
    return s1.lower().replace(' ','').replace('-','').replace('.','')

fkey2 = {}

for key,value in final_keys.items():
    fkey2[strC(key)] = value


small_edu_data = {}
done = False


def getVal(s):
    s = strC(s)
    if s in fkey2:
        return fkey2[s]
    return "NA"

def quer(year,dist,key):
    global done,small_edu_data
    if done == False: collectData()
    if isinstance(year,str):  year = int(year[0:4])
    if isinstance(dist,str): dist = getDistrictCode(dist)
    val = 0
    if key[-1]=='E':
        for types in set_of_special_keys: val += small_edu_data[year][dist][(key + "_" + types)]    
    else:
        val = small_edu_data[year][dist][key]
    return val

def genKeys(year):
    edu_file = open("Education","rb")
    edu_data = pickle.load(edu_file,encoding='utf-8')
    edu_file.close()
    allkey = set()
    ydata = edu_data[year]
    for ddata in ydata.values():
        for keys in ddata.keys():
            allkey.add(keys)
    # for i in sorted(allkey): print(i)
    



def collectData():
    global done,small_edu_data,fkey2
    done = True
    edu_file = open("Education","rb")
    edu_data = pickle.load(edu_file,encoding='utf-8')
    edu_file.close()
    for year,ydata in edu_data.items():
        small_edu_data[int(year[0:4])] = {}
        yr = int(year[0:4])
        if year >= '2007-08':
            for distr,ddata in ydata.items():
                tmp = set()
                dist = getDistrictCode(distr)
                small_edu_data[yr][dist] = {}
                small_edu_data[yr][dist]["TotalTextBookIncentives"] = 0
                small_edu_data[yr][dist]["TotalUniformIncentives"] = 0
                tmp2 = {}
                poss = False
                for item in ddata.keys():
                    if yr<2014:
                        if 'Uniform' in item:
                            try:
                                small_edu_data[yr][dist]["TotalUniformIncentives"] += int(ddata[item])
                            except:
                                pass
                        elif 'Text Book' in item:
                            try:
                                small_edu_data[yr][dist]["TotalTextBookIncentives"] += int(ddata[item])
                            except:
                                pass
                    else:
                        if 'Uniform' in item and 'All' in item:
                            try:
                                small_edu_data[yr][dist]["TotalUniformIncentives"] += int(ddata[item])
                            except:
                                pass
                        elif 'TextBook' in item and 'All' in item:
                            try:
                                small_edu_data[yr][dist]["TotalTextBookIncentives"] += int(ddata[item])
                            except:
                                pass
                    item2 = strC(item)
                    if item2 in fkey2:
                        itemcode = fkey2[item2]
                        small_edu_data[yr][dist][itemcode] = ddata[item]
                        tmp.add(fkey2[item2].split('_')[0])
                        if fkey2[item2].split('_')[0][-1]=='E':
                            poss = True
                        if len(fkey2[item2].split('_')) > 1:
                            if fkey2[item2].split('_')[0] not in tmp2:
                                tmp2[fkey2[item2].split('_')[0]] = set()
                            tmp2[fkey2[item2].split('_')[0]].add(fkey2[item2].split('_')[1])
                
                for key,val in tmp2.items():
                    if len(s2.difference(val)) > 0: 
                        for absnt in s2.difference(val):
                            small_edu_data[yr][dist][key + '_' + absnt] = 0


collectData()
# genKeys('2009-10')

# print(quer(2007,"Balrampur",'TotalUniformIncentives'))
# print(quer(2016,"Bokaro",'SexRation'))
# print(quer(2016,getDistrictCode('Bokaro'),'SexRation'))


