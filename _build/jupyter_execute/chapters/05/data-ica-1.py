#!/usr/bin/env python
# coding: utf-8

# # In Class Activity - Data and Dataframes (Pandas)

# ```{note}
# This exercise authored by [Todd M. Gureckis](http://gureckislab.org/~gureckis) is released under the [license](/LICENSE.html).  *Based on a notebook written by Jin Cheong & Luke Chang*
# ```

# In this lab we are going to learn how to load and manipulate datasets in a dataframe format using Pandas and create beautiful plots using Matplotlib and Seaborn. Pandas is akin to a data frame in R and provides an intuitive way to interact with data in a 2D data frame. Matplotlib is a standard plotting library that is similar in functionality to Matlab's object oriented plotting. Seaborn is also a plotting library built on the Matplotlib framework which carries useful pre-configured plotting schemes. 
# 
# After the tutorial you will have the chance to apply the methods to a new set of data. 
# 
# Also, [here is a great set of notebooks](https://github.com/jakevdp/PythonDataScienceHandbook) that also covers the topic.  In addition, here is a brief [video](https://neurohackademy.org/course/complex-data-structures/) providing a useful introduction to pandas. 
# 
# First, we load the basic packages we will be using in this tutorial.  Notice how we import the modules using an abbreviated name.  This is to reduce the amount of text we type when we use the functions.
# 
# **Note**: `%matplotlib inline` is an example of 'cell magic' and enables plotting *within* the notebook and not opening a separate window. In addition, you may want to try using `%matplotlib notebook`, which will allow more interactive plotting.

# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# The first part of this exercise you just have to go through each cell and execute it.  However, read the surrounding explanation and thing about what each line of the code is doing.  This is a great way to learn.  You can ask your group members if you don't understand anything and also feel free to change the code slightly to experiment with what happens if you repeat an analysis on a different column, etc...

# ## Pandas
# 
# ### Loading Data
# We use the pd.read_csv() to load a .csv file into a dataframe. 
# Note that read_csv() has many options that can be used to make sure you load the data correctly. 

# Pandas has many ways to read data different data formats into a dataframe.  Here we will use the `pd.read_csv` function.

# In[ ]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv', sep = ',', header='infer')


# You can always use the `?` to access the docstring for a function for more information about the inputs and general useage guidelines.

# In[ ]:


get_ipython().run_line_magic('pinfo', 'pd.read_csv')


# ### Ways to check the dataframe
# There are many ways to examine your dataframe. One easy way is to execute the dataframe itself. 

# In[ ]:


df


# However, often the dataframes can be large and we may be only interested in seeing the first few rows.  `df.head()` is useful for this purpose.  `shape` is another useful method for getting the dimensions of the matrix.  We will print the number of rows and columns in this data set by using output formatting.  Use the `%` sign to indicate the type of data (e.g., `%i`=integer, `%d`=float, `%s`=string), then use the `%` followed by a tuple of the values you would like to insert into the text.  See [here](https://pyformat.info/) for more info about formatting text.

# In[ ]:


print('There are %i rows and %i columns in this data set' % df.shape) 


# In[ ]:


df.head()


# On the top row, you have column names, that can be called like a dictionary (a dataframe can be essentially thought of as a dictionary with column names as the keys). The left most column (0,1,2,3,4...) is called the index of the dataframe. The default index is sequential integers, but it can be set to anything as long as each row is unique (e.g., subject IDs)

# In[ ]:


print("Indexes")
print(df.index)
print("Columns")
print(df.columns)
print("Columns are like keys of a dictionary")
print(df.keys())


# You can access the values of a column by calling it directly. Double bracket returns a dataframe
# 

# In[ ]:


df[['salary']]


# Single bracket returns a Series

# In[ ]:


df['salary']


# You can also call a column like an attribute if the column name is a string 
# 

# In[ ]:


df.salary


# You can create new columns to fit your needs. 
# For instance you can set initialize a new column with zeros. 

# In[ ]:


df['pubperyear'] = 0


# Here we can create a new column pubperyear, which is the ratio of the number of papers published per year

# In[ ]:


df['pubperyear'] = df['publications']/df['years']


# In[ ]:


df.head()


# ### Indexing and slicing
# Indexing in Pandas can be tricky. There are four ways to index: loc, iloc, and explicit indexing(useful for booleans).  
# 
# 
# First, we will try using `.loc`.  This method references the explicit index. it works for both index names and also column names.

# In[ ]:


df.loc[0, ['salary']]


# Next we wil try `.iloc`.  This method references the implicit python index (starting from 0, exclusive of last number).  You can think of this like row by column indexing using integers.

# In[ ]:


df.iloc[0:3, 0:3]


