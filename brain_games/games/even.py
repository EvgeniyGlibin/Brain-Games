from random import randint
from brain_games.cli import ask_question
from brain_games.cli import enter_response
from brain_games.cli import confirm_response
from brain_games.cli import report_an_error
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def get_random_number():
    global digit
    digit = randint(1, 100)
    return digit


def check_parity():
    answer = digit % 2
    if answer == 1:
        return 'no'
    if answer == 0:
        return 'yes'


def play_even():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(get_random_number())
        print(enter_response(), end='')
        entered_response = input()
        if entered_response == check_parity():
            confirm_response()
        else:
            report_an_error(entered_response, check_parity())
            try_again_user()
            break
    else:
        congratulate_user()
