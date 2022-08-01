# Day 37: Count the Vowels
# Create a function called count_the_vowels. The function takes one
# argument, a string, and returns the number of vowels in the string.
# For example ‘hello’ should return 2 vowels. If a vowel appears in a
# string more than once it should be counted as one. For example,
# ‘saas’ should return 1 vowel. Your code should count lowercase and
# uppercase vowels.

name = 'hello'
vowels =['a','e','i','o','u','A','E','I','O','U']

def count_the_vowels(name):
    vowel_count = set()
    for i in name:
        if i in vowels:
            vowel_count.add(i)
    print(f"There are/is {len(vowel_count)} vowel")  

count_the_vowels(name)         

