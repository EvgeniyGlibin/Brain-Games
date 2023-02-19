from random import randint


def random_digit():
    global digit
    digit = randint(1, 100)
    print(digit)


def play_even():
    answer = digit % 2
    if answer == 1:
        return 'no'
    if answer == 0:
        return 'yes'


def main():
    random_digit()
    play_even()


if __name__ == '__main__':
    main()
