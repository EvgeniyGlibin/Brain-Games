#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.games.progression import is_progression


def main():
    welcome_user()
    is_progression()


if __name__ == "__main__":
    main()