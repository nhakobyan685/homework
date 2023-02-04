#!bin/bash/python3


def split(string, delimiter):
    result = []
    current_word = ""
    for char in string:
        if char == delimiter:
            result.append(current_word)
            current_word = ""
        else:
            current_word += char
    result.append(current_word)
    return result

# usage example
string = input('Enter text: ')
delimiter = ","
result = split(string, delimiter)
print(result)

