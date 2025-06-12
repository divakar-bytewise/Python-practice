def multiply(a,b):
    m=a*b
    return m

a=[1,2,3,4]
b=[5,6,7,8]
n=list(map(multiply,a,b))

print(n)

#Using loop to print and using small function lambda.
a=[1,2,3,4,5,6,7]
n=map(lambda a:a**2,a)
for i in n:
    print(i)