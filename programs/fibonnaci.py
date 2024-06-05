# with reccursion
# def fibonnaci1(n):
#     if(n<=1):
#         return n
#     else:
#         return fibonnaci1(n-1)+fibonnaci1(n-2)
# def fibonnaci(n):
#     for i in range(n):
#         print(fibonnaci1(i), end=" ")   

# fibonnaci(5)


# without reccursion
def fibonnaci(x):
    a=0
    b=1
    for n in range(x):
        temp=0
        if(n<=0):
            print(n,end=" ")
        else:
            temp = a + b
            print(temp, end=" ")
            a = b
            b = temp
fibonnaci(5)


# using while loop
# def fibonnaci(n):
