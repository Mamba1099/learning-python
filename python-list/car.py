class Mycar:

    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return f"{self.name} drives a {self.car}"
        
    @property
    def car(self):
        return self._car
    
    @car.setter
    def car(self, car):
        self._car = car

def main():
    my_car = get_my_car()
    print(my_car)

def get_my_car():
    name = input("name: ")
    car_name = input("car_name: ")
             
    return Mycar(name, car_name)    

if __name__ == "__main__":
    main()