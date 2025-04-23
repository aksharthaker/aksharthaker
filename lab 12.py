#1
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)

    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)

    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)

    def __truediv__(self, other):
        denom = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denom
        imag = (self.imag * other.real - self.real * other.imag) / denom
        return Complex(real, imag)

    def __str__(self):
        return f"{self.real} + {self.imag}i"

a = Complex(3, 2)
b = Complex(1, 7)
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

#2
class Matrix:
    def __init__(self, data):
        self.data = data

    def add(self, other):
        return Matrix([[self.data[i][j] + other.data[i][j] for j in range(3)] for i in range(3)])

    def multiply(self, other):
        result = [[0]*3 for _ in range(3)]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += self.data[i][k] * other.data[k][j]
        return Matrix(result)

    def transpose(self):
        return Matrix([[self.data[j][i] for j in range(3)] for i in range(3)])

    def __str__(self):
        return '\n'.join([' '.join(map(str, row)) for row in self.data])

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

print("Addition:\n", m1.add(m2))
print("Multiplication:\n", m1.multiply(m2))
print("Transpose:\n", m1.transpose())

#3
class Solid:
    def __init__(self, shape, dimensions):
        self.shape = shape
        self.dimensions = dimensions

    def surface_area(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return 6 * side ** 2
        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return 4 * 3.1416 * r ** 2
        elif self.shape == "cylinder":
            r, h = self.dimensions['radius'], self.dimensions['height']
            return 2 * 3.1416 * r * (r + h)
        return 0

    def volume(self):
        if self.shape == "cube":
            side = self.dimensions['side']
            return side ** 3
        elif self.shape == "sphere":
            r = self.dimensions['radius']
            return (4/3) * 3.1416 * r ** 3
        elif self.shape == "cylinder":
            r, h = self.dimensions['radius'], self.dimensions['height']
            return 3.1416 * r ** 2 * h
        return 0

cube = Solid("cube", {"side": 3})
print("Cube SA:", cube.surface_area(), "Vol:", cube.volume())

#4
class Shape:
    def __init__(self, shape, data):
        self.shape = shape
        self.data = data

    def area(self):
        if self.shape == "circle":
            r = self.data['radius']
            return 3.1416 * r ** 2
        elif self.shape == "square":
            s = self.data['side']
            return s ** 2
        elif self.shape == "rectangle":
            return self.data['length'] * self.data['breadth']
        return 0

    def perimeter(self):
        if self.shape == "circle":
            r = self.data['radius']
            return 2 * 3.1416 * r
        elif self.shape == "square":
            return 4 * self.data['side']
        elif self.shape == "rectangle":
            return 2 * (self.data['length'] + self.data['breadth'])
        return 0

rect = Shape("rectangle", {"length": 5, "breadth": 3})
print("Area:", rect.area(), "Perimeter:", rect.perimeter())

#5
class Time:
    def __init__(self, hours=0, minutes=0):
        self.hours = hours
        self.minutes = minutes

    def add(self, other):
        total_minutes = self.minutes + other.minutes
        total_hours = self.hours + other.hours + total_minutes // 60
        return Time(total_hours, total_minutes % 60)

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}"

t1 = Time(2, 45)
t2 = Time(1, 30)
t3 = t1.add(t2)
print("Time after addition:", t3)

#6
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]

    def __eq__(self, other):
        return self.date == other.date

d1 = Date(22, 4, 2025)
d2 = Date(22, 4, 2025)
print("Dates are equal:", d1 == d2)

#7
class Weather:
    def __init__(self, parameters):
        self.parameters = parameters

    def __contains__(self, item):
        return item in self.parameters

w = Weather(["sunny", "windy", "humid"])
print("sunny" in w)
print("snowy" in w)  

#8
class MyString:
    def __init__(self, value=""):
        self.value = value
    def __iadd__(self, other):
        self.value += other.value
        return self
    def toLower(self):
        return self.value.lower()
    def toUpper(self):
        return self.value.upper()
    def __str__(self):
        return self.value

s1 = MyString("Hello")
s2 = MyString("World")
s1 += s2
print("Concatenated:", s1)
print("Lowercase:", s1.toLower())
print("Uppercase:", s1.toUpper())