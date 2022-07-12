# Fetch the text of the CodingNomads collaborative story from:
# https://raw.githubusercontent.com/CodingNomads/collaborative-story/master/story.txt
# Save it to a variable in this script and remember to use triple-double quotes
# for creating a multi-line string.
#
# Use a `for` loop to iterate over the story text
# and string slicing to translate it to ~pig latin.
# For the purpose of this program, we will say that any word or name can be
# translated to pig latin by moving the first letter to the end, followed by "ay".
# You'll need to use conditional statements to decide when a word is over.
#
# For example: You would never guess --> ouyay ouldway evernay uessgay

script = """You would never guess what can happen when you jump into a seemingly shallow puddle at night time!
It turns out that it is not a puddle rather than a giant hole which brings you to a new world on the other side of the light water. Now you are left stunning and don't know what to do.
So you decide to call Whoolio who lives in Never Never land."""

result = ""

line_list = script.split("\n")
for line in line_list:
    result_line = ""
    result_item = ""
    items = line.split(" ")
    for item in items:
        if item[-1].isalpha() == True:
            result_item = str(item[1:]) + str(item[-1]) + "ay"
        else:
            result_item = item[1:-1] + "ay" + item[-1]
        result_line += result_item + " "
    result += result_line + "\n"
print(result)
