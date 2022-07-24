# DAY 18 : AMY NUMBER OF ARGUMENTS
# Write a function called any_number that can receive any number of
# arguments (integers and floats) and return the average of those
# integers. If you pass 12, 90, 12, 34 as arguments your function
# should return 37.0 as average. If you pass 12, 90 your function
# should return 51.0 as average.

while True:
    try:
        numbers = []
        while True:
            num = (int(input("Please enter any number and enter 0 when done : "))) 
            if num != 0:
                numbers.append(num)
            else:
                break
        break
    except ValueError:
        print("Please enter a valid number")

def any_numbers(numbers):
    average = round((sum(numbers)/len(numbers)),1)
    return average

print(f"The average of {numbers} is : {any_numbers(numbers)}")

# This was fun. Can I make the input and try/exccept section shorter?