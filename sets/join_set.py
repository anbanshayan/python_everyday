#The union() method returns a new set with all items from both sets.
letters = {'a','b','c'}

numbers = {1,2,3}

mix = letters.union(numbers)

print(mix)
#it will generate random order within set.

#You can use the | operator instead of the union() method, and you will get the same result.
mix2 = numbers | letters
print(mix2)

#join multiple set
set1 ={1,2,3}
set2 ={4,5,6}
set3={7,8,9}
set4={10,11,12}

set_uni = set1 | set2 |set3 |set4
print(set_uni)

#

#Note: Both union() and update() will exclude any duplicate items.

snacks = {"nuts","cheese","popcorn","peanuts","grainbar"}

graze = {"chocolate","peanuts","popcorn"}

#The intersection() method will return a new set, that only contains the items that are present in both sets.
common = snacks.intersection(graze)

print(common)

