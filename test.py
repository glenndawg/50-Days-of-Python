# total = 0
# for abc in range(5):
#     total = total + abc
# print(total

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