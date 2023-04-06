#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup as BS
import requests
    
text = requests.get('https://lib.uva.nl/discovery/search?query=any,contains,APM13823&tab=Everything&search_scope=DN_and_CI_and_PURE&vid=31UKB_UAM1_INST:UVA&offset=0').text
soup = BS(text)


# In[2]:


soup


# In[ ]:




