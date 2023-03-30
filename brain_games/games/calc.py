import random


GAME_DESCRIPTION = 'What is the result of the expression?'
MIN_VALUE = 1
MAX_VALUE = 50


def set_expression(first_number, second_number):
    arithmetic_operations = ['+', '-', '*']
    random_index = random.randint(0, len(arithmetic_operations) - 1)
    arithmetic_operation = arithmetic_operations[random_index]
    expression = f"{first_number} {arithmetic_operation} {second_number}"
    return expression


def get_values():
    first_number = random.randint(MIN_VALUE, MAX_VALUE)
    second_number = random.randint(MIN_VALUE, MAX_VALUE)
    question = set_expression(first_number, second_number)
    correct_answer = str(eval(question))
    return question, correct_answer
