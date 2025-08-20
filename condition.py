# b = int(input("Enter a value: "))
# if(b % 2 == 0):
#     print("Even")
# else:
#     print("Odd")
    
# if(b <= 18):
#     print("Teenager")
# elif(b >= 70):
#     print("too old")
# else:
#     print("Senior")

# a = int(input("Enter a number1: "))

# b = int(input("Enter a number2: "))
# c = int(input("Enter a number3: "))
# d = int(input("Enter a number4: "))

# if a > b and a > c and a > d:
#     print("a is the largest number", a)
# elif b > a and b > c and b > d:
#     print("b is the largest number", b)
# elif c > a and c > b and c > d:
#     print("c is the largest number", c)
# else:
#     print("d is the largest number", d)

a = input("Enter your name: ")
print(a.count(""))
print(a.__len__())
if (a.__len__() < 10):
    print("less characters  ")
else:
    print("more characters")