education_over_time.py: It plots the variation of various education parameters over time.

clearnerData.py: A supporting file that it is used by all other codes to query data.

geographic_clustering.py: Clusters district on the basis of their literacy rate and education level and plots the result on the map.

getLiteracyHistograms.py: plots histograms for literacy rate of different years.

incentives_vs_govt-enrollment.py: trains a SVM classifier to predict enrollment in government schools based on incentives.

incentives_vs_total-enrollment.py: trains a SVM classifier to predict total enrollment in schools based on incentives.

literacy_data.py: plots literacy rate on a map.

predict_literacy.py: Trains a SVM Regression model to predict literacy rate based on various education parameters.

regressor.py: Trains a logistic regression model to predict crime rates in various districts based on education parameters of the area. Also plots the decision boudaries based on features. 

svm.py: Trains a svm classifier to predict crime rates in various districts based on education parameters of the area. Also plots the decision boudaries based on features. 

random_forest.py: Trains a decision-tree classifier to predict crime rates in various districts based on education parameters of the area.Also plots the decision boudaries based on features.  

correlation_generator.py: calcuates the correlation(spearman and pearson coefficients) between various parameters.Also generates scatter plots for these parameters.


Dependencies:
-- Pickle is needed to read dictionary which is processed data.
-- The programs need python packages like sklearn, pandas, numpy, matplotlib, geopandas
-- Please download data from: https://drive.google.com/drive/folders/1waYNAyPxsRpmmFtk_SAuuWfWt8xTJI50?usp=sharing