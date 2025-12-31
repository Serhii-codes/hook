# Given two integer numbers, write a
# Python program to return their product only if the product is equal to or lower than 1000. Otherwise, return their sum.

# number1 = 20
# number2 = 30

def num_1(num1, num2):
    product = num1 * num2
    if product <= 1000:
        return product
    else:
        return num1 + num2

print(num_1(20, 30))
print(num_1(30, 40))
