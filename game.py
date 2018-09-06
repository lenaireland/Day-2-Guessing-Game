"""A number-guessing game."""

from random import randint

print('Welcome to the number guessing game!')
playername = input('What is your name? ')

def number_guess():
    play_again = 'y'
    best_score = 1000000000000
    max_tries = 10


    while play_again.lower() == 'y':

        number = randint(1,100)
        print(number)

        i = 0
        guess = int()

        while i < max_tries:
            i += 1

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
            else:
                print('Well done, {}! You found my number in {} tries'.format(playername,i))
                if i < best_score:
                    best_score = i
                print('Your current best is {} tries.'.format(best_score))
                break

        if i == max_tries:
            print("Too many tries!")

        play_again = input('Do you want to play again (Y) or (N)? ')

number_guess()

