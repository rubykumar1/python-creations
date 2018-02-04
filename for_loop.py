# -*- coding: utf-8 -*-
"""
Created on Mon Dec  4 10:17:49 2017

@author: Ruby Kumar
EXCERCISE: for statements
"""
# Measure some strings
words = ['cat', 'monkey', 'human', 'bananas']
for word in words:
    print(word, len(word))
# loop over a slice copy of the entire list (slice any word
#from the list and put it where you like inside the list; insert()

for word in words[:]:
    if len(word) > 6:
        words.insert(0, word)
        print(words)
        