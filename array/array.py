#List is considred as array of python

cities = ['Jaffna','Colombo','Kandy']

cities.append('Galle')

print(cities)

#copying entire a list
copy_cities = cities.copy()
print(copy_cities)

#clear entire list with its element
#cities.clear()
#print(cities)

#inserting element at desired index position
cities.insert(2,'Batticaloa')

#deleting elemnt at desired index
cities.pop(2)
#print(cities)

#adding two list
num1 = [1,2,3,4,5]
num2 = [5,6,7,8,9]

num1.extend(num2)
print(num1)

repeated = [45,96,85,45,78,34,96,55,45,14,27,92,44,14]

#printing list in ascending order
repeated.sort()
print(repeated)

#printing list in decending order
repeated.sort(reverse=True)
print(repeated)

#count is used to count particular element in list
x = repeated.count(45)
print(x)

reverse_list = [9,8,7,6,5,4,3,2,1]
reverse_list.reverse()
print(reverse_list)
