# Write a function called divide_or_square that takes one argument (a number),
# and returns the square root of the number if it is divisible by 5,
# returns its remaindeer if it is not divisible by 5. For example, if you pass 10
# as an argument, then your function should return 3.16 as the square root.

import math

while True:
    try:
        number = int(input("Please enter an integer greater than 5 :"))
        if number < 5:
            raise ValueError
        break
    except ValueError:
        print("Please enter a whole number greater than or equal to 5")

def divide_or_square(number): 
    global test   
    test = int(number % 5)
    if test == 0:
        answer = math.sqrt(number)
    else:
        answer = number % 5
    return(answer) 

answer = divide_or_square(number)
if (test % 5) == 0:
    print(f"The square root of {number} is {round(answer,2)}")
else:
   print(f"{number} Divided by 5 has a remainder of : {answer}")