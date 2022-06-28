# Write a program to swap 2 numbers without taking third variable.

num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

num1 = num1 * num2
num2 = num1 / num2
num1 = num1 / num2

print("Swapping num 1 is : ", num1)
print("Swapping num 2 is : ", num2)