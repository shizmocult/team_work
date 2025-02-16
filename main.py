from utils import factorial, nsd

print(f"Factorial of 5: {factorial(5)}")

print("Найбільший спільний дільник:", nsd(x, y))

from utils import is_prime

number = 11
if is_prime(number):
    print(f"{number} is prime")
else:
    print(f"{number} is not prime")

