class Cricket:
    def __init__(self,name):
        self.name=name
    def captian_cool(self):
        print(f"{self.name} is a very good WK.")
    
class junior(Cricket):
    def captian_cool(self):
        print(f"{self.name} is a very good captain.")

p1=junior("MSD")
p1.captian_cool()