import random


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def get_random_digit():
    random_digit = random.randint(MIN_VALUE, MAX_VALUE)
    return random_digit


def check_for_even(digit):
    answer = 'yes'
    if digit % 2 == 1:
        answer = 'no'
    return answer


def get_game_values():
    question = get_random_digit()
    correct_answer = check_for_even(question)
    return question, correct_answer
