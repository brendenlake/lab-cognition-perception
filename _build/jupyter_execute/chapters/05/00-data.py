#!/usr/bin/env python
# coding: utf-8

# # The Format and Structure of Digital Data

# ```{note}
# This chapter authored by [Todd M. Gureckis](http://gureckislab.org/~gureckis) and [Kelsey Moty](http://kelseymoty.github.io) and is released under the [license for this book](../../LICENSE).
# ```

# ## Video Lecture
# 
# This video provides an complementary overview of this chapter.  There are things mentioned in the chapter not mentioned in the video and vice versa.  Together they give an overview of this unit so please read and watch.
# 
# <center>
# <iframe src="https://player.vimeo.com/video/520946467" width="640" height="360" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe>
# </center>

# ## How to think about data and organize it

# Data is an important concept in science.  The first step is we measure something.   In a [previous chapter we discuss issues in measurement](../../chapters/04/00-researchdesign) including different types of scales, units, etc...  However the main thing is that data is born when a number is assigned to some observation we make.  Here is a lonely single number which maybe measures something:
# 
# <div style="text-align: center">
#     <img src="./images/single_number.png" width="150">
# </div>

# Things get more interesting when we make multiple observations and so we have many data.  In order to do anything with more than one number though we start running into the question of how to organize things.  How do we keep track of which number was collected first, second or third for instance?  If we have just a big jumble of numbers we can easily get lost. 
# 
# Before we get too many numbers we need to start thinking abstractly about **organzing** our measurements into some type of collection.  In our previous chapter on the [basics of Python](../../chapters/03/00-python) we discussed the concept of [collections](chapters/03/00-python.html#collections).  Collections are things in the native Python language space that organize multiple numbers, string, or even other collections.  This included [lists](chapters/03/00-python.html#lists) (which organize things in some order), [dictionaries](chapters/03/00-python.html#dictionaries) (which do not preseve order but allow "looking up" the value of a number by a special address known as a key), or [sets](chapters/03/00-python.html#sets) (which are unordered collections of things useful for counting, and performing set operations like union, etc...).  
# 
# 
# For instance if we measured a number repeatedly in time a list might be a useful way to organize them:
# 
# <div style="text-align: center">
#     <img src="./images/list.png" width="400">
# </div>

# Lets imagine the numbers above represent some measurement on a person on three different days (monday, tuesday, wednesday).  It might be their blood pressure or temperature.  Learning a lot about one person is nice and fits cleanly into a list.  However, more often it gets more complex.  What we if instead have multiple people we are recording information from and so the data starts looking two dimensional.  There is maybe 3 people in the study and each has 3 measurements.  In that case we might then organize the data as a list of lists (or a matrix):
# 
# <div style="text-align: center">
#     <img src="./images/matrix.png" width="550">
# </div>

# Although a matrix is a nice way to organize multiple observations made on multiple people it can get a little bit confusing.  Are the rows or the columns the subjects in the example above?  You have to remember to write that down otherwise you could easily get confused.  What is this data?  What does it describe? For this reason we might look beyond standard Python collections to more complex structures.  
# 
# For example, you are all likely familiar with the concept of a spreadsheet (e.g., Microsoft Excel or Google Sheets).  These are nicer than matricies because they have named rows and columns and so just by looking at the structure of the spreadsheet you can often learn more about the structure of the data.  Columns names are sometimes known as **metadata** because they are data themselves that *describe* other data.
# 
# 
# <div style="text-align: center">
#     <img src="./images/spreadsheet.png" width="550">
# </div>
# 
# This is much nicer because the columns names help us remember what each measurement records and also what is contained in the rows.

# The two dimensional structure of a spreadsheet is generally the most complex types of data that we will deal with.  However, just so you are aware, as data gets really big it can make sense to take other organizational approaches.  For instance, a website that had millions of users reviewing movies might not want to make a long spreadsheet recording each user and the rating they gave and the movie the rating was about.  Stop and think for a moment how you could do that in a spreadsheet.  Perhaps you could make each row a user and each column a movie.  However, as you know Netflix and other sites have hundred of thousands of TV shows and movies and so the data would be really unweildy.  Also most of the data would be "missing" because people only provide a rating for a small subset of the total number of movies.  As a result, big websites adopt alternative ways of organizating data including the use of what are known as **relational databases**.  
# 
# 
# <div style="text-align: center">
#     <img src="./images/database.png" width="550">
# </div>

# Relational databases are made up of multiple spreadsheets (effectively) where each one represents only a smaller piece of the data.  In the figure above the green words are columns of a smaller spreadsheet. This database is thus organized into four separate spreadsheets (or "tables"). For instance the ratings table has an unique id number (i.e. row number) and then the rating a person gave, a user id of who gave it, and a movie id for which movie it was about.  Separately there is a movies table which had its own id (unique id for each movie), the title or name of the movie, and a description/summary of the movie.  The orange lines reflect links where the value in one columns of one table connects with or refers to the entries of another one.  This can be a much more efficient way to organize the data. 
# 
# The main point this example brings forward is that the way you organize your data is something you really have to think about and plan to begin with.  I've found that this topic actually is intuitively interesting to many students.  The reason is that we love organizing our homes and offices.  It feels great.  When it comes to data taking the same mentality - the "fresh" feeling of being organized, is really key to making good scientific analyses that do not have bugs.  Problems with data organization can even be deadly ([How not to kill people with spreadsheets](https://foreignpolicy.com/2020/10/08/uk-coronavirus-covid-spreadsheet-excel-error-outsourcing/)).  If you get really interested in organizing data, there are [entire books](https://www.amazon.com/Discipline-Organizing-MIT-Press/dp/0262518503) {cite}`Glushko:2013` and fields of study about how to best organize data (e.g., library and information sciences).  The choices you make in how to organize your data at one point in time really influence how easy it can be to do certain analyses later.  More on this later.

# ## Common file formats for data

# Data often come in files with particular formatted structure.  This formatted structure makes it easier for computer programs to read in the data and manipulate it.  In this section we will go over a couple of the common data formats you might encounter in traditional psychological research.

# #### Excel Workbooks (.xls, .xslx files)
# XLSX file format (or XLS in older versions of Excel) is the default file format used in Excel. Under the hood, Excel Workbooks are built using a highly structured markup language called Extensible Markup Language (XML). Essentially what this means is while you are using Excel's graphic interface to edit your data, XML is adding a bunch of tags behind the scenes to the XLSX file so it knows how to properly format the data each time you open it up. All of these tags in XML are what allow you to change font colors and sizes, add graphs and images, and use formulas. 
# 
# This is what you see when you when you use Excel: 
# <div style="text-align: center">
#     <img src="./images/excel_worksheet.png" width="200">
# </div>
# 
# 
# And this is what the exact same Workbook looks like behind the scenes:
# <div style="text-align: center">
#     <img src="./images/excel_xml.png" width="550">
# </div>
# 
# But this complexity can also make it difficult to use XLSX files with any other software or programming language that isn't Excel. For one, not all programs can open XLSX files, so these data files can make your data inaccessible to other people. Two, all of this special formatting can sometimes lead to problems when you read in data from XLSX files (e.g., converting variables to weird formats). To avoid issues like these, it is preferable to store your data using plain-text formats (such as CSV and TSV files). 
# 
# 
# #### Comma-separated Values (.csv files)
# CSV, or Comma-separated value files, on the other hand, are written using a plain-text format. No special tags, just text. The only formatting in CSV files are the commas used to delimit different values for columns and new lines to indicate rows. You can see this if you open up a CSV file using Notepad (or other text editors). 
# 
# 
# Here's the same dataset as before but now as a CSV file:
# <div style="text-align: center">
#     <img src="./images/csv_sample.png" width="450">
# </div>
# 
# This means that what you can store within a CSV file is quite limited (no images or special formatting, for example). But it also means that this kind of file is great for storing and sharing data. CSV files can be opened by any software, making it accessible to others. Given that CSV files inherently have no formatting, some of the issues that come with using XLSX files never arise. 
# 
# #### Tab-separated Values (.tsv files)
# TSV files are very similar to CSV files, except that instead of using a comma to delimit between values in a dataset, it uses tabs (a special type of spacing, the same type you get when you hit the tab key on your computer).
# 
# ```{seealso} 
# It is a little bit beyond the scope of our class, but another file format you might encounter is referred to as JSON which stands for Javascript Object Notation (JSON).  JSON is similar to a python dictionary and is stored in a plain text file like a CSV.  However, JSON is somewhat more flexible than the two-dimensional structure of a spreadsheet. Often one analysis step is to convert JSON into a 2D spreadsheet-type structure.  [Here](https://realpython.com/python-json/) is a helpful guide to JSON in python.
# ```

