thislist = ['orange','banana','apple','grapes','guava']

thislist.sort()

print(thislist)

thisnum=[45,74,89,54,22,11,66,97,42,14,85]

thisnum.sort()
print(thisnum)

#printing in reverse order
thisnum.sort(reverse=True)
print(thisnum)


#Sort the list based on how close the number is to 50:
def myFunc(n):
    return abs(n-50)

numlist = [45,56,85,96,41,23,55,97,41,57]
numlist.sort(key = myFunc)
print(numlist)

kingdom=['dubai','sharjah','Abu Dhabi','fujarah','al ain','umm al quin','ras al kaimah']
kingdom.sort(key = str.upper)
print(kingdom)

kingdom.sort(key = str.lower)
print(kingdom)