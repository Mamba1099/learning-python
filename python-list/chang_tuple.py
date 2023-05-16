this_list = ("mango", "apple", "cherry", "banana")
y = list(this_list)
y[2] = "strawberry"
this_list = tuple(y)
print(this_list)