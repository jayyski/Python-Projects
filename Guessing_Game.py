def main():
    guessing_Game()

#Random number from range 1-100
def random_Number():
    import random
    return random.randint(1, 100)

##Accepts user input make sure its a number
def user_Input():
    while True:
        try:
            user_input = int(input('Guess: '))
            return user_input
        except ValueError:
            print('Please enter a number')
            continue

#Guessing game
def guessing_Game():
    print('Guess a number between 1 and 100')
    number = random_Number()
    num_guesses = 10
    while num_guesses > 0:
        guess = user_Input()
        if guess == number:
            print('You got it!')
            return
        elif guess < number:
            print('Too low')
        else:
            print('Too high')
        num_guesses -= 1
        print(f'You have {num_guesses} guesses left.')
    print(f'Sorry, you ran out of guesses. The number was {number}.')

def main():
    guessing_Game()


if __name__ == '__main__':
    main()