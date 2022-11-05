class Grantparent:
    height = 170
    age = 60
    sick = "cool"

class Parents(Grantparent):
    age = 40

class Children(Parents):
    heigt = 170
    def __init__(self):
        print(self.sick)
        print(self.age)
daun = Children()
