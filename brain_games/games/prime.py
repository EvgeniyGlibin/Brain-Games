from random import randint
from brain_games.cli import is_question
from brain_games.cli import is_answer
from brain_games.cli import is_correct
from brain_games.cli import is_wrong_answer
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def random_digit():
    global digit
    digit = randint(1, 100)
    return digit


def play_prime():
    count = 0
    for i in range(2, digit // 2 + 1):
        if digit % i == 0:
            count += 1
    if count == 0:
        return 'yes'
    return 'no'


def is_prime():
    print('Answer "yes" if given number is prime. Otherwise answer "no"')
    for _ in range(NUMBER_OF_ATTEPTS):
        is_question(random_digit())
        print(is_answer(), end='')
        entered_response = input()
        if entered_response == play_prime():
            is_correct()
        else:
            is_wrong_answer(entered_response, play_prime())
            try_again_user()
            break
    else:
        congratulate_user()
