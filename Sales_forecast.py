#! /usr/bin/env python

# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 18:08:27 2020

@author: Amuleen Gulati
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn

from datetime import datetime

#loading the dataset
sales_data = pd.read_csv('train.csv')


#defining functions for data visualization
def scatter_plots(data, col):
    plt.figure()
    plt.scatter(data[col], data['Weekly_Sales'])
    plt.xlabel(col)
    plt.ylabel('Weekly_Sales')

def residual_plots(data, col):
    plt.figure()
    seaborn.residplot(x=data[col], y=data['Weekly_Sales'], data = data)
    plt.show()

def distribution_plots(Rfunction, Bfunction, Rname, Bname, title):
    plt.figure(figsize=(10,6))
    seaborn.distplot(Rfunction, hist = False, color = 'r', label = Rname)
    seaborn.distplot(Bfunction, hist = False, color = 'b', label = Bname)
    plt.title(title)
    plt.show()
    plt.close()

def regression_plots(data, col):
    plt.figure()
    seaborn.regplot(x=data[col], y=data['Weekly_Sales'], data = data, line_kws = {'color' : 'green'})
    plt.ylim(0,)

#Display data
print("Loading data..")
print(sales_data.head())
print(sales_data.tail())


##                 DATA PREPARATION              ##


#change datatype of date feature from object to datetime
sales_data['Date'] = pd.to_datetime(sales_data['Date'], format = "%Y-%m-%d")

#Separate date into day, month and year
sales_data['year'] = sales_data['Date'].dt.year
sales_data['month'] = sales_data['Date'].dt.month
sales_data['week_day'] = sales_data['Date'].dt.weekday

#change datatype of IsHoliday to int
list_holiday = sales_data.IsHoliday.tolist()
sales_data['IsHolidayInt'] = [int(x) for x in list_holiday]

print(sales_data.head())
sales_data.to_csv('train_prepared.csv', index = False)



##              DATA VISUALIZATION                ##

#plot to visualize the number of departments in all stores
plt.figure(figsize = (15,10))
seaborn.barplot(sales_data.Store, sales_data.Dept)
plt.title("Number of Departments across different Stores")
plt.savefig('images/visualize/depts.png')
plt.close()

