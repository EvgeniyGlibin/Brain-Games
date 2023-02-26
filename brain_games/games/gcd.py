from random import randint
from brain_games.cli import ask_question
from brain_games.cli import enter_response
from brain_games.cli import confirm_response
from brain_games.cli import report_an_error
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def get_random_number():
    digit_random_1 = randint(1, 100)
    digit_random_2 = randint(1, 100)
    global digit_random
    digit_random = f'{digit_random_1} {digit_random_2}'
    return digit_random


def is_divider(number='3'):
    number = int(number)
    lst = [number]
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            lst.append(i)
    return sorted(lst)


def is_list(index_list_0=[], index_list_1=[]):
    list_1 = is_divider(index_list_0)
    list_2 = is_divider(index_list_1)
    for i in range(1, len(list_1) + 1):
        if list_1[-i] in list_2:
            return list_1[-i]


def is_gcd():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(get_random_number())
        lst_digit = digit_random.split()
        correct_answer = is_list(lst_digit[0], lst_digit[1])
        print(enter_response(), end='')
        entered_response = input()
        if int(entered_response) == correct_answer:
            confirm_response()
        else:
            report_an_error(entered_response, correct_answer)
            try_again_user()
            break
    else:
        congratulate_user()
