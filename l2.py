#larget ans smallest
a=int(input('enter a value'))
b=int(input('enter a value'))
if(a>b):
    print(a ,'is bigger')
elif(b>a):
    print(b, 'is bigger')
elif(a==b):
    print('both are equal')

#largest of 3
a=int(input('enter a value'))
b=int(input('enter a value'))
c=int(input('enter a value'))
if(a>b and a>c):
    print(a ,'is bigger than',b,c)
elif(a<b and b>c):
    print(b, 'is bigger than',c,a)
elif(a<b and b<c):
    print(c, 'is bigger than',a,b)

#even or odd
a=int(input('enter a value'))
if(a%2==0):
      print("the number is even")
else:
    print("odd")

#div by 10
a=int(input('enter a value'))
if(a%10==0):
      print("the number is divisible")
else:
    print("not divisible")

#major
a=int(input('enter a age'))
if(a<18):
      print("minor")
else:
    print("major")

#no of digits
a=input('enter a num')
print('the length is',len(a))

#leap year
a=int(input('enter a year'))
if(a%4==0):
    print('leap year')
elif(a%400==0):
    print('leap')
else:
    print('not leap')

#valid triangle
a=int(input('enter a angle'))
b=int(input('enter a angle'))
c=int(input('enter a angle'))
if(a+b+c==180):
    print("valid traingle")
else:
    print("invalid")

#abs value
a=int(input('enter a value'))
if(a<0):
    print(-(a))
else:
    print(a)

#area perimeter
a=int(input('enter a length'))
a=int(input('enter a breath'))
area=a*b
perimeter=2(a+b)
if(area>perimeter):
    print("area is greater")
else:
    print("perimeter is greater")

#lie on the line
x1=int(input("enter the x1 coordinate"))
y1=int(input("enter the y1 coordinate"))
x2=int(input("enter the x2 coordinate"))
y2=int(input("enter the y2 coordinate"))
x3=int(input("enter the x3 coordinate"))
y3=int(input("enter the y3 coordinate"))
slope1=(y2-y1)/(x2-x1)
slope2=(y3-y2)/(x3-x2)
if(slope1==slope2):
    print("same line")
else:
    print("not same line")

#in the circle
a=int(input('enter the radius'))
x1=int(input("enter the x1 coordinate"))
y1=int(input("enter the y1 coordinate"))
x1=int(input("enter the x2 coordinate"))
y1=int(input("enter the y2 coordinate"))
area=3.14*(r**2)
r=(x2-x1)**2 + (y2-y1)**2
radius2=r**1/2
if(radius2<a):
    print("inside")
else:
    print("outside")















    


