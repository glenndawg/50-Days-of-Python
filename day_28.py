# DAY 28 : RETURN INDEXES
# Write a function called index_position. THis function takes a string
# as a parameter and returns the positions or indexes of all lowercase
# letters in the string. Fro example 'LovE' shoud return [1,2]

name = 'LovE iS in tHE aiR'

def index_position(name):
    index_list = []
    index_list = [i for i,v in enumerate(name) if v.islower()]
    return index_list
    
print(index_position(name))

# List comprehesion and enumerate function. I like this!

