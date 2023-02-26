#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.calc import run_calculator


def main():
    welcome_user()
    run_calculator()


if __name__ == '__main__':
    main()
