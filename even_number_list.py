# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 13:57:22 2017

@author: Ruby Kumar

EXERCISE:Let’s say I give you a list saved 
in a variable: a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]. 
Write one line of Python that takes this list a and makes 
a new list that has only the even elements of this list in it.
"""
a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 116, 190, 201]
new_list = []
for number in a:
    if number % 2 == 0:
        new_list.append(number)
    else:
        continue
print(new_list)
        
