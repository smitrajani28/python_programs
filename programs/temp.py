# a = int(input("Enter a value of A:"))
# b = int(input("Enter a value of B:"))
# c = input("Enter a operator(+,-,*,/):")
# result = 0

# if(c=="+"):
#     result = a + b
# elif(c=="-"):
#     result = a - b
# elif(c=="*"):
#     result = a * b
# elif(c=="/"):
#     result = a / b
# else:
#     print("Enter valid arguments")

# print(result)

a = input("Enter a expression:")
list1 = []
list1 = a.split(" ")
if(list1[1]=="+"):
    result = int(list1[0]) + int(list1[2])
elif(list1[1]=="-"):
    result = int(list1[0]) - int(list1[2])
elif(list1[1]=="*"):
    result = int(list1[0]) * int(list1[2])
elif(list1[1]=="/"):
    result = int(list1[0]) / int(list1[2])
else:
    print("Enter valid arguments")

print(result)