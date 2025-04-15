#function part-1
#1
def count_lower_upper(string):
    lower = 0
    upper = 0
    for char in string:
        if char.isalpha():
            if char.islower():
                lower += 1
            else:
                upper += 1
    return {'upper': upper, 'lower': lower}

string = "Hello World! 123"
result = count_lower_upper(string)
print(result)

#2
def compute(n):
    return n + int(str(n)*2) + int(str(n)*3) + int(str(n)*4)

for i in range(4, 8):
    print(compute(i))

#3
def create_array(x, y, z, n):
    return [[[n for _ in range(z)] for _ in range(y)] for _ in range(x)]


print(create_array(3, 4, 5, 0))

#4
def sum_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

marks = [90, 80, 70, 60, 50]
total, average = sum_avg(marks)
print(f"Total: {total}, Average: {average}")

#5
def ispangram(string):
    alphaset = set('abcdefghijklmnopqrstuvwxyz')
    return alphaset <= set(string.lower())


string = "The quick brown fox jumps over the lazy dog"
print(ispangram(string))

#6
def create_list(n):
    return [(x, x*2, x*3) for x in range(1, n+1)]


print(create_list(5))

#7
def ispalindrome(string):
    string = string.replace(' ', '').lower()
    return string == string[::-1]


string = "Hello There"
print(ispalindrome(string))

#8
def convert(string):
    return ' '.join(sorted(set(string.split())))


string = "Quick brown fox jumps over the lazy dog"
print(convert(string))

#9
def count_alpha_digits(string):
    alpha = 0
    digits = 0
    for char in string:
        if char.isalpha():
            alpha += 1
        elif char.isdigit():
            digits += 1
    return {'alpha': alpha, 'digits': digits}

string = "Hello World! 123"
result = count_alpha_digits(string)
print(result)

#10
def frequency(string):
    words = string.split()
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return sorted(freq.items())

string = "Quick brown fox jumps over the lazy dog"
print(frequency(string))

#11
def create_list(list1, list2):
    return [x for x in list1 if x in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
print(create_list(list1, list2))

#function part-2
#1
def prime_factors(n, i=2):
    if n == 1:
        return []
    if n % i == 0:
        return [i] + prime_factors(n//i, i)
    return prime_factors(n, i+1)


n = int(input("Enter a number: "))
print(prime_factors(n))

#2
def binary(n):
    if n == 0:
        return ''
    print(f"n: {n}, n//2: {n//2}, n%2: {n % 2}")
    return binary(n//2) + str(n % 2)


n = int(input("Enter a number: "))
print(binary(n))

#3
def count_vowels(string):
    if string == '':
        return 0
    if string[0].lower() in 'aeiou':
        return 1 + count_vowels(string[1:])
    return count_vowels(string[1:])

string = input("Enter a string: ")
print(count_vowels(string))

#4
def reverse_list(lst):
    if len(lst) == 0:
        return []
    return [lst[-1]] + reverse_list(lst[:-1])


lst = [1, 2, 3, 4, 5]
print(reverse_list(lst))

#5
def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b-1)


a = int(input("Enter a: "))
b = int(input("Enter b: "))

print(power(a, b))

#6
def sanitize_list(lst):
    if len(lst) == 0:
        return []
    return [lst[0] if lst[0] >= 0 else 0] + sanitize_list(lst[1:])


lst = [1, -2, 3, -4, 5]
print(sanitize_list(lst))

#7
def average(lst):
    if len(lst) == 0:
        return 0
    return lst[0] + average(lst[1:])


lst = [1, 2, 3, 4, 5]
print(average(lst)/len(lst))

#8
def length(string):
    if string == '':
        return 0
    return 1 + length(string[1:])


string = input("Enter a string: ")
print(length(string))

#function part-3
#1
def fun():
    print("This is fun()")

def disp():
    print("This is disp()")

def msg():
    print("This is msg()")

functions = [fun, disp, msg]

for f in functions:
    f()

#2
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]

result = list(map(lambda x, y: x + y, list1, list2))
print("Resultant list:", result)

#3
import random

nums = random.sample(range(-15, 16), 10)
squares = [x**2 for x in nums]

print("Random numbers:", nums)
print("Squares:", squares)

#4
lst = ['madam', 'Python', 'malayalam', 12321]

for item in lst:
    if str(item) == str(item)[::-1]:
        print(f"Palindrome: {item}")

#5
faculty = ['Dr. Sharma', 'Prof. Radhakrishnan', 'Ms. Patel', 'Dr. Suresh', 'Professor Mehta']
long_names = list(filter(lambda name: len(name) > 8, faculty))

print("Names longer than 8 characters:")
for name in long_names:
    print(name)