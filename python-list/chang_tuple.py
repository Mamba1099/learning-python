this_list = ("mango", "apple", "cherry", "banana")
y = list(this_list)
y.append("strawberry")
this_list = tuple(y)
print(this_list)


# add tuple to a tuple
this_list = ("blue", "white", "orange")
y = ("green", "purple")
this_list += y
print(this_list)


# remove item in a tuple
this_list = ("cow", "goat", "cat")
y = list(this_list)
y.remove("goat")
this_list = tuple(y)
print(this_list)
