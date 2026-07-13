age=int(input("Enter age of person: "))
if age>=18:
    print("Can vote")
else:
    print("Can not vote")

a=int(input("Enter a:"))
b=int(input("Enter b:"))
c=int(input("Enter c:"))
if a>b and a>c:
    print("a is greatest among all three")
elif b>a and b>c:
    print("b is greatest among all three")
else:
    print("c is greatest among all three")

Loops
list1=[10,20,'riya',10.2]
for i in list1:
    print(i)
for i in range(1,5):
    print(i)
for i in range(1,11,2):
    print(i)
for i in range(0,11,2):
    print(i,end=" ")

list2=[12,10,18,63,25,29,91,94,56]
e_count=o_count=0
for i in list2:
    if i%2==0:
        e_count+=1
    else:
        o_count+=1
print("Even count:",e_count)
print("Odd count:",o_count)

num=int(input("Enter number:"))
rev=0
while num!=0:
    rev=rev*10+num%10
    num//=10
print(f"Reverse number:{rev}")

num=int(input("Enter number:"))
original=num
rev=0
while num!=0:
    rev=rev*10+num%10
    num//=10
print(f"Reverse number:{rev}")
if original==rev:
    print(f"{original} is palindrome")
else:
    print(f"{original} is not palindrome")

num=int(input("Enter number:"))
original=num
sum=0
rev=0
while num!=0:
    rev=num%10
    num//=10
    sum+=rev
print(f"Sum of {original} is {sum}")

num=int(input("Enter number: "))
fact=1
for i in range(2,num+1):
    fact=fact*i
print(fact)

# Fabbanico series number important
num=int(input("Enter number: "))
a=0
b=1
print(a,b,end=" ")
for i in range(2,num):
    c=a+b
    print(c,end=" ")
    a=b
    b=c

# Armstrong program
num=int(input("Enter number: "))
original=num
sum=0
count=len(str(num))
while num!=0:
    sum=sum+(num%10)**count
    num//=10
if original==sum:
    print(f"{original} is armstrong")
else:
    print(f"{original} is not armstrong")

