import random


DESCRIPTION = 'Answer "yes" if given number is prime. ' \
    'Otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def check_for_prime(digit):
    result = False
    count = 0
    for i in range(2, digit // 2 + 1):
        if digit % i == 0:
            count += 1
    if count == 0 and digit != 1:
        result = True
    return result


def is_prime(digit):
    if check_for_prime(digit):
        return 'yes'
    else:
        return 'no'


def get_values():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = is_prime(question)
    # correct_answer = 'yes' if check_for_prime(question) else 'no'
    return question, correct_answer
