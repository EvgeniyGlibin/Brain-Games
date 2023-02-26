def is_prime():
    print('Игра простое число')


def play_prime(x):
    count = 0
    for i in range(2, x//2 + 1):
        if x % i == 0:
            count += 1
    if count == 0:
        return 'yes'
    return 'no'
