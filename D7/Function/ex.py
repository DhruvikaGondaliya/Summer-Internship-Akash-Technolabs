# No arg no return

def my_fun():
    print("Hello World...")

my_fun()

# With arg no return

def my_fun(a) :
    print("Value of a is : ", a)

my_fun(20)

# No arg with return

def my_fun() : 
    a = 20 
    return a

c = my_fun()
print("Value of a is : ", c)

# With arg with return

def my_fun(a) :
    return a

a= my_fun(80)
print("Value of a is : ", a)