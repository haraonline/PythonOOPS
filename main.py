
class Car:
    # this is the constructor of the class. It is called when an object of the class is created
    # self is a reference to the current instance of the class, and is used to access the class members (attributes and methods)
    def __init__(self):
        self.brand = None
        self.horse_power = None
        self.color = None


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


print(f"Car 1: brand {car1.brand}, horse power {car1.horse_power}, color {car1.color}")
print(f"Car 2: brand {car2.brand}, horse power {car2.horse_power}, color {car2.color}")
print(f"Car 3: brand {car3.brand}, horse power {car3.horse_power}, color {car3.color}")



    