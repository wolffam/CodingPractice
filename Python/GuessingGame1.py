# Generate random # 1-9, ask for user guess, and return feedback until they get it correct
import random


def main():
    rand_num = random.randint(1,9)
    count = 0
    while True:
        count += 1
        try:
            user_guess = int(input('Guess an integer from 1-9...'))
        except ValueError:
            print('Please provide an integer 1 <= N <= 9')
        if user_guess > 9 or user_guess < 1:
            print('IMPROPER GUESS!!! Try again :P\n')
        elif user_guess > rand_num:
            print('Your guess is too high! Try again :P')
        elif user_guess < rand_num:
            print('Your guess is too low! Try again :P')
        else:
            print('\nCongratulations!!! You found it!')
            print('It only took you {} tries! :P'.format(count))
            break


if __name__ == '__main__':
    main()