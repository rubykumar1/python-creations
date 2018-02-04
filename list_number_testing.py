# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:28:56 2017

@author: Ruby Kumar

EXERCISE: Take a list, say for example this one:
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements 
of the list that are less than 5.

init_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for number in init_list:
    if number < 5: 
        new_list.append(number)
    else:
        continue
print(new_list)


CHALLENGE: Ask the user for a number and return a 
list that contains only elements from the original 
list a that are smaller than that number given by the user.
"""
#CHALLENGE
a = eval(input("Enter a number: ")) 
init_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
new_list = []
for number in init_list:
    if number < a: 
        new_list.append(number)
    else:
        continue
print(new_list)

