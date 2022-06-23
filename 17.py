# Take a number and find factorial of that number.

num = int(input("Enter the number : "))

Fact = 1

if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        Fact = Fact * i
    print("The factorial of",num,"is",Fact)