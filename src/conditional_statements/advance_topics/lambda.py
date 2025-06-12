def func(n):
    return lambda a:a**n

square=func(2)
cube=func(3)

a=int(input("Enter a number: "))
print("square of a number is:",square(a) )
print("cube of a number is:",cube(a))

max_num=lambda x,y:x if x>y else y
r=max_num(10,7)
print(f"The max_number is: {r} ")