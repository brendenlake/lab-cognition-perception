#!/usr/bin/env python
# coding: utf-8

# # Homework 2 - Python for data analysis

# ```{note}
# *by [Todd M. Gureckis](http://gureckislab.org/~gureckis)*  code shared under the [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) license.  Credit given where inspiration was obtained from others!
# ```

# <div class="alert alert-danger" role="alert">
#   Check the class schedule for information about homework due dates. 
# </div>

# <img src="http://imgs.xkcd.com/comics/python.png" width="400">
# 
# The goal of Homework 2 is to make sure you understand enough python for the types of data analysis that we will be doing the rest of the semester.  At this point you should be pretty comfortable with the Jupyter notebook environment.  If you need a refresher on python there are a number of excellent resources you can explore on your own:
# 
# - Google for Education's [Beginner Python course](https://developers.google.com/edu/python/).  Jump to section "Python Intro"
# - Corey Schafer's [Python Programming Beginner Tutorials](https://www.youtube.com/playlist?list=PL-osiE80TeTskrapNbzXhwoFUiLCjGgY7) on Youtube.  These are great if you prefer to watch videos.  Also can skip the first video on installing python because you are using Jupyter and there is nothing to install!
# 
# In the homework I will give you some data, give examples of how to use a key programming construct in the analysis of this data, and then give you a chance to try to perform an analysis using what you have learned.

# ---

# ## Importing libraries

# As you have seen a few times now, before we start we often need to import some additional python libraries.  This is one of the key features of python because there are really amazing libraries that will let you do almost anything!  Also when you get a bit more advanced you can write your own libraries.  
# 
# There are several common ways of importing. Let's say we want to import a package `foo` that defines a function `widget`:
# 
# * `import foo` will import the `foo` package; any reference to modules/classes/functions will need to be prefixed with `foo.`; e.g. `foo.widget()`
# * `import foo as bar` will import the `foo` package with the alias `bar`; any reference to modules/classes/functions will need to be prefixed with `bar.`; e.g. `bar.widget()` This is the preferred method especially when the name of the package is long.
# * `from foo import widget` can be used to import a specific module/class/function from `foo` and it will be available as `widget()`
# * `from foo import *` will import every item in `foo` into the current namespace; this is bad practice, don't do it.
# 
# As you have seen from past notebooks we often want to import `pandas`, `numpy`, and `seaborn`:

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# <div class="alert alert-success" role="alert">
#   <strong>Problem 1 (2 points)</strong> <br>
#   Ooops I forgot to import our favorite plotting library `seaborn`.  Import it below with the shorthand name `sns` and run the code so that this library is available to you later!
# </div>

# In[ ]:


# put your code here


# There are many great libraries for python.  How do you learn about them?  Check out [pypi.org](https://pypi.org) which lets you search for different libraries.  Of course not all the libraries are installed on our class JupyterHub but all of the [standard ones are](https://docs.python.org/3/library/).  One example of a standard library is the `math` library.  This library implements a bunch of simple math functions ([full list](https://docs.python.org/3/library/math.html)).  For example, `math.sqrt(x)` will take the square root of `x`.  Try to execute the folowing cell:

# In[ ]:


math.sqrt(2)


# <div class="alert alert-warning" role="alert">
#   <strong>Oops!</strong><br> 
#     Did this not work?  Don't worry that is expected!
# </div>

# <div class="alert alert-success" role="alert">
#   <strong>Problem 2 (2 points)</strong> <br>
#   What is wrong with the previous cell?  Why did it not run?  Write the code necessary so it works.  You can copy the command again below.  Keep in mind the advice above about libraries!
# </div>

# In[ ]:


# put your code here


# ## Getting Data, Dealing with Lists and Dictionaries

# As we explored in the labs so far, the most common way to read in data for analysis is from a CSV (comma separate values) file.  This is like a simple version of an excel spreadsheet.  Indeed you can export files from Excel as a CSV and also from Google Sheets.
# 
# ```
# df = pd.read_csv("http://myurl.edu/mydata.csv")
# ```
# 
# However there are many ways to get data into Python.  For example, another approach is to use what is known as a data API (or application programming interfaces).  Very simply APIs are ways of getting access to data using code.  Many websites including Twitter, Yelp, Strava, etc.. provide APIs that let you access and process at least parts of the data on their websites.  Often companies release python libraries to make this easier.
# 
# In the rest of the homework we are going to explore one example of this using the [Petfinder.com](https://petfinder.com) website.  Petfinder is a website that helps people locate pets for adoption.  It maintains a searchable database of pets from many different shelters and makes the data on the pets searchable.  There is also a cool python library call `petpy` which help you to interact with the Petfinder website.
# 
# To get started let's import the `petpy` library.  Here I am not using the `import X as Y` syntax because petpy is pretty easy to type.  I am also importing a few other libraries for displaying images in the Jupyter notebook and downloading files over the internet.

