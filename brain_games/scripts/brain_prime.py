#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.prime import play_prime


def main():
    welcome_user()
    play_prime()


if __name__ == "__main__":
    main()
