# EXTRA CHALLENGE : TEACHER'S SALARY
# A school has asked you to write a program that will calculate
# teacher's salaries. The program should ask the user to enter the
# teacher's name, the number of periods taught in a month, and the
# rate per period. The monthly salary is calculated by multiplying the 
# number of periods by the monthly rate. The current monthly rate 
# per period is $20. If a teacher has more than 100 periods in a month,
# everything above is over time. Overtime is $25 per period. For
# example, is a teacher has taught 105 periods, their monthly gross
# salary should be 2,125. Write a function called your_salary that
# # calculate a teacher's gross salary. The function should return the
# teacher's name, periods taught, and a gross salary. Here is how 
# you should format your output:
# Teacher: John Kelly
# Periods: 105
# Gross salary: 2,125

name = input("Please enter the teachers name : ")
periods = int(input(f"How many periods did {name} teach ? "))
rate = 20
ot_rate = 25

def your_salary(name,periods):
    if periods > 100:
        gross = (100 * rate) + (periods - 100) * ot_rate
    else:
        gross = periods * rate
    return gross

print(f"Teacher: {name}")
print(f"Periods: {periods}")
print(f"Gross salary : {your_salary(name, periods)}")

# easy enough