# ## Exporting from spreadsheet programs

# ### Google Sheets 
# 
# To export a .csv file from Google Sheets, you click on File > Download > Comma-separated values (.csv). 
# 
# <div style="text-align: center"><img src="./images/export_csv_google.png" width="450"></div>
# 
# If you created a Google Sheet with multiple sheets, you will have to save each individual sheet as a .csv file because .csv files do not support multiple sheets. To do this, you will have to click on each sheet and go through the save process for each sheet. 

# ### Excel
# 
# To create a .csv file from Excel, click on File (found on the top left of the menu bar).
# 
# <div style="text-align: center"><img src="./images/excel_header.png" width="250"></div>
# 
# A new menu will appear. From there, select "Save as" and then choose where on your computer you want to save the file. A pop-up window will open up, and from there, you can choose what to name the file and what kind of file type to save it as. To save it as a   will there will be a dropdown menu where you can select which kind of file type you would like to save the file as (labeled "Save as type"). 
# 
# <div style="text-align: center"><img src="./images/export_csv_excel.png" width="550"></div>

# ## Uploading csv files to JupyterHub

# Many of the datasets you will be working with this semester will already be available for you to use on JupyterHub. However, if you want to work with your own datasets, you will need to upload them yourselves to the cluster.
# 
# To do that, go to the "Files" tab on JupyterHub and use the "Upload" button. 
# 
# <div style="text-align: center"><img src="./images/jupyter_upload.png" width="450"></div>

# ## The Pandas library and the concept of a dataframe API

# <div style="text-align: center">
#     <img src="./images/pandaslogo.png" width="250">
# </div>
# 
# Throughout this class there are several libraries (i.e., tools which extend the capabilities of the core Python language) which we will use a lot.  One of those is [Pandas](https://pandas.pydata.org).  Pandas is a open-source project for Python that provides a data analysis and manipulation tool.  Pandas gives you a way to interact with a dataset organized like a spreadsheet (meaning columns and rows which are possibly named or labeled with meta data) in order to perform sophisticated data analyses.  Pandas is really the "backbone" of the Python data science and modeling environment.  Pandas could be thought of as a langauge (or [API](https://en.wikipedia.org/wiki/API)) for unlocking tabular data.  **If you want to become better at data analysis with Python there is no single package I can think of that is worth more of your time learning.**
# 
# Although there is no required book for this class, "[Learning the Pandas Library: Python Tools for Data Munging, Analysis and Visualization](https://www.amazon.com/Learning-Pandas-Library-Munging-Analysis/dp/153359824X)" by Matt Harrison {cite}`Harrison:2016` is highly recommended both because it is short and to the point but also because it explains key Pandas concepts very clearly.  In addition, the Pandas project includes a very helpful [user guide](https://pandas.pydata.org/pandas-docs/stable/user_guide/index.html) which explains many of the key concepts.
# 
# ```{admonition} Pandas can be confusing at first!
# :class: tip
# I was aware of Pandas for several years and never really "understood it."  However, when it clicked it opened a universe of data analysis to me.  It takes some patience in part because data manipulation is a very complex topic at least at the conceptual level.
# ```
# 
# The organization of this guide is not to give a complete description of everything in Pandas but to kind of give you a sense of how you use Pandas (with code) to do the types of tasks you typically would do in a spreadsheet like Excel or Google Sheets.  In addition, we show a few of the key features of Pandas that are not that easy to do in Excel which are very useful for behavioral data analysis.
# 
# The first step of understanding Pandas is to load it:

# In[1]:


import numpy as np
import pandas as pd


# The two code lines above are the typical way to load in the Pandas library.  [Numpy](https://numpy.org) is a related library that Pandas is built on top of (it really is like a Russian doll where one project enables the next!).  Tradionally, pandas is imported 'as' **pd** and numpy 'as' **np**.  This means that when you are reading code online if you see `pd.somefunction()` you can probably assume that the function is part of the pandas library because the function begins with the `pd.` syntax.

# ## Reading data (e.g., csvs) into Python using Pandas

# Before getting further with Pandas it helps to first understand how to read some data into a dataframe object or how to create a dataframe from scratch.  Usually you are reading data in from some other file (e.g., a CSV file) and "loading" it into Pandas.  Pandas has <a href="https://pandas.pydata.org/pandas-docs/stable/reference/io.html">many different ways</a> for reading in different file types. Here, we will use <a href="https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html">`pd.read_csv()`</a> because we will mostly be working with .csv files in this class.
# 
# When reading in your .csv file, there are two things you absolutely have to do:
# 
# First, **you need to store the data into a variable.** Otherwise, you won't be able to work with your data. Here, we called the dataframe "df" but you can name it whatever you want. 
# 

# In[ ]:


# incorrect: won't store your data
pd.read_csv('salary.csv')

# correct: creates a dataframe called df that you can work with 
df = pd.read_csv('salary.csv')


# Second, **you need to tell `pd.read_csv` where the file you are trying to import is located.** The path can point to a file located in a folder in your local enviroment (e.g., on your computer, on JupyterHub) or to a file available online. 
# 
# To point to a file available online, you'll put the link to the file. 

# In[3]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')


# If you are pointing to a file on JupyterHub (or to a file on your computer, if you had Python downloaded on your computer), you'll need to specify the path to the file. If the .csv file and your notebook are in the same folder, you only have to put the name of the file. 

# In[ ]:


df = pd.read_csv('salary.csv')


# If the file is located in a different folder than the notebook you are working with, you will have to specify which folder(s) that the computer needs to look at to find it. 

# In[ ]:


df = pd.read_csv('folder1/folder2/salary.csv')


# Sometimes, your .csv file might be saved in a folder that's not in the same folder as your notebook. For example, say you have a folder called "project". And in that the folder, there was a folder called "code" that contained your notebooks/python code, as well as a folder called "data" that contained your data (.csv) files. To import your .csv file, you need to use `..` to tell the your computer go up one folder in your directory (get out of the "code" folder) in order for it to find the "data" folder. 

# In[ ]:


df = pd.read_csv('../data/salary.csv')


# By default, `pd.read_csv` assumes that file uses commas to differentiate between different entries in the file. But you can also explicitly tell `pd.read_csv` that you want to use commas as the delimiter.

# In[ ]:


df = pd.read_csv('salary.csv', sep = ",")


# `pd.read_csv` also assumes by default that the first row in your .csv files lists the names for each column of data (the column headers). You can explicitly tell `pd.read_csv` to do this by writing:
# 

# In[ ]:


