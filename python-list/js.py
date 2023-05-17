import json

x = {
 "name": "john",
 "age": 30,
 "married": True,
 "Divorced": False,
 "children": ("Ann", "Billy"),
 "Pets": None,
 "cars":[
     {"model": "BMW 230", "mpg": 27.5},
     {"model": "Ford Edge", "mpg": 24.1}
 ]    
 }
print(json.dumps(x))