# Take in the following three values from the user:
# 1. investment amount
# 2. interest rate in percentage
# 3. number of years to invest
#
# Calculate the future values and print them to the console.

notional = float(input("please input your investment amount: "))
rate = float(input("please input the interest rate in percentage: "))
year = float(input("please input year to invest: "))

result = notional * ((1 + rate / 100)**year)

print(f"your future value is {result}")