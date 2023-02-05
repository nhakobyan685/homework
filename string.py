#!/bin/bash/python3


st = ""
result = ""

# calculate the length of a string

st = "https://www.w3resource.net"
lenght = len(st)

print("Length string: ", lenght)


# get a string made of the first 2 and last 2 characters of a given string

st = "w3resource"

if len(st) < 2:
    result = ""
else:
    result = st[:2] + st[-2:]

print("Original string:", st)
print("The string made of the first 2 and last 2 characters:", result)


# changed to '$', except the first char itself

st = "restart"

first_char = st[0]
ns = first_char + st[1:].replace(first_char, "$")

print("Original string: ", st)
print("New string: ", ns)


# add 'ing' at the end of a given string (length should be at least 3)

st = "abc"

if len(st) >= 3:
    if st.endswith("ing"):
        st += "ly"
    else:
        st += "ing"

print("Modified string: ", st)


# replace sub_string

def replace_substring(st):
    not_index = st.find('not')
    poor_index = st.find('poor')
    if not_index != -1 and poor_index != -1 and poor_index > not_index:
        st = st[:not_index] + 'good' + st[poor_index + 4:]
    return st

print(replace_substring('The lyrics is not that poor!'))
print(replace_substring('The lyrics is poor!'))


# longest word

def longest_word(words):
    longest = ""
    length = 0
    for word in words:
        if len(word) > length:
            longest = word
            length = len(word)
    return longest, length

words = ['Hello', 'World', 'Exercises']
result = longest_word(words)
print("Longest word:", result[0])
print("Length of the longest word:", result[1])


#  change a given string to a newly string 

st = "hello"
new_string = st[-1] + st[1:-1] + st[0]
print(new_string)


#  input and prints the distinct words in sorted form (alphanumerically)

words = "red, white, black, red, green, black"
word_list = words.split(',')
distinct_words = sorted(set(word_list))
print(','.join(distinct_words))


# function to get a string made of 4 copies of the last two characters of a specified string (length must be at least 2).  

def insert_end(str):
    if len(str) >= 2:
        return str[-2:] * 4
    else:
        return str

print('insert_end Python -> ',insert_end("Python"))
print('insert_end Exercises -> ',insert_end("Exercises"))


#  function to get a string made of the first three characters of a specified string. If the length of the string is less than 3

def first_three(st):
    if len(st) < 3:
        return st
    return st[:3]

print('first_three ipy -> ',first_three("ipy"))
print('first_three python -> ',first_three("python"))

