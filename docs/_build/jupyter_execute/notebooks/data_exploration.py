#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
import requests
import pandas as pd
import matplotlib.pyplot as plt
import sys
import numpy as np
from nltk import word_tokenize
from nltk.corpus import stopwords
from string import punctuation

from bs4 import BeautifulSoup


# # Data exploration
# ## exploration of [UvA Alma Beelbank](https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html#Archeological-objects)
# details: ~40.000 records

# In[2]:


alma_beeldbank = pd.read_xml('../data/CUE/uva_alma_beeldbank_dc_new.xml')
alma_beeldbank

# alma_beeldbank_marc = parse_xml_to_array('data/uva_alma_beeldbank_marc_new.xml')


# In[3]:


# print dataset rule
# alma_beeldbank.loc[alma_beeldbank['identifier'] == 'https://hdl.handle.net/11245/3.826']
alma_beeldbank['schemaLocation'].iloc[0]


# In[4]:


# print random identifier
alma_beeldbank['identifier'].iloc[0]


# In[5]:


# process for latex code
alma_beeldbank.iloc[0].to_markdown()


# In[6]:


# produce description of dataset
print(alma_beeldbank.describe().style.to_latex())


# ### Dataset info. 

# In[7]:


alma_beeldbank.info()


# ### dataset per subject

# In[8]:


subjects = alma_beeldbank[alma_beeldbank['subject'].notnull()]
subjects


# In[9]:


np.set_printoptions(threshold=sys.maxsize)
print(alma_beeldbank[alma_beeldbank['subject'].notnull()]['subject'].value_counts().iloc[:25].to_latex())


# In[10]:


subjects[subjects['subject'] == 'Prenten']


# In[11]:


plt.figure(figsize=(10,4),dpi=200)
sns.countplot(x='type',data=alma_beeldbank)


# In[24]:


print('10 most occuring formats in beelbank data: \n', alma_beeldbank['format'].value_counts().iloc[:10].to_latex())


# In[26]:


print('unique entries in language category:\n', alma_beeldbank['language'].unique())


# In[36]:


print('value counts in language category per language:\n', alma_beeldbank['language'].value_counts().iloc[:10].to_latex())


# In[41]:


print('unique authors of items in beeldbank:\n', alma_beeldbank['contributor'].unique())


# In[42]:


print('n0 of occuring items per author:\n', alma_beeldbank['contributor'].value_counts())


# In[43]:


unique_dates = alma_beeldbank['date'].unique()


# In[44]:


print('items per year: ', alma_beeldbank['date'].value_counts().to_markdown())


# In[27]:


alma_beeldbank = alma_beeldbank.dropna(subset=['date'])


# In[28]:


alma_beeldbank = alma_beeldbank[alma_beeldbank['date'].str.isnumeric()]


# In[29]:


alma_beeldbank['date'] = alma_beeldbank['date'].astype(int)


# In[30]:


alma_beeldbank = alma_beeldbank[alma_beeldbank['date'] <= 2022]


# In[31]:


alma_beeldbank = alma_beeldbank.sort_values('date')


# In[32]:


alma_beeldbank['date'].value_counts(sort=False)


# In[33]:


plt.figure(figsize=(8,4),dpi=200)
sns.countplot(x='date', data=alma_beeldbank)
plt.xticks(size=10)


# In[34]:


sns.displot(data=alma_beeldbank, x='date', kde=True)


# In[28]:


elems_per_year = [len(alma_beeldbank[alma_beeldbank['date'] == years[y]]) for y in range(len(years))]

low = [e for e in elems_per_year if e < 400]
mid = [e for e in elems_per_year if e > 400 and e < 800]
high = [e for e in elems_per_year if e > 800]


# In[29]:


#stats
len(years), len(low), len(mid), len(high)


# In[30]:


plt.figure(figsize=(10,10))
plt.bar(years, elems_per_year)
plt.xticks(color='w')
plt.xlabel('year')
plt.ylabel('occurrences in year')
plt.show()


# In[8]:


joined = " ".join(alma_beeldbank['title'].dropna().unique())


# In[12]:


import wordcloud


# In[14]:


# code copied from: https://jingwen-z.github.io/data-viz-with-matplotlib-series9-word-cloud/
wordcloud = wordcloud.WordCloud(width=1280, height=853, margin=0,
                      colormap='Blues').generate(joined)

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.margins(x=0, y=0)
plt.savefig('descriptions_wordcloud.png')
plt.show()


