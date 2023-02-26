#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.games.even import play_even


def main():
    welcome_user()
    play_even()


if __name__ == '__main__':
    main()
