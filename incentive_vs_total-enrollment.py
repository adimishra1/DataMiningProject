import sys
from cleanerData import *
from getDistrictCode import *
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

year = 2016 
max_unif_dist = 0
max_book_dist = 0
max_uniform = small_edu_data[year][list(small_edu_data[year].keys())[0]]['TotalUniformIncentives']
min_uniform = small_edu_data[year][list(small_edu_data[year].keys())[0]]['TotalUniformIncentives']
max_books = small_edu_data[year][  list(small_edu_data[year].keys())[0]]['TotalTextBookIncentives']
min_books = small_edu_data[year][  list(small_edu_data[year].keys())[0]]['TotalTextBookIncentives']
max_enroll = quer(year, list(small_edu_data[year].keys())[0], 'TotalEnrolmentGovtE') + quer(year, list(small_edu_data[year].keys())[0], 'TotalEnrolmentPrvtE')
min_enroll = quer(year, list(small_edu_data[year].keys())[0], 'TotalEnrolmentGovtE') + quer(year, list(small_edu_data[year].keys())[0], 'TotalEnrolmentPrvtE')

uniform_list = []
book_list = []
enroll_list = []

for district in small_edu_data[year]:
	uniform_list.append(small_edu_data[year][district]['TotalUniformIncentives'])
	if small_edu_data[year][district]['TotalUniformIncentives'] > max_uniform:
		max_unif_dist = district
		max_uniform = small_edu_data[year][district]['TotalUniformIncentives']
	if small_edu_data[year][district]['TotalUniformIncentives'] < min_uniform:
		min_uniform = small_edu_data[year][district]['TotalUniformIncentives']

	book_list.append(small_edu_data[year][district]['TotalTextBookIncentives'])
	if small_edu_data[year][district]['TotalTextBookIncentives'] > max_books:
		max_book_dist = district
		max_books = small_edu_data[year][district]['TotalTextBookIncentives']
	if small_edu_data[year][district]['TotalTextBookIncentives'] < min_books:
		min_books = small_edu_data[year][district]['TotalTextBookIncentives']

	enroll_list.append(quer(year, district, 'TotalEnrolmentGovtE') + quer(year, district, 'TotalEnrolmentPrvtE'))
	if quer(year, district, 'TotalEnrolmentGovtE') + quer(year, district, 'TotalEnrolmentPrvtE') > max_enroll:
		max_enroll = quer(year, district, 'TotalEnrolmentGovtE') + quer(year, district, 'TotalEnrolmentPrvtE')
	if quer(year, district, 'TotalEnrolmentGovtE') + quer(year, district, 'TotalEnrolmentPrvtE') < min_enroll:
		min_enroll = quer(year, district, 'TotalEnrolmentGovtE') + quer(year, district, 'TotalEnrolmentPrvtE')

enroll_array = np.array(enroll_list)
enroll_q1 = np.percentile(enroll_array, 25)
enroll_mid = np.percentile(enroll_array, 50)
enroll_q2 = np.percentile(enroll_array, 75)
# print(enroll_q1, enroll_q2)

def get_enroll_class(num_enroll):
	if num_enroll < enroll_q1:
		return 0
	elif num_enroll < enroll_mid:
		return 1
	elif num_enroll < enroll_q2:
		return 2
	else:
		return 3

train_input = [] #(uniform, textbooks)
train_output = []
for i in range(len(uniform_list)):
	train_input.append([5*uniform_list[i]/(max_uniform - min_uniform), 5*book_list[i]/(max_books - min_books)])
	train_output.append(get_enroll_class(enroll_list[i]))

train_input = np.array(train_input)
train_output = np.array(train_output)
clf = SVC(C = 100, kernel = 'rbf', degree = 10, gamma = 'auto', decision_function_shape='ovo')
print("=== Starting Training SVM ===")
clf.fit(train_input, train_output)
print(clf.score(train_input, train_output))