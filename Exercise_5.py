# Write a code to return True if the list’s first and last numbers are the same.
# If the numbers are different, return False.
#
# Given:

numbers_x = [10, 20, 30, 40, 10]
# output True
numbers_y = [75, 65, 35, 75, 30]
# Output False
def numbers_check(num):
    if num[0] == num[-1]:
        return True
    else:
        return False
print(numbers_check(numbers_x))
print(numbers_check(numbers_y)) 
















