# DAY 2 : STRINGS TO INTEGERS
# Write a function called convert_add that takes a list of strings as an
# argument and converts it to integers and summs the list. For Example
# ['1','3','5'] should be converted to [1,3,5] and summed to 9.

def convert_add(list_int):
    list_int = list(map(int, list_int))
    total = 0
    total = sum(list_int)
    print("The Sum of the list is: ", total)
    return list_int

list_str = ['1','2','3','4','5','6']

print("Original List  :", (list_str))  
print("The new List is: ",convert_add(list_str))

# Question to improve code :
# Can I return the total, and list_int
# How else can I print the sum of the new list outside of the function?

# # Option 1 : Loop and casting
# for i in range(0, len(list_int)):
#       list_int[i] = int(list_int[i])

# Option 2 : List comprehension
# test_list = [int(i) for i in test_list]