df = pd.read_csv('salary.csv', sep = ",", header = 'infer')


# Sometimes, datasets may have multiple headers. (e.g., both the first and second rows of the dataset list column names). `pd.read_csv` allows you to keep both rows as headers by modifying the `header` argument with a list of integers. Remember that 0 actually means the first row. 

# In[ ]:


df = pd.read_csv('salary.csv', sep = ",", header = [0,1])


# When creating your own datasets, it's generally best practice to give your columns headers, so that's it easier for people looking at your data (including yourself!) to know what's in the dataset. However, you may occassionally come across datasets that do not have headers. To tell `pd.read_csv` there's no header to import, set `header` to "None":

# In[ ]:


df = pd.read_csv('salary.csv', sep = ",", header = None)


# :::{warning} 
# When creating your own dataset, refrain from using characters like space or period (.) in the column names.  This will make things easier for you down the line when using Pandas for statistical modeling.
# :::

# ## Viewing the data in a dataframe

# So now we have loaded a dataset into a variable called `df`.  Now we might like to look at the data to check it was properly read in and also to learn more about the structure of this dataset.  Perhaps the simplest method is simply to type the name of the dataframe variable by itself in a code cell:

# In[13]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
df


# This outputs a "table" view of the dataframe showing the column names, and several of the rows of the dataset.  It doesn't show you **all** of the data at once because in many large files this would be too much to make sense of.
# 
# You can also specifically request the first several rows of the dataframe:

# In[14]:


df.head()


# or the last several rows:

# In[15]:


df.tail()


# The "head" of the dataframe is the top.  The "tail" of the dataframe is the bottom.
# 
# 
# We can also access individual rows and columns of a data frame.

# #### Accessing individual columns

# To access a single column you can index it like a dictionary in Python using the column name as a key:

# In[16]:


df['salary']


# In[9]:


df['age']


# Another allowed syntax is to use the name of the dataframe variable and a `.columnname`.  For instance:

# In[10]:


df.salary


# However the dictionary key-lookup method is preferred because it is possible that the name of a column is the same as a dataframe method (see below) and that causes Python to get confused.

# :::{seealso} 
# When we learn about [visualizing data](../../chapters/06/00-plots), [describing data](../../chapters/07/00-describingdata), and [linear regression](../../chapters/13/00-linearregression) you will see how the column struture of dataframes becomes very powerful.
# :::

# #### Accessing individal rows

# Since the Python bracket notation is use to lookup columns, a special command is needed to access rows.  The best way to look up a single row is to use `.iloc[]` where you pass the integer row number you want to access (zero indexed).  So to get the first row you type:

# In[17]:


df.iloc[0]


# Here is the 5th row:

# In[18]:


df.iloc[4]


# or counting three backwards from the end:

# In[19]:


df.iloc[-3]


# ### Indexes and Columns

# Also note that there are two special elements of a normal dataframe called the **column index** and the **row index** (or just index).  The row index is the column on the left that has no name but seems like a counter of the rows (e.g., 72, 73, 74, ...).  The row index is useful in Pandas dataframes for looking things up by row.  Although you can index a row by counting (access the fifth row for instance), the index can be made on arbitrary types of data including strings, etc...  You don't need to know a ton about indexes to use Pandas typically but every once in a while they come up so it is useful to know the special nature of the index column.

# In[83]:


df.index


# In[84]:


df.columns


# The above code shows how to find the row index and column index.
# 
# You can change the row index to another column:

# In[20]:


df.set_index('departm')


# Or to reset it to a counter that count the row number use `.reset_index()`.

# In[21]:


df2=df.set_index('departm')
df2.reset_index()


# Note the syntax we've used a few times here... we referenced the `df` variable which is the variable we created to store the data from our file.  Then the `.functionname()` is known as a method of the data frame which is provided by pandas.  For instance the `.head()` method prints out the first five rows of the data frame.  The `.tail()` method prints out the last five rows of the data frame.  There are many other methods available on data frames that you access by calling it using the `.functionname()` syntax.  The next parts of this chapter explain some of the most common ones.

# ## Adding and deleting things from a dataframe

# Sometimes after we read in a dataset we might want to add new rows or columns or delete rows and columns from a dataframe.  One way to do this is to edit the original CSV file that we read in.  However, there is an important principle I want to emphasize thoughout this class: 
# 
# ```{admonition} **ALWAYS do everything in code**
# :class: tip
# What do I mean by do everything in code?  What I mean is that if you go to your data file that you got from some place and then by hand delete some of the data in Google Sheets or Excel, noone will know that you did that.  There is no record of it.  Once you save the file the data will be deleted and noone will know you did this.  Instead if you keep your data as "raw" as possible and modify it using code, your code will document ALL of the steps you did in your analysis including the step of deleting data.  "Excluding" (not DELETEing) data is sometimes justified but the important thing is we want to document all our steps honestly and truthfully when doing analysis.  Using code to do every single step of an analysis helps us accomplish this.
# ``` 

# ### Deleting rows

# To delete a row you can use the `.drop()` method to drop a particular item using its index value.  The `.drop()` method is not an "in place operation" instead it returns a new dataframe with the particular rows removed.
# 
# 
# ```{admonition} **"In place" operations**
# :class: tip
# From time to time using pandas you will here about a method being described as "in place" or "not in place."  In place means that the change you are making to the dataframe is made to the dataframe variable you describe.  So for instance if you have a dataframe stored in a variable named `df` and you call `df.drop([1])` it will drop the row corresponding to the index value 1.  However, if you look at `df` again using, for instance, `df.head()` you will see that it will not have changed.  To save the changes with a "not in place" operation you need to store the results in a new variable.  For insteance `df2 = df.drop([1])` will make a copy of `df`, drop the row corresponding to index 1 and then store the result in `df2`.  If drop was an "in place" operation it would have actually modified `df` and so you wouldn't need to store the result in a new variable.
# ```

# Here is how to use it.  Suppose we have the salary dataframe from above:

# In[22]:


df.head()


# If we want to delete the first we can drop it using the index it has, in this case 0:

# In[23]:


df2=df.drop([0])
df2.head()


# Notice how I "saved" the modified dataframe into a new variable called `df2` using the equals sign.  Then if we call the `.head()` method on `df2` we can see that the first row has been removed.  `df`, the original dataframe variable, remains unchanged.
# 
# You can also remove multiple rows by their index value at once:

# In[25]:


df.drop([0,2,4,6]).head()


# Here I dropped the rows with index 0,2,4,6, and also show an example of **chaining** dataframe methods.  
# 
# 
# ```{admonition} **Chaining methods**
# :class: tip
# Dataframes in pandas a what is known as an object-oriented structure.  This means that most the functionality of a dataframe is tied to the variables themselves.  That is why in the previous examples we called `df.method()` like `df.drop()` instead of `pd.drop()` (calling from the base pandas library). Given this, most pandas methods either return themselves or a copy of the dataframe that has been altered.  Thus you can "chain" operations and methods together to make the code more concise.  Chaining means calling multiple methods in a row on a single line of code.  `df.drop([0,2,4,6]).head()` calls the `drop()` method on the dataframe and then called the `head()` method on the resulting modified data frame.  This means you don't have to store every intermediate step of your data manipulation into a new variable. 
# ```
# 
# 

# ### Deleting columns

# To delete a column instead of a row you can also use the `.drop()` method, using an additional argument that refers to the "axis" you are dropping from.

# In[26]:


df.head()


# Here are a couple examples of dropping one or more columns by name.  Note that the case of the column name must match and also you need to specific `axis=1` to refer to dropping columns instead of rows.

# In[27]:


df.drop('years',axis=1).head()


# In[14]:


