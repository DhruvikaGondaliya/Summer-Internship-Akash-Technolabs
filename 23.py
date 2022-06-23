# Take a number check if a number is less than 100 or not. If it is less than 100 then check if it is odd or even.

num = int(input("Enter the number is : "))

if num < 100 :
    print("Number is less than 100.")
    if num % 2 == 0 : 
        print("Given number is even.")
    else : 
        print("Given number is odd.")
else :
    print("Number is grater than 100.")