#Example of AND

a = 10
b = 20
c = 30

if a>b and a>c:
    print("a is the largest number")

if b>a and b>c:
    print("b is the largest number")

if c>a and c>b:
    print("c is the largest number")


#Example of OR

ch = input("Enter a character : ")

if(ch == 'A' or ch== 'a' or ch== 'E' or ch== 'e' or ch== 'I' or ch== 'i' or ch== 'O' or ch== 'o' or ch== 'U' or ch== 'u'):
    print(ch, "is a Vowel")

else:
    print(ch, "is a consonant")