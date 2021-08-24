#!/usr/bin/env python
# coding: utf-8

# # COVID Deaths by ZipCode in NYC

# In[1]:


import numpy.random as npr
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import statsmodels.formula.api as smf

import warnings
warnings.filterwarnings("ignore")

from myst_nb import glue # for the Jupyter book chapter


# In[2]:


race_df=pd.read_csv('covid_data/data-6RFy5.csv').set_index('Zipcode')
income_df=pd.read_csv('covid_data/data-dAArg.csv').set_index('Zipcode')
asthma_df=pd.read_csv('covid_data/data-oMup5.csv').set_index('Zipcode')
pop_df=pd.read_csv('covid_data/data-rtgjl.csv').set_index('Zipcode')
age_df=pd.read_csv('covid_data/data-vS9Is.csv').set_index('Zipcode')
house_size_df = pd.read_csv('covid_data/data-yReq2.csv').set_index('Zipcode')


# In[3]:


covid_df = race_df.join(income_df, rsuffix="DROP").filter(regex="^(?!.*DROP)")
covid_df = covid_df.join(asthma_df, rsuffix="DROP").filter(regex="^(?!.*DROP)")
covid_df = covid_df.join(pop_df, rsuffix="DROP").filter(regex="^(?!.*DROP)")
covid_df = covid_df.join(age_df, rsuffix="DROP").filter(regex="^(?!.*DROP)")
covid_df = covid_df.join(house_size_df, rsuffix="DROP").filter(regex="^(?!.*DROP)")
covid_df=covid_df.reset_index()


# In[4]:


covid_df.columns =  ['zip','borough','neighborhood','deathper100k', 'whitepct', 'medianincome', 'asthmapct', 'popdens','medianage', 'housesize']


# In[5]:


covid_df.to_csv('covid.csv')


# In[46]:


covid_df.head()


# In[59]:


covid_df['whitepct_z'] = covid_df['whitepct'].transform(lambda x: (x-x.mean())/x.std())
covid_df['medianincome_z'] = covid_df['medianincome'].transform(lambda x: (x-x.mean())/x.std())
covid_df['asthmapct_z'] = covid_df['asthmapct'].transform(lambda x: (x-x.mean())/x.std())
covid_df['popdens_z'] = covid_df['popdens'].transform(lambda x: (x-x.mean())/x.std())
covid_df['medianage_z'] = covid_df['medianage'].transform(lambda x: (x-x.mean())/x.std())
covid_df['housesize_z'] = covid_df['housesize'].transform(lambda x: (x-x.mean())/x.std())


# In[60]:


lr = smf.ols(formula="deathper100k ~ whitepct_z+medianincome_z+asthmapct_z+popdens_z+medianage_z+housesize_z", data=covid_df).fit()
print(lr.summary())
print(np.sqrt(lr.rsquared))


# In[52]:


lr = smf.ols(formula="deathper100k ~ whitepct", data=covid_df).fit()
print(lr.summary())
print(np.sqrt(lr.rsquared))


# In[53]:


lr = smf.ols(formula="deathper100k ~ medianincome", data=covid_df).fit()
print(lr.summary())
print(np.sqrt(lr.rsquared))


# In[54]:


lr = smf.ols(formula="deathper100k ~ housesize", data=covid_df).fit()
print(lr.summary())
print(np.sqrt(lr.rsquared))


# In[ ]:


lr = smf.ols(formula="deathper100k ~ housesize", data=covid_df).fit()
print(lr.summary())
print(np.sqrt(lr.rsquared))

