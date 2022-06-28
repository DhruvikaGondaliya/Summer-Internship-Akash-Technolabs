for x in range(8):
    print("First Range : ", x)

#print values between some range
for y in range(2,8):
    print("Second Range : ", y)

#print value with some interval
for z in range(2,9,3):
    print("Third Range : ", z)

#range fun. & else statement with tuple
t1=(10, 'abc', 20)

for i in range(len(t1)):
    print("Value is : ", t1[i])
else:
    print("No element left.")
