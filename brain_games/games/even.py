import random


DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def check_for_even(digit):
    result = True
    if digit % 2 == 1:
        result = False
    return result


# def is_even(digit):
#     if check_for_even(digit):
#         return 'yes'
#     else:
#         return 'no'


def get_values():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    # correct_answer = is_even(question)
    # как лучше, через тернарное условие или заменить на функцию is_even()?
    correct_answer = 'yes' if check_for_even(question) else 'no'
    return question, correct_answer
