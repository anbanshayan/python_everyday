#Creating nested dictionary

child1={
    "Name":"Anbalagan Sujanasrishayan",
    "University":"University of Colombo School of Computing",
    "Degree":"B.Sc in Information Systems"
}

child2={
    "Name":"Sivananthi Anbalagan",
    "University":"IIT",
    "Degree":"B.Sc in Software Engineering"
}

myfamily = {
    "child1":child1,
    "child2":child2
}

print(myfamily["child1"])