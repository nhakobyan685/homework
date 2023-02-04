#!bin/bash/python3


def custom_isalpha(string):
    for char in string:
        if ord(char) < 65 or (90 < ord(char) < 97) or ord(char) > 122:
            return False
    return True

string = input('Enter text: ')
result = custom_isalpha(string)
print(result) 

