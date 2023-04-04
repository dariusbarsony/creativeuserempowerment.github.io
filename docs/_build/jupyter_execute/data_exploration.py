#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
import nltk
import seaborn as sns


from wordcloud import WordCloud
from PIL import Image
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation


# ## exploration of [UvA Alma Beelbank](https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html#Archeological-objects)

# In[2]:


alma_beeldbank = pd.read_xml('data/uva_alma_beeldbank_dc_new.xml')


# In[3]:


print(alma_beeldbank.info())


# In[4]:


plt.figure(figsize=(10,4),dpi=200)
sns.countplot(x='type',data=alma_beeldbank)


# In[5]:


print('10 most occuring formats in beelbank data: \n', alma_beeldbank['format'].value_counts().iloc[:10])


# In[6]:


print('unique entries in language category:\n', alma_beeldbank['language'].unique())


# In[7]:


print('value counts in language category per language:\n', alma_beeldbank['language'].value_counts())


# In[8]:


print('unique authors of items in beeldbank:\n', alma_beeldbank['contributor'].unique())


# In[9]:


print('n0 of occuring items per author:\n', alma_beeldbank['contributor'].value_counts())


# In[10]:


unique_dates = alma_beeldbank['date'].unique()


# In[11]:


print('items per year: ', alma_beeldbank['date'].value_counts().to_markdown())


# In[12]:


alma_beeldbank = alma_beeldbank.dropna(subset=['date'])


# In[13]:


alma_beeldbank = alma_beeldbank[alma_beeldbank['date'].str.isnumeric()]


# In[14]:


alma_beeldbank['date'] = alma_beeldbank['date'].astype(int)


# In[15]:


alma_beeldbank = alma_beeldbank[alma_beeldbank['date'] <= 2022]


# In[16]:


alma_beeldbank = alma_beeldbank.sort_values('date')


# In[17]:


alma_beeldbank['date'].value_counts(sort=False)


# In[18]:


# plt.figure(figsize=(8,4),dpi=200)
# sns.countplot(x='date', data=alma_beeldbank)
# plt.xticks(size=10)


# In[19]:


sns.displot(data=alma_beeldbank, x='date', kde=True)


# ### Some analysis of the descriptions

# In[20]:


joined = " ".join(alma_beeldbank['title'].dropna().unique())


# In[21]:


# code copied from: https://jingwen-z.github.io/data-viz-with-matplotlib-series9-word-cloud/

wordcloud = WordCloud(width=1280, height=853, margin=0,
                      colormap='Blues').generate(joined)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.show()


# 

# ## Beeldbank marc
# ### short analysis of the beeldbank marc data

# In[22]:


alma_beeldbank_marc = pd.read_xml('data/uva_alma_beeldbank_marc_new.xml')
titles = [record.title() for record in alma_beeldbank_marc]


# In[23]:


# vergelijking van marc en dublin core record. 
# een aantal velden missen/maar waren hoogstwaarschijnlijk niet nuttig geacht. 

example_record = alma_beeldbank_marc[0]
print(example_record)

print('comparison with \n')

for name, values in alma_beeldbank.loc[0].iteritems():
    print(values)


# marc extension, [download](https://diensten.uba.uva.nl/open_data/downloads/uva_alma_archobjects_marc_new.tar.gz) first edited from xml to marc using [marc editing tool](https://marcedit.reeset.net/downloads). 

# ## theater dataset
# ### preprocessing done on the theatre collections dataset.

# In[ ]:


tin = pd.read_xml('data/wwwopac_TIN_limit100000.xml')
tin


# In[ ]:


# just one record
tin_1 = pd.read_xml('data/theatercollecties_test1.xml')
tin_1


# ### mapping from XML data format to LOD format

# In[ ]:


'''
code below provides a mapping from xml format to LOD format. 
some fields were considered as a test. 
'''

# read in data
tin_1 = pd.read_xml('data/theatercollecties_test1.xml')
values = [tin_1[c].iloc[tin_1[c].first_valid_index()] for c in tin_1.columns]

# expects list of tuples: [('column name', 'column_value'), ..., ]
def to_lod(input_field):
    if input_field[0] == 'creator':
        return ('http://purl.org/dc/elements/1.1/creator', input_field[1])
    if input_field[0] == 'creator.role':
        return ('http://purl.org/dc/elements/1.1/creator', input_field[1])
    if input_field[0] == 'performance.title':
        return ('https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/title/', input_field[1])
    if input_field[0] == 'production.date':
        return ('http://purl.org/dc/elements/1.1/date', input_field[1])
    if input_field[0] == 'reproduction.reference':
        return ('http://purl.org/dc/elements/1.1/identifier', input_field[1])
    if input_field[0] == 'object_category':
        return ('https://www.dublincore.org/specifications/dublin-core/dcmi-terms/elements11/type/', input_field[1])
    else: 
        return input_field

# maps input to appropriate output format
result = map(to_lod, list(zip(tin_1.columns, values)))
lod_result = pd.DataFrame(result, columns= ['predicate', 'object'])
lod_result

