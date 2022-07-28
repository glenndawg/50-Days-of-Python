# DAY 23 : SIMPLE CALCULATOR
# Create a simple calculator. The calculator should be able to perform basic
# math operations, ad, subtract, divide and multiply. The calculator
# should take input from users. The calculator should be able to handle
# ZeroDivisionError, NameError, and ValueError.

import operator

def calculator():
    while True:
        try:
            a = int(input("Please eneter a number : "))
            opp = input("Please enter an opporatoe (+, -, *,/) :")
            b = int(input("Please eneter a number : "))
            if opp not in ['+','-','*','/'] or len(opp) > 1:
                print("Please enter a valid operator")
        except ValueError:
            print('Please prinmt a valid number')
        except ZeroDivisionError:
            print('You cannot divide by zero')
        else:
            if opp == '+':
                return print(f"Answer is : {round(operator.add(a,b),2)}")
            if opp == "-":
                return print(f"Answer is : {round(operator.sub(a,b),2)}")
            if opp == "*":
                return print(f"Answer is : {round(operator.mul(a,b),2)}")
            if opp == "/":
                return print(f"Answer is : {round(operator.truediv(a,b),2)}")
        return print("Try again")

calculator()

# good experience using try and except more. I'll admit this is the first 
# challenge I had to look at the answer for. I wasn't exatly sure what format
# for input would be best. This makes sense now.