# Default

def my_fun(a=5 , b=2):
    c = a + b
    print("Sum is : ",c)

my_fun(10,20)
my_fun()

# Key

def my_fun(a,b):
    print ("Sub is : ", b-a)

my_fun(20,10)
my_fun(b=20,a=10)

# Variable-Length
#No keyword arg
def my_fun(*num):
    sum = 0

    for n in num :
        sum = sum + n
    print("Sum is : ", sum)

my_fun(10,20)
my_fun(10,20,30,40)

#keyword arg
def my_fun(**arg):
    for i,j in arg.items():
        print(i,j)

my_fun(Name = 'Dhruvika', Lname ='Gondaliya')