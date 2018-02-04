# -*- coding: utf-8 -*-
"""
Created on Sat Dec  2 08:24:28 2017

@author: Ruby Kumar

EXERCISE:Ask the user for a string and 
print out whether this string is a 
palindrome or not. (A palindrome is a 
string that reads the same forwards and 
backwards.)
"""
number = input("Enter a number: ") 
num_list = [int(digit) for digit in str(number)] 
if num_list == list(reversed(num_list)):
    print("Your number is a palindrome.")
else:
    print("Your number is not a palindrome.")


