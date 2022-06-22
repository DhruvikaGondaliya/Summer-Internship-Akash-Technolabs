t1 = (10, 20, "Dhruvi", 30 ,40 ,"abc", 50)
print("Tuple is : ",t1)

#print single element of tuple
print("tuple[2] = ", t1[3])
print("Name is : ", t1[-5])

#print some elements
print(t1[1:5])

#print * list elements
print(t1[3:])
print(t1[:6])
print(t1[:])

#print some interval of the list
print(t1[1::2])

'''#change the value in tuple give the error because tuple is immutable.
t1[1] = 20
print("Updated list is : ", t1)'''