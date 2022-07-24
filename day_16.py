# DAY 16 : SUM THE LIST
# 
# Write a function called sum_list with one parameter thattakes a 
# nested list of integers as an argument and return the sum of the 
# integers. Foe Example, if you pass [[2,4,5,6],[2,3,5,6]] as an
# argument your function should return a sum of 33.

l = [[2,8,5,6],[8,3,5,6]]

def sum_list(l):
    tot = 0
    for i in range(len(l)):
        if type(l[i]) == list:
            tot += sum_list(l[i])
        else:
            tot += l[i]    
    return tot 

print(f"The sum of all the nested lists are : {sum_list(l)}")

# This was fun and challenging. First time understanding and 
# using recursion. Using a def function, to call itself. 
# Very satisfying!!