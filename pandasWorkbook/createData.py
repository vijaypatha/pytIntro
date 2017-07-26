#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 22 20:12:48 2017

@author: vijaypatha
The pandas library is used for all the data analysis excluding 
a small piece of the data presentation section. 

The matplotlib library will only be needed for the data presentation section. 
Importing the libraries is the first step we will take in the lesson.
"""
from pandas import DataFrame, read_csv
import matplotlib.pyplot as plt
import pandas as pd #this is how I usually import pandas
import sys #only needed to determine Python version number
import matplotlib #only needed to determine Matplotlib version number


print('Python version ' + sys.version)
print('Pandas version ' + pd.__version__)
print('Matplotlib version ' + matplotlib.__version__)

#CREATE DATA
# The inital set of baby names and bith rates
names = ['Bob','Jessica','Mary','John','Mel','heidi']
births = [968, 155, 77, 578, 973,1000]
BabyDataset = list(zip(names,births))
print BabyDataset

#To MERGE these TWO lists together we will use the ZIP function.

"""We are basically done creating the data set. 
We now will use the pandas library to export this data set into a csv file.

df will be a DataFrame object. 
You can think of this object holding the contents of the BabyDataSet 
in a format similar to a sql table or an excel spreadsheet. 
Lets take a look below at the contents inside df."""
#ARRANGE THE DATA
df = pd.DataFrame(data = BabyDataset, columns = ["Names","Births"]) 
print df
df.to_csv('births1880.csv',index=False,header=False)

"""Location = r'/Users/vijaypatha/Python/pandasWorkbook/births1880.csv'
df = pd.read_csv(Location)"""

#ANALYZE DATA
Sorted = df.sort_values(['Births'], ascending=False)
Sorted.head(1)
df['Births'].max()
