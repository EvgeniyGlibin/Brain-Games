import prompt


NUMBER_OF_ATTEPTS = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    # global name
    # name = prompt.string('May I have your name? ')
    # print(f'Hello, {name}!')

def enter_name():
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    # return name


def ask_question(condition='question'):
    print(f'Question: {condition}')


def enter_answer():
    global entered_answer
    entered_answer = prompt.string('Your answer: ')
    return entered_answer


def enter_response():
    return 'Your answer: '


def confirm_response():
    print('Correct!')


def congratulate_user():
    print(f'Congratulations, {name}!')


def report_an_error(x='no', y='yes'):
    print(f"'{x}' is wrong answer ;(. Correct answer was '{y}'.")


def try_again_user():
    print(f"Let's try again, {name}!")


def main():
    welcome_user()
    ask_question()
    enter_response()
    confirm_response()
    congratulate_user()
    report_an_error()
    try_again_user()
    NUMBER_OF_ATTEPTS


if __name__ == "__main__":
    main()
