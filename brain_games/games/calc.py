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


def random_expression():
    digit_1 = is_random()
    digit_2 = is_random()
    arithmetic_operations = ['+', '-', '*']
    random_index = randint(0, len(arithmetic_operations) - 1)
    arithmetic_operation = arithmetic_operations[random_index]
    global expression
    expression = f"{digit_1} {arithmetic_operation} {digit_2}"
    return expression


def is_calc():
    print('What is the result of the expression?')
    for _ in range(NUMBER_OF_ATTEPTS):
        is_question(random_expression())
        print(is_answer(), end='')
        entered_response = input()
        if int(entered_response) == eval(expression):
            is_correct()
        else:
            is_wrong_answer(entered_response, eval(expression))
            try_again_user()
            break
    else:
        congratulate_user()


def main():
    is_calc()
    random_expression()


if __name__ == "__main__":
    main()
