#1
words = ["hello", "there", "santa"]
s = set()

for i in words:
    s.add(i.upper())

print(s)

#2
from random import randint

s = set()

for i in range(10):
    s.add(randint(15,45))
print(s)

count = 0
for i in s.copy():
    if i < 30:
        count+=1
    if i > 35:
        s.discard(i)

print(f"Count of numbers less than 30 = {count}")
print(s)

#3
s = set()
for i in range(5):
    nm = input("Enter name: ")
    s.add(nm)

print("Modifying...")
nm = input("Enter name to edit: ")
s.discard(nm)
nm = input("Enter new name: ")
s.add(nm)

print(s)

for i in range(2):
    nm = input("Enter name to delete: ")
    s.discard(nm)

print(s)

#4
s = {"Aarnav", "Abhinav", "Aryan", "Aaditya","Bivya", "Barth", "Bet", "Baan"}
A = set()
B = set()

for i in s:
    if i.startswith("A"):
        A.add(i)
    elif i.startswith("B"):
        B.add(i)

print(f"s = {s}")
print(f"A = {A}")
print(f"B = {B}")