# DAY 8 : ODD AND EVEN
# Write a function called odd_even that has one perameter
# and takes a list of numbers as an argument. The function
# returns the difference between the largest even number in
# the listand the smallest odd number in the list. For example
# if you pass [1,2,4,6] as an argument the function should 
# retuen 6-1=5.

numbers = [2,3,4,6,7,12]

def odd_even(numbers):
    # find odd numbers
    odd_nums = list()
    even_nums = list()
    for i in range(len(numbers)):
        if numbers[i] % 2 != 0:
            odd_nums.append(numbers[i])
        else:
            even_nums.append(numbers[i])
    print(f"Odd list  : {odd_nums}")
    print(f"Even list : {even_nums}")
    answer = max(even_nums) - min(odd_nums)
    print(f"The answer is {max(even_nums)} - {min(odd_nums)} = {answer}")
    
odd_even(numbers)
