class student:
    def __init__ (self,name,age):
        self.name=name
        self.age=age
    
    def display(self):
        print(f"Name: {self.name}, Age: {self.age}.")

s1=student("Diva",23)
s2=student("Sanjay",22)

s1.display()
s2.display()