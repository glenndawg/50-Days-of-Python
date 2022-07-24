# DAY 17 : USER NAME GENERATOR
# Write a function called user_name, that creates a username for the
# user. The function should ask a user to input their name. The 
# function should then reverse the name and attach a randomly issued
# number between 0 -9 at the end of the name. The gunction should
# return the user name.

import random

while True:
    try:
        name = str(input("Please enter your name :"))
        break
    except ValueError:
        print("Please enter a string value")

def user_name(name):
    new_name = name[::-1] + str(random.randrange(0,9))
    return new_name

print(f"Your user name is {user_name(name)}")
    



