# DAY 3 : REGISTEER CHECK
# Write a function called register_check that checks how many students 
# are in school. The function takes a dictionary as a parameter. If the 
# student is in school, the dictionary says 'yes'. If the student os not in
# school, the dictionary saya 'no'. Your function should return the number
# of students in school. Use the dictionary below. Your function should
# return 3.

register = {'Michael':'yes','John':'no','Peter':'yes','Mary':'yes'}


def register_check(register):
    count = 0
    for value in register.values():
         if value == 'yes':
             count += 1
         else:
             continue
    return count

print(register)
print("Nuber of students in School :", register_check(register))



# This method works, but how can I be more efficient?
# How can I do this with list comprehension?
# any other method?