# Reverse the string given below in a single line of code
# with the help of string slicing.

palindrome = "too bad i hid a boot"
counter = -1
result = ""

for char in palindrome:
    result += palindrome[counter]
    counter -= 1

print(result)

