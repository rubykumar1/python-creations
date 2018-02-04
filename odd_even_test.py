# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 21:52:56 2017

@author: Ruby Kumar

# EXERCISE: writing sample code to test odd and even numbers

"""

def classify(n):
    if n%2 == 1:
        return("Weird")
    elif n >= 6 and n <= 20 and n%2 == 0:
        return("Weird")  
    else:
        return("Not weird")
    
print(classify(60)) #test


    
    
                
    