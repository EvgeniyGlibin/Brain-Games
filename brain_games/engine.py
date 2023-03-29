from brain_games.cli import welcome_user
import prompt


NUMBER_OF_ROUNDS = 3


def play(game):
    name = welcome_user()
    print(game.GAME_DESCRIPTION)
    for _ in range(NUMBER_OF_ROUNDS):
        question_game, correct_answer = game.get_game_values()
        print(f'Question: {question_game}')
        entered_answer = prompt.string('Your answer: ')
        if entered_answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{entered_answer}' is wrong answer ;(.", end=' ')
            print(f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    else:
        print(f'Congratulations, {name}!')


def main():
    play()


if __name__ == '__main__':
    main()
