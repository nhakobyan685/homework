#!/bin/bash/python3

t = (6, 4, 5, 9, 1)

# Creating a tuple

print(t)


# Creating a tuple with different data types

t = (3, 5.5, "test", (7, 9), True)

print(t)


# Create a tuple of numbers and print one item

print(t[2])


# Add an item to a tuple

new_tuple = t + (5,)

print(new_tuple)


# Convert a tuple to a string

st = str(t)

print(st)

# Create the colon of a tuple

colon = t[1:4]

print(colon)


# Convert a list to a tuple

nl = [1, 2, 4, 6, 0]

convert_tuple = tuple(nl)

print(convert_tuple)


# Reverse a tuple

reverse = t[::-1]

print(reverse)


# Print a tuple with string formatting

print(f"This is a tuple {t}")


# Convert a given tuple of positive integers into an integer

t = (10, 20, 40, 5, 70)
nst = ""
for i in t:
    nst += str(i)
num = int(nst)

print(num)

