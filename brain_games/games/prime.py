import random


GAME_DESCRIPTION = 'Answer "yes" if given number is prime. ' \
    'Otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def check_for_prime(digit):
    answer = 'no'
    count = 0
    for i in range(2, digit // 2 + 1):
        if digit % i == 0:
            count += 1
    if count == 0 and digit != 1:
        answer = 'yes'
    return answer


def get_game_values():
    question = random.randint(MIN_VALUE, MAX_VALUE)
    correct_answer = check_for_prime(question)
    return question, correct_answer
