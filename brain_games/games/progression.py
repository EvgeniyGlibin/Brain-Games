from random import randint


GAME_DESCRIPTION = 'What number is missing in the progression?'
MIN_LENGTH_PROGRESSION = 5
MAX_LENGTH_PROGRESSION = 10


def get_random_number():
    digit_random = randint(1, 50)
    return digit_random


def play_the_game():
    first_element = get_random_number()
    second_element = get_random_number()
    step_progression = second_element - first_element
    list_of_elements = []
    for _ in range(randint(MIN_LENGTH_PROGRESSION, MAX_LENGTH_PROGRESSION)):
        list_of_elements.append(str(first_element))
        first_element += step_progression
    random_list_element = randint(0, len(list_of_elements) - 1)
    hidden_element = list_of_elements.pop(random_list_element)
    list_of_elements.insert(random_list_element, '..')
    question = ' '.join(list_of_elements)
    correct_answer = hidden_element
    return question, correct_answer
