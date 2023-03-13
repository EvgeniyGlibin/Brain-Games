import prompt
# import brain_games.games.even
# from random import randint
# from brain_games.cli import ask_question
from brain_games.cli import enter_answer
# from brain_games.cli import entered_answer
from brain_games.cli import confirm_response
from brain_games.cli import report_an_error
from brain_games.cli import try_again_user
from brain_games.cli import congratulate_user
# from brain_games.cli import NUMBER_OF_ATTEPTS
from brain_games.games.even import show_game_description
from brain_games.cli import welcome_user
from brain_games.cli import enter_name


GAME_DESCRIPTION = 'DDDescription'
NUMBER_OF_ATTEPTS = 3


# def welcome_user():
#     print("Welcome to the Brain Games!")


# def enter_name():
#     global name
#     name = prompt.string('May I have your name? ')
#     print(f'Hello, {name}!')
    

# def show_game_description():
    # return GAME_DESCRIPTION


def ask_question(condition='question'):
    print(f'Question: {condition}')


# def enter_answer():
#     global entered_answer
#     entered_answer = prompt.string('Your answer: ')
#     # return entered_answer



def start_game(game):
    welcome_user()
    enter_name()
    print(show_game_description(game))
    print()
    for _ in range(NUMBER_OF_ATTEPTS):
        question_game, correct_answer = game.check_parity()
        print(question_game)
        print(correct_answer)
        ask_question(question_game)
        if enter_answer() == correct_answer:
            confirm_response()
        else:
            report_an_error('пример', correct_answer)
            try_again_user()
            break
    congratulate_user()





def main():
    start_game()


if __name__ == '__main__':
    main()