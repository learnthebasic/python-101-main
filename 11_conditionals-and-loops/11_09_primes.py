# Print out every prime number between 1 and 1000.

x = 2
y = 2

for x in range(2,1001):
    flag = True
    for y in range(2,x):
        if x % y == 0:
            flag = False
    if flag == True:
        print(x)
