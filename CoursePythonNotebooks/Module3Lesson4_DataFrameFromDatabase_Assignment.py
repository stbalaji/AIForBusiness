#!/usr/bin/env python
# coding: utf-8
# ![](NotebookHeader.jpg)
# Course                  : Python for Data Science
# Module 3 Lesson 4  : Hands On Exercise/Assignment :  DataFrame using Datafile (CSV)

# In this practice exercise you need to work on the examples applying the various DataFrame concepts learned. This practice will familiarize you with working on DataFrame using a data from a file. 
import pandas  as pd
import numpy as np

#> Q1 : Create a dataframe  using the Input Data File.
import os
os.getcwd() # Print Current working directory to be sure of path
df = pd.read_csv("data/StatePerformance.csv", header=None)

#> Q2 :  Assign the column names using Columns from the Metadata File.
df_header = pd.read_csv("data/StatePerformance_metadata.csv")
df_header
df.columns = df_header.columns
df.columns

#> Q3 :  Assign proper Datatype to the columns.
df.dtypes           # Review the column data types as part of the dataframe creation
df['math score'] = df['math score'].astype(float)
df['science score'] = df['science score'].astype(float)
df['english score'] = df['english score'].astype(float)
df.dtypes


#> Q4 Retrieve first five columns.
df.iloc[:,0:4]

#> Q5   Perform following Calculations :

# - Calculate Average (or Mean) Math Score.
df['math score'].mean()

# - Calculate Average (or Mean) Math Score by States.
df_grouped = df.groupby('state').mean()
df_grouped['math score']

# - Calculate Minimum Science Score and print name of the corresponding state 
minscore = df['science score'].min()
cond = df['science score'] == minscore
df[cond]
df.loc[cond,['state','science score']]

#> Q6 Retrieve the following datasets / values::
# - List of states where the science score is greater than average or mean.
avgscore = df['science score'].mean()
avgscore

cond = df_grouped['science score'] > avgscore
df_grouped[cond]['']

# > Print names of top three best performing states -Performance defined as best scores across subjects
# Method 1 : One method is to look at sorted values.
df_grouped
df_sorted = df_grouped.sort_values("science score", ascending = False)
df_sorted                

# Method 2 : Can create a total's column and use
df_sorted['Total'] = df_sorted['math score'] +  df_sorted['science score'] + df_sorted['english score']
df_sorted['Total']