from functools import reduce
l = [2,4,5,6,9,8,5,6,2,9,6,3,2,5,8,7,4,1,0]


# map
# def cube(x):
#     return x*x*x
# newl = list(map(cube,l))
# print(newl)


# filter
# def greater(a):
#     return a>4
# newl1 = list(filter(greater, l))
# print(newl1)

# reduce
def avg(x,y):
    return (x+y)/2
l = reduce(avg,l)
print(l)