#!/usr/bin/env python
# coding: utf-8

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd


# In[60]:


url="http://statisticstimes.com/economy/european-union-countries-by-gdp-per-capita.php"
html=urlopen(url)
soup=BeautifulSoup(html,'lxml')
tables=soup.findChildren('table')
my_table=tables[2]


# In[61]:


rows=my_table.findChildren(['th','tr'])


# In[62]:


country=[]
eu=[]
world=[]
gdp17=[]
gdp18=[]
rows=my_table.findChildren('tr')
for row in rows:
    cells=row.findChildren('td')
    for cell in cells[0:1]:
          country.append(cell.text)
    for cell in cells[1:2]:
          gdp17.append(cell.text)
    for cell in cells[2:3]:
          gdp18.append(cell.text)
    for cell in cells[6:7]:
          eu.append(cell.text)
    for cell in cells[7:8]:
          world.append(cell.text)
country.pop()
eu.pop()
world.pop()
gdp17.pop()
gdp18.pop()
df=pd.DataFrame()


df['Country/Economy']=country
df['EU Rank']=eu
df['World']=world
df['$ GDP 2017']=gdp17
df['$ GDP 2018']=gdp18
df.sort_values(['EU Rank'])

        