# In[5]:


import petpy
from IPython.display import Image
import requests


# To access Petfinder you have to signup on their website.  I have already done this for you so you can use my creditials for class (provided on the class Piazza):

# <div class="alert alert-danger" role="alert">
#   <strong>Warning!</strong><br> 
#     The following code (and the rest of this homework) will not work unless you get the API keys from the class message board (e.g., piazza or edstem) and paste it into your notebook.  Check the website or ask the instructor before continuing!
# </div>

# In[6]:


MYKEY = 'ski1ECR0y8TeW1aiVxOy7fR36ERlAn6GrrX1E9tNllr2B4HRuH'
MYSECRET = 'mEL8xgY4MN1EggFCDqoMFUzASvLk8w1cSKD5h3eq'
pf = petpy.Petfinder(key=MYKEY, secret=MYSECRET)


# The variable `pf` now contains an API interface to the Petfinder website.

# In[7]:


animal_types = pf.animal_types()


# The new variable we created must contain something but honestly I have no idea what it is right at first.  So I will put it in a cell by itself so I can see what it contains.

# In[ ]:


animal_types


# A cool, ok so `animal_types` looks like a [python dictionary](https://www.w3schools.com/python/python_dictionaries.asp) which you learned about in a prior lab session.  How do I know this? Well I notice that the entire output of the cell above is wrapped in `{ }` which is how you denote a dictionary in python.  For example:

# In[ ]:


my_dictionary = {"pasta": "a type of italian food", "pizza": "another type of italian food"}


# In the cell above, I just created a new variable called `my_dictionary` which has two *keys* ('pasta' and 'pizza') and two corresponding values/descriptions.  I can lookup the description of each of the key like this

# In[ ]:


print(my_dictionary['pasta'])


# In[ ]:


print(my_dictionary['pizza'])


# In[ ]:


print(my_dictionary['salad'])


# Oops, that was expected..  'salad' wasn't defined in our original dictionary so it can't be looked up (we got an exception called 'KeyError' because the key 'salad' could not be found in the dictionary.
# 
# The idea with dictionaries is that you can store stuff and easily look it up by name.
# 
# Getting back to these pets!  What are the keys of this dictionary?

# In[ ]:


animal_types.keys()


# Ok so there is one key, `types`.  This must just mean that the API wraps everything up so lets look inside that key.  

# In[ ]:


animal_types['types']


# Ok this is weird but this contains a [python list]().  How do I know that?  Because it is wrapped in `[ ]`.  How many things are in the list?

# In[ ]:


len(animal_types['types'])


# ok, what is in the first slot or position of the list?

# In[ ]:


animal_types['types'][3]


# Ah! Another dictionary (indicated by the `{ }`).  But now I can kind of understand what is going on.  What are the keys of this dictionary?

# In[ ]:


animal_types['types'][0].keys()


# Ok, so the keys are things that are describing a type of pet!  We have a field called `name` and one called `coats` which sounds fascinating, and `colors` and `genders`.  Cool!
# 
# So what is the first type of animal in this list?

# In[ ]:


animal_types['types'][0]['name']


# Ok, so it is good-boy pups.  What are the possible colors?

# In[ ]:


animal_types['types'][0]['colors']


# Really cool stuff.  I think a Merle color dog might really suit me!  Although I don't know that that is actually.  Let me consult wikipedia really quick!

# In[ ]:


import wikipedia
wikipedia.summary("Merle (dog coat)")


# Isn't python so cool?  You can grab wikipedia entiries with one line just by typing `import wikipedia`.  Now you might start understanding the cartoon at the beginning of the homework!

# Ok, so let's challenge our understanding of working with lists and dictionaries.  What are the possible colors for cats according to the petfinder website?

# In[ ]:


# Try to access the different colors of cats here


# Did you get stuck?  Give it your best shot but if you really get fustrated you can run the cell below to reveal my solution.

# In[ ]:


