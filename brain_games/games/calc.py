from random import randint
from random import choices
from brain_games.cli import is_question


def random_expression():
    first_number = randint(1, 30)
    second_namber = randint(1, 15)
    list_arithmetic_operations = [' + ', ' - ', ' * ']
    arithmetic_operation = list_arithmetic_operations[randint(0, len(list_arithmetic_operations) - 1)]
    #random_operation = choices(('+', '-', '*'))
    print(str(first_number) + arithmetic_operation + str(second_namber))
    #print(type(arithmetic_operation))



def is_calc():
    print('What is the result of the expression?')


def main():
    is_calc()
    random_expression()


if __name__ == "__main__":
    main()