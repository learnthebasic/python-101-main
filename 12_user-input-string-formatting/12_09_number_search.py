# Ask your user for a number between 0 and 1,000,000,000.
# Use a `while` loop to find the number. When the number is found,
# exit the loop and print the number to the console.

query = int(input("please input a number between 0 and 1,000,000,000: "))
x = 0
if not (query >= 0 and query <= 1000000000):
    print("invalid number")
else:
    while x != query:
        print(".")
        x += 1
    print(x)
