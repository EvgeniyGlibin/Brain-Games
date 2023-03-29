import random


GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_VALUE = 1
MAX_VALUE = 50
MIN_LENGTH = 5
MAX_LENGTH = 10


def get_arithmetic_progression():
    initial_term = random.randint(MIN_VALUE, MAX_VALUE)
    succeeding_term = random.randint(MIN_VALUE, MAX_VALUE)
    common_difference = succeeding_term - initial_term
    arithmetic_progression = []
    lenght_arithmetic_progression = random.randint(MIN_LENGTH, MAX_LENGTH)
    for _ in range(lenght_arithmetic_progression):
        arithmetic_progression.append(str(initial_term))
        initial_term += common_difference
    return arithmetic_progression


def get_values():
    progression = get_arithmetic_progression()
    random_tern = random.randint(0, len(progression) - 1)
    hidden_element = progression.pop(random_tern)
    progression.insert(random_tern, '..')
    question = ' '.join(progression)
    correct_answer = hidden_element
    return question, correct_answer
