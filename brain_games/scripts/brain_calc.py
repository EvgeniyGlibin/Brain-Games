#!/usr/bin/env python3


from brain_games.cli import welcome_user
from brain_games.cli import congratulate_user
from brain_games.games.calc import is_calc
from brain_games.games.calc import random_expression

def main():
    welcome_user()
    is_calc()
    congratulate_user()
    random_expression()
    


if __name__ == '__main__':
    main()
