# EXTRA CHALLENGE : STRINGS WITH A THOUSAND SEPERATOR
# Your new company has a list of figures saved in a list. The issue is
# that these numbers have no seperator. The number are saved in
# the following format: [1000000,2356989,2354672,987098]

# You have been asked to write a code that will convert each of the 
# numbers in the list into a string. Your code should then add a
# comma on each number as a thousand seperator for readability.
# When you run your code on the above list, your output should be :

# ['1,000,000','2,356,9989','2,354,672','9,878,098']

numbers = [1000000,2356989,2354672,987098,34687654]
print(numbers)

def add_comma(numbers):
    return (f'{numbers:,}') # return ("{:,}".format(number)) also works

new_list = [add_comma(x) for x in numbers]
print(new_list)


# This is easy to do woth out converting to a string.
# num_list = [str(x) for x in numbers] will convert the list 
# to strings, but I do not know how to add the commas to a string.
