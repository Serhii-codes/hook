# Class Inheritance
#
# Given:
#
# Create a Bus class that inherits from the Vehicle class. Give the capacity argument of Bus.seating_capacity() a default value of 50.
#
# Use the following code for your parent Vehicle class.
#
# class Vehicle:
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage
#
#     def seating_capacity(self, capacity):
#         return f"The seating capacity of a {self.name} is {capacity} passengers"
#
# Expected Output:
#
# The seating capacity of a bus is 50 passengers

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    pass

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(50)


bus = Bus('bus', 120, 30)
print(bus.seating_capacity())