#!/usr/bin/env python
# coding: utf-8

# In[2]:


import re
import pandas as pd
import dhlab as dh


# In[3]:


def findone(regex, s):
    res = re.findall(regex,s)
    try:
        r = res[0]
    except:
        r = "tjo"
    return r


# In[4]:


#korpus = dh.Corpus(doctype="digibok", subject = "språkvitenskap", limit = 1000,from_year=1950)
#korpus


# In[13]:


def citation_finder(corpus, yearspan = (1900,2020)):
    

    tall = list(range(yearspan[0],yearspan[1]))

    tallOR = ' OR '.join([str(x) for x in tall])

    tallconc = dh.Concordance(corpus, tallOR, limit=4000)

    concs = tallconc.frame
    concs.concordance = concs.concordance.apply(lambda x:x.replace('<b>', '').replace('</b>', '').replace('...', ''))
    
    books1 = concs[['urn', 'concordance']]

    regex1 = r'[\(;].*?\D\d{4}\D.*?[\);]'

    books1['parentes'] = books1.concordance.apply(lambda x: findone(regex1, x))

    books2 = books1[books1['parentes'] != 'tjo']
    books2 = books2[['urn', 'concordance']]

    #kombinasjon av et al./og + mulige navn + årstall + sidetallkonstruksjoner
    regex2 = r'(?:og|and|&)?(?:[A-ZÆØÅ](?:[A-ZÆØÅa-zæøå-]+|\s*\.)\s*,?\s*)+(?:\s*et\sal\.\s*)?,?\s*\[?\s*\d{4}\s*[a-zæøå]?\s*\.?\s*\]?(?:\s*[,-;:/\)\s]\s*(?:[ps]\s*\.?)?\[?\s*\d{1,4}\s*[a-zæøå]?\s*\.?\s*\]?)*\s*[\);]'
     
    books2['sitering + parentes'] = books2.concordance.apply(lambda x: findone(regex2, x))
    
    books3 = books2[books2['sitering + parentes'] != 'tjo']
    books3 = books3[['urn', 'concordance']]

    regex3 = r'(?<=[\(;]).*?\d{4}.*?(?=[\);])'

    books3['citation'] = books3.concordance.apply(lambda x: findone(regex3, x))
    
    return books3[['urn','citation']]


# In[14]:


#citation_finder(korpus, yearspan = (2000,2005))


# In[ ]:




