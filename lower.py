#!/bin/bash/python3

str = input("Enter uppercase text):")
i = 0
ch2 = ''
# convert capital letter string to small letter string
while str[i:]:
    ch = ord(str[i])
    if ch > 64 and ch < 91:
        ch2 += chr(ch+32)
    else:
        ch2 += chr(ch)
    i += 1
print(ch2)
