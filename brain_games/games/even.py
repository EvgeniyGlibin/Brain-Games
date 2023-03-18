from random import randint


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def play_the_game():
    random_digit = randint(1, 100)
    answer = random_digit % 2
    if answer == 1:
        answer_game = 'no'
    if answer == 0:
        answer_game = 'yes'
    return random_digit, answer_game    
   


def main():
    play_the_game()


if __name__ == "__main__":
    main()
