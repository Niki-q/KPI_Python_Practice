import math


def root2(n):
    while True:
        if n != abs(n):
            n = float(input("Please re-enter n, n - Positive value: "))
        else:
            break
    return math.sqrt(n)


def root3(n):
    if n < 0:
        n = abs(n)
        return -math.pow(n, 1 / 3)
    return math.pow(n, 1 / 3)


