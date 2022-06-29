# No argu no return

def my_fun():
    a = 10
    b = 50 
    c = a + b
    print("Sum is : ", c)

my_fun()

# With argu no return

def my_fun(a , b):
    c = a + b
    print("Sum is : ", c)

my_fun(100 , 200)

# No argu with return

def my_fun() :
    a = 50
    b = 60
    c = a + b
    return c

ans = my_fun()
print("Sum is  : ", ans)

# With argu with return

def my_fun(a , b):
    c = a + b
    return c

ans = my_fun(2 , 10)
print("Sum is : ", ans)