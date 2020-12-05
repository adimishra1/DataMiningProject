import sys
from cleanerData import *
from getDistrictCode import *
import numpy as np
from sklearn.svm import SVR
import math
from sklearn.metrics import accuracy_score
import random

year = 2016

features = ['GovtSchoolE', 'PrvtSchoolE', 'TotalUniformIncentives', 'TotalTextBookIncentives', 'TotalEnrolmentGovtE', 'TotalEnrolmentPrvtE', 'RuralEnrolmentGovtE', 'RuralEnrolmentPrvtE']
max_feature = []
min_feature = []

train_input = []
train_output = []
test_input = []
test_output = []

for district in small_edu_data[year]:
	for i in range(len(features)):
		max_feature.append(quer(year, district, features[i]))
		min_feature.append(quer(year, district, features[i]))
	break

count_test = -1
count_train = -1
for district in small_edu_data[year]:
	if math.isnan(quer(year, district, 'LiteracyRate')):
		continue
	if random.random() < 0.8:
		count_train = count_train + 1
		train_input.append([])
		for i in range(len(features)):
			train_input[count_train].append(quer(year, district, features[i]))
			if quer(year, district, features[i]) > max_feature[i]:
				max_feature[i] = quer(year, district, features[i])
			if quer(year, district, features[i]) < min_feature[i]:
				min_feature[i] = quer(year, district, features[i])
		train_output.append(quer(year, district, 'LiteracyRate'))
	else:
		count_test = count_test + 1
		test_input.append([])
		for i in range(len(features)):
			test_input[count_test].append(quer(year, district, features[i]))
			if quer(year, district, features[i]) > max_feature[i]:
				max_feature[i] = quer(year, district, features[i])
			if quer(year, district, features[i]) < min_feature[i]:
				min_feature[i] = quer(year, district, features[i])
		test_output.append(quer(year, district, 'LiteracyRate'))

for dist_code in range(len(train_output)):
	for i in range(len(features)):
		train_input[dist_code][i] = 100*train_input[dist_code][i]/max_feature[i]

for dist_code in range(len(test_input)):
	for i in range(len(features)):
		test_input[dist_code][i] = 100*test_input[dist_code][i]/max_feature[i]


train_input = np.array(train_input)
test_input = np.array(test_input)

print("=== Starting Training SVM ===")
clf = SVR(C = 1, kernel = 'rbf', degree = 10, gamma = 'auto')
clf.fit(train_input, train_output)

predictions = clf.predict(test_input)
correct = 0
total = 0
for i in range(len(test_output)):
	total = total + 1
	if abs(test_output[i] - predictions[i]) < 10:
		correct = correct + 1
print(correct/total)
