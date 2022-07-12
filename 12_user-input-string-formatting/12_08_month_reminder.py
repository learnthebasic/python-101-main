# Take in a number between 1 and 12 from the user
# and print the name of the associated month:
# "January", "February", ... "December"
# Print "Error" if the number from the user is not between 1 and 12.
# Use a nested `if` statement.

month_assign = {
    1:"Janurary",
    2:"Feburary",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"Novemember",
    12:"December"}

query = int(input("please input a number between 1 and 12: "))
if not (query >= 1 and query <= 12):
    print("invalid number")
else:
    result = month_assign[query]
    print(f"the number is month {result}")