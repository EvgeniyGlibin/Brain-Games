from random import randint


GAME_DESCRIPTION = 'What is the result of the expression?'


def set_expression():
    digit_1 = randint()
    digit_2 = randint()
    arithmetic_operations = ['+', '-', '*']
    random_index = randint(0, len(arithmetic_operations) - 1)
    arithmetic_operation = arithmetic_operations[random_index]
    expression = f"{digit_1} {arithmetic_operation} {digit_2}"
    return expression


def play_the_game():
    question = set_expression()
    correct_answer = str(eval(question))
    return question, correct_answer
