# Import randint function that returns a random number
from random import randint

# Create a list with options
options = ['Rock', 'Paper', 'Scissor']

# Add the computer to play respecting the options
computer = options[randint(0, 2)]

# Add the player as false
player = False

while not player:
    player = input('Rock, Paper, Scissor? ')
    if player == computer:
        print('Draw!')
    elif player == 'Rock':
        if computer == 'Paper':
            print('You lose', computer, 'wraps', player)
        else:
            print('You win!', player, 'smashes', computer)
    elif player == 'Paper':
        if computer == 'Scissor':
            print('You lose', computer, 'cuts', player)
        else:
            print('You win!', player, 'wraps', computer)
    elif player == 'Scissor':
        if computer == 'Rock':
            print('You lose', computer, 'smashes', player)
        else:
            print('You win!', player, 'cuts', computer)
    else:
        print('This is an invalid option. Check your orthography!')

    # To continue the game
    player = False
    computer = options[randint(0, 2)]