df.drop(['years','age'],axis=1).head()


# ### Adding rows

# Using pandas it is best to resist the urge to add rows one at a time to a dataframe.  For various reasons is this not the ideal way to use pandas [^columnbased].  Instead you can combine the rows of two different dataframes into one.  This might be useful in psychology for instance if each participant in your experiment had their own data file and you want to read each file into a dataframe and them combine them together to make one "uber" dataframe with all the data from your experiment.
# 
# [^columnbased]: Internally, pandas is primarily organized using columns.  This just means that the computer code underneath pandas likes adding columns and hates adding new rows one at a time.  It is just a thing.  Thus, adding one row at a time is very inefficient.  As a result it is usually best to get all your rows set and then create the dataframe.

# Here's two simple dataframes and we can combine them:

# In[30]:


df1 = pd.DataFrame({"age": [10,27,45,23,21], "salary": [0,23000,100000,35000,60000]})
df2 = pd.DataFrame({"age": [60,70,53,56,80], "salary": [50000,23000,60000,135000,0]})

df_combined = pd.concat([df1,df2])

df_combined


# This only works because they have the same columns.  If they have different columns then the missing entries of either are filled in with `NaN` which is the code for "missing values" in pandas.  

# In[31]:


df1 = pd.DataFrame({"age": [10,27,45,23,21], "salary": [0,23000,100000,35000,60000]})
df2 = pd.DataFrame({"age": [60,70,53,56,80], "height": [5.2,6.0,5.7,3.4,4.6]})

df_combined = pd.concat([df1,df2])

df_combined


# We will talk about dealing with "missing" values shortly but basically missing values in pandas allows for incomplete rows: you might have have information about every single field of a row and so you can uses `NaN` (stands for Not-a-number in computer speak) to represent missing values.

# ### Adding columns

# As we have considered adding rows, now let's consider adding columns.  This is actually pretty easy.  You just assign some values to a new columns name.  First we will create a data frame with two random columns:

# In[32]:


df = pd.DataFrame({"col_1": np.random.rand(10), "col_2": np.random.rand(10)})
df


# Now we simply assign a new column `df[\'sum\']` and define it to be the sum of two columns.

# In[33]:


df['sum'] = df['col_1']+df['col_2']
df


# You can also define new columns to be a constant value:

# In[27]:


df['constant'] = 2
df


# There are of course some limitations and technicalities here but for the most part you just name a new column and define it as above.

# ### Deleting rows with missing data

# Since we are talking about adding and removing rows and columns it can also make sense to discuss removing rows with missing data.   You might want to for example drop any trial from an experiment where a subject didn't give a response before a timer deadline.  In this case the column coding what the response was might be "empty" or "missing" and you would want to use the `NaN` value to indicate it was missing.  To totally delete rows with any missing value use the `dropna()` function:

# In[34]:


df = pd.DataFrame({"age": [10,27,45,23,21], "salary": [0,23000,None,35000,60000]})
df


# As you can see the salary value is missing for row with index 2 (age 45).  To drop any row with a missing value:

# In[35]:


df.dropna()


# There are several other tricks for dropping missing data besides this.  For example, you can delete rows with only a specific column value missing, etc...  However for now this should work for us.

# ### Getting individual values and changing them

# Sometimes you want to just extract a single value or row from a dataframe or change a single value.  The `.iat` method lets you pull out a single value from the data frame given the position of the index and column.  The `.iat` method is one of the very weird parts of Pandas which has no real good explanation.  Instead of the parentheses used to call normal methods, `.iat` and a few others use square brackets.  One way to think about it is that `.iat` is like looking something up in a normal Python array but it also seems like a method attached to the dataframe.

# In[37]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
df


# This gets the value at row 0 column 0 which is the salary of the first person in the data frame.

# In[38]:


df.iat[0,0]


# This gets the age of the person in the sixth row, fourth column.

# In[39]:


df.iat[6,4]


# A slighly more reader-friendly option is to use `.at[]` which is a method that lets you look things up using the names of columns.

# In[40]:


df.at[10, 'age']


# You can also use this to **change** the value of a particular cell.

# First we see that the person in the first row has age 64.

# In[63]:


df.head()


# Using `.at[]` we set it to 100.

# In[41]:


df.at[0,'age']=100


# Then when we look at the result the age has been changed in the dataframe `df`.

# In[42]:


df.head()


# The way to remember this is that methods that look things up use square brackets.  And if the method begins with an i (like `.iat[]`) it will look it up by integer index (i.e., the number of the column or row).  Otherwise `.at[]` looks up by row (or a named index) and column name.
# 

# ### Checking the size/dimensions of your data

# One common thing you need to do is to verify the number of rows and columns in your dataframe.  The `.shape` property can help with that.

# In[43]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
df.shape


# This tells us that the dataframe contained in variable `df` has 77 rows and 6 columns.  This is often helpful when you first read in a dataset to verify it has all the data you expected to be there!

# ```{admonition} **Methods versus properties**
# :class: tip
# The `.shape` property doesn't include a final `()` unlike other methods we have learned about like `.drop()` which required parentheses.  This reflects that size is known as a property of the dataframe while `.drop()` is a method.  The conceptual differences can be confusing for why one is one way or the other.  However, it is helpful to often think about them as the distinction between nouns and verbs in langauge.  Properties (nouns) are static descriptors of a dataset such as the size of the dataset or the column names.  In contrast, methods (verbs) are things that require computation or modification of the dataframe like deleting things or performing computations on columns or rows.
# ```

# Ultimately the step we just covered recreate much of what you do with the graphical user interface in Excel (change cell values, add/delete rows and columns, etc...).  The real power of Pandas comes from more complex things you can do with dataframes.  That is what we will explore in the next section.

# ## Things you can do with dataframes

# The main goal of getting your data into a dataframe is that enables several methods for manipulating your data in powerful ways.

# ### Sorting

# Often times it can help us understand a dataset better if we can sort the rows of the dataset according to the values in one or more columns.  For instance in the salary data set we have been considering it is hard to know who is the highest and lowest paid faculty.  One approach would to be sort the values.

# In[44]:


df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/salary.csv')
df.head()


# We can sort this dataset in ascending order with:

# In[45]:


df.sort_values('salary')


# Now we can easily see from this output at 44,687 is the lowest salary and 112,800 is the highest.  `sort_values()` is **not** an inplace operation so the original dataframe is still unsorted and we have to store the sorted result in a new dataframe variable if we want to keep working with it.

# In[46]:


df.head()  # still unsorted


# We can sort the other way by adding an additional parameter:

# In[47]:


df.sort_values('salary',ascending=False)


# And if you sort by two columns it will do them in order (so the first listed column is sorted first then the second):

# In[48]:


df.sort_values(['salary','age'])


# In this data set it is mostly the same to sort by salary first then age because most people don't have the same salary so that already provides an order.  However if we do it the other way, i.e., age first then salary, it will order by people age and then for the people who are the same age sort by salary.

# In[49]:


df.sort_values(['age','salary'])


# As you can see in this shortened output there are several people who are 32 in the database and their salaries are ordered from smallest to biggest.
# 
# Sorting is easy to do in Pandas but also easy to do in Excel because there is a "sort" tool in such programs.

# ### Arithmetic

# Perhaps one of the most useful features of dataframes (and spreadsheets) is the ability to create formulas that compute new values based on the rows and columns.  For instance if you had a dataframe that had rows for students and each column was the grade on an assignment a common operation might be to compute the average grade as a new column.  Let's take a look at a simple example of this and then discuss arithmetic operations in Pandas more generally.

# In[50]:


