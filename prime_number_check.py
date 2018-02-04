# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 18:56:45 2017

@author: Agni Kumar

EXERCISE: Ask the user for a number and determine if it is prime or not.
"""
divisors_list = []
def prime_check():
    number = eval(input("Type a number to check its primality: "))
    sqrt_number = int(number ** (0.5))
                     
    for divisor in range(2, sqrt_number + 1):
        if number % divisor == 0:
            divisors_list.append(divisor)
        else:
            continue
    if len(divisors_list) == 0:
        print("The number", number, "is prime.")
    else:
        print("The number", number, "is not prime.")
prime_check()

