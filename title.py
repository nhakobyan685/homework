#!/bin/bash/python3


def custom_title(text):
    result = ""
    should_capitalize = True
    for char in text:
        if char == " ":
            should_capitalize = True
        elif should_capitalize:
            result += char.upper()
            should_capitalize = False
        else:
            result += char
    return result

text = input('Enter text: ') 
result = custom_title(text)
print(result) # outputs: "Hello, World!"

