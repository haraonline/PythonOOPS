
class Car:
    # this is the constructor of the class. It is called when an object of the class is created
    # self is a reference to the current instance of the class, and is used to access the class members (attributes and methods)
    def __init__(self):
        self.brand = None
        self.horse_power = None
        self.color = None

class Driver:
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car

car1 = Car()
car1.brand = "BMW"
car1.horse_power = 200
car1.color = "Red"

car2 = Car()
car2.brand = "Mercedes"
car2.horse_power = 250
car2.color = "Black"

car3 = Car()
# assign values to the attributes of car3 in one line
car3.brand, car3.horse_power, car3.color = "Audi", 300, "White"

# loop over a list of cars and print their attributes
cars = [car1, car2, car3]
for car in cars:
    print(str(car), ":",  f"Car: brand {car.brand}, horse power {car.horse_power}, color {car.color}")

# create a driver and assign a car to him
driver1 = Driver("John", 30, car1)
print(f"Driver: name {driver1.name} age {driver1.age}, drives {driver1.car.brand} with horse power {driver1.car.horse_power} and color {driver1.car.color}")






    