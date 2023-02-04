#!bin/bash/python3


string = input('Enter text with space: ')
result = ""

for i in string:
    if i != " ":
        result += i 

result = result.rstrip()
print(result)

