#Print random number between 1 and 6
import random

def roll_dice(): 

    print('\nRolling the dice...')
    rolled = []
    dice_one = random.randint(1,6)
    dice_two = random.randint(1,6)
    dice_three = random.randint(1,6)

    rolled.append(dice_one)
    rolled.append(dice_two)
    rolled.append(dice_three)
    print('The values are:', dice_one, dice_two, dice_three)
    return rolled


def check_two_occurrences(arr):
    for num in arr: # iterate through the  elements in the array
        if arr.count(num) == 2: # count the occurrences of the current number
            return True
    return False
        
def check_three_occurrences(arr):
    for num in arr: # iterate through the  elements in the array
        if arr.count(num) == 3: # count the occurrences of the current number
            return True
    return False


def main():
    while True:
        input('\nPress Enter to roll the dice...')
        rolled = roll_dice()
        if check_two_occurrences(rolled):
            print('You rolled two of a kind!')
        if check_three_occurrences(rolled):
            print('You rolled three of a kind!')
        if not check_two_occurrences(rolled) and not check_three_occurrences(rolled):
            print('Pass to next player.')

if __name__ == '__main__':
    main()




