# DAY 6 : USER NAME GENERATOR
# Write a function called user_name that generates a username from 
# the user's email. The code should ask the user to input an email and
# the code should return everything before the @ sign as their user 
# name. For example, if someone enters ben@gmail.com, the code 
# should return ben as their user name.

import re
def user_name(email):
    name = email.split('@')[0]
    return name

email = input("Please enter you email address : ")

print(f"Your user name is : {user_name(email)}")

# How do I check the text to see if it in fact 
# an email address?

# Another method, but less efficient is :
# name = email.rpartition('@'[0])
# retuen name[0]

