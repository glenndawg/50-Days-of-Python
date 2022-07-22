# DAY 12 : COUNT THE DOTS
# Write a function called count_dots. This function takes a string
# seperated by dots as a parameter and counts how many dots are in
# the string. For examlpe, 'h.e.l.p.' should return 4 dots, and 'he.lp'
# should return 2 dots.

string = 'h.e.l.p.'

def count_dots(string):
    count = string.count('.')
    return count

print(count_dots(string))

# using the count() function was the easiest

# here is the list comprehension method
# sum = [x for x in string if x == '.']
# count = len(sum)

# you can also us the filter() function instead with a lambda
# expression instead of list comprehension
# sum = list(filter(lambda x: x == '.', string))

# here is the long version using for loop
# string = 'h.e.l.p'
#
# def count_dots(string):
#     count = 0
#     for x in range(len(string)):
#         if "." == string[x]:
#             count += 1
#             continue
#     return count
#
# print(count_dots(string))
#
# sum = [x for x in string if x = '.']
