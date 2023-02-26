from random import randint
from brain_games.cli import ask_question
from brain_games.cli import enter_response
from brain_games.cli import confirm_response
from brain_games.cli import report_an_error
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def get_random_number():
    digit_random = randint(1, 50)
    return digit_random


def get_the_progression():
    first_element = get_random_number()
    second_element = get_random_number()
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


def play_progression():
    print('What number is missing in the progression?')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(get_the_progression())
        print(enter_response(), end='')
        entered_response = input()
        if entered_response == hidden_element:
            confirm_response()
        else:
            report_an_error(entered_response, hidden_element)
            try_again_user
            break
    else:
        congratulate_user()
