#!/usr/bin/env python
# coding: utf-8

# # In Class Activity - Sampling

# ```{note}
# This exercise authored by [Todd M. Gureckis](http://gureckislab.org/~gureckis) is released under the [license](/LICENSE.html).
# ```

# In the chapter and lecture we discussed some basic issues in sampling.  In this notebook you will explore some handy python methods for sampling and consider the implications of sampling on what you understand about some target group (i.e., what you can generalize).

# ## Importing and using existing functions

# In[23]:


import numpy as np
import numpy.random as npr
import pandas as pd
import seaborn as sns


# ## Problem 0: Seeding a random number generator

# When we use the computer to play with random numbers (or random samples), we aren't actually using random numbers.  Generally speaking your computer is a deterministic machine so it is unable to make truely random numbers.  Intead the numbers your computer gives you are known as pseudo-random because they have many of the properties we want from random numbers but are not exactly and entirely random.
# 
# Anytime we use random numbers in a script, simulation, or analysis it is important to "seed" the random number generator.  This initialized the random number generator function to a particularly "state" and this makes the number in the script random but repeatable.  
# 
# Let's experiment with this.  First try running the following cell and seeing what the output is.  Try running it multiple times and seeing how the numbers change.

# In[20]:


npr.randint(0,10,10)


# Now run this cell:

# In[21]:


npr.seed(10)
print(npr.randint(0,10,10))
print(npr.randint(0,10,10))


# Again, try repeating the cell execution over and over.  What do you observe?
# 
# Try restarting the kernel and run the cell again.  What do you notice?  Compare to other people in your group.  Also change the argument to `npr.seed()` and see what happens.

# #### Answer 0 here:

# In[ ]:


## Enter solution here


# Bottom line:  Always seed the random number generator at the start of any script that uses random numbers so your code is more repeatable.

# ## Problem 1: Sampling from a finite population
# 
# Imagine I create a list with 100 randomly determined values as below.  Using the web, research the the numpy random `choice()` function.  Use it generate a random sample of size 10 from this data.  Do it twice one with replacement and once without replacement.

# In[12]:


my_data = np.array([75, 25, 59, 63, 48, 29,  3, 17, 68, 39,  9, 62, 61, 52, 64, 45, 90,
       87,  0, 42, 26, 52, 22, 25, 20, 22, 81, 25, 48, 79, 37,  6, 33, 30,
       81,  5, 37, 85, 65,  0, 27, 40, 96, 67, 77, 29, 32, 25,  4, 53, 46,
        7, 51, 65, 46, 91, 60, 52, 93, 26,  2, 42, 18, 19, 97, 45, 78, 33,
       25, 30, 97, 96, 99, 32, 86, 43, 81, 83, 51, 81, 36, 29,  2, 33, 95,
       39, 79,  1, 80, 17, 50, 38,  1, 98, 30, 89, 93, 27, 43, 30])


# #### Answer 1 here:

# In[ ]:


## Enter solution here


# ## Problem 2: Sampling from a data frame

# Sometimes what we are interested in is sampling from a pandas dataframe rather than a list or numpy array.  Why might we want to sample from a dataset?  One is to randomly select subset of test-training if we are doing machine learning projects on the data (we'll talk about this later).  Another is if there are two many records to analyze so it makes sense to randomly select a subset and analyze those.  Another is to repeatedly sample over and over again from a dataset to do a statistical method called "boostrapping" (https://en.wikipedia.org/wiki/Bootstrapping_(statistics))

# This code loads an example pandas dataset of different penguins.  

# In[25]:


penguins_df = sns.load_dataset('penguins')


# In[26]:


penguins_df.head()


# In[27]:


penguins_df.info()


# Research the pandas `sample()` method and randomly sample 20 penguins from the dataframe.

# #### Answer 2a here:

# In[ ]:


## Enter solution here


# Now, for part b of this question, in a for loop, 100 times create a random sample of the dataframe and compute the mean body mass of the penguins in your sample.  Append all these values to a list and then plot a histogram of these values.  Compare it to the mean of the dataset containing all the penguins.

# #### Answer 2b here:

# In[ ]:


## Enter solution here


# ## Problem 3: Stratified sampling

# One problem with the simple random samples we made of the penguins is that in each sample we might exclude some important groups of the data.  For example, if we only sampled 10 penguins perhaps all of them are male.  If we wanted to be more even handed name make sure our samples were _representative_ of the sex differences then we might want to sample from the subpopulations.  This is called "stratified sampling".
# 
# Please read this example webpage: https://www.statology.org/stratified-sampling-pandas/
# on stratified sampling and adapt the code to generate a random sample of 10 penguins that is stratified so that there are 5 male and 5 female examples in the sample

# #### Problem 3: Answer here

# In[37]:


## Enter solution here


# In[ ]:




