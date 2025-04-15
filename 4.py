#1
import string

print("Uppercase letters:")
print(" ".join(string.ascii_uppercase))

print("Lowercase letters:")
print(" ".join(string.ascii_lowercase))

#2
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

#3
s = input("Enter a string: ")
alphabets = sum(c.isalpha() for c in s)
digits = sum(c.isdigit() for c in s)

print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")

#4
import math

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n):
    digits = len(str(n))
    return sum(int(d)**digits for d in str(n)) == n

def is_palindrome(n):
    return str(n) == str(n)[::-1]

def is_automorphic(n):
    return str(n*n).endswith(str(n))

num = int(input("Enter a number: "))
print(f"Prime: {is_prime(num)}")
print(f"Perfect: {is_perfect(num)}")
print(f"Armstrong: {is_armstrong(num)}")
print(f"Palindrome: {is_palindrome(num)}")
print(f"Automorphic: {is_automorphic(num)}")

#5
for a in range(1, 31):
    for b in range(a, 31):
        c = math.sqrt(a*a + b*b)
        if c.is_integer() and c <= 30:
            print(f"({a}, {b}, {int(c)})")

#6
for hour in range(24):
    if hour == 0:
        print("12 Midnight")
    elif hour < 12:
        print(f"{hour} AM")
    elif hour == 12:
        print("12 Noon")
    else:
        print(f"{hour - 12} PM")

#7
import math

n = int(input("Enter n: "))
r = int(input("Enter r: "))

nCr = math.comb(n, r)
nPr = math.perm(n, r)

print(f"nCr = {nCr}")
print(f"nPr = {nPr}")

#8
n = int(input("Enter a number: "))
fact = math.factorial(n)
print(f"Factorial = {fact}")

#9
n = int(input("Enter N: "))
for i in range(n, 0, -1):
    print(i, end=" ")
print()

#10
n = int(input("Enter number of terms: "))
a, b = 0, 1

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

#11
def sin_x(x, terms=5):
    result = 0
    for i in range(terms):
        sign = (-1) ** i
        term = (x ** (2*i + 1)) / math.factorial(2*i + 1)
        result += sign * term
    return result

degrees = float(input("Enter angle in degrees: "))
radians = math.radians(degrees)
print(f"sin({degrees}°) ≈ {sin_x(radians):.5f}")