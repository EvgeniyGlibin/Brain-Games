#!/usr/bin/env python3


#from brain_games.cli import welcome_user
from random import randint
import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')


def is_even():
    count = 0
    while count < 3:
        digit = randint(1, 100)
        print(f'Question: {digit}')
        print('You answer: ', end='')
        answer = input()
        if digit % 2 == 0:
            if answer == "yes":
                print('Correct!')
                count += 1
            else:
                print(f"'no' is wrong answer ;(. Correct answer was 'yes'.Let's try again, {name}!")
                break
        if digit % 2 == 1:
            if answer == "no":
                print('Correct!')
                count += 1
            else:
                print(f"'yes' is wrong answer ;(. Correct answer was 'no'.Let's try again, {name}!")
                break
    print(f'Congratulations, {name}')

def main():
    welcome_user()
    is_even()


if __name__ == '__main__':
    main()
