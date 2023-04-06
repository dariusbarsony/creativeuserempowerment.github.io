#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


filename_queries = '../data/catalogs/crossroads.csv'
queries = pd.read_csv(filename)


# In[ ]:


queries


# In[ ]:


filename_documents = '../data/CUE/uva_alma_beeldbank_dc_new.xml'
documents = pd.read_xml(filename_documents)


# In[ ]:


documents


# In[ ]:


from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')
query = tokenizer.tokenize(queries['text'].iloc[0])


# In[ ]:


len(query)


# In[ ]:


from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
filtered_sentence = [w for w in query if not w.lower() in stop_words]


# In[ ]:


len(filtered_sentence)


# In[ ]:


filtered_sentence = [w.lower() for w in filtered_sentence if not w.lower().isdigit()]


# In[ ]:


len(filtered_sentence)


# ### stemming

# In[ ]:


from nltk.stem.snowball import SnowballStemmer


# In[ ]:


stemmer = SnowballStemmer("english")


# In[ ]:


filtered_sentence = [stemmer.stem(w) for w in filtered_sentence]


# In[ ]:


" ".join(filtered_sentence)


# ### process document

# In[ ]:


document = tokenizer.tokenize(documents['title'].iloc[0])


# In[ ]:


len(document)


# In[ ]:


filtered_document = [w for w in document if not w.lower() in stop_words]


# In[ ]:


len(filtered_document)


# In[ ]:


filtered_document = [w.lower() for w in filtered_document if not w.lower().isdigit()]


# In[ ]:


filtered_document


# ### vector 

# In[ ]:


from sklearn.feature_extraction.text import TfidfVectorizer


# In[ ]:


model = TfidfVectorizer()


# In[ ]:


tfidf.fit_transform([" ".join(filtered_sentence)])


# In[ ]:


analyze = vectorizer.build_analyzer()
analyze("This is a text document to analyze.") == (['this', 'is', 'text', 'document', 'to', 'analyze'])


# In[ ]:


analyze


# In[ ]:




