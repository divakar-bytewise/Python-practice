import S1
name=input("Enter Your name: ")
marks=[]

for i in range(5):
    m=int(input(f"Enter the marks{i+1} : "))
    marks.append(m)

S1.priniting_stud(name,marks)