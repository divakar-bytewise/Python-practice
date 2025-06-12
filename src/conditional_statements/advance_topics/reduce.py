from functools import reduce
def add(a,b):
    return a+b

l=[14,60,2,3,4,5,6,7]
n=reduce(add,l)
print(n)