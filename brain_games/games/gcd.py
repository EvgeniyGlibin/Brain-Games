from random import randint


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def get_random_number():
    digit_random = randint(1, 50)
    return digit_random


def get_divisors(number):
    list_of_divisors = [number]
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            list_of_divisors.append(i)
    list_divisors = sorted(list_of_divisors)
    return list_divisors


def play_the_game():
    first_number = get_random_number()
    second_number = get_random_number()
    list_of_divisors_1 = get_divisors(first_number)
    list_of_divisors_2 = get_divisors(second_number)
    for i in range(1, len(list_of_divisors_1) + 1):
        if list_of_divisors_1[-i] in list_of_divisors_2:
            max_common_divisor = list_of_divisors_1[-i]
            correct_answer = str(max_common_divisor)
            question = f'{first_number} {second_number}'
            return question, correct_answer
