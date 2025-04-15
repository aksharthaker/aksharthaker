#1
dictionary1 = {"key1": "value1", "key2": "value2"}
dictionary2 = {"key3": "value3", "key4": "value4"}
dictionary3 = {"key5": "value5", "key6": "value6"}

dictionary4 = {**dictionary1, **dictionary2, **dictionary3}

print("Concatenated Dictionary:")
print(dictionary4)

#2
dictionary = {}

if not dictionary:
    print("The dictionary is empty.")
else:
    print("The dictionary is not empty.")

#3
data = [{"dept_no": 101, "emp_roll_no": 1, "salary": 50000},{"dept_no": 102, "emp_roll_no": 2, "salary": 60000},{"dept_no": 101, "emp_roll_no": 3, "salary": 45000},
    {"dept_no": 101, "emp_roll_no": 5, "salary": 52000}]
result = {}

for record in data:
    dept = record["dept_no"]
    salary = record["salary"]
    if dept not in result:
        result[dept] = {"min": salary, "max": salary}
    else:
        result[dept]["min"] = min(result[dept]["min"], salary)
        result[dept]["max"] = max(result[dept]["max"], salary)

print(result)

#4
string = input("Enter a string: ")
frequency = {}

for char in string:
    frequency[char] = frequency.get(char, 0) + 1

print(frequency)

#5
prices = {"apple": 50, "banana": 20, "milk": 30}
quantities = {"apple": 2, "banana": 5, "milk": 1}

total_bill = sum(prices[item] * quantities[item] for item in prices if item in quantities)

print("Total Bill:", total_bill)