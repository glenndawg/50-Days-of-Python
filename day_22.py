# DAY 22 : ADD UNDER_SCORE
# CReate three functions. The first called add_hash takes a string and
# adds a hash # between the words. The second function called
# add_underscore removes the hash(#) and replaces it woith an 
# underscore removes the hash(#) and replaces it with an underscore (_)
# the third function called remove_underscore, removes the underscore 
# and replaces it with nothing. If you pass 'Python' as an argument for 
# the three functions, and you call them at the same time like:
# print(remove_underscore(add_underscore(add_hash("Python")))) it should
# return 'Python'

a = 'Python'

def add_hash(a):
    x = [str(i) for i in a] # x = "#".join(x)  - is all you need
    x = "#".join(x)
    return x

def add_underscore(a):
    x = ''.join([str(i.replace("#","_")) for i in a])
    return x # str(a).replace("#","_") - is all you need

def remove_underscore(a):
    x = ''.join([str(i.replace("_","")) for i in a])
    return x # str(a).replace("_","") - is all you need

print(a)
print(add_hash(a))
print(add_underscore(add_hash(a)))
print(remove_underscore(add_underscore(add_hash(a))))

# I made this more comlicated than needed, but noting is lost.
# I gained some more list comprehension skills and string 
# manipulation understanding. Thumbs up!!