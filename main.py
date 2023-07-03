
# # modulirize python code
# import calc 
# # Or import calc as calculation (alias)
# # Or from calc import * (import all)
# # Or from calc import addtion, subtraction (import specific)
# # Or from calc import addtion as add (import specific with alias)

# print(calc.addtion(1, 2))
# print(calc.subtraction(1, 2))
# print(calc.multiplication(1, 2))
# print(calc.division(1, 2))
# print(calc.PI)


import math, random

# print(math.pi)

# # what is factorial
# # 5! = 5 * 4 * 3 * 2 * 1
# print(math.factorial(5))


# random module: EXPLORE LATER

print(random.random())
print(random.random() * 10)

print(random.randint(1, 10))

print(random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
print(random.choice(range(1, 10)))

print(random.sample(range(1, 10), 3))
print(random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))
print(random.sample(range(1, 10), 3))

print(random.seed(1))
print(random.uniform(1, 10))

lottery = ["susi", "Carsten", "Dieter", "Hans", "Daniela"]
random.shuffle(lottery)
print(random.choice(lottery))
print(random.choices(lottery, k=2))
print(random.sample(lottery, k=3)) # ONE VALUE CAN ONLY BE CHOSEN ONCE




