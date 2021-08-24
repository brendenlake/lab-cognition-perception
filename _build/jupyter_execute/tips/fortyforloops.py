#!/usr/bin/env python
# coding: utf-8

# # Intro to For loops

# ```{note}
# For the first section of this page, the original content was developed by [Lisa Tagliaferri](https://twitter.com/lisaironcutter) for digitalocean.com released under the Creative Commons Attribution-NonCommercial-ShakeAlike 4.0 International Licence.  The text of Lisa's tutorial had been modified in a minor way by [Todd Gureckis](http://gureckislab.org/~gureckis) in a few sections.  Todd added 40 different examples of for loops ranging from simple to more complex.  This page is released under the [license for this book](/LICENSE.html)
# ```

# Using loops in computer programming allows us to automate and repeat similar tasks multiple times. This is very common in data analysis.  In this tutorial, we’ll be covering Python’s **for loop**.
# 
# A `for` loop implements the repeated execution of code based on a loop counter or loop variable. This means that `for` loops are used most often when the number of repetitions is known before entering the loop, unlike **while loops** which can run until some condition is met.

# ## For Loops

# In Python, `for` loops are constructed like so:

# ```
# for [iterating variable] in [sequence]:
#     [do something]
# ```

# The something that is being done (known as a code block) will be executed until the sequence is over.  The code block itself can consist of any number of lines of code, as long as they are tabbed over once from the left hand side of the code.

# Let’s look at a `for` loop that iterates through a range of values:

# In[ ]:


for i in range(0,5):
   print(i)


# When we run this program, the output looks like this:

# In[3]:


for i in range(0,5):
   print(i)


# This `for` loop sets up `i` as its iterating variable, and the sequence exists in the range of 0 to 5.
# 
# Then within the loop we print out one integer per loop iteration. Keep in mind that in programming we tend to begin at index 0, so that is why although 5 numbers are printed out, they range from 0-4.
# 
# You’ll commonly see and use `for` loops when a program needs to repeat a block of code a number of times.

# ## For Loops using range()

# One of Python’s built-in immutable sequence types is `range()`. In loops, `range()` is used to control how many times the loop will be repeated.
# 
# When working with `range()`, you can pass between 1 and 3 integer arguments to it:
# 
# - `start` states the integer value at which the sequence begins, if this is not included then start begins at 0
# - `stop` is always required and is the integer that is counted up to but not included
# - `step` sets how much to increase (or decrease in the case of negative numbers) the next iteration, if this is omitted then step defaults to 1
# 
# We’ll look at some examples of passing different arguments to `range()`.
# 
# First, let’s only pass the `stop` argument, so that our sequence set up is `range(stop)`:

# In[ ]:


for i in range(6):
   print(i)


# In the program above, the stop argument is 6, so the code will iterate from 0-6 (exclusive of 6):

# In[4]:


for i in range(6):
   print(i)


# Next, we’ll look at `range(start, stop)`, with values passed for when the iteration should start and for when it should stop:

# In[ ]:


for i in range(20,25):
    print(i)


# Here, the range goes from 20 (inclusive) to 25 (exclusive), so the output looks like this:

# In[6]:


for i in range(20,25):
    print(i)


# The step argument of `range()` can be used to skip values within the sequence.
# 
# With all three arguments, `step` comes in the final position: `range(start, stop, step)`. First, let’s use a `step` with a positive value:

# In[ ]:


for i in range(0,15,3):
   print(i)


# In this case, the `for` loop is set up so that the numbers from 0 to 15 print out, but at a step of 3, so that only every third number is printed, like so:

# In[7]:


for i in range(0,15,3):
   print(i)


# We can also use a negative value for our `step` argument to iterate backwards, but we’ll have to adjust our start and stop arguments accordingly:

# In[ ]:


for i in range(100,0,-10):
   print(i)


# Here, 100 is the `start` value, 0 is the `stop` value, and -10 is the range, so the loop begins at 100 and ends at 0, decreasing by 10 with each iteration. We can see this occur in the output:

# In[9]:


for i in range(100,0,-10):
   print(i)


# When programming in Python, for loops often make use of the `range()` sequence type as its parameters for iteration.

