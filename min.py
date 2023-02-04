#!/bin/bash/python3



def custom_min(numbers):
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

numbers = [3, 4, 1, 5, 2]
minimum = custom_min(numbers)
print(minimum) # Outputs: 1
