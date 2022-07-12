# Use a `for` loop to print out every fifth number counting from 1 to 1000.
# i.e. sum 5, 10, 15, 20 ...

x=1
for x in range(1001):
    if x % 5 == 0:
        print(x)