# In[10]:


## For Loops using Sequential Data Types


# Lists and other data sequence types can also be leveraged as iteration parameters in for loops. Rather than iterating through a `range()`, you can define a list and iterate through that list.
# 
# We’ll assign a list to a variable, and then iterate through the list:

# In[ ]:


sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for shark in sharks:
   print(shark)


# In this case, we are printing out each item in the list. Though we used the variable shark, we could have called the variable any other valid variable name and we would get the same output:

# In[12]:


sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for shark in sharks:
   print(shark)


# The output above shows that the `for` loop iterated through the list, and printed each item from the list per line.

# Lists and other sequence-based data types like strings and tuples are common to use with loops because they are iterable. You can combine these data types with range() to add items to a list, for example:

# In[13]:


sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']

for item in range(len(sharks)):
   sharks.append('shark')

print(sharks)


# Here, we have added a placeholder string of 'shark' for each item of the length of the sharks list.
# 
# You can also use a `for` loop to construct a list from scratch:

# In[ ]:


integers = []

for i in range(10):
   integers.append(i)

print(integers)


# In this example, the list `integers` is initialized as an empty list, but the for loop populates the list like so:

# In[15]:


integers = []

for i in range(10):
   integers.append(i)

print(integers)


# Similarly, we can iterate through strings:

# In[16]:


sammy = 'Sammy'

for letter in sammy:
   print(letter)


# Iterating through tuples is done in the same format as iterating through lists or strings above.

# When iterating through a dictionary, it’s important to keep the `key:value` structure in mind to ensure that you are calling the correct element of the dictionary. Here is an example that calls both the key and the value:

# In[17]:


sammy_shark = {'name': 'Sammy', 'animal': 'shark', 'color': 'blue', 'location': 'ocean'}

for key in sammy_shark:
   print(key + ': ' + sammy_shark[key])


# When using dictionaries with `for` loops, the iterating variable corresponds to the keys of the dictionary, and `dictionary_variable[iterating_variable]` corresponds to the values. In the case above, the iterating variable key was used to stand for `key`, and `sammy_shark[key]` was used to stand for the values.
# 
# 

# Loops are often used to iterate and manipulate sequential data types.

# ## Nested For Loops

# Loops can be nested in Python, as they can with other programming languages.
# 
# A nested loop is a loop that occurs within another loop, structurally similar to nested if statements. These are constructed like so:

# ```
# for [first iterating variable] in [outer loop]: # Outer loop
#     [do something]  # Optional
#     for [second iterating variable] in [nested loop]:   # Nested loop
#         [do something]  
# ```

# The program first encounters the outer loop, executing its first iteration. This first iteration triggers the inner, nested loop, which then runs to completion. Then the program returns back to the top of the outer loop, completing the second iteration and again triggering the nested loop. Again, the nested loop runs to completion, and the program returns back to the top of the outer loop until the sequence is complete or a break or other statement disrupts the process.

# Let’s implement a nested `for` loop so we can take a closer look. In this example, the outer loop will iterate through a list of integers called `num_list`, and the inner loop will iterate through a list of strings called `alpha_list`.

# In[ ]:


num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)


# When we run this program, we’ll receive the following output:

# In[19]:


num_list = [1, 2, 3]
alpha_list = ['a', 'b', 'c']

for number in num_list:
    print(number)
    for letter in alpha_list:
        print(letter)


# The output illustrates that the program completes the first iteration of the outer loop by printing `1`, which then triggers completion of the inner loop, printing `a`,`b`, `c` consecutively. Once the inner loop has completed, the program returns to the top of the outer loop, prints `2`, then again prints the inner loop in its entirety (`a`, `b`, `c`), etc.

# Nested `for` loops can be useful for iterating through items within lists composed of lists. In a list composed of lists, if we employ just one for loop, the program will output each internal list as an item:

# In[20]:


list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]

for list in list_of_lists:
    print(list)


# In order to access each individual item of the internal lists, we’ll implement a nested `for` loop:

# In[21]:


list_of_lists = [['hammerhead', 'great white', 'dogfish'],[0, 1, 2],[9.9, 8.8, 7.7]]

