l1 = [20, 50.0, "Dhruvika Gondaliya"]
print("List is : ", l1)

l2 = [1, 2, 3, "Dhruvika", 4, 5, "Gondaliya", 6]
print(l2)

#print single element of list
print("list[2] = ", l2[2])
print("Name is : ", l2[-5])

#print some elements
print(l2[1:5])

#print * list elements
print(l2[3:])
print(l2[:6])
print(l2[:])

#print some interval of the list
print(l2[1::2])

#change the value
l2[1] = 20
print("Updated list is : ", l2)