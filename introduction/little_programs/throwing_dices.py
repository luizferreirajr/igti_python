import random
min_dice = 1  # Minimum value a dice shows
max_dice = 6  # Maximum value a dice shows

play_again = 'yes'
dice_quant = int(input('How many dices do you want?: '))


while play_again == 'yes' or play_again == 'y':
    print('Throwing ' + str(dice_quant) + ' dices...')
    print('The values are....')
    for i in range(1, dice_quant+1):
        random_dice = random.randint(min_dice, max_dice)
        print('Dice ' + str(i) + ': ' + str(random_dice))

    play_again = input('Do you want to play again? ')
    dice_quant = int(input('How many dices do you want?: '))