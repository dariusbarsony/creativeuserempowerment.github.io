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

# In[97]:


df = pd.read_csv('extract_' + ROME_EN + '.csv')


# ## analyse data

# In[98]:


text = df['text'].str.cat(sep=', ')
tokens = word_tokenize(text)


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


preprocess(ROME_EN)


# In[ ]:


corpus


# In[ ]:


tagged = nltk.pos_tag(tokens)


# In[ ]:


tagged[100:110]


# In[57]:


entities = nltk.chunk.ne_chunk(tagged)


# In[60]:


entities


# In[68]:


import sys

np.set_printoptions(threshold=sys.maxsize)


# # Linking from offline --> online
# obtaining the apm numbers from the 'illustratie verantwoording'

# In[7]:


def apm(descr):
    return re.findall('(?:APM)\s*\d+', descr)


# In[69]:


crossroads_en = ' 10 above (APM16324),  \n1 3 (APM13822, APM9370),  \n29 above (APM7855),  5 1 (APM9276, APM9278, APM9280),  52 (APM16772),  \n66 (APM7468),  \n6 7 (APM12995),  \n69, 71 (APM7798),  \n72 (APM16388),  73 (APM3830),  \n7 4 (APM7798),  \n103 below (APM12974), \n1 46 (APM8471),  1 47 (APM8107),  \n1 6 2 (APM7071),  1 63 left (APM09163),  \n1 63 right (APM15589),  \n1 7 6 above (APM16369), 1 80 (APM3831, APM10998)'
sicily_en = 'Amsterdam, Allard Pierson Museum: p. 17 bottom, 36 (APM 1974-1975), 42 (APM9995-9998), 44 top (APM8386), 44 bottom (APM13986), 48 (APM 1599), 51(APM 3702), 53 left (APM16.272), 53 right (APM1196), 54 bottom (APM6453), 55 top (1142-1143), 55middle (APM 13.362), 55bottom (APM 2149), 77 top(10601-10607), 142 (APM16763).


# In[73]:


df = pd.read_csv('extract_' + EGYPTE_NL + '.csv')
df['data'].iloc[91]


# In[11]:


df['apm'] = df['text'].dropna().apply(apm)


# In[13]:


df['apm'].iloc[208]

