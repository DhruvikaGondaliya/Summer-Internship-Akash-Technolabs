# Take 2 numbers and find smallest number.

num1 = int(input('Enter the num 1 : '))
num2 = int(input('Enter the num 2 : '))

if num1 < num2 :
    if num1 == num2 :
        print("Both numbers are equal.")
    else :
        print("num 1 is smaller than num 2")
else :
    print("num 2 is smaller than num 1")