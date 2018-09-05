"""A number-guessing game."""

from random import randint

print('Welcome to the number guessing game!')
playername = input('What is your name? ')

def number_guess():
    number = randint(1,100)
    print(number)

number_guess()
# Put your code here
