#Creating a list
Names=["John","Dominic","Simeon","Sarvanana"]
print(Names)

#Using len() function.
Names=["John","Dominic","Simeon","Sarvanana"]
print(len(Names))

#Accesing list item.
Names=["John","Dominic","Simeon","Sarvanana"]
print(Names[1])

#-ve indexing.
Names=["John","Dominic","Simeon","Sarvanana"]
print(Names[-2])

#Range of Index.
Names=["John","Dominic","Simeon","Sarvanana"]
print(Names[:2])
print(Names[1:])

#Changing the List item value.
Names=["John","Dominic","Simeon","Sarvanana"]
n=Names.insert(2,"Chotu") #Using insert() method.
Names[0]="Praveen" #Changing Particular index.
Names[:2]=["Tharun","Jay","joe"] #Changing the item value in range.
print(Names)


#Adding the item to List.
Names=["John","Dominic","Simeon","Sarvanana"]
Names.append("Vicky")#Appending the value to List.
nl=("Tharun","David","Miller")#Tuple
Names.extend(nl)#Adding the tuple to the List.
print(Names)

#Removing the item in List.
Names=["John","Dominic","Simeon","Sarvanana"]
Names.remove("Simeon")#using remove().
Names.pop()#Pop removes last element in List.
del Names#Deleting the complete List.
Names=["John","Dominic","Simeon","Sarvanana"]
Names.clear()#Removes all the item in List but the List will not be deleted.
print(Names)


#Sorting the List and Using List Comprehension.
Names=["John","Dominic","Simeon","Sarvanana"]
Names.sort()
Names=["John","Dominic","Simeon","Sarvanana"]
nl=[i for i in Names]
print(nl)

