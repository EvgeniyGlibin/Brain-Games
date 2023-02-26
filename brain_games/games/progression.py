from random import randint
from brain_games.cli import is_question
from brain_games.cli import is_answer
from brain_games.cli import is_correct
from brain_games.cli import is_wrong_answer
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def is_random():
    digit_random = randint(1, 50)
    return digit_random


def arifmetic_progression():
    first_element = is_random()
    second_element = is_random()
    step_progression = second_element - first_element
    list_of_elements = []
    for _ in range(randint(5, 10)):
        list_of_elements.append(str(first_element))
        first_element += step_progression
    random_list_element = randint(0, len(list_of_elements) - 1)
    global hidden_element
    hidden_element = list_of_elements.pop(random_list_element)
    list_of_elements.insert(random_list_element, '..')
    return ' '.join(list_of_elements)


def is_progression():
    print('What number is missing in the progression?')
    for _ in range(NUMBER_OF_ATTEPTS):
        is_question(arifmetic_progression())
        print(is_answer(), end='')
        entered_response = input()
        if entered_response == hidden_element:
            is_correct()
        else:
            is_wrong_answer(entered_response, hidden_element)
            try_again_user
            break
    else:
        congratulate_user()
