# Re-create the guess-my-number game from scratch. Don't peek!
# This time, give your players only a certain amount of tries 
# before they lose.

import random
import sys

input_num = int(input("please guess a number: "))
guess_num = random.randrange(10)
counter = 0

while input_num != guess_num:
    print("oops please try again")
    counter += 1
    if counter >= 5:
        print("sorry, there is no more try")
        sys.exit()
    input_num = int(input("please guess a number: "))


print("Congratulation, you guess right!")

