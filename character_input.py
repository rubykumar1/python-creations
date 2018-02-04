# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 17:43:10 2017

@author: Ruby Kumar

EXERCISE: Create a program that asks the user to enter their 
name and their age. Print out a message addressed to 
them that tells them the year that they will turn 
100 years old.Ruby
"""

#program only works with users 100 years or younger

name = input("Enter your name: ")
age = input("Enter your age: ")
actual_age = int(age)
num_years = 100 - actual_age #num_years is the number of years until 100 years old
century = 2017 + num_years #century is the year you will turn 100
print(name , ", you will turn 100 years old in the year" , century , ".")

