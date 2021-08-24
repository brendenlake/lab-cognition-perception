#!/usr/bin/env python
# coding: utf-8

# In[6]:


from IPython.core.display import HTML, Markdown, display

import numpy.random as npr
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.formula.api as smf
import pingouin as pg

import ipywidgets as widgets

# Enable plots inside the Jupyter Notebook
get_ipython().run_line_magic('matplotlib', 'inline')


# # Differences between means (review)

# Authored by *Todd Gureckis* with input from *Matt Crump*.

# ## Exercise 1: Bootstrapping the t-distribution

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 1</strong> <br>
#     Create a plot of the sampling distribution of the t statistic for 10,000 random normal samples of size 6 and 500.
# </div>

# In[ ]:


ts=[]
for _ in range(10000): # repeat 10000 times
    r_sample = np.random.normal(0,1,size=XXX) #set size size according to instruction
    sem = np.std(r_sample,ddof=1)/np.sqrt(len(r_sample))
    t_stat = np.mean(r_sample)/sem
    ts.append(t_stat)
    
ts2=[]
for _ in range(10000):
    r_sample = np.random.normal(0,1,size=XXXX) #set size according to instructions
    sem = np.std(r_sample,ddof=1)/np.sqrt(len(r_sample))
    t_stat = np.mean(r_sample)/sem
    ts2.append(t_stat)
    
sns.distplot(ts)
sns.distplot(ts2)


# <div class="alert alert-success" role="alert">
#   <strong>Stop and think</strong> <br>
#     Do these distibutions look identical?  What is different and why?
# </div>

# ## Exercise 2: Relationship between p and t values

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 2</strong> <br>
#     Using the following interactive widget, explore the critical value of t shown for different degrees of freedom (sample sizes) and alpha levels.  Report in a cell below the critical p values for a t-distribution with 9 degrees of freedom and alpha is 0.05, a t-distribution with 50 degrees of freedom and alpha 0.05 and a the critical value of a t-distribution with 25 degrees of freedom and alpha = 0.4.
# </div>

# In[60]:


@widgets.interact(dof=widgets.IntSlider(min=1, max=53, step=1, value=10), alpha=widgets.FloatSlider(min=0,max=0.5, step=0.01, value=0.2))
def plot_t_onsided(dof, alpha):
    fix, ax = plt.subplots(1,1,figsize=(10,6))

    x=np.linspace(-3.5,3.5,100)
    y=stats.t.pdf(x,df=dof)
    t_crit=stats.t.ppf(1.0-alpha, df=dof)
    print(t_crit)
    ax.plot(x,y)
    ax.set_ylabel("probability")
    ax.set_xlabel("value of t statistic")
    ax.set_title("One Sided Test")
    ax.fill_between(x,y,where=x>t_crit,interpolate=True,facecolor='lightblue',alpha=0.2,hatch='/',edgecolor='b')
    ax.set_xticks([0, t_crit])
    #ax.set_yticklabels([])


    sns.despine(top=True, right=True, left=True)

    plt.show()


# <div class="alert alert-success" role="alert">
#   <strong>Stop and think</strong> <br>
#     How does the critical p-value change based on sample size?
# </div>

# ## Exercise 3: Computing a one sample t-test by hand

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 3</strong> <br>
#     The following cell defines a small dataset as a numpy array.  Compute the t-value for this array under the null hypothesis that the true mean is 0.25.  You will find the functions np.mean(), np.std(), and np.sqrt() useful.  Print the t-value out in a cell by itself.  Then use the stats.t.cdf() function to compute the p-value associated with that t using a one sided test. 
# </div>

# In[66]:


scores=np.array([.5,.56,.76,.8,.9])  # here is your data
# compute the "effect" (i.e., difference between the mean of the values and the null hypothesis)
# compute the error (i.e., the standard error of the mean)
# Pay attention to the degrees of freedom!!
# compute the t-value
# use stats.t.cdf() to compute the area in the dail of the correct t-distribution for a one sided test.


# <div class="alert alert-success" role="alert">
#   <strong>Stop and think</strong> <br>
#     If you have trouble try Googling these functions to find information about the arguments!
# </div>

# ## Exercise 4: Using `pingouin` to do a on sample `ttest()`

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 4</strong> <br>
#     The following cell shows how to do a one sample t-test from a numpy array.  Repeat this for the null hypothesis of 0.25, 0.5, and 0.75.  All tests should be one-sided.  Write one sentence below each t-test to describe how you would report the test in a paper.
# </div>

# In[68]:


import pingouin as pg
scores=np.array([.5,.56,.76,.8,.9])
pg.ttest(x=scores, y=0.25, tail='one-sided')


# ## Exercise 5: Melting data

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 5</strong> <br>
#     The cell below sets up a simple pandas dataframe like the one in my slides.  Is this data frame tidy or wide? 
# </div>

# In[71]:


exp_df = pd.DataFrame({"subjects": [1,2,3,4,5], "level_A": [1,4,3,6,5], "level_B": [4,8,7,9,10]})
exp_df


# <div class="alert alert-info" role="alert">
# The pandas `melt()` function convert from a wide representation to the tidy representation.   Try playing with different settings of the id_vars, var_name, and value_name. 
# </div>

# In[79]:


tidy_exp_df=exp_df.melt(id_vars='subjects', var_name='level', value_name='test_value')
tidy_exp_df


# <div class="alert alert-info" role="alert">
# The pandas `pivot()` function convert from a tidy representation to the wide representation.   Try playing with different settings of the index, columns, and values to see what they do. 
# </div>

# In[84]:


tidy_exp_df.pivot(index='subjects',columns='level', values='test_value').reset_index()


# <div class="alert alert-info" role="alert">
#     Using the tidy format add a new column to the dataframe called 'differences' that is the difference between level B and level A for each subject.  Show this new dataframe below.
# </div>

# <div class="alert alert-info" role="alert">
#     Follow along with the steps in the lecture to compute the paired t-test.
# </div>

# ## Exercise 6: Paired t-test example

# ### STUDY DESCRIPTION
# 
# Parents often sing to their children and, even as infants, children listen to and look at their parents while they are singing. Research by Mehr, Song, and Spelke (2016) sought to explore the psychological function that music has for parents and infants, by examining the hypothesis that particular melodies convey important social information to infants. Specifically, melodies convey information about social affiliation.
# 
# The authors argue that melodies are shared within social groups. Whereas children growing up in one culture may be exposed to certain songs as infants (e.g., “Rock-a-bye Baby”), children growing up in other cultures (or even other groups within a culture) may be exposed to different songs. Thus, when a novel person (someone who the infant has never seen before) sings a familiar song, it may signal to the infant that this new person is a member of their social group.
# 
# To test this hypothesis, the researchers recruited 32 infants and their parents to complete an experiment. During their first visit to the lab, the parents were taught a new lullaby (one that neither they nor their infants had heard before). The experimenters asked the parents to sing the new lullaby to their child every day for the next 1-2 weeks.
# 
# Following this 1-2 week exposure period, the parents and their infant returned to the lab to complete the experimental portion of the study. Infants were first shown a screen with side-by-side videos of two unfamiliar people, each of whom were silently smiling and looking at the infant.The researchers recorded the looking behavior (or gaze) of the infants during this ‘baseline’ phase. Next, one by one, the two unfamiliar people on the screen sang either the lullaby that the parents learned or a different lullaby (that had the same lyrics and rhythm, but a different melody).  Finally, the infants saw the same silent video used at baseline, and the researchers again recorded the looking behavior of the infants during this ‘test’ phase.For more details on the experiment’s methods, please refer to Mehr et al. (2016) Experiment 1.

# The first thing to do is download the .csv formatted data file, using the link above, or just click [here](http://gureckislab.org/courses/fall19/labincp/data/MehrSongSpelke2016.csv). 

# In[112]:


# get the baby data frame
baby_df = pd.read_csv('http://gureckislab.org/courses/fall19/labincp/data/MehrSongSpelke2016.csv')
# filter to only have the data from experiment 1
experiment_one_df = baby_df[baby_df['exp1']==1]
experiment_one_df.head()


# ### Baseline phase: Conduct a one sample t-test
# 
# You first want to show that infants' looking behavior did not differ from chance during the baseline trial. The baseline trial was 16 seconds long. During the baseline, infants watched a video of two unfamiliar people, one of the left and one on the right. There was no sound during the baseline. Both of the actors in the video smiled directly at the infant.
# 
# The important question was to determine whether the infant looked more or less to either person. If they showed no preference, the infant should look at both people about 50% of the time. How could we determine whether the infant looked at both people about 50% of the time?
# 
# The `experiment_one_df` data frame has a column called `Baseline_Proportion_Gaze_to_Singer`. All of these values show how the proportion of time that the infant looked to the person who would later sing the familiar song to them. If the average of these proportion is .5 across the infants, then we would have some evidence that the infants were not biased at the beginning of the experiment. However, if the infants on average had a bias toward the singer, then the average proportion of the looking time should be different than .5.
# 
# Using a one-sample t-test, we can test the hypothesis that our sample mean for the `Baseline_Proportion_Gaze_to_Singer` was not different from .5.
# 

# <div class="alert alert-info" role="alert">
#   <strong>Exercise 6</strong> <br>
#     The cell below shows how to get the looking time proportions from the baseline phase.  Conduct a one-sample t-test using pinguoin to see if this data is different than a null hypothesis of 0.5 (no preference).</div>

# In[113]:


# here is how to get the column
experiment_one_df['Baseline_Proportion_Gaze_to_Singer']


# Remember how the experiment went. Infants watched silent video recordings of two women (Baseline). Then each person sung a song, one was familiar to the infant (their parents sung the song to them many times), and one was unfamiliar (singing phase). After the singing phase, the infants watched the silent video of the two singers again (test phase). The critical question was whether the infants would look more to the person who sung the familiar song compared to the person who sun the unfamiliar song. If the infants did this, they should look more than 50% of the time to the singer who sang the familiar song. We have the data, we can do another one sample t-test to find out.

# <div class="alert alert-info" role="alert">
#     The cell below shows how to get the looking time proportions from the test phase.  First conduct a one sample t-test on this test data compared to a null hypothesis of 0.5.  What do you find?  Finally, conduct a paired t-test between the baseline and test phase using pinguoin to see if this data is different than a null hypothesis of 0.0 (no difference).
# </div>

# In[116]:


# here is how to get the column
experiment_one_df['Test_Proportion_Gaze_to_Singer']


# <div class="alert alert-info" role="alert">
# Alright. What did we find? You should take a stab at writing down what we found. You can use the same kind of language that I used from the first one sample-test. You should state the mean proportion, the t-value, the dfs, and the p-value. You should be able to answer the question, did the infants look longer at the singer who sang the familiar song? And, did they look longer than would be consist with chance at 50%.
#     </div>
