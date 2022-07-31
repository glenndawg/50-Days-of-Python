# Day 36: Count String
# Write a function called count that takes one argument a string, and
# returns a dictionary of how many times each element appears in the
# string. For example ‘hello’ should return:
# {‘h’:1,’e’: 1,’l’:2, ‘o’:1}.
from collections import Counter

string = 'hello'

def count_string(name):
  return dict(Counter(name))

print(count_string(string))