grades_df = pd.DataFrame({'student':['001','002','003'], 'assignment1': [90, 80, 70], 'assignment2': [82,84,96], 'assignment3': [89,75,89]})
grades_df


# This is not necessarily the easier way to **enter** this data (you might prefer to use a spreadsheet for that), but you could read in a csv to load the grades for instance.  Next you would want to create the average grade for each student.

# In[51]:


grades_df['average']=(grades_df['assignment1']+grades_df['assignment2']+grades_df['assignment3'])/3
grades_df


# So you can see here we added up the column for assignment 1, 2, and 3 and then divided by three.  Then we assigned that resulting value to a new column called average.  You might wonder how did Pandas know to do this for all three students?  The answer is the power of **broadcasting** a feature of many programming languages that automatically detects when you are doing arithmetic operations on collections of numbers and then does that operation for **each entry** rather than like the first one.

# We can also broadcast the addition of constant values to a column.  For instance to give all the students a five point bonus we could do this"

# In[52]:


grades_df['average']=grades_df['average']+5
grades_df


# Again, here it added 5 to *each entry* of the grades column rather than just one or the first row.

# Basically any math function can be composed of the columns.  You might also be interested in functions you could compute down the columns rather than across them, however we will consider those in more detail in the later chapter on [](../../chapters/07/00-describingdata).

# ### Slicing

# A very useful and common feature for manipulating data is slicing.  Slicing refers to selecting out subsets of a dataset for further analysis.  For example we might want to plot only the salaries of the women in this data set.  To do this we want to "slice" out a subset of the data and analyze that further.  We saw slicing before in a previous chapter on Python programming with strings and lists where you can "slice" pieces of a collection out.  Pandas takes this several steps further making it more functional for data composed of multiple rows and columns.

# If you remember we can slice a piece of a list by specifying the starting element and the ending element and including the `:` operator to indicate that we want the values "in between":

# In[53]:


a_list = ['a','b','c','d','e','f','g']
a_list[1:4]


# We can do the same thing using the `.iloc[]` method on a data frame.  However since a Pandas dataframe is two dimensional we can specify two slide ranges one for the rows and one for the columns. `iloc[]` is simialr to `iat[]` we say above in that it is used via square brackets (because it is a lookup indexing operation) and the `i` part refer to that we are providing the integer location of the rows and columns (i.e., using numbers to say which row and columns we want).

# In[54]:


df.iloc[2:4,0:3]


# That example takes row 2 and 3 and columns 0,1,2 (remember Python is zero indexed so the first row or column is numbered zero).

# We can also slice using column names using just `loc[]`:

# In[55]:


df.loc[1:2,"gender":]


# Similar to `.iat[]` and `.at[]`, `iloc[]` uses integer lookup and `loc[]` uses index names.  You might wonder why I still used numbers for the rows in the above.  This is because this dataframe still has an **index** for the rows which is integer based.  However, indexes are an important part of Dataframes.

# ### Selecting

# Related to slicing is "selecting" which is grabbing subsets of a dataframe's rows based on the **values** of some of the rows.  This is different than slicing which takes little chunks out of a larger dataframe using indexes or column names.  Here we are interested in selecting rows that meet a particular criterion.  For instance in the professor salary dataset we read in we might want to select only the rows that represent women in the dataset.  Let's look at an example of how to do that and then discuss the principle.

# First we need to discuss the concept of logical operations which are broadcast along the columns.  For instance if we write something like

# In[117]:


df['age']>50


# We get a column of `True`/`False` values (also known as Boolean values since they take on two values) which reflect a test for each row if the age value is greater than 50.  If it is, then `True` is entered into the new column and if it isn't then `False` is entered in.
# 
# We can write more complex logical operations as well.  For instance:

# In[56]:


(df['age']>50) & (df['age']<70)


# This expression does a logical `and` due to the `&` symbol and will be true if the age is greater than 50 AND less than 70.

# The examples so far used a single row but we can also make combination using multiple columns.  For instance we could select all the rows corresponding to professors that are male and under 50.

# In[57]:


(df['age']<50) & (df['gender']==1)


# If you want to make an "or" you use the '|' (pipe) character instead of the '&'.
# 
# Now that we have this boolean column we can use it to select subsets of the original dataframe:

# In[123]:


df[df['age']<35]


# The previous line selects all the professors under 35.  Notice the syntax here as it is kind of sensible.  On the outer part we have `df[]` and in the middle of the bracket we provide the logical column/series as we just discussed.  You can break them into two steps if you like:

# In[58]:


under35=df['age']<35
df[under35]


# This makes clear that we define the "rule" for what things are true and false in this column (`under35`) and then use it to select rows from the original dataframe.
# 
# You use this a lot in data analysis because often a data file from a single subject in an experiment has trials you want to skip or analyze, or you might use it to select trials from particular subjects, or trials that meet a certain requirement (E.g., if a reaction time was too long or something).  Thus it is important to bookmark this concept and we will return to it several times throughout the semester.

# An event simpler synatx for this is provided by the `.query()` method on Pandas data frames.  For example, using this command this is how you would select all the professors under age 35 in the the salary dataset:

# In[4]:


df.query('age<35')


# This is nice because it does the same thing as the above without all the extra brackets which sometimes contribute to typos.  Here is a slightly more complex version using the logical and operator:

# In[5]:


df.query("age<35 & departm=='chem'")


# In[6]:


df.query("age<35 & departm=='chem' & publications == 12")


# So nice!

# ### Iteration

# Iteration refers to stepping through either the rows of the columns of your dataframe one by one and doing some thing with each row or column.  We have encountered iteration before when we learned about Python for loops.  If you remember, the typical for loop we had we iterated over a list.  For example this code iterates down a list of values and prints each one.

# In[45]:


for i in range(10):
    print(i)


# We can iterate over both rows and columns of a dataframe since the format is two dimensional.  This prints out the titles of each column.

# In[47]:


for column in df:
    print(column)


# The above method only gets you the individual column name.  To get the data within each column, you use a special methods called `.iteritems()`.  For example:

# In[52]:


for columnname, columndata in df.iteritems():
    print(columnname)
    print('---')
    print(columndata)


# Finally, if you want to step through row-by-row use the `.iterrows()` method.

# In[5]:


for row in df.iterrows():
    print(row)


# A [substantially faster version](https://medium.com/@formigone/stop-using-df-iterrows-2fbc2931b60e) of `.iterrows()` is `.itertuples()` which returns a slightly different representation of each row:

# In[7]:


for row in df.itertuples():
    print(row)


# ## Data organization - tidy and wide formats

# Now that you have seen how to import your data and the basic operations of dataframe, you might think that you're now ready to start analyzing and visualizing your data—yet there's still quite a bit of work that has to be done cleaning up your dataset before you do this. Some of this clean up might include fixing typos in your datasets, or filtering out participants with incomplete data. But even more important, you'll need to make sure that your data is organized and structured in a consistent manner. One way of organizing your data, referred to as **tidy format** (<a href="https://vita.had.co.nz/papers/tidy-data.pdf">a term coined by Hadley Wickham</a>), is particularly helpful for facilitating data analysis. 
# 
# To clarify what tidy format is, we will also talk about another common format of data called **wide format** that isn't very tidy. While there are some reasons to use wide format over tidy format when programming (e.g., some functions in R require data to be in wide format), wide format is more commonly used when working with interface-based software (such as Excel and SPSS).
# 
# The clearest way of demonstrating the differences between wide versus tidy formats is by simply looking at datasets of both kinds. Take the example dataset below. It shows quiz scores for four participants across three timepoints plus some demographic data. It's currently in wide format:  

# In[60]:


import pandas as pd 

