#!bin/bash/python3




def guess_game(secret):
    x = ['x'] * len(secret)
    secret_x = ''.join(x)
    guess = ''

    while secret != guess:
        guess = input(f'What is the capital of France? {secret_x} > ').lower()
        if guess == secret:
            print('You win the game')
            break
        for i in range(len(secret)):
            if secret[i] == guess:
                x[i] = guess
        secret_x = ''.join(x)
        print(secret_x)
        if secret_x == secret:
            break

    print('You win the game')

secret = 'paris'
guess_game(secret)

