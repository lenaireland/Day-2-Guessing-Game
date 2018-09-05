"""A number-guessing game."""

from random import randint

print('Welcome to the number guessing game!')
playername = input('What is your name? ')

def number_guess():
    number = randint(1,100)
    print(number)

    i = 1
    while True:
        guess = int(input('Guess my number... '))
        # if guess != number:
        if guess > number:
            print('Your guess is too high, try again')
            i += 1
        elif guess < number:
            print('Your guess is too low, try again')
            i += 1
        else:
            print('Well done, {}! You found my number in {} tries'.format(playername,i))
            break

number_guess()
# Put your code here
