#List comprehension offers a shorter syntax when you 
#want to create a new list based on the values of an existing list.

vegetables=['brinjal','pumpkin','potato','tomato','beetroot','ladies finger']

new_vegetables = []


for x in vegetables:
    if "i" in x:
        new_vegetables.append(x)

print(new_vegetables)

fresh_vegetables = [y for y in vegetables if "e" in y]
print(fresh_vegetables)

cars = ['toyota','benz','nissan','audi','infiniti']

new_cars=[x for x in cars if x != ""]