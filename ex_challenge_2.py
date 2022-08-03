# EXTRA CHALLENGE : YOUR AGE IN MINUTES
# Write a function called age_in_minutes that tells a user how old they
# are in minutes. Your code should ask the user to enter their year of
# birth, and it should return their age in minutes (by subtracting their year
# of birth to the current year). Here are the things to look for:
#
# a. The user can olny input a 4 digit year of birth. For example, 1930
#    is a valid year. However, entering any number longer or less than 
#    4 digits long should render inout invalid. Notify the user to input a
#    four digit number.
# b. If user enters a year before 1900, your code should tell the user
#    that the input is invalid. If the user enters the year after the current 
#    year, the code should tell the user, to input a valid year.
# 
# The code should run until the user inputs a valid year. Your function
# should return the user's age in minutes. For example, if someone enters
# 1930, as their year of birth, your function should return:
#  You are 48,355,300 minutes old. 

from datetime import date

todays_date = date.today()

while True: 
    yob = int(input("Please enter you year of birth : "))
    if len(str(yob)) == 4 and todays_date.year >= yob >= 1900:
        break
    else:
        print("Please enter a valid year")

def age_in_minute(yob):
    age = todays_date.year - yob
    age_min = age*365*24*60
    return (age_min)
    
print(f'{age_in_minute(yob):,}')    
