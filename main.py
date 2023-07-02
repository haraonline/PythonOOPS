
class Car:
    # this is the constructor of the class. It is called when an object of the class is created
    # self is a reference to the current instance of the class, and is used to access the class members (attributes and methods)
    def __init__(self, brand, horse_power, color):
        self.brand = brand
        self.horse_power = horse_power
        self.color = color
        self.x_position = 5
        self.y_position = 5        

    # this is a method of the class
    def print_car(self):
        print(f"Brand: {self.brand}, Horse Power: {self.horse_power}, Color: {self.color}, Position: ({self.x_position}, {self.y_position})")
    
# create objects of the class
car1 = Car("BMW", 200, "Red")
car2 = Car("Mercedes", 250, "Black")
car3 = Car("Audi", 300, "White")

# call the method of the class
car1.print_car()
car2.print_car()
car3.print_car()










    