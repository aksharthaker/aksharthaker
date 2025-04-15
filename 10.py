import csv

with open('students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Roll No', 'Name', 'Subject1', 'Subject2', 'Subject3'])
    writer.writerow([1, 'Alice', 85, 90, 92])
    writer.writerow([2, 'Bob', 78, 88, 84])

print("CSV file created as 'students.csv'")

#2
import csv

data = {}
with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        rollno = int(row['Roll No'])
        total = int(row['Subject1']) + int(row['Subject2']) + int(row['Subject3'])
        data[rollno] = {
            'Name': row['Name'],
            'Marks': [int(row['Subject1']), int(row['Subject2']), int(row['Subject3'])],
            'Total': total
        }

for k, v in data.items():
    print(f"Roll No: {k}, Name: {v['Name']}, Marks: {v['Marks']}, Total: {v['Total']}")

#3
name = input("Enter name: ")
phone = input("Enter phone: ")
email = input("Enter email: ")

with open(f"{name}.vcf", 'w') as file:
    file.write("BEGIN:VCARD\n")
    file.write("VERSION:3.0\n")
    file.write(f"N:{name}\n")
    file.write(f"TEL:{phone}\n")
    file.write(f"EMAIL:{email}\n")
    file.write("END:VCARD\n")

print(f"vCard '{name}.vcf' created.")

#4
import os
import shutil

src_file = 'old_dir/sample.txt'
dest_dir = 'new_dir'

os.makedirs(dest_dir, exist_ok=True)
shutil.copy(src_file, dest_dir)

print(f"Copied '{src_file}' to '{dest_dir}'")

#5
with open('source.txt', 'r') as src, open('target.txt', 'w') as tgt:
    for line in src:
        tgt.write(line.upper())

print("File copied with lowercase converted to uppercase.")

#6
with open('file1.txt') as f1, open('file2.txt') as f2, open('merged.txt', 'w') as out:
    lines1 = f1.readlines()
    lines2 = f2.readlines()

    for i in range(max(len(lines1), len(lines2))):
        if i < len(lines1):
            out.write(lines1[i])
        if i < len(lines2):
            out.write(lines2[i])

print("Merged file created as 'merged.txt'")

#7
import pickle

class Employee:
    def _init_(self, code, name, doj, salary):
        self.code = code
        self.name = name
        self.doj = doj
        self.salary = salary

    def _str_(self):
        return f"{self.code}, {self.name}, {self.doj}, {self.salary}"

emp = Employee(101, 'John Doe', '2023-01-01', 50000)

with open('employee.dat', 'wb') as file:
    pickle.dump(emp, file)

with open('employee.dat', 'rb') as file:
    loaded_emp = pickle.load(file)

print("Deserialized Employee:", loaded_emp)

#8
with open('input.txt', 'r') as infile, open('cleaned.txt', 'w') as outfile:
    for line in infile:
        for word in [' a ', ' an ', ' the ']:
            line = line.replace(word, ' ')
        outfile.write(line)

print("Words removed and saved in 'cleaned.txt'")