# Uncomment and run next line for a sample solution
# %load hw2-hint1.py


# <div class="alert alert-success" role="alert">
#   <strong>Problem 3 (2 points)</strong> <br>
#   What are the colors for the "small and furry" animals (mice, gerbils, etc...)?
# </div>

# In[ ]:


# put your code here


# ## For loops and other ways to repeat things

# So far we have kind of been playing with dictionaries and list by accessing individual elements.  However sometimes we want to know more general stuff like what is the name of all the types of animals?  To do this we kind of want to use the methods we developed above to look inside this data frame but to repeat this for each element within the structure.  This brings us to the dreaded `for` loop.  Many students are afraid of for loops because they can get a bit complex.  However, they are also a super critial tool for working with data effectively and open up so many more interesting types of analyses to you.

# The most common use for a `for` loop in data analysis is to repeat at step for each record of some data.  For instance you might want to print out the value of each item in a list:

# In[21]:


my_list = ['a','b','c','d']
for item in my_list:
    print(item)


# you can use features of list to reverse the printout.

# In[ ]:


my_list = ['a','b','c','d']
for item in my_list[::-1]:
    print(item)


# or each item in a dictionary:

# In[2]:


weapon_strengths = {
    'tomahawk': 20,
    'katana': 60,
    'hand of god': 100,
}

for weapon in weapon_strengths.keys():
    print(f"I have a {weapon}!")

print("\n---\n")

for weapon, strength in weapon_strengths.items():
    print(f"My {weapon} has a strength of {strength}!")


# This second example shows how you can repeat the printing command for each key in the dictionary `weapon_strengths.keys()` or all the items (like a list): `weapon_strengths.items()`.

# Lets try it out for the animals!  What are the types of animals in the Petfinder system?

# In[8]:


for animal in animal_types['types']:
    print(animal['name'])


# Here I am repeating the same code for each entry in the `animal_types['types']` list.  Each entry in that list is first assigned to the variable `animal` and then I look inside that dictionary and access the `name` key.

# <div class="alert alert-success" role="alert">
#   <strong>Problem 4 (2 points)</strong> <br>
#   Write a for loop that print out the name of each animal category and the coats they have.  Your output should look like this:
# <pre>
# Dog: ['Hairless', 'Short', 'Medium', 'Long', 'Wire', 'Curly']
# Cat: ['Hairless', 'Short', 'Medium', 'Long']
# Rabbit: ['Short', 'Long']
# Small & Furry: ['Hairless', 'Short', 'Long']
# Horse: []
# Bird: []
# Scales, Fins & Other: []
# Barnyard: ['Short', 'Long']
# </pre>
# </div>

# In[1]:


# put your code here


# So far we have been exploring repeating loops for each entry in a dataset that we obtained via an API.  However, sometimes we just want to repeat things a few times in order to do other stuff.  For instance, as you will see you can use python and `for` loops to draw simple pictures!
# 
# In order to use `for` loops in this way we have to *create data*.  One of the easiest ways to create data is the `range()` command which creates a list with a sequence of numbers.

# In[ ]:


list(range(5))


# In[ ]:


list(range(10))


# So if we wanted to repeat the same thing 5 times we could do this:

# In[ ]:


for x in range(5):
    print("hi")


# You can also place `for` loops inside another `for` loop if you tab is over appropriately.  If this happens you can repeat things in more complex ways.  For instance you can print out a square like this:

# In[ ]:


for i in range(10):
    for j in range(10):
        print("*", end = ' ')
    print("")


# <div class="alert alert-success" role="alert">
#   <strong>Problem 5 (4 points)</strong> <br>
#   Modify the code for the square above to write a nested for loop that prints out a triangle with height 5 and width 5.  Your output should look like this:
# <pre>
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# </pre>
# </div>

# In[ ]:


# your code here


# `for` loops are really interesting when combined with `if` statement.  This means while you are repeating the loop you can skip thing or do something different.  

# In[ ]:


for i in range(10):
    for j in range(10):
        if i < 2 or i > 7:
            print("*", end = ' ')
        else:
            print(" ", end = ' ')
    print("")


# For example the code above prints out the stars for each square only if the row (i) is less than 2 or greater than 7 (otherwise it prints a empty space instead due to the `else`).  Think about this one for a bit:

# In[ ]:


for i in range(10):
    for j in range(10):
        if (i < 3 or i > 6) or (j < 3 or j > 6):
            print("*", end = ' ')
        else:
            print(" ", end = ' ')
    print("")


