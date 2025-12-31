# Get each digit from a number in the reverse order.
#
# For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
#
# Given:
number = 7536
# Output 6 3 5 7


def digit(number):
    result = []
    while number > 0:
        last_num = number % 10
        result.append(str(last_num))
        number = number // 10
    return ' '.join(result)

print(digit(number))
# print(end=" ")
