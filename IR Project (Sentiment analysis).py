#!/usr/bin/env python
# coding: utf-8

# In[44]:


import json
import re 
import pandas as pd
from pandas.io.json import json_normalize
from textblob import TextBlob


# In[43]:


#json_data=open("/home/madhuresh/Documents/Dataset for Detection of Cyber-Trolls.json").read()


# In[39]:


def clean_tweet(tweet): 
    return ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())


# In[40]:


with open('/home/madhuresh/Documents/Dataset.json') as f:
    i=1
    for line in f:
        j_content = json.loads(line)
        print (i,'.  ',clean_tweet(j_content['content']),'\t',j_content['annotation']['label'][0])
        i=i+1
        if i > 10:
            break
    


# In[ ]:





# In[ ]:




