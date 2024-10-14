#adding function into class

class pupil:
    def __init__(self,name,town):
        self.name = name
        self.town = town

    def __str__(self):
        return f"{self.name} {self.town}"
    
    def myFunc(self):
        print("Good Morning!!!")

pupil1 = pupil("Anbashayan","Kopay")
print(pupil1)
pupil1.myFunc()