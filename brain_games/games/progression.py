from random import randint


def is_random():
    global digit_random_1
    digit_random_1 = randint(1, 100)
    global digit_random_2
    digit_random_2 = randint(1, 100)
    return f'{digit_random_1} {digit_random_2}'


def is_progression():
    print("Начинаем игру")
