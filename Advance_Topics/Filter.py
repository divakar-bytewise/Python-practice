def finding_largest(a):
    return a<=40

a=[14,60,2,3,4,5,6,7]
n=list(filter(finding_largest,a))
n.sort()
print(n)