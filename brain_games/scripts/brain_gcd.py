#!/usr/bin/env python3

from brain_games.cli import welcome_user
from brain_games.games.gcd import is_gcd


def main():
    welcome_user()
    is_gcd()


if __name__ == '__main__':
    main()
