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


def try_again_user():
    print(f"Let's try again, {name}!")


def main():
    welcome_user()
    is_question()
    is_answer()
    congratulate_user()
    try_again_user()
    is_correct


if __name__ == "__main__":
    main()
