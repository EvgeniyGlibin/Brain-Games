from random import randint
from brain_games.cli import ask_question
from brain_games.cli import enter_response
from brain_games.cli import confirm_response
from brain_games.cli import report_an_error
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def get_random_number():
    global digit_random_1
    global digit_random_2
    digit_random_1 = randint(1, 50)
    digit_random_2 = randint(1, 50)
    return f'{digit_random_1} {digit_random_2}'


def get_divisors(number):
    number = int(number)
    list_of_divisors = [number]
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    return sorted(list_of_divisors)


def get_max_common_divisor(first_number, second_number):
    list_of_divisors_1 = get_divisors(first_number)
    list_of_divisors_2 = get_divisors(second_number)
    for i in range(1, len(list_of_divisors_1) + 1):
        if list_of_divisors_1[-i] in list_of_divisors_2:
            return list_of_divisors_1[-i]


def play_gcd():
    print('Find the greatest common divisor of given numbers.')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(get_random_number())
        correct_answer = get_max_common_divisor(digit_random_1, digit_random_2)
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
