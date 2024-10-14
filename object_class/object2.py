class student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name } {self.age}"
    

student1 = student("Kanban",56)
student2 = student("Akugan",49)

print(student1)
print(student2)