for list in list_of_lists:
    for item in list:
        print(item)


# When we utilize a nested for loop we are able to iterate over the individual items contained in the lists.

# ## Conclusion

# This tutorial went over how for loops work in Python and how to construct them. For loops continue to loop through a block of code provided a certain number of times.

# # 40 Example For Loops

# In the next section I will provide 40 for loops.  Each for loop is a different example of using for loops in cases the often come up in python data analysis.

# ## Simple For Loops

# ### Print the same thing 10 times

# In[26]:


for i in range(10):
    print("hi")


# ### Print the numbers 0-9

# In[28]:


for i in range(10):
    print(i)


# ### Print the numbers 1-10

# In[30]:


for i in range(1,11):
    print(i)


# ### Print only the even numbers 1-10 combining a for loop with a if statement

# In[115]:


for i in range(1,11):
    if i%2==0:
        print(i)


# ### Print the elements of a list

# In[33]:


students = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
for student in students:
    print(student)


# ### Print the elements of a list backwards

# In[37]:


students = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
for student in students[::-1]:
    print(student)


# ### Print the first four elements of a list

# In[41]:


students = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
for student in students[:4]:
    print(student)


# ### Print the entire list of students four times

# Careful with this one!  Notice the small difference between the variables `students` (plural) and `student` (singular).

# In[43]:


students = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
for student in students[:4]:
    print(students)


# ### Keep a counter (i) of how many times the loop repeated

# In[48]:


students = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
for i, student in enumerate(students):
    print(i, student)


# ### Do something 10 times (make a random number) and don't use a named variable for iterator

# This is kind of a python style thing.  You can create a variable with a name just `_` (underscore).  Since you would probably never name a variable something like that anywhere else in the code it can be good in `for` loops were you mostly care about repeating the same code a bunch of times and not iterating down the values of a list.

# In[51]:


import numpy as np

for _ in range(10):
    print(np.random.randn())


# ### Iterate down two lists at the same time

# The `zip` command takes to lists and combines them element by element.  The lists need to be the same length!

# In[56]:


firstname = ['anna','alex','anselm','david','pam','zhiwei','ili','shannon','neil']
lastname = ['smith','johnson','alexander','baker','palmeri','zoubok','weng','foster','shields']
for person in zip(firstname, lastname):
    print(person)


# ### Iterating the entries in a dictionary by the key

# In[60]:


id_cards = {"123": "Anna", "d131": "Alex", "3f32": "Anselm"}
for key in id_cards.keys():
    print(key,id_cards[key])


# ### Iterating the values in a dictionary directly

# In[64]:


for name in id_cards.values():
    print(name)


# ### Keeping track of a result within a loop

# All the examples so far have just repeated some simple block of code like printing something out.  However, sometimes you want each iteration of the loop to compute something for you and store the result for further analysis.  For example here we will square each number in a list and store it in a new list called results.  Then we we plot the results.

# In[99]:


import matplotlib.pyplot as plt
a = range(10)
results = []
for i in a:
    results.append(i**2)
print(results)

plt.plot(a,results)
plt.show()


# ### Print out the contents of a text file

# This will open a text file on your computer or jupyter hub instance and will print out each line of the file.

# In[ ]:


myfile = 'something.txt'
with open(myfile, 'r') as f:
    for line in f:
        print(line)


# ## For Loops Inside of For Loops (Nested)

# ### Print out a square using a nested loop

# Notice here that I used the underscore character for the `_i` and `_j` iterator variables.

# In[78]:


for _i in range(10): # rows
    for _j in range(10): # columns
        print("* ", end='') # this prevents a new line being printed each time
    print() # this only prints the new line at the end of each row


# ### Use the counter from the outer loop to change the inner loops

# In[81]:


for _i in range(10):
    for _j in range(_i): # add as many columns as we have experienced rows
        print("* ", end='')
    print()


# ### Three nested loops?  Why not!?

# The more outer loops make squares of growing sides

# In[82]:


for _i in range(10):
    for _j in range(_i): # add as many columns as we have experienced rows
        for _k in range(_i):
            print("* ", end='')
        print()
    print('----')


# ## For Loops and Numpy

# This section looks at the use of for loops in the context of a couple of common `numpy` functions.

