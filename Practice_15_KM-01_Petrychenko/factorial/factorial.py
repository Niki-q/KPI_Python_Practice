def fact(n):
    while True:
        if n != int(n):
            n = input("Please re-enter n, n - Integer value: ")
        else:
            break
    if n == 1:
        return 1
    return n * fact(n-1)
