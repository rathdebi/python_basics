#!/usr/bin/env python
# coding: utf-8

# In[1]:


# often mutation takes place 
# in case of df operation
# but python and pandas offers
# a cool way to achieve that same objective
# aka, method chaining


# In[69]:


import pandas as pd
import os
os.getcwd()


# In[67]:


df = pd.DataFrame({"sitting_time":[30,45,60,15,15],
                   "type":["reg","reg","reg","irregular","irregular"],
                  "score_1":[70,80,86,69,91],
                   "score_2":[65,76,59,82,77],
                  "session":["half_year","half_year","half_year","annual","annual"]})
df


# In[65]:


# mutation ----------DO NOT DO THIS -------
df = df.query("sitting_time > 30 and type=='reg'")
df["score"] = df[["score_1","score_2"]].sum(axis=1)
df = df[["session","score"]]
df = df.groupby("session").agg(["count","mean"])
df = df.droplevel(axis=1,level=0)
df = df.query("count > 1")
df


# In[68]:


# method chaining ----------DO THIS--------
df = (df.query("sitting_time > 30 and type=='reg'")
      .assign(score = lambda df:df[["score_1","score_2"]].sum(axis=1))[["session","score"]]
      .groupby("session")
      .agg(["count","mean"])
      .droplevel(axis=1,level=0)
      .query("count>1"))
df


# In[ ]:




