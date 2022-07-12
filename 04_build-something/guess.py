# All the text in here are Python code comments.
# A Python code comment starts with a hash symbol (#).
# Python will ignore this when running the file.
# You'll see instructions for your labs written in code comments.
# --------------------------------
# Here's your first task:
# Re-create the guess-my-number game from the course.
# Type the whole code out instead of copy-pasting.
# Typing out code, even if you just copy it, trains your coding skills!
# Write your code below:

import random

input_num = int(input("please guess a number: "))
guess_num = random.randrange(10)

while input_num != guess_num:
    print("oops please try again")
    input_num = int(input("please guess a number: "))

print("Congratulation, you guess right!")

