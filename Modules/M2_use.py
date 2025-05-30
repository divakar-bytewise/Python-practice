import M1
print(M1.arth(7,4))

#Renaming the module.
import platform as p
a=p.system()
print(a)
b=dir(p)
print(b)

#variables in module.
x=M1.person1['age']
print(x)

#using built-in module.
import datetime

now = datetime.datetime.now()
print("Current Date and Time:", now)

