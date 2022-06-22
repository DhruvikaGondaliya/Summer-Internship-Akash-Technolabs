#IF statement

a = 50
b = 100

if a > b :
    print("a is grater number ")

if b > a :
    print("b is grater number ")


#IF...ELSE statement
a = 100
b = 40

if a > b :
    print("a is grater number ")
else:
    print("b is grater number ")


#IF...ELIF...ELSE statement
x = 20
y = 20

if x == y :
    print("Both numbers are equal")
elif x > y :
    print("x is grater number")
else:
    print ("y is grater number")


#Nested If statement
x=25

if x>=0:
    if x == 0:
        print("Zero")
    else:
        print("x is grater number")
else:
    print ("x is grater number")