# <div class="alert alert-success" role="alert">
#   <strong>Problem 6 (4 points)</strong> <br>
#   Modify your code for the triangle to write a nested for loop that prints out a diamond with height 7 and width 7.  You'll probably want to combined nested loops with if/else statements.  Your output should look like this:
# <pre>
#       *
#     * * *
#   * * * * *
# * * * * * * *
#   * * * * * 
#     * * *
#       *
# </pre>
# </div>

# In[ ]:


# your code here


# 
# <div class="alert alert-success" role="alert">
#     <strong>BONUS Problem 1 "The Wave"(4 points)</strong> <br>
#     
#   
#     
# Create a list called 'people' which is full of zeros, except the first number is a 1. Then write a simple program that steps through each element of the vector. If the "person" to the left is standing (i.e., is set to 1.0) then have this current person stand up too. If the current person is already standing then have them sit back down. On each pass through print the contents of the people list. Bonus points for making the wave go forwards and backwards (i.e., left to right then back right to left).
#     
# <pre>
# people = [1,0,0,0,0,0,0,0,0,0]
# for each number "i"" in between 0 (the start) and the length of people (minus 1):
#     if person "i" is standing up:
#         make the person one to the right of person "i" stand up
#         make person "i" sit down
#         print people
# <pre>
# also remember,
# <pre>
# len(people)   # gives you the length of the "stadium" of people        
# people[0] # this is how  you select individual "people"
# people[1]
# people[2]
# </pre>
# </div>

#   <img src="https://media.giphy.com/media/Zl0dYeDrDjmms/giphy.gif" width="550">

# Enough of this programming!  As a reward for completing these tough new problems, we'll look at some cute pets using `for` loops.  The petfinder API has a function which will return the set of pets currently available for adoption.  This takes a number of options but by default will return 20 pet listings.

# In[ ]:


animals = pf.animals(return_df=True)


# This returns a pandas dataframe that contains lots of information about the pet including if it is declawed, house trained, etc...

# In[ ]:


animals.columns


# In[ ]:


animals.head()


# In[ ]:


from skimage import io

def show_animal(animals, number, ax):
    record=animals.iloc[number]
    if record.photos:
        if record.photos[0]:
            if 'medium' in record.photos[0]:
                photo = record.photos[0]['medium']
                img=io.imread(photo)
                ax[number].set_axis_off()
                ax[number].imshow(img)
                

fig, axes = plt.subplots(4, 5, figsize=(12, 12))
ax = axes.ravel()

for i in range(20):  # check out my for loop!
    show_animal(animals,i, ax)

plt.show()


# The previous cell requires a bit of [matplotlib](https://matplotlib.org) magic to create a grid of images but the key is that there is a for loop that steps through and displays each image.  Try to understand this code and compare it to the loops described above.

# ## Random numbers

# In many aspects of analysis you need to generate random numbers.  You need this for a few reasons
# 1. to create data from a distibution to check your intuitions about randomness (simulation)
# 2. to create cognitive models that have "noise" in them so that their behavior is not deterministic
# 3. to test your code by providing "fake" data that looks realistic
# 
# One of the useful libraries for this is numpy's `random` submodule.  The full list of available functions in this library is [here](https://docs.scipy.org/doc/numpy-1.14.0/reference/routines.random.html) and reading through can give you a good sense of what is possible.

# In[ ]:


import numpy.random as npr


# `randn()` gives you a random number of a standard normal distribution (one with the mean = 0 and standard deviation equal to 1.0:

# In[ ]:


npr.randn()


# you can get more than one like this:

# In[ ]:


npr.randn(10)


# lets get even more (1000) and plot them

# In[ ]:


sns.distplot(npr.randn(1000))


# if you want the numbers to be uniform you can use `rand()` which draws random numbers from 0 to 1 (but not including exactly 1.0).

# In[ ]:


npr.rand()


# In[ ]:


npr.rand(1000).max()


# as you can see the maximum value even of 1000 random `rand()` numbers is less than 1.0.  while for `randn()` it can be much higher:

# In[ ]:


npr.randn(1000).max()


# `randint()` will only include the integers between the given range.

# In[ ]:


npr.randint(0,10,10)


# In[ ]:


npr.randint(0,100,10)


# you can also choose a random element of an array or list so that only certain values can be chosen:

# In[ ]:


npr.choice(np.array([3,6,1,4]))


