class Grantparent:
    height = 170
    age = 70
    sick = "cool"

class Parents(Grantparent):
    age = 40

class Children(Parents):
    heigt = 170
    def __init__(self):
        print(self.sick)
        print(self.age)
daun = Children()

class Wow:
    def _wow(self):
        print('Wow')
    def _hello(self):
        print('Hello')
some_obj = Wow()
some_obj._hello()
some_obj._wow()

class Hello:
    def __init__(self):
        print('Hello')
class Hello_Woeld(Hello):
    def __init__(self):
        super().__init__()
        print("World")
HELLO_WOELD = Hello_Woeld()


#les 6
import requests

help(requests)

def first_function():
    pass

class Human:
    pass

rq  = requests
first_f = first_function
nazar = first_function
print(requests.__name__)
print(rq.__name__)
print(first_function.__name__)
print(r__name__)
print(tyre(__name__))

Ls = []
for i in dir(ls)
    print(i)