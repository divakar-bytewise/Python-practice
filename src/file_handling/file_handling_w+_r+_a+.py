#Using with help's us in closing the file
with open("Text1.txt") as f:
    r=f.read()
    print(r)

#normally running opening a file.
f=open("Text1.txt")
print(f.read())
f.close()

#Using a+ append's and read the file.
with open("Text1.txt","a+") as f:
    f.write("\nPython has several functions for creating, reading, updating, and deleting files.")
    q=f.read()
    print(q)

#Using write + read.
with open("Text1.txt","w+") as f:
    f.write("\nPython has several functions for creating, reading, updating, and deleting files.")
    q=f.read()
    print(q)

#Using read + write.
with open("Text1.txt","r+") as f:
    f.write("Hii!!!!\n.")
    q=f.read()
    print(q)

with open("Text1.txt","w") as f:
with open("Text1.txt","r") as f:
with open("Text1.txt","a") as f: