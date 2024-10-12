#tuples can't be chnaged. So they have to be converted into list and made change & back to tuples

this_tuples = (("Hello","Hi","what'sup","Nothing"))
print(this_tuples)

#conversion of tuple to list
this_list = list(this_tuples)

this_list.append("Awesome")
this_list.remove("Nothing")

#conversion of list to tuple
update_tuple=tuple(this_list)

#delete an entire tuple
mock_tuple = tuple(("little","beauty","benz","car"))
print(mock_tuple)
del mock_tuple

print(update_tuple)

print(type(update_tuple))