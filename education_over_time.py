import sys
from cleanerData import *
from getDistrictCode import *
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import random
import math

year = [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016]
education_parameters = ["GovtSchoolE", "PrvtSchoolE", "TotalUniformIncentives", "TotalTextBookIncentives", "TotalEnrolmentGovtE", "TotalEnrolmentPrvtE", "RuralEnrolmentGovtE"]

def get_avg_literacy_rate(target_year):
    total_pop = 0
    literacy = 0
    for district in small_edu_data[target_year]:
        try:
            if math.isnan(float(small_edu_data[target_year][district]['TotalPopulation'])) or math.isnan(float(small_edu_data[target_year][district]['LiteracyRate'])):
                continue
            else:
                total_pop = total_pop + float(small_edu_data[target_year][district]['TotalPopulation'])
                literacy = literacy + float(small_edu_data[target_year][district]['TotalPopulation']) * float(small_edu_data[target_year][district]['LiteracyRate'])
        except:
            continue
    return literacy/total_pop

def get_sum(target_year, parameter):
    total = 0
    for district in small_edu_data[target_year]:
        try:
            total = total + quer(target_year, district, parameter)
        except:
            continue
    return total

for parameter in education_parameters:
    parameter_sum=[]
    for YEAR in year:
        parameter_sum.append(get_sum(YEAR, parameter))
    if parameter == "GovtSchoolE":
        plt.ylabel("Total Number of Government Schools")
    if parameter == "PrvtSchoolE":
        plt.ylabel("Total Number of Private Schools")
    if parameter == "TotalUniformIncentives":
        plt.ylabel("Total number of free uniforms distributed")
    if parameter == "TotalTextBookIncentives":
        plt.ylabel("Total number of free books distributed")
    if parameter == "TotalEnrolmentGovtE":
        plt.ylabel("Total number of students enrolled in Government SChools")
    if parameter == "TotalEnrolmentPrvtE":
        plt.ylabel("Total number of students enrolled in Private Schools")
    if parameter == "RuralEnrolmentGovtE":
        plt.ylabel("Total number of students enrolled in Rural areas")
    plt.xlabel("Year")
    plt.bar(year,parameter_sum)
    plt.tight_layout()
    plt.savefig("Education_params/" + parameter + ".png")
    plt.clf()