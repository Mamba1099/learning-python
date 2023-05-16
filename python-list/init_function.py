class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = person("kevin", 33)
print(f"{p1.name} is {p1.age}")
