from cleanerData import *

collectData()

adi1 = ['TotalPopulation', 'SexRation', 'LiteracyRate', 'FemaleLiteracyRate', 'TotalSchoolE', 'GovtSchoolE', 'PrvtSchoolE', 'TeacherGovtE', 'TeacherPrvtE', 'WithElectricityE', 'WithComputerE', 'WithRoadsE', 'NumberOfClassroomE', 'TotalUniformIncentives', 'TotalTextBookIncentives', 'TotalEnrolmentGovtE', 'TotalEnrolmentPrvtE', 'RuralEnrolmentGovtE', 'RuralEnrolmentPrvtE']

print("Done Loading data . . .")

print('Aditya is Awesome')


def get_sum(target_year, parameter):
    total = 0
    # print(small_edu_data.keys())
    for district in small_edu_data[target_year]:
        try:
            total = total + quer(target_year, district, parameter)
        except:
            pass
    return total

print(get_sum(2016,'GovtSchoolE') - get_sum(2007,'GovtSchoolE') , "<- Difference in GovtSchoolE in 2016 and 2007")
print(get_sum(2016,'PrvtSchoolE') - get_sum(2007,'PrvtSchoolE') , "<- Difference in PrvtSchoolE in 2016 and 2007")



print((get_sum(2016,'GovtSchoolE') - get_sum(2007,'GovtSchoolE'))/get_sum(2007,'GovtSchoolE'), "<- Prct Difference in GovtSchoolE in 2016 and 2007")
print((get_sum(2016,'PrvtSchoolE') - get_sum(2007,'PrvtSchoolE'))/get_sum(2007,'PrvtSchoolE'), "<- Prct Difference in PrvtSchoolE in 2016 and 2007")


def get_percnt_govt_school(year):
    print(get_sum(year,'GovtSchoolE')/(get_sum(year,'GovtSchoolE') + get_sum(year,'PrvtSchoolE')),"<- Percent Govt School in " + str(year))


get_percnt_govt_school(2007)
get_percnt_govt_school(2016)




print(get_sum(2016,'TotalEnrolmentGovtE') - get_sum(2007,'TotalEnrolmentGovtE') , "<- Difference in Total Enrolment Govt School in 2016 and 2007")
print(get_sum(2016,'TotalEnrolmentPrvtE') - get_sum(2007,'TotalEnrolmentPrvtE') , "<- Difference in Total Enrolment Prvt School in 2016 and 2007")


print((get_sum(2016,'TotalEnrolmentGovtE') - get_sum(2007,'TotalEnrolmentGovtE') ) / get_sum(2007,'TotalEnrolmentGovtE')  , "<- Prct Difference in Total Enrolment Govt School in 2016 and 2007")


print((get_sum(2016,'TotalEnrolmentPrvtE') - get_sum(2007,'TotalEnrolmentPrvtE') ) / get_sum(2007,'TotalEnrolmentPrvtE')  , "<- Prct Difference in Total Enrolment Prvt School in 2016 and 2007")

def get_percnt_govt_school(year):
    print(get_sum(year,'TotalEnrolmentGovtE')/(get_sum(year,'TotalEnrolmentGovtE') + get_sum(year,'TotalEnrolmentPrvtE')),"<- Percent Govt School Enrolment in " + str(year))


get_percnt_govt_school(2007)
get_percnt_govt_school(2016)





print(get_sum(2016,'TeacherGovtE') - get_sum(2012,'TeacherGovtE') , "<- Difference in Total Teachers in Govt School in 2016 and 2012")
print(get_sum(2016,'TeacherPrvtE') - get_sum(2012,'TeacherPrvtE') , "<- Difference in Total Teachers in Prvt School in 2016 and 2012")


def get_percnt_govt_school(year):
    print(get_sum(year,'TeacherGovtE')/(get_sum(year,'TeacherGovtE') + get_sum(year,'TeacherPrvtE')),"<- Percent of all teachers in Govt School in " + str(year))


get_percnt_govt_school(2012)
get_percnt_govt_school(2016)










