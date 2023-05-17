def for_factorial(n):
    n = int(input())

    factorial = 1

    for i in range(2, n + 1):
        factorial *= i

    return factorial


def rec_factorial(n):
    if n == 1:
        return 1
    return rec_factorial(n - 1) * n