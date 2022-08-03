# Day 48: Binary Search
# Write a function called search_binary that searches for the number
# 22 in the following list and returns its index. The function should take
# two parameters, the list and the item that is being searched for. Use
# binary search (iterative Method).

list1 = [12, 34, 56, 78, 98, 22, 45, 13]
num = 22

def search_binary(list1, num):
    for k,v in enumerate(list1):
        if v == num:
            return k

print(search_binary(list1, num))

# The question asked for binary itteration to be used. I saw that after enumerating the
# list, which seems far more sensible. 