#plot to visualize the weekly sales in all stores
plt.figure(figsize=(15,10))
seaborn.barplot(sales_data.Store, sales_data.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of different Stores")
plt.savefig('images/visualize/weekly_sales.png')
plt.close()

#plot to visualize the monthly sales of all Stores for each year
plt.figure(figsize=(15,10))
seaborn.lineplot(sales_data.month, sales_data.Weekly_Sales, hue = sales_data.year)
plt.title('Weekly_Sales of the company for each Year by Months')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.savefig('images/visualize/monthly.png')
plt.close()

#plot to visualize sales year-wise for the month of October

january = sales_data[sales_data['month'] == 1]
plt.figure(figsize=(15,10))
seaborn.barplot(january.year, january.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in January")
plt.savefig('images/visualize/jan_sales.png')
plt.close()

feb = sales_data[sales_data['month'] == 2]
plt.figure(figsize=(15,10))
seaborn.barplot(feb.year, feb.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in February")
plt.savefig('images/visualize/feb_sales.png')
plt.close()

mar = sales_data[sales_data['month'] == 3]
plt.figure(figsize=(15,10))
seaborn.barplot(mar.year, mar.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in March")
plt.savefig('images/visualize/mar_sales.png')
plt.close()

apr = sales_data[sales_data['month'] == 4]
plt.figure(figsize=(15,10))
seaborn.barplot(apr.year, apr.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in April")
plt.savefig('images/visualize/apr_sales.png')
plt.close()

may = sales_data[sales_data['month'] == 5]
plt.figure(figsize=(15,10))
seaborn.barplot(may.year, may.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in May")
plt.savefig('images/visualize/may_sales.png')
plt.close()

june = sales_data[sales_data['month'] == 6]
plt.figure(figsize=(15,10))
seaborn.barplot(june.year, june.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in June")
plt.savefig('images/visualize/june_sales.png')
plt.close()

jul = sales_data[sales_data['month'] == 7]
plt.figure(figsize=(15,10))
seaborn.barplot(jul.year, jul.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in July")
plt.savefig('images/visualize/jul_sales.png')
plt.close()

aug = sales_data[sales_data['month'] == 8]
plt.figure(figsize=(15,10))
seaborn.barplot(aug.year, aug.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in August")
plt.savefig('images/visualize/aug_sales.png')
plt.close()

sep = sales_data[sales_data['month'] == 9]
plt.figure(figsize=(15,10))
seaborn.barplot(sep.year, sep.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in September")
plt.savefig('images/visualize/sep_sales.png')
plt.close()

october = sales_data[sales_data['month'] == 10]
plt.figure(figsize=(15,10))
seaborn.barplot(october.year, october.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in October")
plt.savefig('images/visualize/oct_sales.png')
plt.close()

nov = sales_data[sales_data['month'] == 11]
plt.figure(figsize=(15,10))
seaborn.barplot(nov.year, nov.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in November")
plt.savefig('images/visualize/nov_sales.png')
plt.close()

dec = sales_data[sales_data['month'] == 12]
plt.figure(figsize=(15,10))
seaborn.barplot(dec.year, dec.Weekly_Sales, alpha=0.8)
plt.title("Weekly Sales of stores in December")
plt.savefig('images/visualize/dec_sales.png')
plt.close()

plt.figure(figsize=(16,8))
plt.title('Weekly Sales of stores in 2010')
plt.xlabel('Store')
plt.ylabel('Sales')
year = sales_data['year'] == 2010
year1 = sales_data[year]
seaborn.lineplot(year1.Store, year1.Weekly_Sales)
plt.savefig('images/visualize/year1.png')
plt.close()

plt.figure(figsize=(16,8))
plt.title('Weekly Sales of stores in 2011')
plt.xlabel('Store')
plt.ylabel('Sales')
year = sales_data['year'] == 2011
year2 = sales_data[year]
seaborn.lineplot(year2.Store, year2.Weekly_Sales)
plt.savefig('images/visualize/year2.png')
plt.close()

plt.figure(figsize=(16,8))
plt.title('Weekly Sales of stores in 2012')
plt.xlabel('Store')
plt.ylabel('Sales')
year = sales_data['year'] == 2012
year3 = sales_data[year]
seaborn.lineplot(year3.Store, year3.Weekly_Sales)
plt.savefig('images/visualize/year3.png')
plt.close()

#function to visualize performance of stores for each year during Thanksgiving time-
def thanksgiving_year(year):
    plt.figure(figsize=(15,10))
    plt.title("Performance during Thanksgiving in " + str(year))
    mnth = sales_data['month'] == 10
    yr = sales_data['year'] == year
    october = sales_data[mnth & yr]
    seaborn.barplot(october.Store, october.Weekly_Sales, alpha=0.8)

#function to visualize performance of stores for each year during Christmas time-
def christmas_year(year):
    plt.figure(figsize=(15,10))
    plt.title("Performance during Christmas in " + str(year))
    mnth = sales_data['month'] == 12
    yr = sales_data['year'] == year
    december = sales_data[mnth & yr]
    seaborn.barplot(december.Store, december.Weekly_Sales, alpha=0.8)

#plot to visualize performance of stores for 2010 during Thanksgiving time
thanksgiving_year(2010)
plt.savefig('images/visualize/Thanksgiving2010.png')
plt.close()

#plot bar chart of performance of stores for 2011 during Thanksgiving time
thanksgiving_year(2011)
plt.savefig('images/visualize/Thanksgiving2011.png')
plt.close()

#plot bar chart of performance of stores for 2012 during Thanksgiving time
thanksgiving_year(2012)
plt.savefig('images/visualize/Thanksgiving2012.png')
plt.close()

#plot bar chart of performance of stores for 2010 during Christmas time
christmas_year(2010)
plt.savefig('images/visualize/christmas2010.png')
plt.close()

#plot bar chart of performance of stores for 2011 during Christmas time
christmas_year(2011)
plt.savefig('images/visualize/christmas2011.png')
plt.close()


#plot line plot to visualize the trends of store performances for each year during Thanksgiving time
plt.figure(figsize=(16,8))
plt.title('Performance of stores during Thanksgiving time by Years')
plt.xlabel('Store')
plt.ylabel('Sales')
mnth = sales_data['month'] == 10
october = sales_data[mnth]
seaborn.lineplot(october.Store, october.Weekly_Sales, hue = october.year)
plt.savefig('images/visualize/allThanksgiving.png')
plt.close()

#plot line plot to visualize the trends of store performances for each year during Christmas time
plt.figure(figsize=(16,8))
plt.title('Performance of stores during Christmas time by Years')
plt.xlabel('Store')
plt.ylabel('Sales')
mnth_12 = sales_data['month'] == 12
december = sales_data[mnth_12]
seaborn.lineplot(december.Store, december.Weekly_Sales, hue = december.year)
plt.savefig('images/visualize/allChristmas.png')
plt.close()

##plot line plot to visualize the trends of store performances for each year during Super Bowl time
plt.figure(figsize=(16,8))
plt.title('Performance of stores during Super Bowl time by Years')
plt.xlabel('Store')
plt.ylabel('Sales')
mnth_02 = sales_data['month'] == 2
feb= sales_data[mnth_02]
seaborn.lineplot(feb.Store, feb.Weekly_Sales, hue = feb.year)
plt.savefig('images/visualize/allSuperBowl.png')
plt.close()

##plot line plot to visualize the trends of store performances for each year during Labor Day time
plt.figure(figsize=(16,8))
plt.title('Performance of stores during Labor Day time by Years')
plt.xlabel('Store')
plt.ylabel('Sales')
mnth_09 = sales_data['month'] == 9
sept = sales_data[mnth_09]
seaborn.lineplot(sept.Store, sept.Weekly_Sales, hue = sept.year)
plt.savefig('images/visualize/allLabourDay.png')
plt.close()
