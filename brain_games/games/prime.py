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


def check_the_number_prime():
    count = 0
    for i in range(2, digit // 2 + 1):
        if digit % i == 0:
            count += 1
    if count == 0:
        return 'yes'
    return 'no'


def play_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(get_random_number())
        print(enter_response(), end='')
        entered_response = input()
        if entered_response == check_the_number_prime():
            confirm_response()
        else:
            report_an_error(entered_response, check_the_number_prime())
            try_again_user()
            break
    else:
        congratulate_user()
