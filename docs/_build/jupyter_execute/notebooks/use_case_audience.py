#!/usr/bin/env python
# coding: utf-8

# ## Takeaways from the report
# 
# " Women with digital affinity prefer "making connections visible" and "individual recommendations"."
# 
# " People with a strong digital affinity favor "Individual Recommendations". Less important respondents cited "text creation", "speech recognition", "AI-generated art", "emotion recognition", "image recognition" and "generation of stories". " 
# 
# " It was considered particularly important that AI should contribute to accessibility, but somewhat more important for womenthan for men. The preference for automatic translations is at the forefront. " 
# 
# summary: making connections visible, individual reccomendations, contribute to accessibility

# In[1]:


# this is a document containing a short overview of use case data of the BLM

import pandas as pd


# In[2]:


# the data made available by the BLM 
# a user survey on use cases of the museum
# an analysis was done too by the FH Kiel

path = 'data/Use_Case_Audience_Segmentation/Seminar_FH_Kiel/Abgabe_SOM_Badisches_Landesmuseum/'
filename = 'umfrageonline-2728300.xlsx'

df = pd.read_excel(path + filename)


# In[42]:


df


# In[43]:


archaeology = df[df['Antike &amp; Archäologie'] == 1.0]


# In[44]:


def gender(input_field):
    if input_field == 'männlich':
        return 0
    if input_field == 'weiblich':
        return 1
    if input_field == 'divers':
        return 2
    else: 
        return -1

archaeology['3. Ich bin'] = archaeology['3. Ich bin'].apply(gender)
archaeology


# In[45]:


def age(input_field):
    if input_field == '15-29 Jahre':
        return 0
    if input_field == '30-59 Jahre':
        return 1
    if input_field == '60 Jahre und älter':
        return 2
    else: 
        return -1

archaeology['4. Mein Alter'] = archaeology['4. Mein Alter'].apply(age)
archaeology


# In[37]:


## side track calculate the image entropy
import skimage.measure    
import cv2

img = cv2.imread('data/user_reviews/review_1.png')
entropy = skimage.measure.shannon_entropy(img)

## compare with
img2 = cv2.imread('data/user_reviews/review_2.png')
entropy1 = skimage.measure.shannon_entropy(img2)

entropy, entropy1


# In[38]:


page = cv2.imread('data/user_reviews/IMG-2579.jpg')
page2 = cv2.imread('data/user_reviews/IMG-2578.jpg')

entropy = skimage.measure.shannon_entropy(page)

# supposedly the less chaotic image:
entropy1 = skimage.measure.shannon_entropy(page2)

entropy, entropy1


# In[ ]:




