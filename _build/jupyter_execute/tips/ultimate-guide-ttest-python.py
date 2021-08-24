#!/usr/bin/env python
# coding: utf-8

# # The Ultimate (Concise) Guide to t-test type things in Python

# ```{note}
# This chapter authored by [Todd M. Gureckis](http://gureckislab.org/~gureckis) and is released under the [license for this book](../../LICENSE).
# ```

# So you have a dataset with two groups in it.  Might be and "experimental" group and a "control" group, or "treatment 1" versus "treatment 2" and you want to know if they are different.  First you have to define different.  Obviously if this is real data unlike that both groups have the exact same values in them.  Often you are interested in if the mean of the two groups is different.  
# 
# The statistical test most often used to do this is a "Students t-test".  This notebook does not bother too much with explaining the theory behind t-tests, particularly in the traditional form.  Instead this is a guide to like "how do I do this in python?".  Other chapters of this course/book go into more of the theory.  It starts off with the most common situations for standard "null hypothesis significance testing" t-tests.  It ends with an example of an approach to replace the student t-test with the BEST test (Bayesian Estimation Supercedes the T-test) which is a fully Bayesian approach to comparing two groups published by Kruschke (2013).  It mostly shows the code and libraries you need, how you typically report in a paper, and also checks to make sure you ran the right test.

# ### Import some libraries

# First we need to load the relevant libraries.  These libraries don't _all_ need to be loaded depending on what you are doing but this will generally work.  See the end of this notebook for information about the versions of the packages used here.

# In[6]:


# basic datascience/data manipulation libraries
import numpy as np
import pandas as pd
import numpy.random as npr
import scipy.stats as stats

# graphs
import seaborn as sns
import matplotlib.pyplot as plt

# formulat interface to statsmodels (standard linear models)
import statsmodels.formula.api as smf

# easy-to-use traditional psychological stats (t-test, anova)
import pingouin as pg

# hate these things
import warnings
warnings.filterwarnings("ignore")


# ## Define some data

# For this example we'll consider several datasets.

# In[9]:


drug = np.array([101,100,102,104,102,97,105,105,98,101,100,123,105,103,100,95,102,106,
        109,102,82,102,100,102,102,101,102,102,103,103,97,97,103,101,97,104,
        96,103,124,101,101,100,101,101,104,100,101])
placebo = np.array([99,101,100,101,102,100,97,101,104,101,102,102,100,105,88,101,100,
           104,100,100,100,101,102,103,97,101,101,100,101,99,101,100,100,
           101,100,99,101,100,102,99,100,99])


# packing the data into a tidy dataframe can be nice
exp_df = pd.DataFrame(dict(group=[0]*len(drug)+[1]*len(placebo), score=np.r_[drug,placebo]))

exp_df.head()


# ## Two-group independent samples t-test (Student test)

# Is the mean of the drug group different than the mean of the placebo group?

# In[18]:


print("Mean of drug group:", drug.mean())
print("Mean of placebo group:", placebo.mean())
print("The difference in means is: ", drug.mean()-placebo.mean())


# The look close but not identical.  However, "look" isn't enough.
# 
# Lets begin with a two-sample, independent samples t-test.  We will assume that both groups have equal variance here.

# In[17]:


pg.ttest(x=drug, y=placebo,paired=False, tail='two-sided', correction=False)


# We specified group `x` as `drug` and `y` as `placebo` (arbitrarily, you could flip that).  We used 'two-sided' which is the traditionally more conservative test which you use unless you have a strong a-priori belief one group is going to have a higher mean value.  We did not apply a correction known as the Welch-Satterthwaite correction for unequal variances.  We will try that later.

# The results show that the t-value for the mean difference is 1.599.  The test has 87 degrees of freedom.  The p-value is 0.122699 which is greater than the traditional "alpha" cut off at p=0.05.  Therefore this test is not significant.  The 95% confidence interval for the differences between the means is -0.43 on the low end to 3.54 with (1.5577 the center).  The effect size (Cohen's d) is 0.331.  The Bayes Factor in favor of the alternative hypothesis (that the means are difference) is lower than one (0.642).  The post-hoc power of the test is 0.338. 
# 
# All of this is consistent with there being basically no differences between these two groups.

# ```{admonition} Example way to report this in a paper
# :class: tip
# We conducted an independent sample t-test comparing the mean score in the drug and placebo group which failed to detect a  significant difference ($t(87)=1.56, p=0.12, d=0.331$).
# ```

# ## Two Group Independent Samples unequal variance (Welch test)

# The assumption in the previous example was that the standard deviation of the data in the two groups was identical.  This assumption may be inappropriate.  To do a test where this is relaxed is not longer technically a t-test but a Welch test.   All we do is test correction to `True`:

# In[21]:


pg.ttest(x=drug, y=placebo,paired=False, tail='two-sided', correction=True)


# ```{admonition} Example way to report this in a paper
# :class: tip
# We conducted an independent sample Welch test comparing the mean score in the drug and placebo group which failed to detect a  significant difference ($t(63.04)=1.622, p=0.11, d=0.331$).
# ```

# There can be some strong arguments that this should be the preferred indendent sample t-test because the assumption of equal variance is unlikely to be met.

# ## Paired samples t-test

# In the previous example the two groups were necessarily measuring different individuals (placebo versus a drug study).  However sometimes we measure the same person twice (pre-test, post-test) for instance.  In that case we use the "paired" samples t-test because there is a natural link between individual numbers in both groups (usually a person or some other unit of measurement).
# 
# To perform this test we are going to create slightly different data set but you could copy-paste numbers into the `test_1` and `test_2` arrays as in the example above.

# In[29]:


test_1 = np.array([101,100,102,104,102,97,105,105,98,101,100,123,105,103,100,95,102,106,
        109,102,82,102,100,102,102,101,102,102,103,103,97,97,103,101,97,104,
        96,103,124,101,101,100,101,101,104,100,101])
test_2 = test_1 + npr.normal(loc=2, scale=10, size=len(test_1))


# packing the data into a tidy dataframe can be nice
exp_df = pd.DataFrame(dict(group=[0]*len(test_1)+[1]*len(test_2), score=np.r_[test_1, test_2]))

exp_df.head()


# To perform this test we set `paired` to `True`.

# In[32]:


pg.ttest(x=test_1, y=test_2,paired=True, tail='two-sided')


# ```{admonition} Example way to report this in a paper
# :class: tip
# We conducted a paired t-test comparing the scores in the first and second test which was significant ($t(46)=3.3, p<.002, d=0.547$).
# ```

# ## One sample t-test

# What if you only have one sample and you just want to test if it is different than some specific "null" hypothesis.  For instance many of the scores seem to be about 100 in the `drug` group from the dataset above so we could test the hypothesis "is the mean of that group significantly different than 100?".  A one-sample t-test is appropriate for this:

# In[36]:


pg.ttest(x=drug, y=100, paired=True, tail='two-sided')


# ```{admonition} Example way to report this in a paper
# :class: tip
# We conducted a one-sample t-test comparing the scores in the drug group against the null hypothesis of a mean of 100 which did not reach significance ($t(46)=2.18, p=.034, d=0.318$).
# ```

# ## Non-normal data (Wilcoxon or Mann-Whitney test)

# All the tests above assume the data is normally distributed.  But we can't just assume that.  How do you know for sure?  Well it is a bit of a longer topic but there are tests for `non-normality` you can uses which are summarized [here](http://gureckislab.org/courses/fall20/labincp/chapters/10/00-ttest.html#checking-the-normality-of-a-sample).  
# 
# In cases where there is strong suspicion your data are not normally distributed in one or the other group you can use a non-parametric test known as the Wilcoxon (paired samples/within subject) or Mann-Whitney (independent samples) test.  It also exists in `pingouin`:

# In[38]:


pg.mwu(x=drug, y=placebo, tail='two-sided')


# ```{admonition} Example way to report this in a paper
# :class: tip
# Since our data were non-normal, we conducted a two-side Mann-Whitney test comparing the scores in the drug group against the placebo group which was significant ($U=1267.5, p<.02$).
# ```

# The one paired samples version of this is the Wilcoxon test:

# In[40]:


pg.wilcoxon(x=test_1, y=test_2, tail='two-sided')


# ```{admonition} Example way to report this in a paper
# :class: tip
# Since our data were non-normal, we conducted a two-sided Wilcoxon test comparing the scores at test time 1 with the scores at test time 2 which was significant ($W=305.0, p<.007$).
# ```

# ## Be Bayesian! The BEST test

# The examples above all show how to tell if two groups are different using traditional "null hypothesis significance testing."  However there are several ways in which this is non ideal.  Instead, the best way to evaluate differences between groups it do dump the hypothesis testing framework all together and use Bayesian estimation of the differences between groups.  Kruschke (2013) describes a simplified/standardize work flow called the BEST test (Bayesian ESTimation) although I've also heard it call the Bayesian Estimation Superceeds the T-test!.
# 
# Luckily there is a simplified python package that implements this test for you! https://best.readthedocs.io/en/latest/

# In[42]:


import best


# In[44]:


best_out = best.analyze_two(drug, placebo)


# In[ ]:


best.plot_all(best_out)


# ### Watermark

# The code here successfully ran with these versions of the packages:

# In[43]:


get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '-n -u -v -iv -w')


# In[ ]:




