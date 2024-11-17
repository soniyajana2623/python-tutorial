# MAP( map function can be used for list tuple and alse set)
def cube(x):
    return x*x*x

print(cube(2))

l=[1,2,3,4,5,6,7,8]
newl= set(map(cube,l))
newl1= list(map(lambda x:x*x,l))
print(newl1)
print(newl)


# FILTER(filter the list or set or tuple)
def filter_function(a):
    return a<4

newl2= list(filter(filter_function,l))
print(newl2)


#REDUCE
from functools import reduce  #impo
num=[1,2,3,4,5,6,7,8]
# 1+2, 3+3, 6+4, 10+5, 15+6, 21+7, 28+8+36
# def mysum(x,y):
#     return x + y
sum= reduce(lambda x, y:x+y,num)
print(sum)