# ### Print out a range from a numpy array

# This acts pretty much like the `range()` function described above.  A `np.arange()` just returns a numpy array instead of a list.

# In[84]:


import numpy as np
for i in np.arange(0,10):
    print(i)


# ### Print out 20 steps between 0 and 10

# This does a normal for loop over a `np.linspace()` array.  This function returns an numpy array between a start values (0) and end value (10) taking (20) steps.  What is nice about this is that it figure how big the steps have to be so that you take two between the start and end value.

# In[86]:


import numpy as np
for i in np.linspace(0,10,20):
    print(i)


# ### Using a nested loop to iterated over an array

# If you have an array of arrays (sometimes called a matrix, although there is a specific matrix type in numpy), you might need to iterate over the elemnts:

# In[89]:


x = np.array([[1,2,3],[4,5,6]])
for _row in x:
    for _col in _row:
        print(_col,end=' ')
    print()


# ### Interating over an array using indicies

# Python is nice because you can iterate in a for loop directly over things in a collection like a list, dictionary or numpy array.  However, sometimes you want to iterate by an index.

# In[95]:


x = np.array([[1,2,3],[4,5,6]])
rows, cols = x.shape
for i in range(rows):
    for j in range(cols):
        print(x[i][j],end=' ') # here we are looking up the value in the array using our indicies
    print()


# ## For Loops and Pandas

# This section looks at the use of for loops in the context of a couple of common `pandas` data munging operations.  For these examples, I am loading a .csv file hosted on the class webpage on salary of professors that we encountered in a previous homework.

# ### Iterating over columns

# First let's print out each of the columns in this data frame

# In[104]:


import pandas as pd
salary_data = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
for col in salary_data.columns:
    print(col)


# ### Iterating over rows

# Dataframes have a couple of ways you can iterate over the rows.  The best is the `.iterrows()` method available on any data frame which is a proper [iterator](https://treyhunner.com/2018/06/how-to-make-an-iterator-in-python/) similar to what you get using the `enumerate()` function we explored above.  If you wanted to print out the entire data frame you can just delete the `.head(n=3)` part of the command (i.e., `salary_data.iterrows()`.

# In[109]:


import pandas as pd
salary_data = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
for index, row in salary_data.head(n=3).iterrows():
    print(index, row)
    print('---')


# ### Iterating over groups

# One of the most useful functions of pandas dataframes is the `groupby` operation which divides up a larger dataframe into smaller groups based on the value of one or more columns.  This is ideal for psychological data analysis because you might want to divide up your data based on trial type, participant number, etc...  After you form the groups it is often useful to iterate over the groups to do additional analyses.

# In[113]:


import pandas as pd
salary_data = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')

grouped = salary_data.groupby("departm")

for name, group in grouped:
    print(name)
    print('-----')
    print(group)
    print()


# ### Iterating over muliple groups

# You can group not just on a single column but combinations of multiple combinations.

# In[114]:


import pandas as pd
salary_data = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')

grouped = salary_data.groupby(["departm","gender"])

for name, group in grouped:
    print(name)
    print('-----')
    print(group)
    print()


# ### Reading in an entire directory of files

# Sometimes you need to read in an process individual files in a folder.  This code snippet for instance reads all the .csv files in a particular folder into a pandas dataframe and concatenates them.

# In[ ]:


import pandas as pd
data_path = './myfile/'
files = os.listdir(data_path)
frames = []
for data_file in files:
    if data_file[-3:] == 'csv':
        df = pd.read_csv(data_path+data_file)
        frames.append(df)
alldata_df = pd.concat(frames)


# ## For Loops and Seaborn

# This section looks at the use of for loops in the context of plotting with `seaborn`.

# ### Plotting to subpanels of a matplotlib figure with a for loop

# In[ ]:


fig,ax = plt.subplots(7,3,figsize=(12,24))
ax = ax.ravel()
for i,s in enumerate(subs):
    part_df=all_df[all_df.participant==s]
    p1=sns.regplot(x='angle',y='trialResp.rt',data=part_df,ax=ax[i])
plt.show()


# ## For Loops and Matplotlib

# In[ ]:




