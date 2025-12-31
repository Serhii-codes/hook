#Print characters present at an even index number
# Write a Python code to accept a string from the user and display characters present at an even index number.
# For example, str = "PYnative". so your code should display ‘P’, ‘n’, ‘t’, ‘v’.
#
# Expected Output:
#
# Orginal String is  PYnative
# Printing only even index chars
# P
# n
# t
# v

str_1 = input()
for i in range(0, len(str_1), 2):
    print(str_1[i])

# *_, = 'PYnative'
# print(_)