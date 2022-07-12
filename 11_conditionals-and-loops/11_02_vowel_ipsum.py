# Print the total number of vowels that are used in the lorem ipsum text.

lorem_ipsum = """Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut 
aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in 
voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt 
mollit anim id est laborum."""

a_count = lorem_ipsum.count("a")
e_count = lorem_ipsum.count("e")
i_count = lorem_ipsum.count("i")
o_count = lorem_ipsum.count("o")
u_count = lorem_ipsum.count("u")

print(a_count + e_count + i_count + o_count + u_count)