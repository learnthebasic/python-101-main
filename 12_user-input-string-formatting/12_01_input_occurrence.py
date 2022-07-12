# Write a script that takes a string of words and a letter from the user.
# Find the index of first occurrence of the letter in the string. For example:
#
# String input: hello world
# Letter input: o
# Result: 4

phrase = str(input("please input a letter: "))
char = str(input("please input a character: "))
result = phrase.find(char)

if result == -1:
    result = "not found"

print(f"your result index is: {result}")