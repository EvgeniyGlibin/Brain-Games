import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def is_question():
    print('Question: ')


def is_answer():
    print('Your answer: ')


def is_correct():
    print('Correct!')


def congratulate_user():
    print(f'Congratulations, {name}!')


def is_wrong_answer(x='no', y='yes'):
    print(f"'{x}' is wrong answer ;(. Correct answer was '{y}'.")


def try_again_user():
    print(f"Let's try again, {name}!")


def main():
    welcome_user()
    is_question()
    is_answer()
    is_correct()
    congratulate_user()
    is_wrong_answer()
    try_again_user()


if __name__ == "__main__":
    main()
