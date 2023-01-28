#!/bin/bash/python3.10



secret = 'paris'
x = ['x'] * len(secret)
secret_x = ''.join(x)

while True:
     guess = input(f'What is capital of Franche: {secret_x } > ').lower()
     if guess == secret:
         print('You win game')
         break
     for i in range(len(secret)):
         if secret[i] == guess:
             x[i] = guess[0]
     s = ''.join(x)
     print(s)
     if s == secret:
         print('You win game')
         break
