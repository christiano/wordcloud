#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 27 18:21:57 2016

@author: anderson
"""

import re
import nltk
from wordcloud import WordCloud
import matplotlib.pyplot as plt

data = {}

data['blog'] = open('nosql2.txt','r').read()

for k in data.keys():
    data[k] = data[k].lower()
    
# Remove pontuacao
for k in data.keys():
    data[k] = re.sub(r'[-./?!,":;()\']',' ',data[k])
    
# Remove numeros
for k in data.keys():
    data[k] = re.sub('[-|0-9]',' ',data[k])
    

# Stopwords em portugues
stopwords = nltk.corpus.stopwords.words('portuguese')

for k in data.keys():
    data[k] = data[k].split()
    
for k in data.keys():
    data[k] = [ w for w in data[k] if not w in stopwords ]
    
wordcloud = WordCloud(background_color="black", width = 1366, height = 768).generate(' '.join(data[k]))

plt.figure(figsize=(15,8))

plt.imshow(wordcloud)
    
plt.axis("off")

plt.show()
