print("welcome to the if else program")
a =int(input("enter a value of a :"))
b =int(input("enter a value of b :"))

# if else
# if(a>b):
#     print("a is greater")
#     if(a>0):
#         print("number is positive")
#     elif(a<0):
#         print("number is negative")
#     elif(a==0):
#         print("number is zero")
# elif(a<b):
#     print("b is greater")
#     if(b>0):
#         print("number is positive")
#     elif(b<0):
#         print("number is negative")
#     elif(b==0):
#         print("number is zero")
# else:
#     print("both are equal")

# match case
# match a:
#     case _ if a>b:
#         print("a is greater")
#     case _ if a<b:
#         print("b is greater")
#     case _ if a==b:
#         print("both are equal")
#     case _:
#         print("nothing")

# short hand
print(a) if a>b else print("a=b") if a==b else print(b)