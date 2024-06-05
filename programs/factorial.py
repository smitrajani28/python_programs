def factorial(a):
    if(a==0 or a==1):
        return 1
    else:
        return a*factorial(a-1)
a = int(input("enter number do you want for factorial:"))
print(factorial(a))     