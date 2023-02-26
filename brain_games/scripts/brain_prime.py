#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.prime import is_prime


def main():
    welcome_user()
    is_prime()


if __name__ == "__main__":
    main()
