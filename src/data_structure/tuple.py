n=("John","A.P.J","Stev","Joe","Kain")
m=list(n)#if we have to update or change,
#something in tuple first we have convert, 
#it for list and we have to do the operations.
m.append("Iron man")#appending
n=tuple(m)#again converting to tuple.
print(n)

#Tuple methods.
#count() gives the frequency of a number.
n=(1,2,3,4,5,8,4,6,7,8,9,7,10,11)
m=n.count(4)
print(m)

#index() gives the first index where 7 appears.
n=(1,2,3,4,5,8,4,6,7,8,9,7,10,11)
m=n.index(7)
print(m)