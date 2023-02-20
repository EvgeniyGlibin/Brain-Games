from random import randint
from random import choices
from brain_games.cli import is_question


def random_expression():
    first_number = randint(1, 30)
    second_namber = randint(1, 15)
    random_operation = choices(('+', '-', '*'))
    print(first_number, random_operation, second_namber)



def is_calc():
    print('What is the result of the expression?')


def main():
    is_calc()
    random_expression()


if __name__ == "__main__":
    main()