# In[ ]:


# author to keywords (from titles)
french = set(stopwords.words('french'))
english = set(stopwords.words('english'))
german = set(stopwords.words('german'))
dutch = set(stopwords.words('dutch'))

punctuation = set(list(punctuation))

keywords = {}

for author in alma_beeldbank['contributor'].unique():

    body = " ".join(alma_beeldbank[alma_beeldbank['contributor'] == author]['title']).lower()
    values = word_tokenize(body)

    lang = alma_beeldbank[alma_beeldbank['contributor'] == author]['language']
    print(lang)

    if author in keywords: 
        print('entry already present!')
        keywords[author][0] += values 
    else:
        keywords[author] = (values, lang)

    keywords[author] = (set(keywords[author][0]), keywords[author][1])
    filtered = []

    for w in keywords[author][0]:

        if keywords[author][1] == 'fre':
            if w not in french:
                if w not in punctuation:
                    filtered.append(w)
        elif keywords[author][1] == 'eng':
            if w not in english:
                if w not in punctuation:
                    filtered.append(w)
        elif keywords[author][1] == 'ger':
            if w not in german:
                if w not in punctuation:
                    filtered.append(w)
        elif keywords[author][1] == 'dut':
            if w not in dutch:
                if w not in punctuation:
                    filtered.append(w)
        else:
            if w not in punctuation:
                filtered.append(w)

    # potentially add language 
    keywords[author] = filtered


# 

# In[ ]:


keywords


# ## search for APM in any of the columns of alma beeldbank export

# In[37]:


substring = 'apm'
df[df.apply(lambda row: row.astype(str).str.contains(substring, case=False).any(), axis=1)]


# ## Beeldbank marc

# In[14]:


titles = [record.title() for record in alma_beeldbank_marc]


# In[19]:


# vergelijking van marc en dublin core record. 
# een aantal velden missen/maar waren hoogstwaarschijnlijk niet nuttig geacht. 

example_record = alma_beeldbank_marc[0]
print(example_record)

print('comparison with \n')

for name, values in alma_beeldbank.loc[0].iteritems():
    print(values)


# ## Data exploration of [archaeological objects](https://uba.uva.nl/en/support/open-data/data-sets-and-publication-channels/data-sets-and-publication-channels.html#Archeological-objects)
# dublin core, [download](https://diensten.uba.uva.nl/open_data/downloads/uva_alma_archobjects_dc_new.tar.gz)

# In[37]:


# dc export
archobjects_dc = pd.read_xml('data/uva_alma_archobjects_dc_new.xml')
archobjects_dc


# marc extension, [download](https://diensten.uba.uva.nl/open_data/downloads/uva_alma_archobjects_marc_new.tar.gz) first edited from xml to marc using [marc editing tool](https://marcedit.reeset.net/downloads). 

# In[ ]:


from pymarc import MARCReader

with open('data/uva_alma_archobjects_marc_new.mrc', 'rb') as fh:
    reader = MARCReader(fh)
    for record in reader:
        print(record)


# In[ ]:


from pymarc import parse_xml_to_array

records = parse_xml_to_array('data/uva_alma_archobjects_marc_new.xml')
records


# ## theater dataset

# In[11]:


tin = pd.read_xml('data/wwwopac_TIN_limit100000.xml')
tin


# In[5]:


tin_1 = pd.read_xml('data/theatercollecties_test1.xml')
tin_1


# In[3]:


archobjects = pd.read_xml('data/uva_alma_archobjects_dc_new.xml')
archobjects


# In[15]:


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

result = map(to_lod, list(zip(tin_1.columns, values)))
lod_result = pd.DataFrame(result, columns= ['predicate', 'object'])
lod_result


# In[12]:


import requests

URL = "https://servicetin.adlibhosting.com/te4/wwwopac.ashx?command=search&database=collectTEphotos3&search=pointer%20353&output=xml&limit=10&startfrom=1&xmltype=grouped"

response = requests.get(URL)
with open('feed.xml', 'wb') as file:
    file.write(response.content)


# In[15]:


tin_1 = pd.read_xml('feed.xml')
tin_1


# ## export images from alma beeldbank

# In[ ]:


import requests
from bs4 import BeautifulSoup

