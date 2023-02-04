#!/bin/bash/python3


string= input('Enter lowercase text: ')
new_string="" 
for i in string: 
   # 'ord' is used to find the ascii value 
   if ord(i) >=97 and ord(i)< 123: 
       #'chr' used to find the character from ascii value 
        new_string+=chr(ord(i)-32) 
   else: 
        new_string+=i 
print(new_string) 