# notice that even in 100 draws you never see 0 or 9 because they are not in the given array.

# In[ ]:


npr.choice(np.array([3,6,1,4]),100)


# You can also use random to randomly "shuffle" a list (meaning changing the order of things like you would a deck of playing cards).

# In[ ]:


cards = np.arange(10)
print(cards)
npr.shuffle(cards)
print(cards)


# The second list is the same as the first just randomly shuffled.

# There are lots of distributions you can draw random numbers from:

# **Chi-square**

# In[ ]:


sns.distplot(npr.chisquare(2,10000))


# **lognormal**

# In[ ]:


sns.distplot(npr.lognormal(0,1,10000))


# **F**   
# you'll see this again when we get to ANOVA!

# In[ ]:


sns.distplot(npr.f(2,16,10000))


# The `cumsum()` command computes the cumulative sum of a list.  Meaning it is the sum created by adding each entry to the list to the values of all the ones that come before.

# In[ ]:


np.array([1,2,3,4]).cumsum()


# So the result is `array([1, 2+1, 3+2+1, 4+3+2+1])`.  Now we can start adding up random numbers.  For example, 

# In[ ]:


npr.randn(20).cumsum()


# This is sometimes called a "random walk" because you are taking small steps either up or down each time you add a number (the value from `npr.randn()`) but how far you move depends on the current sum.  You can get a sense of this by plotting the sum as it evolves:

# In[ ]:


plt.plot(npr.randn(200).cumsum())


# Try running the above cell a few times to get a sense of the range of random walks that are possible.
# 
# You can also plot a few random walks on the same plot together:

# In[ ]:


for i in range(5):
    plt.plot(npr.randn(200).cumsum(),alpha=0.2)


# Let's change the code to plot even more of these... maybe like 500!

# In[ ]:


for i in range(500):
    plt.plot(npr.randn(200).cumsum(),alpha=0.2)


# That's interesting... the sum start at zero (makes sense) and then kind of grows to get bigger as time goes on.  Not all paths get bigger of course but some randomly add up a bunch of positive or negative numbers and tend to drift further and further from the starting point.

# Now instead of computing the sum, let's compute the average at each step.  So for each step we need to divide by the number of things we have added together so far.

# In[ ]:


npr.randn(50).cumsum()/(np.arange(1,50+1))


# Notice we needed to use `np.arange(1,50+1)` because we want to start with value 1 for the first number (`np.arange(50)` would count from 0 to 49 and we would then be dividing by zero on the first sum.
# 
# Let's plot a bunch of these random averages:

# In[ ]:


for i in range(50):
    plt.plot(npr.randn(50).cumsum()/(np.arange(50)+1), alpha=0.2)


# That's interesting, you can see that early on the average is quite variable but as you add more and more numbers the averages seem to converge around a particular value.  As it turns out you are looking at the sampling distribution of the mean for different values of N.  If you took a slice out of the plot at say 10 sums and made a histogram of the averages you would get a histogram of the sampling distribution of the mean.

# In[ ]:


sns.distplot(npr.randn(10,50).sum(axis=0)/10)


# Interestingly the "envelope" of the sampling distribution of the mean seems to be shrinking according to a particular mathematical relationship which is $1/\sqrt N$ where $N$ is the number of numbers you have added to the sum.
# 
# In fact we can plot the sqrt(N) on the same plot to see the relationship

# In[ ]:


for i in range(50):
    plt.plot(npr.randn(50).cumsum()/(np.arange(1,50+1)), alpha=0.2)
plt.plot(1.0/np.sqrt(np.arange(1,50+1)),'k-')


# Here, the thick black line is $1/\sqrt N$ which is how the variance of the sampling distribution changes as the sample size increases!  (remember the formulat for the standard error fo the mean is the standard devision of the sample divided by the square root of N).  Now you can see why!

# <div class="alert alert-success" role="alert">
#   <strong>Problem 7 (4 points)</strong> <br>
#   Modify the code above to plot the sampling distribution for number drawn from a random uniform distribution and from the chi-sq distribution (see above, you have all the ingredients you need).  Does the shape of the curves look that same?  Why is that?
# </div>

# In[ ]:


# your code here


# ---

# <img src="https://i.redd.it/u8j4x4jiz1q31.jpg" width="400">

# ## Pandas and Data Frames

