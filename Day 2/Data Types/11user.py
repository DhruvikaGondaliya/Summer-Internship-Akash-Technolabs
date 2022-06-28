# Take a value from the user

l1 = []

n = int(input("Enter the number of element : "))

for i in range(0,n) : 
    ele = input("Enter the value : ")

    l1.append(ele)

t1 = tuple(l1)
print(l1)
print(t1)

# Dictionary

d = {}

n = int(input("Enter the number of element : "))

for i in range(0,n) : 
    a , b = input("Enter key value and pair data : ").split()
    d[a] = [b]

print(d)