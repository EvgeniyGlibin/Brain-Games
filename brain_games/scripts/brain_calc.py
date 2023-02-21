#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.calc import is_calc


def main():
    welcome_user()
    is_calc()


if __name__ == '__main__':
    main()
