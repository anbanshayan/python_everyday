#remove exisitng key value pair

my_mom = dict(Name = "Anbalagan Kugananthi",Age = 49,Home_Town = "Wattla",Mode_of_transport = "Bike")
my_sister = dict(Name = "Sivaanthi Anbalagan",Age = 22,Home_Town = "Kopay",Mode_of_transport = "Car")

print(my_mom)

#The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
my_mom.popitem()

my_sister.pop("Mode_of_transport")
print(my_sister)

#The clear() method empties the dictionary:
my_sister.clear()

#del my_sister

print(my_sister)
print(my_mom)