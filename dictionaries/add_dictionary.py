#adding new key value pair

myself ={
    "name":"Anbalagan Sujanasrishayan",
    "Age":24,
    "School":"Jaffna Hindu College",
    "University":"University of Colombo",
    "Home Town":"Jaffna"
}

print(myself)
print(myself["name"])

#add new key value pair
myself["Mode of transport"] = "Bus"

my_dad = dict(Name="Kandiah Anbalagan",Age=56,Job_Town="Dubai")

print(myself)

#update existing value of key
myself.update({"Mode of transport":"Motor Bike"})

print(myself)

print(my_dad)