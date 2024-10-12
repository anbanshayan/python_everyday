#The difference() method will return a new set that will contain only the items from the first set that are not present in the other set.
set1={"Sri Lanka","India","Maldives","Pakistan"}

set2={"Afghansitan","Laos","Bhutan","Sri Lanka"}

set3 = set2.difference(set1)

print(set3)

#You can use the - operator instead of the difference() method, and you will get the same result.

org1 = {"Dubai","Fujarah","Amman","Baharain"}

org2 = {"Jaffna","Colombo","Wattala","Melbourne","Adelaide"}

org3 = org1 - org2

print(org3)


#Use the difference_update() method to keep the items that are not present in both sets:
count1 = {4,5,6,8,9}

count2 = {1,2,3,4,7}

count1.difference_update(count2)

print(count1)