# Making a GET request
r = requests.get('https://www.theatercollectie.uva.nl/Details/collect/42164')

# Parsing the HTML
soup = BeautifulSoup(r.content, 'html.parser')
print(soup.prettify())


# In[ ]:


s = soup.find('div', class_='record')

labels = s.find('div', class_='label')
values = s.find('div', class_='value')
s


# In[3]:


from PIL import Image
import requests
import bs4


# In[43]:


alma_beeldbank['identifier']

# for handl in alma_beeldbank['identifier']:
#     print(handl)

# url = 'some.site.com'

# response = requests.get(url)

# soup = bs4.BeautifulSoup(response.text, 'html.parser')

# image = soup.find('img')
# image_url = image['src']


# img = Image.open(requests.get(image_url, stream = True).raw)

# img.save('image.jpg')


# # linking from online --> offline

# In[6]:


literature = []

def literature(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.content, "html.parser")

    lit = []

    litsec = soup.find_all(class_="row label-publications")

    for l in litsec:
        lit += [l.find_all(class_='object-detail-data')[0].text]
    return lit

l = alma_beeldbank['identifier'].iloc[:50].apply(literature)


# In[7]:


alma_beeldbank['literature'] = l


# In[10]:


alma_beeldbank['literature']
alma_beeldbank['literature'].iloc[8]


# In[12]:


query = ['Bibliotheca']
df_x = alma_beeldbank.explode('literature')
df_x.set_index('literature').loc[query].reset_index(drop=True)


# In[7]:


alma_beeldbank['literature'] = literature


# # ground truth APM labels

# In[3]:


import math


# In[4]:


df = pd.read_excel('../data/catalogs/Crossroads - spreadsheet.xlsx', header=9)


# In[5]:


import re

def apm(descr):
    return re.findall('(?:APM)\s*\d+', descr)

df['APM'] = df['Image name'].dropna().apply(apm)


# In[6]:


df['APM']


# In[7]:


references = df['APM'].values.tolist()


# In[8]:


references = [r for r in references if r != [] and type(r) != float]


# In[9]:


references
online_indices = [(0,0),(3,0),(5,0),(6,0),(9,1)]


# In[10]:


references


# actually we have to cross reference this against the APM numbers in the pdf of the catalog

# In[11]:


# from catalog


# In[12]:


illustratieverantwoording = ' 10 above (APM16324),  \n1 3 (APM13822, APM9370),  \n29 above (APM7855),  5 1 (APM9276, APM9278, APM9280),  52 (APM16772),  \n66 (APM7468),  \n6 7 (APM12995),  \n69, 71 (APM7798),  \n72 (APM16388),  73 (APM3830),  \n7 4 (APM7798),  \n103 below (APM12974), \n1 46 (APM8471),  1 47 (APM8107),  \n1 6 2 (APM7071),  1 63 left (APM09163),  \n1 63 right (APM15589),  \n1 7 6 above (APM16369), 1 80 (APM3831, APM10998)'


# In[13]:


references_book = apm(str(illustratieverantwoording))


# In[14]:


def cross_reference(references, references_book):
    
    cr = []
    
    for r in references_book:
        if [r] in references:
            cr += [r]
    return cr


# In[15]:


references, references_book


# In[16]:


# all of the 


# In[17]:


cross_reference(references, references_book)


# In[18]:


