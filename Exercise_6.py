# Write a Python code to display numbers from a list divisible by 5
# Expected Output:
# Given list is  [10, 20, 33, 46, 55]
# Divisible by 5
# 10
# 20
# 55

numbers = [10, 20, 33, 46, 55]

def divisible():
    for i in numbers:
        if i % 5 == 0:
            print(i)

divisible()

# numbers = [12, 75, 150, 180, 145, 525, 50]
for i in numbers:
    if i >= 50:
        print(i)


