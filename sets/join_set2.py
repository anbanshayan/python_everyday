#intersection_update

set1={"google","microsoft","amazon","yahoo"}
set2={"apple","google","flipkart","amazon"}

#The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
set1.intersection_update(set2)

print(set1)