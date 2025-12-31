# Remove first n characters from a string
#
# Write a Python code to remove characters from a string from 0 to n and return a new string.
# Note: n must be less than the length of the string.
# Given:

def remove_chars(word, n):
    new_str = word[n:]
    return new_str

    # write your code

print("Removing characters from a string")
print(remove_chars("pynative", 4))
# output 'tive' first four characters are removed

print(remove_chars("pynative", 2))
# output 'native'