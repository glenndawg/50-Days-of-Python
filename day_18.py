# DAY 18 : AMY NUMBER OF ARGUMENTS
# Write a function called any_number that can receive any number of
# arguments (integers and floats) and return the average of those
# integers. If you pass 12, 90, 12, 34 as arguments your function
# should return 37.0 as average. If you pass 12, 90 your function
# should return 51.0 as average.

from types import NoneType


numbers = []
number = 0

while number != 9:
    try:
        number = float(input("Please enter any number and enter 9 when done : "))
        numbers.append(number)
        break
    except ValueError:
        print("Please enter a valid number")

print(numbers)


def any_numbers(numbers):
    average = round((sum(numbers)/len(numbers)),1)
    print(type(average))
    return average

print(f"The average of your list is : {any_numbers(numbers)}")