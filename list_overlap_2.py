"""Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements
that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes.

EXTRA: Randomly generate two lists."""

import random
from random import randint

list1_len = randint(10, 15)
list2_len = randint(10, 15)
list1 = []
list2 = []
new_list = []

for num in range(list1_len):
    number = randint(1, 50)
    list1.append(number)
print("List 1:", list1)

for num in range(list2_len):
    number = randint(1, 50)
    list2.append(number)
print("List 2:", list2)

for number in list1:
    if number in list2 and number not in new_list:
        new_list.append(number)
    else:
        continue
print("Common numbers:", new_list)



        
