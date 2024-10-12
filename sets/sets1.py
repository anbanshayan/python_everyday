#Creating a set
my_set={"apple","orange","grapes","pine apple","guava","dates"}
print(my_set)

#Set items are unordered, unchangeable, and do not allow duplicate values.
fruits = {"apple","banana","grapes","apple"}
print(fruits)
#Duplicate values will be ignored:

#False and 0 is considered the same value:
values={False,0,True,False,True}
print(values)

#printing length of set
print(len(my_set))

#Set items can be of any data type:
set1={1,2,3,4}
set2={True,False,True,False}
set3={"appa","amma","naan","thankachi"}

#set can contain  ultiple data type 
set_mix={"aapa",56,True}

print(type(set_mix))

#using set constructor
cities = set(("Jaffna","Colombo","Gampaha"))
print(cities)
