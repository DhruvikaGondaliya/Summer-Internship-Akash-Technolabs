# Take 2 numbers and display greatest number. (Also check equal number condition)

num1 = int(input("Enter the num 1 : "))
num2 = int(input("Enter the num 2 : "))

if num1 >= num2 :
    if num1 == num2 :
        print("Both numbers are equal.")
    else :
        print("num 1 is grater than nam 2")
else :
    print("num 2 is grater than num 1")