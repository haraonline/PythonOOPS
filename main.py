
class Car:

    # the class constructor is always called __init__
    # the first argument is always self, which is a reference to the current instance of the class    
    # self is used to access the members of the class
    # self is not a keyword, you can use any word you want, but it is a convention to use self
    # the other arguments are the arguments you pass to the constructor when you create an instance of the class
    # the constructor is primarily used to initialize the members of the class (a desired state)
    # __init__ implicitly returns None, returning anything else will raise an error

    
    def __init__(self, brand, horse_power, color, is_started=False, current_speed=0):
        self.brand = brand
        self.horse_power = horse_power
        self.color = color
        self.is_started = is_started
        self.current_speed = current_speed

    
# Naming conventions in python programming language
# Class names are written in Pascal, e.g. Car, CarEngine
# Function names are written in snake_case, e.g. get_car, get_car_engine
# Variable names are written in snake_case, e.g. car, car_engine
# Constants are written in CAPITAL_SNAKE_CASE, e.g. MAX_SPEED, MAX_POWER
