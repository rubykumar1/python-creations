# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 22:56:06 2017

@author: Ruby Kumar

EXERCISE: Create a program that asks the 
user for a number and then prints out a 
list of all the divisors of that number. 
"""

number = eval(input("Enter your number to find its divisors: "))
divisors_list = []
for divisor in range(1, number + 1):
    if number % divisor == 0:
        divisors_list.append(divisor)
    else: 
        continue
print(divisors_list)
    

