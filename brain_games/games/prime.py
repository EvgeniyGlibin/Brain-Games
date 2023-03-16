from random import randint


GAME_DESCRIPTION = 'Answer "yes" if given number is prime.'\
    'Otherwise answer "no".'


def play_the_game():
    digit = randint(1, 100)
    count = 0
    for i in range(2, digit // 2 + 1):
        if digit % i == 0:
            count += 1
    if count == 0 and digit != 1:
        answer_game = 'yes'
    else:
        answer_game = 'no'
    return digit, answer_game
