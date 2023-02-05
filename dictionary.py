#!/bin/bash/python3


d = {}


#  sort (ascending and descending) a dictionary by value 

d = {'a': 1, 'b': 3, 'c': 2}
sorted_d = sorted(d.items(), key=lambda x: x[1])
print('ascending: ',sorted_d)

d = {'a': 1, 'b': 3, 'c': 2}
sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
print('descending: ',sorted_d)


# add a key to a dictionary.

d = {0: 10, 1: 20}

d[2] = 30

print('adding key: ',d)


# concatenate the following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic_final = {**dic1, **dic2, **dic3}

print('Dictionary concatenate: ',dic_final)


# check whether a given key already exists in a dictionary

d = {1: 10, 2: 20, 3: 30}

key = 3
if key in d:
    print(f"Key {key} there is such a key in the dictionary ")
else:
    print(f"Key {key} does not exist in the dictionary")


# sum dictionary values

def sum_dict(dic):
    return sum(dic.values())

d = {'a': 5, 'b': 4, 'c': 8}
print("Sum of the dictionary: ", sum_dict(d))


# removing a key from a dictionar

d = {'a': 1, 'b': 2, 'c': 3}

print('Orginal dictionary: ', d)
if 'b' in d:
    del d['b']

print('Remove key b:  ',d)


#  dublicate remove

d = {'a':1, 'b':2, 'c':3, 'a':4}

print(d)
result = {}

for key, value in d.items():
    if key not in result:
        result[key] = value

print('Remove duplicates update list: ',result)


# map two lists into a dictionary.

keys = ['a', 'b', 'c', 'd']
values = [1, 2, 3, 4]

d = dict(zip(keys, values))

print('Map two lists in dictionary: ', d)


#  sort a list alphabetically in a dictionary

d = {'key1': ['cat', 'dog', 'fish'], 'key2': ['apple', 'banana', 'cherry']}

for key in d:
    d[key].sort()

print('Sort list alphabetically result: ',d)


#  print a dictionary line by line 

d = {'key1': 'value1', 'key2': 'value2', 'key3': 'value3'}

print("print a dictionary line by line")

for k, v in d.items():
    print(k + ": " + v)


