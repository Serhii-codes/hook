#Check Palindrome Number

# Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward.
# For example, 545 is a palindrome number.
#
# Expected Output:
#
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number

new_num1 = input('Please enter our number:')
if new_num1[::-1] == new_num1:
    print('Yes. given number is palindrome number')
else:
    print('No. given number is not palindrome number')

new_num1 = int(input('Please enter our number:'))
original_num = new_num1
rev_num = 0
while new_num1 > 0:
    last_num = new_num1 % 10
    rev_num = rev_num * 10 + last_num
    new_num1 = new_num1 // 10
if original_num == rev_num:
    print('Yes. given number is palindrome number')
else:
    print('No. given number is not palindrome number')