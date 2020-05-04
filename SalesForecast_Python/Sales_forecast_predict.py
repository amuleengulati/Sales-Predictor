#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Fri Apr 24 12:02:18 2020

@author: Amuleen Gulati
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn
import numpy as np

from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

from sklearn.model_selection import cross_val_score

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost.sklearn import XGBRegressor

def distribution_plots(Rfunction, Bfunction, Rname, Bname, title):
    plt.figure(figsize=(10,6))
    seaborn.distplot(Rfunction, hist = False, color = 'r', label = Rname)
    seaborn.distplot(Bfunction, hist = False, color = 'b', label = Bname)
    plt.title(title)

def scatter_plot(target_test, predicted_sales):
    plt.title('Scatter Plot of Predicted values of test data vs Actual values of test data')
    plt.scatter(target_test, predicted_sales)
    plt.xlabel('Actual Sales')
    plt.ylabel('Predicted Sales')

sales_data = pd.read_csv('train_prepared.csv')
sales_data = sales_data.drop('Date', axis=1)
output_file = open('results.txt', 'w')

sales_data_corr = sales_data.corr()
plt.subplots(figsize=(20,10))
htmp = seaborn.heatmap(sales_data_corr, cmap = 'RdGy', linewidth =.005, annot = True)
htmp.set_yticklabels(htmp.get_yticklabels(), rotation=45, horizontalalignment='right')
plt.savefig('images/predict/corr_heatmap.png')
plt.close()

#Split the data and assign 'Weekly_Sales' to 'target_sales' and the rest of the features to 'other_data'.
other_data = sales_data[sales_data.loc[ :, sales_data.columns != 'Weekly_Sales'].columns]
target_sales = sales_data['Weekly_Sales']
other_train, other_test, target_train, target_test = train_test_split(other_data, target_sales, test_size = 0.2, random_state = 1)


###                              LINEAR REGRESSION                                         ###
linear_reg = LinearRegression()
linear_reg.fit(other_train,target_train)
predicted_sales = linear_reg.predict(other_test)

mae_linear = round(mean_absolute_error(target_test, predicted_sales),3)
mse_linear = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_linear = round(linear_reg.score(other_test, target_test),3)

#write results to output file
output_file.write("------------------------------------\n")
output_file.write("LINEAR REGRESSION MODEL STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_linear) + "\nMean Squared Error: " + str(mse_linear) + "\nMean Absolute Error: " + str(mae_linear)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/linear.png')
plt.close()

###                          RIDGE REGRESSION                  ###

#create a ridge regression object and fit it to training data
ridge_reg = Ridge(alpha = 1000)
ridge_reg.fit(other_train, target_train)

predicted_sales_ridge = ridge_reg.predict(other_test)

mae_ridge = round(mean_absolute_error(target_test, predicted_sales),3)
mse_ridge = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_ridge = round(ridge_reg.score(other_test, target_test),3)

#write results to output file
output_file.write("\n------------------------------------\n")
output_file.write("RIDGE REGRESSION STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_ridge) + "\nMean Squared Error: " + str(mse_ridge) + "\nMean Absolute Error: " + str(mae_ridge)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/ridge.png')
plt.close()

###                          RANDOM FOREST                  ###

#create a random forest object and fit it to training data
rf_reg = RandomForestRegressor(n_estimators = 150, n_jobs = 2, max_features = 7)
rf_reg.fit(other_train, target_train)
predicted_sales_ridge = rf_reg.predict(other_test)

mae_rf = round(mean_absolute_error(target_test, predicted_sales),3)
mse_rf = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_rf = round(rf_reg.score(other_test, target_test),3)

#write results to output file
output_file.write("\n------------------------------------\n")
output_file.write("RANDOM FOREST STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_rf) + "\nMean Squared Error: " + str(mse_rf) + "\nMean Absolute Error: " + str(mae_rf)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/random_forest.png')
plt.close()

###                              KNN                                         ###
knn = KNeighborsRegressor(n_neighbors=10,n_jobs=4)
knn.fit(other_train,target_train)
predicted_sales = knn.predict(other_test)

mae_knn = round(mean_absolute_error(target_test, predicted_sales),3)
mse_knn = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_knn = round(knn.score(other_test, target_test),3)

#write results to output file
output_file.write("\n------------------------------------\n")
output_file.write("KNN MODEL STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_knn) + "\nMean Squared Error: " + str(mse_knn) + "\nMean Absolute Error: " + str(mae_knn)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/knn.png')
plt.close()


###                              DECISION TREE                                        ###
dt = DecisionTreeRegressor(random_state=0)
dt.fit(other_train,target_train)
predicted_sales = dt.predict(other_test)

mae_dt = round(mean_absolute_error(target_test, predicted_sales),3)
mse_dt = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_dt = round(dt.score(other_test, target_test),3)

#write results to output file
output_file.write("\n------------------------------------\n")
output_file.write("DECISION TREE STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_dt) + "\nMean Squared Error: " + str(mse_dt) + "\nMean Absolute Error: " + str(mae_dt)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/dt.png')
plt.close()

###                              XGB REGRESSOR                                     ###
xgbr = XGBRegressor(objective='reg:linear', nthread= 4, n_estimators= 500, max_depth= 6, learning_rate= 0.5)
xb = xgbr.fit(other_train,target_train)
predicted_sales = xgbr.predict(other_test)

mae_xgbr = round(mean_absolute_error(target_test, predicted_sales),3)
mse_xgbr = round(mean_squared_error(target_test, predicted_sales),3)
accuracy_xgbr = round(xgbr.score(other_test, target_test),3)

#write results to output file
output_file.write("\n------------------------------------\n")
output_file.write("XGB REGRESSOR STATISTICS:\n")
output_file.write("------------------------------------\n")

text = "Accuracy: " + str(accuracy_xgbr) + "\nMean Squared Error: " + str(mse_xgbr) + "\nMean Absolute Error: " + str(mae_xgbr)
output_file.write(text)

scatter_plot(target_test, predicted_sales)
plt.savefig('images/predict/xgbr.png')
plt.close()

output_file.close()
