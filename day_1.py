# Write a function called divide_or_square that takes one argument (a number),
# and returns the square root of the number if it is divisible by 5,
# returns its remaindeer if it is not divisible by 5. For example, if you pass 10
# as an argument, then your function should return 3.16 as the square root.

import math

number = input("Please enter an integer greater than 5 :")

try:
    number = int(number)
except:
    print("Error, please input a whole number")
    quit()
    
test = int(number % 5)

if test == 0:
    answer = math.sqrt(number)
    print("The square root of", number, "is", answer)
else:
    answer = number % 5
    print(number, "Divide by 5 has a remainder of :", answer)
