from random import randint


GAME_DESCRIPTION = 'Find the greatest common divisor of given numbers.'
MIN_VALUE = 1
MAX_VALUE = 50


def get_random_digit():
    random_digit = randint(MIN_VALUE, MAX_VALUE)
    return random_digit


def get_divisors(number):
    list_divisors = [number]
    for i in range(1, number // 2 + 1):
        if number % i == 0:
            list_divisors.append(i)
    sorted_list_divisors = sorted(list_divisors)
    return sorted_list_divisors


def play_the_game():
    first_number = get_random_digit()
    second_number = get_random_digit()
    list_of_divisors_1 = get_divisors(first_number)
    list_of_divisors_2 = get_divisors(second_number)
    for i in range(1, len(list_of_divisors_1) + 1):
        if list_of_divisors_1[-i] in list_of_divisors_2:
            max_common_divisor = list_of_divisors_1[-i]
            correct_answer = str(max_common_divisor)
            question = f'{first_number} {second_number}'
            return question, correct_answer


# def get_gcd(a, b):
#     first_digit = max(a, b)
#     second_digit = min(a, b)
#     remains = 1
#     while remains > 0:
#         remains = first_digit % second_digit
#         first_digit, second_digit = second_digit, remains
#     return first_digit
