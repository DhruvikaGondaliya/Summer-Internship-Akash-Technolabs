# Take a number to print the square of a number if it is less than 10.

num = int(input("Enter the number is : "))

if num < 10 :
    print("Number is less than 10.")
    a = num * num
    print("Square of a" ,num, 'is', a)
else :
    print("Number is grater than 10.")