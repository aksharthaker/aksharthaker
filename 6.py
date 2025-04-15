#1
def cnt(nlist):
    boys = 0
    girls = 0
    for i in nlist:
        if isinstance(i, tuple):
            lenn = len(i)
            boys = boys+lenn
        else:
            girls += 1
    return boys, girls

names = [("Divy","Prayag"), "Nisha", ("Raju",), "priya", ("Tom",), "Jennie"]
boys, girls = cnt(names)
print(f"Number of boys: {boys}")
print(f"Number of girls: {girls}")

#2
students = [(1, 'b1', 20), (2, 'b2', 21), (3, 'b3', 22)]

rolln = [student[0] for student in students]
name = [student[1] for student in students]
ages = [student[2] for student in students]

print("Roll Numbers:", rolln)
print("name:", name)
print("Ages:", ages)

#3
import datetime
d1 = (18,2,2025)
d2 = (18,2,2024)
date1= datetime.date(d1[2],d1[1],d1[0])
date2= datetime.date(d2[2],d2[1],d2[0])
print(date1,date2)
x= abs(date1-date2)
print(x)

#4
food_items = [("Pizza", 1.50),("Burger", 0.75),("Cherry", 2.00),("Cake", 1.25),("Nachos", 3.00)]
sortedlist = sorted(food_items, key=lambda item: item[1], reverse=True)
print(sortedlist)

#5
l1 = [(), (1, 2), (), (3, 4, 5), (), (6, 7, 8, 9)]
l2 = [i for i in l1 if i]
print(l2)

#6
tup = (1, 2, 3, 4)
print(tup)
lis = list(tup)
lis[1] = 20
tup = tuple(lis)
print(tup)

#7
tup = (1, 2, 3, 4, 5)
lis = list(tup)
lis.pop(2)  
tup = tuple(lis)
print(tup)