# Let's make a new data frame with just Males and another for just Females. Notice, how we added the `.reset_index(drop=True)` method?   This is because assigning a new dataframe based on indexing another dataframe will retain the *original* index.  We need to explicitly tell pandas to reset the index if we want it to start from zero.

# In[ ]:


male_df = df.query('gender == 0').reset_index(drop=True)
female_df = df.query('gender == 1').reset_index(drop=True)


# 
# Boolean or logical indexing is useful if you need to sort the data based on some True or False value.  
# 
# For instance, who are the people with salaries greater than 90K but lower than 100K ?

# In[ ]:


df.query('salary > 90000 & df.salary < 100000')


# ### Dealing with missing values
# It is easy to quickly count the number of missing values for each column in the dataset using the `isnull()` method.  One thing that is  nice about Python is that you can chain commands, which means that the output of one method can be the input into the next method.  This allows us to write intuitive and concise code.  Notice how we take the `sum()` of all of the null cases.
# 
# The `isnull()` method will return a dataframe with True/False values on whether a datapoint is null or not a number (nan).

# In[ ]:


df.isnull()


# We can chain the `.null()` and `.sum()` methods to see how many null values are added up.
# 

# In[ ]:


df.isnull().sum()


# You can use the boolean indexing once again to see the datapoints that have missing values. We chained the method `.any()` which will check if there are any True values for a given axis.  Axis=0 indicates rows, while Axis=1 indicates columns.  So here we are creating a boolean index for row where *any* column has a missing value.

# In[ ]:


df[df.isnull().any(axis=1)]


# You may look at where the values are not null. Note that indexes 18, and 24 are missing. 

# In[ ]:


df[~df.isnull().any(axis=1)]


# There are different techniques for dealing with missing data.  An easy one is to simply remove rows that have any missing values using the `dropna()` method.

# In[ ]:


df = df.dropna()


# Now we can check to make sure the missing rows are removed.  Let's also check the new dimensions of the dataframe.

# In[ ]:


print('There are %i rows and %i columns in this data set' % df.shape)
df.isnull().sum()


# ### Describing the data
# We can use the `.describe()` method to get a quick summary of the continuous values of the data frame. We will `.transpose()` the output to make it slightly easier to read. 

# In[ ]:


df.describe().transpose()


# We can also get quick summary of a pandas series, or specific column of a pandas dataframe.

# In[ ]:


df.departm.describe()


# ### Manipulating data in Groups
# One manipulation we often do is look at variables in groups. 
# One way to do this is to usethe `.groupby(key)` method. 
# The key is a column that is used to group the variables together. 
# For instance, if we want to group the data by gender and get group means, we perform the following.

# In[ ]:


df.groupby('gender').mean()


# Other default aggregation methods include .count(), .mean(), .median(), .min(), .max(), .std(), .var(), and .sum()
# 
# Before we move on, it looks like there were more than 2 genders specified in our data. 
# This is likely an error in the data collection process so let recap on how we might remove this datapoint. 

# In[ ]:


df.query('gender==1')


# replace original dataframe without the miscoded data
# 

# In[ ]:


df = df.query('gender!=2')


# Now we have a corrected dataframe!
# 

# In[ ]:


df.groupby('gender').mean()


# Another powerful tool in Pandas is the split-apply-combine method. 
# For instance, let's say we also want to look at how much each professor is earning in respect to the department. 
# Let's say we want to subtract the departmental mean from professor and divide it by the departmental standard deviation. 
# We can do this by using the `groupby(key)` method chained with the `.transform(function)` method. 
# It will group the dataframe by the key column, perform the "function" transformation of the data and return data in same format.
# To learn more, see link [here](http://nbviewer.jupyter.org/github/jakevdp/PythonDataScienceHandbook/blob/master/notebooks/03.08-Aggregation-and-Grouping.ipynb)

# In[ ]:


# key: We use the departm as the grouping factor. 
key = df['departm']

# Let's create an anonmyous function for calculating zscores using lambda:
# We want to standardize salary for each department.
zscore = lambda x: (x - x.mean()) / x.std()

# Now let's calculate zscores separately within each department
transformed = df.groupby(key).transform(zscore)
df['salary_in_departm'] = transformed['salary']


# Now we have `salary_in_departm` column showing standardized salary per department.
# 

# In[ ]:


df.head()


# ### Combining datasets - pd.concat
# Recall that we sliced the dataframes into male and female dataframe in 2.3 Indexing and Slicing. Now we will learn how to put dataframes together which is done by the pd.concat method. Note how the index of this output retains the old index.

# In[ ]:


pd.concat([femaledf, maledf],axis = 0)


# We can reset the index to start at zero using the .reset_index() method

# In[ ]:


pd.concat([maledf, femaledf], axis = 0).reset_index(drop=True)