data = [['tom', 26, "m", 12, 15, 15], 
        ['nick', 23, "m", 10, 9, 12], 
        ['julie', 18, "f", 15, 13, 14], 
        ['angela', 21, "f", 10, 10, 12]] 
df_wide = pd.DataFrame(data, columns = ['name', 'age', 'gender', 'time1', 'time2', 'time3']) 
df_wide 


# In wide format, each *individual* has their own row, and all data pertaining to that individual is contained within that row. For example, the first row has all of the data for Tom, including his scores across each of the three timepoints. 
# 
# Now let's compare this to tidy format:

# In[61]:


df_tidy = pd.melt(df_wide, id_vars=['name', 'age', 'gender'], var_name='timepoint', value_name='score') 
df_tidy = df_tidy.sort_values(ascending=False, by='name')
df_tidy


# In this format, now each *observation* has their own row. That is, we now have three separate rows for Tom, with each row reflecting a single quiz score from one of the three timepoints. 

# ### What is tidy data, and why use it? 

# Pulling directly from <a href="https://r4ds.had.co.nz/tidy-data.html">Wickham's book chapter on tidy data</a> (his book is written for R users, but the principles of tidying data works the same across languages), there are three rules that work together to make a dataset tidy ({cite}`Wickham:2017`): 
# 
# 1. Each _observation_ must have its own row (observations could be _each person_, _each timepoint_, etc.)
# 2. Each _variable_ must have its own column (variables are some kind of measurement: _gender_, _age_, _score_, etc.)
# 3. Each _value_ must have its own cell (value are the actual measurement: _female_, _23 years_, _12 points_, etc.)
# 
# <div style="text-align: center">
#     <img src="./images/tidy_data.png" width="600">
# </div>
# Above, a visual representation of each of the three rules for tidy data: variables are in columns, observations are in rows, and values are in cells. Image borrowed from <a href="https://r4ds.had.co.nz/tidy-data.html"><i>R for Data Science</i></a>.
# 
# So going back to our dataset from before, we can see that it follows each of these three rules. Each person and each timepoint has their own rows (Rule 1). Every type of data measured (gender, age, etc.) has their own column (Rule 2), and each cell within the dataframe has only one value (Rule 3).
# 
# Let's look at some examples where one or more of these rules are being violated. 

# In[12]:


data_untidy = [['tom', "26_m", 12, 15, 15], 
              ['nick', "23_m", 10, 9, 12], 
              ['julie', "18_f", 15, 13, 14], 
              ['angela', "21_f", 10, 10, 12]] 
df_untidy = pd.DataFrame(data_untidy, columns = ['name', 'age_gender', 'time1', 'time2', 'time3'])
df_untidy


# In the example above, this dataset is messy because two variables (age and gender) have been coded into the same column. Having multiple variables in the same column in this way makes it much harder to calculate the average age of participants or get a gender breakdown for the sample.  
# 
# But this can easily be fixed by splitting the column into two. 

# In[18]:


df_untidy[['age', 'gender']] = df_untidy.age_gender.str.split("_", expand=True)
del df_untidy['age_gender']

df_untidy


# Here's another case of untidy data, similar to one we've seen before. 

# In[59]:


data_messy = [['tom', 26, 12, 15, 15, 17, 18, 20], 
              ['nick', 23, 10, 19, 12, 14, 11, 18], 
              ['julie', 18, 15, 23, 14, 18, 12, 19], 
              ['angela', 21, 10, 11, 12, 14, 15, 30]] 
df_messy = pd.DataFrame(data_messy, columns = ['name', 'age', 't1_min', 't1_max', 't2_min', 't2_max', 't3_min', 't3_max'])
df_messy


# This dataset violates the rules of a tidy dataset because a) there's more than one observation in each row, and b) we have multiple columns reflecting the same variable (the distinction between a minimum and maximum score). 
# 
# But we can fix it using `pd.melt` with a combination of few other things. In this tidied version, we now see that each variable (_name_, _age_, _time_, _min_ score, and _max_ score) all have their own columns. 

# In[80]:


df_messy = pd.melt(df_messy, id_vars=['name', 'age'], var_name='time_minmax', value_name='score')

df_messy[['time','minmax']] = df_messy.time_minmax.str.split("_", expand = True)
del df_messy['time_minmax']

df_messy = df_messy.pivot_table(index=['name','age','time'], columns='minmax', values='score')
df_messy.reset_index(drop=False, inplace=True)
df_messy


# Don't worry if the actual code to make the data tidy doesn't make sense right away (you will get there). We'll talk more later about strategies you can use to wrangle data into tidy formats using Python. What you should be taking away from these examples is the differences in how these datasets are structured both before and after we tidied them. 
# 
# Cleaning up and rearranging datasets is inevitable part of doing psychological research. Lots of data you work with may come to you in untidy formats, and you will have to clean that data up before you can analyze it. The good news is that knowing these principles of tidy, organized datasets will serve you well as you to start to design your experiments! **The more you can build in tidy principles into how your data is recorded during the experiment, the more time you can save later when it comes to processing your data in Python.**
# 
# Also importantly, this discussion highlights one major purpose of the Pandas library: namely to help you clean up and reorganize data.  The commands like `pd.melt()` and `pd.pivot_table()` are pretty complex operations which alter your view of a dataset and make it easier to perform certain types of analysis.  These reorganizations of data can be very difficult to do by hand but are facilitated by the dataframe library provided by Pandas.

# ### A case example: organizing data for an psychological experiment

# The discussion so far might strike you as somewhat abstract.  However, principles of data formatting and organization are very important for psychological research.  Let's consider the case most central to this course which is organizing a data file for a psychological experiment conducted on several participants composed of multiple trials and trial types. This is perhaps the most typical type of data format we will encounter in this work and is somewhat different from survey questions and other types of data which has a more complex structure often.

# To keep things simple, let's imagine that we are doing a decision making experiment.  On each trial of the experiment the subject will be offered a choice between a gamble and a sure amount of money.  For instance the subject might be presented with an option like "Would you prefer \$10 now or a 50\% chance to win 20 dollars otherwise nothing."  If you think about it a bit for this specific pair of options they *on average* give the same expected value because the expected value of the uncertain option is $0.5*\$20 + 0.5*0 = \$10.$  If people were perfectly rational they should be indifferent between these two gambles.  However, a common phenomena is that people show a biased called **risk aversion** where they prefer a certain reward over a risky gamble.  Thus, even though on average you get the same, they do not want to take the gamble for the larger amount of money.  There are several explanations of this but one intuitive one is that people don't like regret and the feeling if you get nothing is so bad that makes people prefer the certain \$10.

# So imagine we do an experiment attempting to explore loss aversion.  We might present people with several of these types of gambles across multiple trials.  The reason is that we want more than one measurement and want to vary things like the probability of the higher reward on the risky gamble (e.g., instead of 50% chance we might want to explore 10% chance of winning).  In addition, we might want to change the magnitudes of the rewards across different trials.   Finally we will want to run multiple people so that our conclusions aren't tied to one person.  How should we structure our data file for this?  You might think that we should first write the code for the experiment and then consider the data format.  However, I find it is usually helpful to do the opposite.  We start with the data format in mind right from the start.

