# Define a property that must have the same value for every class instance (object)
#
# Define a class attribute”color” with a default value white. I.e., Every Vehicle should be white.
#
# Use the following code for this exercise.
#
# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
# class Bus(Vehicle):
#     pass
#
# class Car(Vehicle):
#     pass
#
# Expected Output:
#
# Color: White, Vehicle name: School Volvo, Speed: 180, Mileage: 12
# Color: White, Vehicle name: Audi Q5, Speed: 240, Mileage: 18

class Vehicle:
    color = 'White'

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

b = Bus('School Volvo', 180, 12)
b1 = Car('Audi Q5', 240, 18)
print(f'Color: {b.color}, Vehicle name: {b.name}, Speed: {b.max_speed}, Mileage: {b.mileage}')
print(f'Color: {b1.color}, Vehicle name: {b1.name}, Speed: {b1.max_speed}, Mileage: {b1.mileage}')



