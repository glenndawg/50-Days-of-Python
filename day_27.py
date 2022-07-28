# DAY 27 : IUNIQUE NUMBERS
# Write a function called inique_numbers that takes a list of numbers
# as an argument. Your function is going to find all the unique numbers
# in the list. It will then sum up the unque numbers. You will calculate
# the difference between the sum of all numbers in the original list
# and the sum of unique numbers in the list. If the difference is an even 
# number, your function should return the original list. If the difference
# is an odd number, your function should return a list with unique numbers 
# only numbers only. Fro example[1,2,4,5,6,7,8,8] should return [1,2,4,5,6,7,8,8]

num = [1,2,4,5,6,7,8,8]

def unique_numbers(num):
    uniq_num = set(num)
    if (sum(num) - sum(uniq_num)) % 2 == 0:
        return f"The difference is even and the original list is {num}"
    else:
        return f"The difference is odd and the unique list is : {list(uniq_num)}"
    
print(unique_numbers(num))

