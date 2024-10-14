#intrdouction of class
class myClass:
    x = 5

obj1 = myClass()
print(obj1.x)

#Above ones are simple form of class and object

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    
    
person1 = Person("Anbashayan",24)
person2 = Person("AKugananthi",49)

print(person1.name,person1.age)
print(person2.name,person2.age)
