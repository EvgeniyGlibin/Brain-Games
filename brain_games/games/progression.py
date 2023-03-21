from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_VALUE = 1
MAX_VALUE = 50
MIN_LENGTH_PROGRESSION = 5
MAX_LENGTH_PROGRESSION = 10


def get_random_number():
    digit_random = randint(MIN_VALUE, MAX_VALUE)
    return digit_random


def play_the_game():
    initial_term = get_random_number()
    succeeding_term = get_random_number()
    common_difference = succeeding_term - initial_term
    arithmetic_progression = []
    for _ in range(randint(MIN_LENGTH_PROGRESSION, MAX_LENGTH_PROGRESSION)):
        arithmetic_progression.append(str(initial_term))
        initial_term += common_difference
    random_tern = randint(0, len(arithmetic_progression) - 1)
    hidden_element = arithmetic_progression.pop(random_tern)
    arithmetic_progression.insert(random_tern, '..')
    question = ' '.join(arithmetic_progression)
    correct_answer = hidden_element
    return question, correct_answer
