# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 07:43:34 2017

@author: Ruby Kumar

Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
  
and write a program that returns a list that 
contains only the elements that are common 
between the lists (without duplicates). Make 
sure your program works on two lists of 
different sizes.

SOLUTION 2:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []
for number in b:
    if number in a and number not in new_list:
        new_list.append(number)
    else:
        continue
print(new_list)
"""
list1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []
for number in list1:
    if number in list2 and number not in new_list:
        new_list.append(number)
    else:
        continue
print(new_list)
        


