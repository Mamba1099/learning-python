
#using asterik *
print("use of asterik in tuples")
fruits = ("banana", "watermelon", "apple", "cherry", "plums")
(yellow, green, *red) = fruits
print(yellow)
print(green)
print(*red)
