import math


def log(a, b):
    while True:
        if a < 0 or a == 1:
            a = input("Please re-enter a, 'a' must be >0 and != 1 : ")
        else:
            break
    while True:
        if b < 0:
            b = input("Please re-enter b, 'b' must be >0 : ")
        else:
            break
    return math.log(b,a)


def ln(b):
    while True:
        if b < 0:
            b = input("Please re-enter b, 'b' must be >0 : ")
        else:
            break
    return math.log1p(b)


def lg(b):
    while True:
        if b < 0:
            b = input("Please re-enter b, 'b' must be >0 : ")
        else:
            break
    return math.log10(b)