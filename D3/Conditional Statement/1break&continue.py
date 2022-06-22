#Example of break statement
i = 0
while i < 10:
    print("Val is :  ", i)
    i += 1
    if i >= 5:
        break


#Example of continue statement
for x in range(10):

    if x % 2 == 0:
        continue
    print("Value is : ", x)


#Pass is just a placeholder for
#functionality to be added later.

i = {10, 20, 30, 40}
for val in i:
    pass