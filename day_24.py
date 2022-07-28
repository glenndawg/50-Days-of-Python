# DAY 24 : AVERAGE CALORIES
# Create a function called average_calories that calculate the average
# calories intake of a user. The function should ask the user to input their 
# calories intake for any number of days and once they hit 'done' it should
# calculater and return the average intake.

calories = []
daily = 0

while True:
    try:
        while True:
            daily = int(input("Please enter you daily calorie intake (type done when finished)"))    
            calories.append(daily)
    except ValueError:
        break

def average_calories(calories):
        day_avg = sum(calories) / len(calories)
        print(f'You average daily calorie intake is : {day_avg:.2f}')

average_calories(calories)

# Ok, the inout will break with any non integer input. How can I get it to 
# error and ask for an integer, except when the string 'done' is inputed ?