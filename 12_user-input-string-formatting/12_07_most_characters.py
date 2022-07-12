# Write a script that takes three strings from the user
# and prints the longest string together with its length.
#
# Example Input:
#     hello
#     world
#     greetings
#
# Example Output:
#     9, greetings

phrase = input("please input three strings: ")
items = phrase.split(" ")
x = []
for item in items:
    x.append(len(item))
result = str(max(x)) + ", " + str(items[x.index(max(x))])
print(f"your longest string is: {result}")