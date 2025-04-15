#!
import random

odd = [random.randint(range(1, 100, 2)) for _ in range(5)]
print("List of 5 odd integers:", odd)

even = [random.randint(range(0, 100, 2)) for _ in range(4)]
print("List of 4 even integers:", even)

odd[2] = even
print("List after replacing the third element with even integers:", odd)

fl = [item for sublist in odd for item in (sublist if isinstance(sublist, list) else [sublist])]
print("Flattened list:", fl)

sl = sorted(fl)
print("Sorted list:", sl)

#2
import random


r = [random.randint(1, 100) for _ in range(20)]
print("Generated list of random integers:", r)

num = int(input("Enter a number to find its pos in the list: "))

pos = [index for index, value in enumerate(r) if value == num]

if pos:
    print(f"The number {num} is found at pos: {pos}")
else:
    print(f"The number {num} is not found in the list.")

#3
import random

num = [random.randint(1, 30) for _ in range(50)]

un = list(set(num))

print(un)

#4
import random
num = [random.randint(-100, 100) for i in range(30)]
pos = [num for num in num if num > 0]
neg = [num for num in num if num < 0]
print("Random Numbers:", num)
print("Positive Numbers:", pos)
print("Negative Numbers:", neg)

#5
strings = ["hello", "world", "raju", "nice", "bad"]
upper = [i.upper() for i in strings]

print(upper)

#6
def fc(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def lis(flist):
    return [fc(temp) for temp in flist]


flist = [32, 68, 100, 212]
cl = lis(flist)
print(cl)

#7
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]

list3 = [num for num in list1 if num not in list2]

print(list3)