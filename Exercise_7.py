#Find the number of occurrences of a substring in a string

# Write a Python code to find how often the substring “Emma” appears in the given string.
#
# Given:
# str_x = "Emma is good developer. Emma is a writer"
# Expected Output:
# Emma appeared 2 times

str_x = "Emma is good developer. Emma is a writer"
new_s = str_x.count('Emma')
print(f'Emma appeared {new_s} times')