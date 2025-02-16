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

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