# Let's look back at the key idea in a "tidy" dataset because we definitely want to be tidy here.
# 
# 1. Each _observation_ must have its own row (observations could be _each person_, _each timepoint_, etc.)
# 2. Each _variable_ must have its own column (variables are some kind of measurement: _gender_, _age_, _score_, etc.)
# 3. Each _value_ must have its own cell (value are the actual measurement: _female_, _23 years_, _12 points_, etc.)
# 
# So each _observation_ would be a trial and so it needs its own row.
# 
# Each _variable_ would be information about the trial, both the details of what the subject saw on that trial (e.g., the magnitude of the rewards and gambles) and also how they responded (reaction time, what choice they made, etc...).
# 
# Each _value_ must have its own cell means that each of these numbers need to have their own column and not be combined.  So let's make a pretend dataframe from scratch to illustrate this example.  
# 
# So let's imagine that there are 10 stimuli in the experiment.  We can denote them as the value of the certain option and then the value of the high and low reward for the gamble.  This means each stimulus/trial in the experiment can be described with four numbers:
# 
# - certain value
# - upper risky value
# - lower risky value
# - probability of upper risky value
# 
# We can fix a few alternatives (let's say enough for 4 trials) using a python dictionary:

# In[8]:


stim={"certain": [10, 15, 25, 50], 
      "upper_risk": [20, 40, 30, 32], 
      "lower_risk": [0, 23, 29, 0], 
      "prob": [0.5, 0.5, 0.25, 0.75]}


# Next we can pretend to generate some responses from one subject.

# In[10]:


responses = {"reaction_time":[200, 400, 500, 600], 
             "choice": [0, 1, 1, 0]}


# Now we can build up a dataframe for one subject.  We will do this by first defining a python dictionary called `trials` which includes all the _variables_ associated with one measurement  (trial number, the value of the certain gamble, the probabilty, etc...) as well as all the measurements made on that trial (response time, choice).  These start out at the beginning of the cell as empy lists and then a for loop below fills them in.

# In[15]:


subject_id = "some_subject_id0"

trials = {'subject_id':[],
          'trial_num':[],
          'certain':[],
          'upper_risk':[],
          'lower_risk':[],
          'prob':[],
          'reaction_time':[],
          'choice':[]}

for i in range(4):
    trials['subject_id'].append(subject_id)
    trials['trial_num'].append(i)
    trials['certain'].append(stim['certain'][i])
    trials['upper_risk'].append(stim['upper_risk'][i])
    trials['lower_risk'].append(stim['lower_risk'][i])
    trials['prob'].append(stim['prob'][i])
    trials['reaction_time'].append(responses["reaction_time"][i])
    trials['choice'].append(responses["choice"][i])

trials


# The result is a python dictionary that includes column names and then the data that goes in the columns which is perfect for initializing a Pandas dataframe:

# In[17]:


df=pd.DataFrame(trials)
df


# This is great and shows a very natural way to structure the data from an experiment.  Each trial is a row in the dataframe.  Each column either describes what the stimulus was on that trial or the response from the participant.  In addition two columns code the trial number and the subject idea.  This is critical for analysis as we might be interested in order effects on trials and so we need to know which trials were first or last.  In addition we want to keep subjects separate.  Eventually we will build up a more complex dataframe that includes multiple subjects.  For example:

# In[25]:


stim={"certain": [10, 15, 25, 50], 
      "upper_risk": [20, 40, 30, 32], 
      "lower_risk": [0, 23, 29, 0], 
      "prob": [0.5, 0.5, 0.25, 0.75]}

trials = {'subject_id':[],
          'trial_num':[],
          'certain':[],
          'upper_risk':[],
          'lower_risk':[],
          'prob':[],
          'reaction_time':[],
          'choice':[]}

def generate_subject_data(subject_id, trials):
    for i in range(4):
        trials['subject_id'].append(subject_id)
        trials['trial_num'].append(i)
        trials['certain'].append(stim['certain'][i])
        trials['upper_risk'].append(stim['upper_risk'][i])
        trials['lower_risk'].append(stim['lower_risk'][i])
        trials['prob'].append(stim['prob'][i])
        trials['reaction_time'].append(np.random.randint(200,1000))
        trials['choice'].append(np.random.randint(0,2))
        
for subj in ["some_subject_id0","some_subject_id1","some_subject_id2"]:
    generate_subject_data(subj,trials)
    
exp_df=pd.DataFrame(trials)
exp_df


# Ok, take a careful look at this output.  This is a dataframe with 3 subjects worth of data.  The first column is the subject id.  The second is the trial number but notice how it starts at 0 and counts up to 3 and then stops when a new subject id begins.  Next is the stimulus definitions (certain, upper_risk, lower_risk, prob, etc...) and the responses.  This is exactly the way people usually code a data file for a cognitive or perceptual experiment.  It is "tidy" and includes all the information in a handy way we can use to analyze the data later.  Here we **generated** the data with a simple program that I wrote in the cell above but generally we write a more complex program to handle this including showing the stimlus to the subject, recording their reaction time and so forth.  This simple program is a proxy for that more complex program but shows you the important principle of how to **organize** your data in preparation for analysis.  The analysis itself is what we will contemplate over the next several chapters.

# ## The Split-Apply-Combine Workflow

# Perhaps one of the most common data analysis steps is known at the **split-apply-combine** workflow.  Helping with this workflow is one of the more interesting and powerful features of Pandas (and other dataframe) libraries.
# 
# The **split-apply-combine** workflow refers to a very common sequence of data analysis steps that data analysts have to make.  Usually a dataset arrives with multiple sub-units inside it.  For example, we might get a .csv file that has all the trials of an experiment from several subjects.  Often we want to perform analyses that aggregate across these various subject categories.  For example we might want to analyze the performance of each subject.  Or alternatively we might want to analyze the difficulty of each item on the test.
# 
# Both of these analyses require us to **split** the larger dataframe up into pieces and perform and analysis on each of these pieces.  The step where you perform this analysis is called **apply**.  So we break the bigger dataframe up into pieces, apply an analysis to each piece.  The final step is to **combine** the results of those analyses back into a new dataframe structure for further analysis.
# 
# {numref}`split-apply-combine` tries to emphasize these steps:
# 
# 
# ```{figure} ./images/split-apply-combine.png
# :width: 800px
# :name: split-apply-combine
# 
# Illustration of the split-apply-combine workflow!
# ```
# 
# On the left we begin with our original dataframe (`df`) which has two columns.  One column is categorical and takes on values 'A', 'B', or 'C' while the second column is numeric.  The first step of the split-apply-combine workflow is that we might want to split the original dataframe into smaller groups based on the value of one or more of the columns.  For this example it makes sense to break the original dataframe into smaller dataframes called "groups" based on the value of `col1` (that is to say  if the row is in category 'A','B', or 'C').  The method that does this in Pandas is `.groupby` and we will discuss it in a moment.  The result of the groupby operation is a partitioning of the original dataframe into smallers sets (called groups) which are the rows of the original dataframe just reorganized.  The reorganization is such that all the rows that share the same value on the specified column are group together.  For instance in {numref}`split-apply-combine` all the rows that had value 'A' in `col1` are placed into the same group separate from all the rows that had value 'B' in `col1` and so forth.  This is the **split** operation.
# 
# Next there are several things we can do to each of the groups.  We can iterate down them in a for loop for instance (more on that later) but also there are methods that will quickly compute various descriptives statistics to each group, or allow you to "apply" a custom function to each group.  This custom function could be quite complex and so it allows you do do a lot of additional processing of the groups.  The syntax for this tends to be very compact and helps to limit bugs so it is helpful to learn.
# 
# Let's begin by the simple example in {numref}`split-apply-combine`:
# 
# 

# Here is the dataframe:

# In[3]:


sac_df=pd.DataFrame({"col1":['A','B','C','C','B','B','A'],"col2": [1,2,3,4,2,5,3]})
sac_df


# Next we will group the rows by the values in `col1`:

# In[36]:


sac_df.groupby('col1')


