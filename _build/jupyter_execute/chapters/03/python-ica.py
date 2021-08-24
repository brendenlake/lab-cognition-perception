#!/usr/bin/env python
# coding: utf-8

# # In Class Activity - Python

# In this notebook we will try to put some of the Python knowledge you acquired into use.  For each exercise, you will see some code that has some bugs or asks you to write a little program.  Simply fix the code cell to make code that runs correctly, or write the code to specification.  Then add a markdown cell below your answer that says what you changed and why, or explains what your code is doing in English.

# ## Importing and using existing functions

# ### Problem 0: Random number generation

# The following code imports the random number functionality in Python from the `numpy` library and uses to do generate random numbers.  Why won't this code run?

# In[2]:


import numpy.random as npr

print("My random number is ", numpy.random.random())


# ### Problem 1: Random sample

# The next line chooses a random sample of 5 elements from a list.  What is wrong here?

# In[15]:


import numpy.random as npr
my_list = list(range(100)
               
npr.choice(my_list,size=10,replace=False)


# ### Problem 2: Looking things up

# In the above example when you get it to work what does the `choice()` function do?  The documentation for this function is available by googling for "numpy.random choice".  Add your answer in a cell below.  Then look up the `random()` function used in Problem 0.  What does it do?

# ## Writing a function

# In the problem that remain you will need to write little function that accomplish various goals.  Let's verify your understanding of functions.

# ### Problem 3: Defining a function

# What does this function do?  Write a new cell below the function definition that calls the function using five different inputs and verify the outputs match your expectation.

# In[9]:


def my_function(x, y):
    return x+y


# ### Problem 4: What is not great about this function?

# This function works but is not ideal, why?

# In[ ]:


def my_function_2(x, y, z):
    return x+y


# ### Problem 5: Write you own function

# Write your own custom function named `catchy_name()` to write a program that takes as input two arguments which are assumed to be strings.  Return a new string which is the concatenations of the first two letters of each of the inputs.  e.g. 
# ```
# catchy_name("South","Houston") -> "SoHo"
# catchy_name("Jennifer", "Lopez") -> "JeLo"
# ```

# ## Strings

# ### Problem 6: Cat-Dog

# Write a function called `catdog` that returns True if a input string given has the word cat and dog an equal number of times.  For example, 
# ```
# cat_dog('catdog') # shoudl return True
# cat_dog('catcat') # should return false
# cat_dog('1cat1cadodog') # should return true
# ```

# Google 'python count occurrences in string' to find a existing function of method that counts the number of times a substring appears in a string to get started.

# ## Lists

# ### Problem 7: Summing

# Write a function call `summing()` that takes a list of numbers as input and return the sum of all the numbers.  Use a for loop to do this.
# 
# ```
# summing([1, 2, 3]) → 6
# summing([5, 11, 2]) → 18
# summming([7, 0, 0]) → 7
# ```

# ### Problem 8: Biggest difference

# 
# Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
# 
# ```
# big_diff([10, 3, 5, 6]) → 7
# big_diff([7, 2, 10, 9]) → 8
# big_diff([2, 10, 7, 2]) → 8
# ```
