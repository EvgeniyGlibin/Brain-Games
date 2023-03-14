from brain_games import cli


NUMBER_OF_ATTEPTS = 3


def start_game(game):
    cli.welcome_user()
    cli.enter_name()
    print(game.GAME_DESCRIPTION)
    for _ in range(NUMBER_OF_ATTEPTS):
        question_game, correct_answer = game.check_parity()
        cli.ask_question(question_game)
        entered_answer = cli.enter_answer()
        if entered_answer == correct_answer:
            cli.confirm_response()
        else:
            cli.report_an_error(entered_answer, correct_answer)
            cli.try_again_user()
            break
    else:
        cli.congratulate_user()


def main():
    start_game()


if __name__ == '__main__':
    main()
