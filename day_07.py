# DAY 7 : A strring Range
# Write a function called string_range that takes a single number and
# returns a string of its range. The string characters should be 
# seperated by dots(.). For example, if you pass 6 as an argument, 
# your functiomn should return '0.1.2.3.4.5'

def string_range(num):
    string = ""
    count = 0
    while count < num:
        if count < num - 1:
            string = string + (str(count) + ".")
        else:
            string = string + (str(count))
        count += 1
    return(string)
    
while True:
    try:
        num = int(input("Please enter an integer : "))
        break
    except ValueError:
        print("Please enter a whole number")

print(string_range(num))

# works great! Whats the better way ??


