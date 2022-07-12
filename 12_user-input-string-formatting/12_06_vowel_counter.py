# Write a script that takes a string input from a user
# and prints a total count of how often each individual vowel appeared.

phrase = str(input("please input a phrase: "))

a_count = phrase.count("a")
e_count = phrase.count("e")
i_count = phrase.count("i")
o_count = phrase.count("o")
u_count = phrase.count("u")

print(f"a occurs {a_count} times")
print(f"e occurs {e_count} times")
print(f"i occurs {i_count} times")
print(f"o occurs {o_count} times")
print(f"u occurs {u_count} times")
