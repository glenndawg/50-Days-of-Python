# DAY 4 : ONLY FLOATS
# Write a function called only_floats, which takes two parameters
# a and b, and returns 2 if both arguments are floats, returns 1 
# if only on argument is a float, and returns 0 if neither argument
# is a float. If youpass (12.1,23) as an argument, youfunction should 
# return a 1.

test = [1.2,23]
a = test[0]
b = test[1]

def only_float(a,b):
    if isinstance(a, float) and isinstance(b, float):
        count = 2
    elif isinstance(a, float) or isinstance(b, float):
        count = 1
    else:
        count = 0
    return count


print(f"The variables are a = {a} and b = {b}")
print(f"The answer is : {only_float(a,b)}")

# ok, so this works great! There must be an easier way.

