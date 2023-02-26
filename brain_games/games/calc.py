from random import randint
from brain_games.cli import is_question
from brain_games.cli import is_answer
from brain_games.cli import is_correct
from brain_games.cli import is_wrong_answer
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
from brain_games.cli import NUMBER_OF_ATTEPTS


def random_expression():
    first_number = randint(1, 30)
    second_number = randint(1, 15)
    list_arithmetic_operations = ['+', '-', '*']
    arithmetic_operation = list_arithmetic_operations[
        randint(0, len(list_arithmetic_operations) - 1)]
    global arithmetic_expression
    arithmetic_expression = f"{first_number} {arithmetic_operation} {second_number}"
    return arithmetic_expression


def is_calc():
    print('What is the result of the expression?')
    for _ in range(NUMBER_OF_ATTEPTS):
        is_question(random_expression())
        print(is_answer(), end='')
        entered_response = input()
        if int(entered_response) == eval(arithmetic_expression):
            is_correct()
        else:
            is_wrong_answer(entered_response, eval(arithmetic_expression))
            try_again_user()
            break
    else:
        congratulate_user()


def main():
    is_calc()
    random_expression()


if __name__ == "__main__":
    main()
