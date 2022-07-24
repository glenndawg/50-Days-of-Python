# DAY 14 : FLATTEN THE LIST
# Write a function called flat_list that takes one argument, a nested
# list. The function converts the nested list into a one dimensional list.
# For example [[2,3,4,5]] should return [2,3,4,5].

list = [[1,4,7,9]]

def flat_list(list):
    new_list = []
    new_list = [x for x in list[0]]
    return new_list

print(f"The nested list is {list}")
print(f"The one dimensional list is {flat_list(list)}")

