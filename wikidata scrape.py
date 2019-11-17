#!/usr/bin/env python
# coding: utf-8

from urllib.request import urlopen
from bs4 import BeautifulSoup
import pandas as pd

url="https://en.wikipedia.org/wiki/List_of_European_countries_by_area"
html=urlopen(url)
soup=BeautifulSoup(html,'lxml')
#names of the countries is under class Wikitable Sortable
my_table=soup.find('table',{'class':'wikitable sortable'})

country=[]
population=[]
rows=my_table.findChildren('tr')
for row in rows:
    cells=row.findChildren('td')
    for cell in cells[1:2]:
          country.append(cell.text)
for row in rows:
    cells=row.findChildren('td')
    for cell in cells[2:3]:
          population.append(cell.text)
country.pop()
population.pop()

country[:] = [dataa.rstrip('\n') for dataa in country]
country[:] = [dataa.rstrip('*') for dataa in country]
country[:] = [dataa.rstrip('[1]') for dataa in country]
population[:] = [dataa.rstrip('\n') for dataa in population]
df=pd.DataFrame()
df['Country']=country
df['Population']=population
df
