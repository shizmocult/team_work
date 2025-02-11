def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def nsd(a, b):
    while b != 0:
        remainder = a - b * (a // b)  #remainder це з анг залишок
        a = b
        b = remainder
    return a
