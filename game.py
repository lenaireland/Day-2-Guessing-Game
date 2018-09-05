"""A number-guessing game."""

from random import randint

print('Welcome to the number guessing game!')
playername = input('What is your name? ')

def number_guess():
    number = randint(1,100)
    print(number)

    i = 0

    # while True:
    #     i += 1
    #     guess = int(input('Guess my number between 1 and 100! '))
    #     # if guess != number:

    #     # if guess is not between 1 and 100, then..0
    #         # give error message, please enter valid number
    #     # (else) if valid number:
    #         # 

    #     if guess > number:
    #         print('Your guess is too high, try again')
    #         #i += 1
    #     elif guess < number:
    #         print('Your guess is too low, try again')
    #         #i += 1
    #     else:
    #         print('Well done, {}! You found my number in {} tries'.format(playername,i))
    #         break


    guess = int()
    while not guess == number:
        i += 1
        # guess = int(input('Guess my number between 1 and 100! '))
        while True:
            try:
                guess = int(input('Guess my number between 1 and 100! '))
                break
            except ValueError:
                print("That's not an int! Please enter a valid integer!")

        if guess > 100 or guess < 1:
            print("Can't you read? Your number must be between 1 and 100. Try again!")
        elif guess > number:
            print('Your guess is too high, try again')
        elif guess < number:
            print('Your guess is too low, try again')
    print('Well done, {}! You found my number in {} tries'.format(playername,i))



number_guess()
# Put your code here
