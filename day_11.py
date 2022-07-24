# DAY 11 : ARE THEY EQUAL ?
# Write a function called equal_strings. The function takes two strings
# as arguments and compared them. If the strings are equal (if they 
# have the same characters and have equal length), it should return
# TRUE, if they are not, it should return FALSE. For example, 'love' and 
# 'evol' should return True

string_1 = 'gelato'
string_2 = 'letago'

def equal_strings(x,y):
    if len(x) == len(y):
        for i in range(len(x)):
            if x[i] in y:
                continue
            else:
                return False
        return True
    else:
        return False  

print(equal_strings(string_1,string_2))

# in another method, I used list comprehension to create a list of
# True values for all that are true. If The list is as long as the string
# then the answer is true. Fun to use list comprehension for this.

# string_1 = 'charm'
# string_2 = 'cdmra'

# def equal_strings(x,y):
#     if len(x) == len(y):
#         answer = [True for x in x if x in y] 
#         if len(answer) == len(x):
#             return True
#         else:
#             return False 
#     else:
#         return False  

# print(equal_strings(string_1,string_2))
