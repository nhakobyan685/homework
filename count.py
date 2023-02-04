#!/bin/bash/python3


def custom_count(sequence, item):
    count = 0
    for el in sequence:
         if el == item:
            count += 1
    return count
   

sequence = [1, 2, 3, 1, 2, 1, 3, 4, 1, 2]
item = 1
result = custom_count(sequence, item)
print(result) 
