#accessing sets
country={"Srilanka","UAE","Australia","Thailand","New Zealnd"}

for x in country:
    print(x)

#You cannot access items in a set by referring to an index or a key. Following coddes amkes error message.
#for i in range(len(country)):
 #   print(country)

#checking particular element in set
if "Sri Lanka" in country:
    print("My country is there!!")
else:
    print("Oops! Sorry try again :(")

#Check if "UAE" is NOT present in the set:
print("UAE" not in country)