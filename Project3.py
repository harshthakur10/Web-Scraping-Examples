#!/usr/bin/env python
# coding: utf-8

# ## 1. Students are required to scrape data from the IMDB page titled "List of Movies and castings".
# 

# In[2]:


pip install requests beautifulsoup4 pandas


# In[3]:


import requests

from bs4 import BeautifulSoup

import pandas as pd

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36'
}


url="https://www.imdb.com/chart/top/"


# In[4]:


r=requests.get(url,headers=headers)


# In[5]:


soup=BeautifulSoup(r.content,'html.parser')


# In[6]:


soup.select('h3',class_='ipc-title__text')


# In[7]:


s=soup.select('h3',class_='ipc-title__text')[0].text


# In[8]:


s


# In[9]:


movies=[]

for i in soup.select('h3',class_='ipc-title__text'):
    movies.append(i.text)


# In[10]:


movies


# ##  2. Student are required to scrape data from the  Wikipedia with the URL (https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States) . This page contains the list of states in the U.S, population, and other details. We will try to get the names of the states and the population columns of the table. 

# In[11]:


import requests

from bs4 import BeautifulSoup

import pandas as pd

url1="https://en.wikipedia.org/wiki/List_of_states_and_territories_of_the_United_States"


# In[12]:


r=requests.get(url1)


# In[13]:


r


# In[14]:


r.content


# In[17]:


soup1=BeautifulSoup(r.content,'html.parser')


# In[18]:


soup1


# In[32]:


table=soup1.find_all('table')[1]


# In[33]:


table.find_all('th')


# In[36]:


th=[]
c=0
for i in table.find_all('th'):
    th.append(i.text.strip())
    c+=1
    if c==5:
        break
th


# In[37]:


import pandas as pd


# In[38]:


t=pd.DataFrame(columns=th)
t


# In[79]:


tr=table.find_all('tr')


# In[83]:


th=table.find_all('th')
th


# In[75]:


tr


# In[89]:


names=[]
for i in table.find_all('th'):
    names.append(i.text.strip())
    
    
names


# In[ ]:




