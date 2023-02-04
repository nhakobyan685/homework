#!/bin/bash/python3


def my_find(string, substring):
    for i in range(len(string)):
        if string[i:i + len(substring)] == substring:
            return i
    return -1


string = input('Enter hellow world: ')
substring = "world"
index = my_find(string, substring)
print(index) 

