#!/usr/bin/env python
# coding: utf-8

# # exhibition catalogs
# extract text from: Sicily EN, Crossroads NL, crossroads EN, Eeuwig Egypte NL, Rome EN

# In[1]:


# importing required modules 
import PyPDF2
import csv
import matplotlib.pyplot as plt
import pandas as pd

dirname = '../data/catalogs/'

# filenames: 
ROME_EN = 'Rome_EN_LR_compleet'
EGYPTE_NL = 'Eeuwig_Egypte_NL_LR'
CROSSROADS_NL = 'CrossRoads_NEDERLANDS_LR_compleet'
CROSSROADS_EN = 'CrossRoads_ENGELS_LR_compleet'
SICILY_EN = 'sicily_en'

books = [ROME_EN, EGYPTE_NL, CROSSROADS_EN, CROSSROADS_NL, SICILY_EN]


# ## extract text

# In[2]:


fields = ['data']

for b in books: 
    
    with open('extract_' + b + '.csv', 'w') as csvfile:

        # creating a csv writer object 
        csvwriter = csv.writer(csvfile) 
         
        # writing the fields 
        csvwriter.writerow(fields) 

        reader = PdfReader(dirname + b + '.pdf')
        for pagei in range(len(reader.pages)):
            page = reader.pages[pagei]
            csvwriter.writerow([page.extract_text()])


# ## import csv
# 

# In[ ]:


df = pd.read_csv('extract_' + EGYPTE_NL + '.csv')
df


# ## analyse data

# In[ ]:


# code copied from: https://jingwen-z.github.io/data-viz-with-matplotlib-series9-word-cloud/
wordcloud = wordcloud.WordCloud(width=1280, height=853, margin=0,
                      colormap='Blues').generate([corpus][0])

plt.imshow(wordcloud, interpolation='bilinear')

plt.axis('off')
plt.margins(x=0, y=0)
# plt.savefig('descriptions_wordcloud.png')
plt.show()


# ## text preprocessing

# In[ ]:


from nltk.tokenize import RegexpTokenizer
from nltk.corpus import stopwords

# expects dataframe as input
def preprocess(book):
    
    df = pd.read_csv('extract_' + book + '.csv')
    df = df.dropna()
    
    tokenizer = RegexpTokenizer(r'\w+')
    stop_words = set(stopwords.words('english'))

    corpus = ''

    for i in range(len(df.index)):

        # tokenize
        query = tokenizer.tokenize(df['data'].iloc[i])

        # filter stop words convert to lower
        filtered_sentence = [w.lower() for w in query if not w.lower() in stop_words]

        # filter digits
        filtered_sentence = [w for w in filtered_sentence if not w.isdigit()]

        df['data'].iloc[i] = " ".join(filtered_sentence)
        corpus += " ".join(filtered_sentence)
        
    return df, corpus


# In[ ]:


df, corpus = preprocess(EGYPTE_NL)


# In[ ]:


corpus


# In[ ]:


df.to_csv('processed_egypte_nl.csv')


# ## Egypte_nl

# In[ ]:


credits = df.iloc[91]


# In[ ]:


credits['data']


# In[ ]:


tokenizer = RegexpTokenizer(r'\w+')


# In[ ]:


credits = tokenizer.tokenize(credits['data'])


# In[ ]:


credits


# In[ ]:


credits = credits[credits.index('omslag'): credits.index('nederlands')]


# In[ ]:


' '.join(credits)


# In[ ]:


apm_egypte = re.findall('\d{4,}', " ".join(credits))


# In[ ]:


len(apm_egypte)


# In[ ]:


pages_apm_egypte = re.findall('(blz\s)(\d+)(.*?)blz', " ".join(credits))


# In[ ]:


pages_apm_egypte


# In[ ]:


pages_apm_egypte


# In[ ]:


labels_egypte = []

for _, p, apm in pages_apm_egypte:
    labels_egypte += (p, re.findall('\d{4,}', apm))


# In[ ]:


labels_egypte


# In[ ]:


labels = np.zeros_like(df.index)
labels


# In[ ]:


start = 2
mapping = []
mapping += [1]

for i in range(1, len(df.index) - 1):
    pages = [(start, start + 1)] 
    mapping += pages
    start += 2
    
mapping += [start]
mapping


# ## finding the right text Egypte

# In[ ]:





# # obtaining the ground truth
# obtaining the apm numbers from the 'illustratie verantwoording'

# In[ ]:


import math
import re


# In[ ]:


def apm(descr):
    return re.findall('(?:APM)\s*\d+', descr)


# In[ ]:


credits_crossroads = ' 10 above (APM16324),  \n13 (APM13822, APM9370),  \n29 above (APM7855),  51 (APM9276, APM9278, APM9280),  52 (APM16772),  \n66 (APM7468),  \n67 (APM12995),  \n69, 71 (APM7798),  \n72 (APM16388),  73 (APM3830),  \n74 (APM7798),  \n103 below (APM12974), \n146 (APM8471),  147 (APM8107),  \n162 (APM7071),  163 left (APM09163),  \n163 right (APM15589),  \n176 above (APM16369), 180 (APM3831, APM10998)'
page_numbers = [10, 13, 13, 29, 51, 51, 51, 52, 66, 67, 69, 72, 73, 74, 103, 146, 147, 162, 163, 163, 176, 180, 180]


# In[ ]:


references_crossroads = apm(credits_crossroads)


# In[ ]:


len(references_crossroads)


# In[ ]:


len(page_numbers)


# ## match page numbers to pages book

# In[ ]:


import numpy as np


# In[ ]:


page_offset = -2
df


# In[ ]:


labels = np.zeros_like(df.index)
len(labels)


# In[ ]:


mapping = zip(page_numbers, references_crossroads)
mapping


# In[ ]:


for pageid, apm in mapping:
    labels[pageid + page_offset] = apm[3:]


# In[ ]:


labels


# In[ ]:


np.savetxt("crossroads.csv", labels, delimiter=",")


# In[ ]:


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


# In[ ]:


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





# In[ ]:





# In[ ]:





# In[ ]:




