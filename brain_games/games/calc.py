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


def set_expression():
    digit_1 = get_random_number()
    digit_2 = get_random_number()
    arithmetic_operations = ['+', '-', '*']
    random_index = randint(0, len(arithmetic_operations) - 1)
    arithmetic_operation = arithmetic_operations[random_index]
    global expression
    expression = f"{digit_1} {arithmetic_operation} {digit_2}"
    return expression


def run_calculator():
    print('What is the result of the expression?')
    for _ in range(NUMBER_OF_ATTEPTS):
        ask_question(set_expression())
        print(enter_response(), end='')
        entered_response = input()
        if int(entered_response) == eval(expression):
            confirm_response()
        else:
            report_an_error(entered_response, eval(expression))
            try_again_user()
            break
    else:
        congratulate_user()
