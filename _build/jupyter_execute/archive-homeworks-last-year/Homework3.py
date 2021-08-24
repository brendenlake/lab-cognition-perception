#!/usr/bin/env python
# coding: utf-8

# # Exploring Data
# 
# *Written by Todd Gureckis*
# 
# So far in this course we've learned a bit about using Jupyter, some Python basics, and have been introduced to Pandas dataframes and at least a start at some of the ways to plot data.
# 
# In this lab, we are going to pull those skills into practice to try to "explore" a data set.  At this point we are not really going to be doing much in terms of inferential statistics.  Our goals are just to be able to formulate a question and then try to take the steps necessary to compute descriptive statistics and plots that might give us a sense of the answer.  You might call it "Answering Questions with Data."

# First, we load the basic packages we will be using in this tutorial.  Remeber how we import the modules using an abbreviated name (`import XC as YY`).  This is to reduce the amount of text we type when we use the functions.
# 
# **Note**: `%matplotlib inline` is an example of something specific to Jupyter call 'cell magic' and enables plotting *within* the notebook and not opening a separate window.

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import io
from datetime import datetime
import random


# ## Reminders of basic pandas functions

# As a reminder of some of the pandas basics lets revisit the data set of professor salaries we have considered over the last few lectuers.

# In[5]:


salary_data = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv', sep = ',', header='infer')


# Notice that the name of the dataframe is now called `salary_data` instead of `df`.  It could have been called anything as it is just our variable to work with.  However, you'll want to be careful with your nameing when copying commands and stuff from the past.

# ### peek at the data

# In[6]:


salary_data.head()


# ### Get the size of the dataframe

# In rows, columns format

# In[7]:


salary_data.shape


# ### Access a single column

# In[8]:


salary_data[['salary']]


# ### Compute some descriptive statistics

# In[9]:


salary_data[['salary']].describe()


# In[25]:


salary_data[['salary']].count()  # how many rows are there?


# ### creating new column based on the values of others

# In[10]:


salary_data['pubperyear'] = 0
salary_data['pubperyear'] = salary_data['publications']/salary_data['years']


# ### Selecting only certain rows

# In[11]:


sub_df=salary_data.query('salary > 90000 & salary < 100000')


# In[12]:


sub_df


# In[13]:


sub_df.describe()


# ## Get the unique values of a columns

# In[14]:


salary_data['departm'].unique()


# How many unique department values are there?

# In[15]:


salary_data['departm'].unique().size


# or

# In[16]:


len(salary_data['departm'].unique())


# ### Breaking the data into subgroups

# In[17]:


male_df = salary_data.query('gender == 0').reset_index(drop=True)
female_df = salary_data.query('gender == 1').reset_index(drop=True)


# ### Recombining subgroups

# In[18]:


pd.concat([female_df, male_df],axis = 0).reset_index(drop=True)


# ### Scatter plot two columns

# In[20]:


ax = sns.regplot(x=salary_data.age, y=salary_data.salary)
ax.set_title('Salary and age')


# ### Histogram of a column

# In[21]:


sns.displot(salary_data['salary'])


# You can also combine two different histograms on the same plot to compared them more easily.

# In[24]:


fig,(ax1,ax2) = plt.subplots(ncols=2,figsize=(10,3),sharey=True,sharex=True)
sns.histplot(male_df["salary"], ax=ax1,
             bins=range(male_df["salary"].min(),male_df["salary"].max(), 5000),
             kde=False,
             color="b")
ax1.set_title("Salary distribution for males")
sns.histplot(female_df["salary"], ax=ax2,
             bins=range(female_df["salary"].min(),female_df["salary"].max(), 5000),
             kde=False,
             color="r")
ax2.set_title("Salary distribution for females")
ax1.set_ylabel("Number of users in age group")
for ax in (ax1,ax2):
    sns.despine(ax=ax)
fig.tight_layout()


# ### Group the salary column using the department name and compute the mean

# In[37]:


salary_data.groupby('departm')['salary'].mean()


# ### Group the age column using the department name and compute the modal age of the faculty

# First let's check the age of everyone.

# In[44]:


salary_data.age.unique()


# Ok, there are a few people who don't have an age so we'll need to drop them using `.dropna()` before computing the mode.

# Since there doesn't seem to me a mode function provided by default we can write our own custom function and use it as a descriptive statistics using the `.apply()` command.  Here is an example of how that works.

# In[29]:


def my_mode(my_array):
    counts = np.bincount(my_array)
    mode = np.argmax(counts)
    return mode, counts[mode]

# wee need to drop the 
salary_data.dropna().groupby('departm')['age'].apply(my_mode)


# ### OkCupid Data

# This document is an analysis of a public dataset of almost 60000 online dating profiles.
# The dataset has been [published](http://ww2.amstat.org/publications/jse/v23n2/kim.pdf) in the [Journal of Statistics Education](http://ww2.amstat.org/publications/jse/), Volume 23, Number 2 (2015) by Albert Y. Kim et al., and its collection and distribution was explicitly allowed by OkCupid president and co-founder [Christian Rudder](http://blog.okcupid.com/).  Using these data is therefore ethically and legally acceptable; this is in contrast to another recent release of a [different OkCupid profile dataset](http://www.vox.com/2016/5/12/11666116/70000-okcupid-users-data-release), which was collected without permission and without anonymizing the data (more on the ethical issues in [this Wired article](https://www.wired.com/2016/05/okcupid-study-reveals-perils-big-data-science/)).
# 

# In[17]:


profile_data = pd.read_csv('https://github.com/rudeboybert/JSE_OkCupid/blob/master/profiles.csv.zip?raw=true', compression='zip')


# <div class="alert alert-info" role="alert">
#   <strong>Question 1</strong> <br>
#     Plot a historam of the distribution of ages for both men and women on OkCupid.  Provide a brief (1-2 sentence summary of what you see).
# </div>

# <div class="alert alert-warning" role="alert">
#   <strong>Your Answer</strong> <br>
#   Delete this text and put your answer here.  The code for your analysis should appear in the cells below.
# </div>

# <div class="alert alert-info" role="alert">
#   <strong>Question 2</strong> <br>
#     Find the mean, median and modal age for men and women in this dataset.
# </div>

# <div class="alert alert-warning" role="alert">
#   <strong>Your Answer</strong> <br>
#   Delete this text and put your answer here.  The code for your analysis should appear in the cells below.
# </div>

# <div class="alert alert-info" role="alert">
#   <strong>Question 3</strong> <br>
#     Plot a histogram of the height of women and men in this dataset.
# </div>

# <div class="alert alert-warning" role="alert">
#   <strong>Your Answer</strong> <br>
#   Delete this text and put your answer here.  The code for your analysis should appear in the cells below.
# </div>

# <div class="alert alert-info" role="alert">
#   <strong>Question 4</strong> <br>
#     Propose a new type of analysis you'd like to see.  Work with instructor or TA to try to accomplish it.  Be reasonable!
# </div>

# ### Citibike Data
# 
# As you know, Citibikes are the bike share system in NYC.  What you might not realize is that a lot of the data about citibikes is made public by the city.  As a result it is a fun dataset to download and to explore.  Although this dataset is not exactly "cognition and perception" it is readily available and is a great way to train up your exploratory data analysis skills!

# #### Loading Data
# 
# The data for the citibike are provided on a per-month basis as a .zip file.  As a result we first have to download the file and unzip it.  Luckily python can do that for you!
# 
# Remember, we use the pd.read_csv() to load a .csv file into a Pandas dataframe.  In this case our citibike data frame will be called `trip_data`.  Be sure to read the code and try to get a sense of what it is doing.  Ask questions if you are unsure.
# 

# In[7]:


trip_data = pd.read_csv('https://s3.amazonaws.com/tripdata/201603-citibike-tripdata.zip', compression='zip')


# This command loads the data from March, 2016 (The data is called 201603-citibike-tripdata.csv).  Can you guess how we know the date of the data?  Also note that we added a special option to the `read_csv()` to deal with the fact that the datafile we are loading is kind of big and so is a .zip file.

# <div class="alert alert-info" role="alert">
#   <strong>Question 1</strong> <br>
#     Take a look at the data in the dataframe `trip_data` using the tools we have discussed for peaking inside data frames.  What are the columns?  Using a Markdown list describe what you think each one probably means and what the values within in column mean?  You may not know for sure so you might have to make a guess (this is common when you get data from another source... you have to go on hunches and reasonable guesses).  For example what do you think the `usertype` column means and what are the different values in the data?
# </div>

# <div class="alert alert-warning" role="alert">
#   <strong>Your Answer</strong> <br>
#   Delete this text and put your answer here.
# </div>

# <div class="alert alert-info" role="alert">
#   <strong>Question 2</strong> <br>
#     The data set contains information on individual trips but we might be more interested in the number of trips per bike (to find how often each bike is used ).  Try using the groupby command from pandas to compute the number of trips per bike (`bikeid`) in the dataset.  Plot a histogram of this data.  What did you expect this distribution to look like.  Is it a normal/gaussian distribution?  Why do you think it has this particular shape?
# </div>

# <div class="alert alert-warning" role="alert">
#   <strong>Your Answer</strong> <br>
#   Delete this text and put your answer and code below.
# </div>
