# Create a sarcastic program that asks a user for their honest opinion,
# then prints the same sentence back to them in aLtErNaTiNg CaPs.

phrase = input("please input a phrase: ")
result = ""

counter = 2
for char in phrase:
    if char.isalpha() == True:
        if counter % 2 == 0:
            result += char.lower()
        if counter % 2 != 0:
            result += char.upper()
        counter += 1
    else:
        result += char
print(result)