# The result here doesn't print out the individual groups but instead returns a `pandas.core.groupby.generic.DataFrameGroupBy` object.  However we can print out the groups using iteration:

# In[40]:


for name, group_df in sac_df.groupby('col1'):
    print(name)
    print('-----')
    print(group_df)
    print()
    print()


# As you can see, the rows have been sorted into groups based on the value in `col1`.  Since there are three distinct/unique values in `col1` there are three groups here but if there were more distinct values there would be more groups.
# 
# Next we compute the sum() which applies the sum to each group.  We can chain these operations in a sequence:

# In[42]:


sac_df.groupby('col1').sum()


# The result here is a new dataframe where the sum of the values of `col2` for the different subgroups 'A','B', 'C' has been computed.
# 
# :::{tip}
# Check the results by hand to make sure you understand what has been calculated here!
# :::

# Ok this example is fairly simple, what if we consider a more complex dataframe with more columns:

# In[4]:


sac_df_2=pd.DataFrame({"col1":['A','B','C','C','B','B','A'],"col2":['A','A','A','B','B','B','B'],"col3": [1,2,3,4,2,5,3],"col4": [1.1,2.3,12.,16,22.21,9,0.5]})
sac_df_2


# If we `.groupby()` column 1 (`col1`) we get the same groups as before but notice they includes all the rows:

# In[52]:


for name, group_df in sac_df_2.groupby('col1'):
    print(name)
    print('-----')
    print(group_df)
    print()
    print()


# And now the apply-combine step computes the sum for all the numeric columns.

# In[55]:


sac_df_2.groupby('col1').sum()


# Of course you don't have to apply the sum to all the columns.  If you just want to analyze `col4` you can select it out before applying the sum:

# In[58]:


sac_df_2.groupby('col1')['col4'].sum()


# You can also group using more than one column as the grouping factors.  For example in `sac_df_2` there are actually two columns that have discrete values and so you might want to make groups that are all combinations of those two factors.  If so you just pass a list of grouping columns to `.groupby()`: 

# In[59]:


for name, group_df in sac_df_2.groupby(['col1','col2']):
    print(name)
    print('-----')
    print(group_df)
    print()
    print()


# Then the sum operation will apply to all combinations.

# In[60]:


sac_df_2.groupby(['col1','col2']).sum()


# The output here looks a little different because the columns are organized hierarchically (the specific terms is that the index is hierarchical).  But we can call `.reset_index()` a function we mentioned earlier to delete the hierarchical index and flatten things back to a standard data frame.

# In[63]:


sac_df_2.groupby(['col1','col2']).sum().reset_index()


# The final result here is itself a dataframe and so can be use for further analysis and plotting.

# ### Changing the "apply" step

# In the example we considered so far we summed the columns within in group.  However there are actually several types of things you can do to groups  in the "apply" step:
#     
# - **Aggregation**: computes a descriptive statistic like a sum, mean, max, min, etc...
# - **Transformation**: perform a group-specific computation like standardsize (z-score) within a group
# - **Filtration**: discard data from small groups or filter data from a group based on the sum or mean in that group (e.g., removing outliers in a group)

# #### Aggregation

# So far we computed the sum of columns within each group.  However there are several other functions you can use.  For example to compute the median instead:

# In[66]:


sac_df_2.groupby('col1').median()


# Here is a list of common aggregation functions:
# 
# 
# 
# ```{list-table} Example aggregation functions
# :header-rows: 1
# :name: aggregation-table
# :width: 200px
# 
# * - Function
#   - Description
# * - `.mean()`
#   - Compute mean of groups
# * - `sum()`
#   - Compute sum of group values
# * - `size()`
#   - Compute group sizes
# * - `count()`
#   - Compute count of group
# * - `std()`
#   - Standard deviation of groups
# * - `var()`
#   - Compute variance of groups
# * - `sem()`
#   - Standard error of the mean of groups
# * - `describe()`
#   - Generates descriptive statistics
# * - `first()`
#   - Compute first of group values
# * - `last()`
#   - Compute last of group values
# * - `nth()`
#   - Take nth value, or a subset if n is a list
# * - `min()`
#   - Compute min of group values
# * - `max()`
#   - Compute max of group values
# ```

# In addition there is a special `.agg()` (or `.aggregate()`) function that you can pass mulitple functions to from other libraries: 

# In[68]:


sac_df.groupby('col1').agg(np.sum)


# The previous example used the numpy `np.sum()` function.  You can also provide multiple functions at once:

# In[72]:


sac_df


# In[75]:


sac_df.groupby('col1').agg([np.sum, np.mean, np.std])


# Which as you can see actually computes mutiple statistics on each group.

# ```{seealso}
# You can read more about aggregation in the Pandos docs on [Aggregation](https://pandas.pydata.org/docs/user_guide/groupby.html#aggregation).
# ```

# #### Transform

# Aggregation methods take in a grouped dataframe and compute a single number of statistics for each group.  In contrast transform applies a function to a column and returns a column of the same size usually.  This allows you to change the data within each sub group.  A common version of this for behavioral science is to z-score data within a group to detect outliers, etc...  Since that is the most common use case we'll focus on that here.

# In[8]:


sac_df_2.groupby('col1').transform(lambda x: (x-x.mean())/x.std())


# The transform function takes as argument a `lambda` function which is a way to write short one-line functions in python.  This function takes 1 argument (`x`) which is the dataframe coresponding to each column of each group.  It then computes the z-score of this data within the group and column and the result is combined into a new dataframe.  This new data frame has the same column names as the original but we might want to rename them:

# In[10]:


transformed_df=sac_df_2.groupby('col1').transform(lambda x: (x-x.mean())/x.std())
transformed_df=transformed_df.rename(columns={'col3':'col3_trans', 'col4': 'col4_trans'})
transformed_df


# To add these transformed columns back into our original data frame as new column we can use the `.join()` function which is like `.concat()` which we leared about earlier but combines the columns from a dataframe rather than appending the rows:

# In[12]:


sac_df_2.join(transformed_df)


# The end result is that we z-scored `col3` and `col4` within the groups implies by `col1`.

# ```{seealso}
# You can read more about aggregation in the Pandos docs on [Transformation](https://pandas.pydata.org/docs/user_guide/groupby.html#transformation).
# ```

# #### Filtration

# With the filtration *apply* step you provide a function that returns true or false for each group.  Any group that the function returns `True` for is kept for the new dataframe and any group that returns `False` is dropped. 
# For example this step removes rows from the dataframe that belong to groups with only one or two members:

# In[17]:


dff = pd.DataFrame({'A': np.arange(8), 'B': list('aabbbbcc')})
dff


# In[18]:


dff.groupby('B').filter(lambda x: len(x) > 2)


# Notice 'a' and 'c' entries have been removed because those groups have only two members each.

# ```{seealso}
# You can read more about aggregation in the Pandos docs on [Filtration](https://pandas.pydata.org/docs/user_guide/groupby.html#filtration).
# ```

# ## Further Reading and Resources
# 
# - 10 minute [intro to pandas](https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html)
# - A longer standalone video [on how to use pandas](https://www.youtube.com/watch?v=vmEHCJofslg)
# - A visual guide to [split-apply-combine](https://towardsdatascience.com/how-to-use-the-split-apply-combine-strategy-in-pandas-groupby-29e0eb44b62e) strategies in Pandas by Towards data science
# - [Split-Apply-combine strategy for data mining](https://medium.com/analytics-vidhya/split-apply-combine-strategy-for-data-mining-4fd6e2a0cc99) includes some additional facts and features of this approach

# ## References
# 
# ```{bibliography} ../../references.bib
# :filter: docname in docnames
# ```
