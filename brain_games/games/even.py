from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'
MIN_VALUE = 1
MAX_VALUE = 100


def get_random_digit():
    random_digit = randint(MIN_VALUE, MAX_VALUE)
    return random_digit


def check_for_even(digit):
    answer = 'yes'
    if digit % 2 == 1:
        answer = 'no'
    return answer


def play_the_game():
    question = get_random_digit()
    correct_answer = check_for_even(question)
    return question, correct_answer
