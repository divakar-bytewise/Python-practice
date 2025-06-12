#Creating and accessing the set.
S = {"apple", "banana", "cherry","apple"}
print(S)
#prints false.
print("banana" not in S)
for x in S:
  print(x)

#adding items to set.
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.add("orange")
thisset.update(tropical)
print(thisset)

#Joining sets.
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
#In place of union we can use '|'.
set3 = set1.union(set2)
print(set3)

#update
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2)
print(set1)

#intersection.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#instead of intersection we can use '&'.
set3 = set1.intersection(set2)
print(set3)

#difference
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#instead of difference we can use '-'
set3 = set1.difference(set2)

print(set3)

#symmetric_difference.
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
#instead of symmetric_difference we can use '^'
set3 = set1.symmetric_difference(set2)

print(set3)