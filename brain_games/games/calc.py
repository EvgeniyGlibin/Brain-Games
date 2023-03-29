import random


GAME_DESCRIPTION = 'What is the result of the expression?'
MIN_VALUE = 1
MAX_VALUE = 50


def set_expression():
    digit_1 = random.randint(MIN_VALUE, MAX_VALUE)
    digit_2 = random.randint(MIN_VALUE, MAX_VALUE)
    arithmetic_operations = ['+', '-', '*']
    random_index = random.randint(0, len(arithmetic_operations) - 1)
    arithmetic_operation = arithmetic_operations[random_index]
    expression = f"{digit_1} {arithmetic_operation} {digit_2}"
    return expression


def get_values():
    question = set_expression()
    correct_answer = str(eval(question))
    return question, correct_answer
