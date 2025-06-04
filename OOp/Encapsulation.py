class Employee:

    def __init__(self,name,dept,age):
        self.__name=name
        self.dept=dept
        self.age=age

    def getter(self):
        return self.__name

    def setter(self,new_name):
        self.__name=new_name


e1=Employee("Diva", "Data Engineer", 24)
e1.age=25
print(e1.getter(),e1.dept,e1.age)
e1.setter("Appu")
print(e1.getter())