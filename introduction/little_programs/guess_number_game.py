import random

# importing random module randint to generate a random int number
number = random.randint(1, 99)

guess = int(input('Guess a number between 1 and 99: '))

while guess != number:
    print()
    if guess < number:
        guess = int(input('Too low, guess again: '))
    elif guess > number:
        guess = int(input('Too high, guess again: '))
    else:
        break # using break to stop the while loop showing the message bellow.
print('Finally!, right number: ' + str(number))
