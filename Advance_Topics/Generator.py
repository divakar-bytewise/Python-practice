def fab(limit):
    n,m=0,1
    while n<=limit:
        yield n
        n,m=m,n+m

a=fab(10)
for i in a:
    print(i)

         