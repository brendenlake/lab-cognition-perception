#!/usr/bin/env python
# coding: utf-8

# # Mumford Stats practice

# ## Video 2: Two stage random effects formaulation

# Standard simple regression
# 
# $RT = \beta_0 + \beta_1 Days + \epsilon$
# 
# or another way of writing it is:
# 
# $\begin{bmatrix}265\\252\\451\\335\end{bmatrix} = \begin{bmatrix}1&0\\1&1\\1&2\\1&3\end{bmatrix} \begin{bmatrix}\beta_0\\\beta_1\end{bmatrix} + \begin{bmatrix}\epsilon_1\\\epsilon_2\\\epsilon_3\\\epsilon_4\end{bmatrix}$
# 
# which can be more compatx like this
# $Y = \mathcal{Z}\beta + \epsilon, \epsilon \sum N(0, \sigma^2 I_n)$
# 
# where $\mathcal{Z}$ is the design matrix:
# 
# $\mathcal{Z}=\begin{bmatrix}1&0\\1&1\\1&2\\1&3\end{bmatrix}$
# 
# 
# In the two stage model were estimate each subject's slope and intercept separately:
# 
# $Y_i = \mathcal{Z_i}\beta_i + \epsilon_i, \epsilon_i \sum N(0, \sigma^2 I_{n_i})$
# 
# we are assuming $\sigma$ is the same for each subject.  Some other packages can do this.
# 
# The second stage model is
# 
# $\beta_i = \mathcal{A_i}\beta + b_i, b_i \sim N(0, G)$
# 
# $b_i$ is the amount of noise between subjects in the slopes and intercept.  It is expressed with a covariance term $G$ because they might be correlated (slope and intercept).   You don't actually estimate the $b_i$ values you estimate the $G$.
# 
# $\mathcal{A_i}$ is the identity matrix usually.
# 
# If you plug second stage into first stage:
# 
# $Y_i = \mathcal{Z_i}\mathcal{A_i}\beta + \mathcal{Z_i}b_i+\epsilon_i, \epsilon_i \sim N(0, \sigma^2 I_{n_i}), b_i \sim N(0, G)$
# 
# The $\beta$ is the "fixed effect" usually what we are interested in assessing.
# 
# The $\beta_i$ is the random effect variable of between subject variance
# 
# The $epsilon_i$ is the within subject variance.
# 
# 

# In[36]:


import numpy as np
import numpy.random as npr
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

# for py2r stuff
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'

import pymer4.models as pymer


# In[4]:


def makeFakeSleepStudyData(subj_num, days, sigma):
    subj_col = np.full((days,),subj_num)
    day_col = np.arange(0,days)
    intercept, slope = npr.multivariate_normal([251,10], [[24**2,0],[0,10**2]])
    rt = intercept + slope*day_col + npr.normal(loc=0, scale=sigma, size=days)
    return pd.DataFrame({'subj':subj_col, 'day':day_col, 'rt': rt})

nsubj=16
sigma = 30
days = 10

df = pd.concat([makeFakeSleepStudyData(subj_num,days, sigma) for subj_num in range(nsubj)])


# In[5]:


sns.relplot(x='day', y='rt', col='subj', col_wrap=4, kind='line', data=df)


# In[21]:


md=smf.mixedlm('rt ~ day', df, groups='subj', re_formula='~day')
mdf= md.fit()
print(mdf.summary())


# In[37]:


model=pymer.Lmer('rt ~ day + (1+day|subj)', data=df)
print(model.fit(REML=True))


# In[38]:


model=pymer.Lmer('rt ~ day + (day|subj)', data=df)
print(model.fit(REML=True))


# In[41]:


model.fixef


# In[35]:


res.BIC


# ## t-test equivalent

# In[71]:


group1mean, group2mean = 10, 20
groupstd = 2.
subj_col = range(30)
data = np.concatenate((npr.normal(loc=group1mean, scale=groupstd, size=15),npr.normal(loc=group2mean, scale=groupstd, size=15)))
cond = [1]*15+[2]*15
df=pd.DataFrame({'subj': subj_col, 'cond': cond, 'dv': data})


# In[56]:


df.head()


# In[72]:


pd.get_dummies(df.cond)


# In[70]:


model=pymer.Lm('dv ~ 1+cond', data=df)
print(model.fit(REML=True))


# In[68]:


import pingouin as pg

pg.ttest(df[df['cond']==0]['dv'],df[df['cond']==1]['dv'])


# In[ ]:




