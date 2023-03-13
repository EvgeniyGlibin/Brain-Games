from random import randint
# from brain_games.cli import ask_question
# from brain_games.cli import enter_response
# from brain_games.cli import confirm_response
# from brain_games.cli import report_an_error
# from brain_games.cli import try_again_user
# from brain_games.cli import congratulate_user
# from brain_games.cli import NUMBER_OF_ATTEPTS


GAME_DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'

# def get_random_number():
#     digit = randint(1, 100)
#     return digit


def check_parity():
    random_digit = randint(1, 100)
    answer = random_digit % 2
    if answer == 1:
        answer_game = 'no'
    if answer == 0:
        answer_game = 'yes'
    return random_digit, answer_game


def show_game_description(game):
    return game.GAME_DESCRIPTION




def main():
    check_parity()
    


if __name__ == "__main__":
    main()

