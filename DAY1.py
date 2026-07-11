# Why python is called as dynamically typed languaged = Python is called dynamically language because at runtime python interpretor take decision of assigning data types.
# python is called interpreted languages.
# Is python pure object oriented languages?
# python interpretor takes responsibility of data type of variable.
# type() = data type class  
# ctrl + /

# How to check address of any variable ? = using id()

math = 50
chem = 60
phy = 70
pi = 3.14
name = "riya"

print(type(math))
print(type(chem))
print(type(phy))
print(type(pi))
print(type(name))

print(id(math))
print(id(chem))
print(id(phy))
print(id(pi))
print(id(name))

# write a program to accept 3 paper marks and calculate total marks, percentage and display

phy = 50
chem = 60
math = 70
total = phy + chem + math
percentage = total / 3.0
print("Total marks = ", total)
print("Percentage = ", percentage)

# What is type casting? = convert one data type to another data type is called type casting.
# By default input function only accept string value.
print(2+2)
print("2"+"2")
val1 = int(input("Enter 1st value : "))
val2 = int(input("Enter 2 value: "))
print(val1 + val2)

# we use complex datatype in data science project. we can't type cast

print(int(3.14)) # 3
# print(int(10+5j)) # we can't convert complex value to int
print(int(True)) # 1
print(int(False)) # 0
# print(int("4.22")) # we can't convert floating point value  string to int
print(int("4")) # 4

# # float() convert 
print(float(3)) # 3.0
# print(float(50+2j))
print(float(True)) # 1.0
print(float(False)) # 0.0
print(float(4.22)) # 4.22
print(float("4")) # 4.0
# print(float("name"))

# complex() used to convert
print(complex(3)) # 3.0j
print(complex(12.5)) # 12.5+0j
print(complex(True)) # 1+0j
print(complex(False)) #0j
print(complex("5")) # 5.0j
print(complex("5.6")) # 5.6+0j
# print(complex("name")) # string can't convert
print(complex(5,-3)) # 5-3j
print(complex(True,False)) # 1+0j

# # bool() used to 
print(bool(0)) # False
print(bool(15)) # True
print(bool(3.14)) # True
print(bool(0.0)) # False
print(bool(1+2j)) 
print(bool(0.0j)) # False
print(bool(-1))
print(bool(False)) # False
print(bool(True))
print(bool()) # False
print(bool("Abc")) # True

# program for swapping 2 numbers using 3rd variable
num1 = 100
num2 = 200
print("Number 1 before swapping: ",num1)
print("Number 2 before swapping: ",num2)
temp = num1
num1 = num2
num2 = temp
print("Number 1 after swapping: ",num1)
print("Number 2 after swapping: ",num2)

# Swapping numbers without using 3rd variable
num1 = 100
num2 = 200
print("Number 1 before swapping: ",num1)
print("Number 2 before swapping: ",num2)
num1=  num1 + num2
num2 = num1 - num2
num1 = num1 - num2
print("Number 1 before swapping: ",num1)
print("Number 2 before swapping: ",num2)

# WAP to calculate simple interrest
principle = 100000
rate_of_interest = 10
time =1
simple_interest=(principle * rate_of_interest * time)/100
print("Simple Interest amount =",simple_interest)

# WAP to calculate compound interest
# principle = 100000
# rate_of_interest = 10
# time = 1

# CI = principle(1+(rate_of_interest)/100)**time 
# print("Compound Interest amount =",CI)

# WAP to calculte area of circle
p1=3.14
radius=int(input("Enter radius: "))
area=p1*radius*radius
print("Area of circle: ",area)

# CWAP to calculate circumference of circle
p1=3.14
radius=int(input("Enter radius: "))
circum=2*p1*radius
print("Circumference of circle: ",circum)

# WAP to enter height of  user in feet and convert it into inch and centimeter

h=float(input("Enter height in feet: "))
inch=h*12
cm=inch*2.54
print("Height in inch: ",inch)
print("Height in cm: ",round(cm,2))

# WAP to reverse number
num=123
a=num % 10 # 3
num=num // 10 # 12
b=num % 10 # 2
c=num // 10
rev=a*100+b*10+c*1
print("Reverse number: ",rev)

# num=1234567
a=num % 10 # 7
num=num // 10 # 123456
b=num % 10 # 6
num=num // 10 
c=num % 10
num=num // 10
d=num% 10
num=num//10 # 123
e=num % 10 # 6
num=num // 10 
f=num % 10
num=num // 10
g=num% 10
rev=a*1000000+b*100000+c*10000+d*1000+e*100+f*10+g*1
print("Reverse number: ",rev)

# WAP to take centigrade temp and convert it into fah temp
cent=int(input("num: "))
f=1.8*cent+340
print("Fahrenheit: ",f)

# Special operators
# Identity Operator = When we want do address comparision then we should  go for identity operators. 
# There are 2 identity operators. 
# 1.is 
# 2.is not

# memory management
math= 50
chem= 50
phy= 50
eng=80
print(id(math)) 
print(id(chem))
print(id(phy)) # same address
print(id(eng)) # address is different others are same

print(math is chem) # True
print(math is not chem) # False
print(math is eng) # False
print(math is not eng) # True

# Membership Operators = we check if object is present or not in collection data structure(list,tuple,set,string) 
# 1. in 
# 2. not in
a="help4code"
print("e" in a) # true
print("f" not in a) # true

# string slicing
name = "prashant jha"

print(name[0])
print(name[1])
print(name[-1])
# print(name[15])
print(name[0:5])
print(name[1:])
print(name[:5])
print(name[:])
print(name[1:8:2])
print(name[::-1])

s="help4code is a best programming "
print(s.find("help4code")) # 0
print(s.find("python")) # -1
print(s.find("programming")) # 20

s="prashant","riya","sapnil"
m='|'.join(s)
print(m)

s="Python is a High level programming Language"
print(s.lower())
print(s.upper())
print(s.swapcase())
print(s.title())
print(s.capitalize())

print("Subject Marks: ")
math= 70
chem= 60
phy= 50

print("physics={} chemistry={} math={}".format(phy,chem,math))
print("physics={0} chemistry={1} math={2}".format(phy,chem,math))
print("physics={x} chemistry={y} math={z}".format(x=phy,y=chem,z=math))
total=phy+chem+math
print(f"Total marks {total}",)
print("Roll no=","7".zfill(4))

print("prd123".isalnum())
print("asd".isalpha())
print("123s".isdigit())
print("aas".islower())
print("".islower())
print("123s".isdigit())