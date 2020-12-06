import sys
from cleanerData import *
from getDistrictCode import *
import numpy as np
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import random

years = [2016, 2007, 2008, 2009, 2015]
for year in years:
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

	test_input = []
	test_output = []

	for i in range(len(uniform_list)):
		uniform = 5*uniform_list[i]/max_uniform
		books = 5*book_list[i]/max_books
		if uniform > 3 or books > 3:
			continue
		if random.random() < 0.8:
			train_input.append([uniform, books])
			train_output.append(get_enroll_class(enroll_list[i]))
		else:
			test_input.append([uniform, books])
			test_output.append(get_enroll_class(enroll_list[i]))

	train_input = np.array(train_input)
	train_output = np.array(train_output)
	clf = SVC(C = 100, kernel = 'rbf', degree = 10, gamma = 'auto', decision_function_shape='ovo')
	print("=== Starting Training SVM ===")
	clf.fit(train_input, train_output)
	print(year, clf.score(test_input, test_output))


	# upper_limit1 = np.percentile(train_input[:, 0], 98)
	# upper_limit2 = np.percentile(train_input[:, 1], 98)
	# mesh1_size = upper_limit1/1000
	# mesh2_size = upper_limit2/1000
	# print(upper_limit1, upper_limit2)

	# xx, yy = np.meshgrid(np.arange(0, upper_limit1, mesh1_size), np.arange(0, upper_limit2, mesh2_size))
	# predictions = clf.predict(np.c_[xx.ravel(), yy.ravel()])
	# predictions = predictions.reshape(xx.shape)
	# plt.contourf(xx, yy, predictions, cmap=plt.cm.coolwarm, alpha=0.8)
	# plt.scatter(train_input[:, 0], train_input[:, 1], c = train_output, cmap=plt.cm.coolwarm)
	# plt.xlabel('Normalized number of free uniforms distributed')
	# plt.ylabel('Normalized number of free textbooks distributed')
	# plt.xlim(xx.min(), xx.max())
	# plt.ylim(yy.min(), yy.max())
	# plt.xticks(())
	# plt.yticks(())
	# plt.title("Predicting total enrollment in schools based on incentives")
	# plt.show()
	# break