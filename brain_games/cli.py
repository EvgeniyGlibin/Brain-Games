import prompt


def welcome_user():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')


def congratulate_user():
    print(f'Congratulations, {name}!')


def try_again_user():
    print(f"Let's try again, {name}!")


def main():
    welcome_user()
    congratulate_user()
    try_again_user()


if __name__ == "__main__":
    main()
