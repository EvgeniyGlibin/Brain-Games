#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.cli import congratulate_user


def main():
    welcome_user()
    print("This is brain-calc")
    congratulate_user()


if __name__ == '__main__':
    main()