# A DataFrame is like a dictionary where the keys are column names and the values are Series that share the same index and hold the column values. The first "column" is actually the shared Series index (there are some exceptions to this where the index can be multi-level and span more than one column but in most cases it is flat).

# In[ ]:


names = pd.Series(['Alice', 'Bob', 'Carol'])
phones = pd.Series(['555-123-4567', '555-987-6543', '555-245-6789'])
dept = pd.Series(['Marketing', 'Accounts', 'HR'])

staff = pd.DataFrame({'Name': names, 'Phone': phones, 'Department': dept})  # 'Name', 'Phone', 'Department' are the column names
staff


# Note above that the first column with values 0, 1, 2 is actually the shared index, and there are three series keyed off the three names "Department", "Name" and "Phone".
# 
# Like `Series, DataFrame` has an index for rows:

# In[ ]:


staff.index


# `DataFrame` also has an index for columns:

# In[ ]:


staff.columns


# In[ ]:


staff.values


# The index operator actually selects a column in the DataFrame, while the .iloc and .loc attributes still select rows (actually, we will see in the next section that they can select a subset of the DataFrame with a row selector and column selector, but the row selector comes first so if you supply a single argument to .loc or .iloc you will select rows):

# In[ ]:


staff['Name']  # Acts similar to dictionary; returns a column's Series


# In[ ]:


staff.loc[2]


# You can get a transpose of the DataFrame with the .T attribute:

# In[ ]:


staff.T


# You can also access columns like this, with dot-notation. Occasionally this breaks if there is a conflict with a UFunc name, like 'count':

# In[ ]:


staff.Name


# You can add new columns. Later we'll see how to do this as a function of existing columns:

# In[ ]:


staff['Fulltime'] = True
staff.head()


# Use `.describe()` to get summary statistics:

# In[ ]:


staff.describe()


# Use `.quantile()` to get quantiles:

# In[ ]:


df = pd.DataFrame([2, 3, 1, 4, 3, 5, 2, 6, 3])
df.quantile(q=[0.25, 0.75])


# Use `.drop()` to remove rows. This will return a copy with the modifications and leave the original untouched unless you include the argument `inplace=True`.

# In[ ]:


staff.drop([1])


# In[ ]:


# Note that because we didn't say inplace=True,
# the original is unchanged
staff


# There are many ways to construct a DataFrame. For example, from a Series or dictionary of Series, from a list of Python dicts, or from a 2-D NumPy array. There are also utility functions to read data from disk into a DataFrame, e.g. from a .csv file or an Excel spreadsheet. We'll cover some of these later.
# 
# Many DataFrame operations take an axis argument which defaults to zero. This specifies whether we want to apply the operation by rows (axis=0) or by columns (axis=1).
# 
# You can drop columns if you specify `axis=1`:

# In[ ]:


staff.drop(["Fulltime"], axis=1)


# Another way to remove a column in-place is to use `del`:

# In[ ]:


del staff["Department"]
staff


# You can change the index to be some other column. If you want to save the existing index, then first add it as a new column:

# In[ ]:


staff['Number'] = staff.index
staff


# In[ ]:


# Now we can set the new index. This is a destructive
# operation that discards the old index, which is
# why we saved it as a new column first.
staff = staff.set_index('Name')
staff


# Alternatively you can promote the index to a column and go back to a numeric index with `reset_index()`:

# In[ ]:


staff = staff.reset_index()
staff


# <div class="alert alert-success" role="alert">
#   <strong>Problem 8 (2 points)</strong> <br>
#   Create a data frame from the disctionary called `example_data` below.  Then generate a summary of the data.  Calculate the sum of all the visits (i.e., the total number of visits).
# </div>

# In[ ]:


example_data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],
           'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],
           'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
           'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}


# In[ ]:


# Put your code to create the DataFrame here
# Generate a summary of the data
# Calculate the sum of all the visits (the total number of visits)


# ## Course feedback

# <div class="alert alert-success" role="alert">
#   <strong>Give us some feedback</strong> <br>
#     How is the course going for you so far?  What can we try to work on in future?  Please remember that professors and TAs have feelings to but if you have a constructive idea to make the class work better for you please share in a markdown cell below!
# </div>

# **Your thoughts here please**

# ## Turning in homeworks

# When you are finished with this notebook. Save your work in order to turn it in.  To do this select *File*->*Download As...*->*HTML*.
# 
# <img src="images/save-pdf.png" width="300">
# 
# Homeworks will be submitted according to the instructions provided in class.
