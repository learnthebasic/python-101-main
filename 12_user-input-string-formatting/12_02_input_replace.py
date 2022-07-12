# Write a script that takes a string of words and a symbol from the user.
# Replace all occurrences of the first letter with the symbol. For example:
#
# String input: more python programming please
# Symbol input: §
# Result: §ore python progra§§ing please

phrase = str(input("please input a letter: "))
symbol = str(input("please input a symbol: "))
result = ""

for char in phrase:
    if char == phrase[0]:
        result += symbol
    else:
        result += char

print(f"your result index is: {result}")