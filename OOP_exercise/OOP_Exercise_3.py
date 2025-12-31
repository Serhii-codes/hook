#Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

# Given:

# class Vehicle:
#
#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

# Create a Bus object that will inherit all of the variables and methods of the parent Vehicle class and display it.
#
# Expected Output:
#
# Vehicle Name: School Volvo Speed: 180 Mileage: 12

class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self):
        return f'Vehicle Name: {self.name}, Speed: {self.max_speed}, Mileage: {self.mileage}'

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage):
        super().__init__(name, max_speed, mileage)

school_bus = Bus('School Volvo',180,12)
print(school_bus)





