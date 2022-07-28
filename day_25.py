# DAY 25 : ALL THE SAME
# Create a function called all_the_same that takes one argument, a
# string, a list, or a tuple and checks if all the elements are the same.
# If the elements are ther same, the function should return True. If not,
# it should return False. For example, ['Mary','Mary','Mary'] shoud return True.

thelist =['Mary','Maty','Mary']
word = 'aaabb'
things = ('nicky','nicky','nick')

def all_the_same(thegoods):
    for i in range(len(thegoods)):
        if thegoods[i] == thegoods[0]:
            ans = True
        else:
            ans = False
            break
    return ans


print(f"are all the elements the same ? : {all_the_same(things)}")     

# cool. use a loop to check each element against the first.
# or just use the all() and a list comprehension statement - from the answers
# a = all(i == a[0] for i in a)
# return a