"Inventory numbers Allard
Pierson Museum
Cover: 14232
p. 6: 16751
p. 28: 3493
p. 31: 3271
p. 33: 7802
p. 35: above 7164, below 7316
p. 37: 7971
p. 38: 9227
p. 40: 16883
p. 41: 16228
p. 43: 13055
p. 45: 1379
p. 48: 13937
p. 50: above 12378, below
10167
p. 52: 13825
p. 53: 1627
p. 55: 7347 and 7349
p. 56: 7286
p. 57: 7359 and 13963
p. 59: 7326
p. 61: 2907
p. 62: 1786 (photo Restauratieatelier
Restaura)
p. 64: above 3239 and 2845,
below 1785
p. 65: 788
p. 69: 1892
p. 72: 8343
p. 73: above 13946,
below 15758
p. 74: above 15369 and 15370
p. 75: 14005
p. 76: 6349
p. 77: 12428
p. 78: 7592
p. 80: 15396
p. 81: 8188
p. 82: 3242 and 3243
p. 84: above 9374, below 1774
p. 85: 8180
p. 86: 3269
p. 87: 3422
p. 92: 12
p. 93 above 1606
p. 95: 8552
p. 96: 35
p. 97: above 12417, below
12534
p. 100: above 7066, 8124, 8116,
below 8117, 7065, 8120
p. 101: 7974
p. 102: 7757
p. 103: 8133
p. 104: left 7288, 7290, 7874
and 8023, right 725
p. 105: 7768
p. 107: 8146.001-009
p. 108: 8169
p. 109: 16217
p. 110: 16166
p. 115: 9234
p. 118: 1674
p. 119: 15076
p. 122: 1402
p. 123: 8016
p. 124: 7799
p. 126: 8175
p. 128: 7946
p. 131: 11972
p. 132: 1765
p. 133: 15914
p. 137: 5205, 5208, 5216, 5220,
5222, 5230
p. 139: 15927
p. 140: 9894-9900, 10675
p. 141: 9350
p. 142: 8133
p. 143: 7022
p. 144: 6295, 6296, 7304,
7308, 14165
p. 145: 7001, 7003, 7004
p. 146: 724
p. 148: 1687
p. 151: above 15746, below
1722
p. 153: 8363, 319, 1681, 6319,
p. 156: 12.324
p. 157: left 16618, right 12481
p. 158: above 15689,
below 15999
p. 161: 451
p. 162: 3579
p. 163: 7163
p. 164: 7310
p. 165: 9224
p. 167: 7379
p. 174: 14.409
p. 176: 5180
p. 177: 16763
p. 178-179: 10854
p. 180: 10.854
p. 181: 9241
p. 182: 6287
p. 183: 16882
p. 185: 16604, 16607, 16612,
16614, 16616, 16610


# In[19]:


Inventarisnummers
Allard Pierson Museum
omslag: 4076
blz. 17: boven 196-1/2; onder
4170-4173, 4222
blz. 18: 4206, 4143, 4145
blz. 21: 15290
blz. 22: boven 4162, 4218, 4164, 4219;
onder 3974/3863, 3972A
blz. 23: 12637
blz. 33: 12720, 15276, 3943
blz. 34: boven 3858; onder 12676,
12678
blz. 35: boven 4044; onder 15999,
16476
blz. 37: 15302, 15301
blz. 39: boven 7298; onder 4306
blz. 40: 3635, 12683
blz. 42: boven 8752/14021; onder
Schriftmuseum Dortmond
P. Amsterdam 22
blz. 43: 9274, 15592
blz. 46: 3933
blz. 47: 8850
blz. 48: 3400
blz. 49: 16000
blz. 51: 8539
blz. 53: 12698
blz. 54: 12647, 14238
blz. 63: 15350
blz. 64: 9237
blz. 65: 8789
blz. 69: 12978
blz. 73: APM 9115
blz. 75: 1387
blz. 76: boven 3408, 360, 3799;
onder 11960
blz. 77: 12718, 8537
blz. 78: 8851; Schriftmuseum
Dortmond, no. 115
blz. 79: boven 9114; onder 8875, 1676
blz. 86: 16500
blz. 87: boven 9223; onder 8811
blz. 88: 13283a-j, 8800
blz. 99: 391
blz. 100: boven 8065; onder 13292
blz. 102: 7774
blz. 103: 12760, 4307, 15326
blz. 104: 12977
blz. 105: 9475, 9492, 9502
blz. 106: 8562, 8563, 8417
blz. 107: 8831
blz. 108: 20
blz. 109: 8837
blz. 111: 13219
blz. 115: 8795/6
blz. 116: 7126
blz. 117: 7772
blz. 118: 6289
blz. 119: 7993
blz. 120: 8846
blz. 124: 7216, 7238, 7272
blz. 125: 13158
blz. 129: 7758
blz. 130: 7763
blz. 131: 9369
blz. 132: 8517
blz. 133: 7796
blz. 135: 14232
blz. 136: 7860, 7861
blz. 137: 9353
blz. 138: 7874, 9227
blz. 139: 7803
blz. 141: 7766
blz. 142: boven 7757; onder 7974
blz. 143: 7761
blz. 144: 8188
blz. 145: 6286
blz. 150: 12995, 14513
blz. 152: boven 16750; onder 14510
blz. 153: 8189
blz. 159: 16385


# In[ ]:





# In[ ]:




