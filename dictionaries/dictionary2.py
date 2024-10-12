#dictionary as a constructor

country = dict(name = "Sri Lanka",independance_year = 1948,continent = "Asia",Capital = "Colombo")
print(country)

#You can access the items of a dictionary by referring to its key name, inside square brackets:


#The keys() method will return a list of all the keys in the dictionary.
x = country.keys()
print(x)

#Changing a value of key
country["Capital"] = "Sri Jayawardenapura Kotte"
print(country)

#Adding a new key, value pair to existing dictionary
country["President"] = "Anura Kumara Dissanayake"

print(country)

#The items() method will return each item in a dictionary, as tuples in a list.
y = country.items()
print(y)

if "President" in country:
    print("9th President of this country")

#update a particular vlaue of ky using'update' method

country.update({"President":"Ranil Wickiramasinghe"})
country.update({"President":"Anura Kumara Dissanayake"})

print(country)