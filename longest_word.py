# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 09:02:17 2017

@author: Agni Kumar

EXERCISE: Write a function longest() that takes one argument, 
a list of words, and returns the length of the longest word in the list.
"""
"""def longest_word():
    text = input("Please input a list of words to evaluate in the form a, b, c, d: ")

    longest_len = 0

    for word in text.split():
        if len(word) > longest_len:
            if "," in word:
                longest_len = len(word) - 1
                longest_word = word
                longest_word = word.replace(",", "")
            else: #only words that are last in the list
                longest_len = len(word)
                longest_word = word
    print("The longest word is", longest_word, "with length", longest_len)

longest_word()"""
            
    def longest(words):
        value = 0
        for word in words:
            if len(word) > 0:
               value = len(word)
        return value
       


    

    