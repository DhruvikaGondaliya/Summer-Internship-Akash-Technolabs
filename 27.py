# Take a number and check whether it is zero, positive or negative using nested IF…ELSE statement .

num = int(input("Enter the number : "))

if num >= 0 :
    if num == 0 :
        print("Number is zero. ")
    else : 
        print("Number is positive.")
else :
    print("Number is nagative.")