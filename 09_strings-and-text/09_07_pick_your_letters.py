# Use string indexing and string concatenation
# to write the sentence "we see trees" only by picking
# the necessary letters from the given string.

word = "tweezers "

t = word[0]
w = word[1]
e = word[2]
r = word[-3]
s = word[-2]

result = w + e + " " + s + e + e + " " + t + r + e + e + s

print(result)
