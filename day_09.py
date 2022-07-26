# DAY 9 : BIGGEST ODD NUMBER
# Create a function called biggest_odd that takes a string of numbers
# and returns the biggest odd number in the list. For example, if you 
# pass '23569' as an argument, your funsction should return 9.
# Use list comprehension.

while True:
    try:
        num = int(input("Please enter an integer : "))
        break
    except ValueError:
        print("Please enter a whole number")

def biggest_odd(num):
    num_list = [int(x) for x in str(num)]
    odd_list = [x for x in num_list if x % 2 != 0]
    biggest = max(odd_list)
    return biggest

print(f"The largest odd number in {num} is {biggest_odd(num)}") 

# This was fun, and a great way to learn list comprehension better.
# can I incorporate the first list comprehension statement into the next
# for only one ??? YES!! Convert to a string in the list comprehension
# odd_list = [x for x in num if int(x) % 2 != 0]