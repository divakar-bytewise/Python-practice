#Creating and Calling the function
def v_happy(name):
    print(f"Happy birthday {name}")
v_happy('stev')
v_happy('josh')

#With arguments.
def arth(a,b):
    print(a+b)
    print(a//b)
    print(a/b)
    print(a-b)
    print(a*b)
arth(7,4)

#Arbitrary arguments.
def v_happy(*name):
    print("Happy birthday",name[1])

v_happy('stev','john','dominic')

#Keyword Function
def v_happy(f1,f2,f3):
    print("Happy birthday",f3)

v_happy(f1='stev',f2='john',f3='dominic')

#Function with return value.
def expo(a,b):
    r=a**b
    return r

r=expo(7,4)
print(r)

#Passing list on function.
def names_list(n):
    for i in n:
        print(i)
names=('stev','john','dominic')
names_list(names)


    