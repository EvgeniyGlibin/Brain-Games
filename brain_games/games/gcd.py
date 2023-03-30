import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_VALUE = 1
MAX_VALUE = 50


def get_gcd(first_number, second_number):
    large_number = max(first_number, second_number)
    lower_number = min(first_number, second_number)
    remains = 1
    while remains > 0:
        remains = large_number % lower_number
        large_number, lower_number = lower_number, remains
    return large_number


def get_values():
    first_number = random.randint(MIN_VALUE, MAX_VALUE)
    second_number = random.randint(MIN_VALUE, MAX_VALUE)
    question = f'{first_number} {second_number}'
    correct_answer = str(get_gcd(first_number, second_number))
    return question, correct_answer
