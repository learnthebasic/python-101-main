# Write a program that takes a number between 1 and 1,000,000,000
# from the user and determines whether it is divisible by 3 using an `if` statement.
# Print the result.

integer = int(input("please input an integer between 1 and 1,000,000,000: "))
result = None
if integer < 1 or integer > 1000000000:
    print("invalid number")
else:
    if integer % 3 == 0:
        result = integer / 3
        print (f"your result is {result}")
    else:
        print(f"your integer is not divisible by 3")