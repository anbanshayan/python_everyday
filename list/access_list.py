#accessing list 

#printing elements from index m to n-1
numbers=[8,9,6,5,7,4,5,2,1,3,0]
print(numbers[2:5])

this_fruits = (("Banana","Apple","Grapes","Guava","Pears","Palm"))
print(this_fruits[1:4])

#printing elements in reverse
print(this_fruits[-4:-1])

#check if an item exists
if "Apple" in this_fruits:
    print("Apple is in list")
else:
    print("No, Apple is not there")