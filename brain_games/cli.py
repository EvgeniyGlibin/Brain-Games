import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

# def enter_name():
#     global name
#     name = prompt.string('May I have your name? ')
#     print(f'Hello, {name}!')


def ask_question(condition):
    print(f'Question: {condition}')


def enter_answer():
    entered_answer = prompt.string('Your answer: ')
    return entered_answer


def confirm_response():
    print('Correct!')


def congratulate_user():
    print(f'Congratulations, {name}!')


def report_an_error(entered_answer, correct_answer):
    print(f"'{entered_answer}' is wrong answer ;(.", end=' ')
    print(f"Correct answer was '{correct_answer}'.")


def try_again_user():
    print(f"Let's try again, {name}!")


def main():
    welcome_user()
    ask_question()
    confirm_response()
    congratulate_user()
    report_an_error()
    try_again_user()


if __name__ == "__main__":
    main()
