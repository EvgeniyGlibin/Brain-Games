#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.cli import is_question
from brain_games.cli import is_answer
from brain_games.cli import is_correct
from brain_games.cli import congratulate_user
from brain_games.cli import is_wrong_answer
from brain_games.cli import try_again_user
from brain_games.games.even import play_even
from brain_games.games.even import random_digit


def is_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 3
    while count > 0:
        is_question()
        random_digit()
        is_answer()
        entered_response = input()
        if entered_response == play_even():
            is_correct()
            count -= 1
        else:
            is_wrong_answer(entered_response, play_even())
            try_again_user()
            break
    else:
        congratulate_user()


def main():
    welcome_user()
    is_even()


if __name__ == '__main__':
    main()
