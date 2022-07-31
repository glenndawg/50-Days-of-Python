# Day 35: Pangram
# Write a function called check_pangram that takes a string
# and checks if it is a pangram. A pangram is a sentence that
# contains all the letters of the alphabet. If it is a pangram,
# the function should return True, otherwise, return False. The
# following sentence is a pangram so it should return True:
# 'the quick brown fox jumps over a lazy dog'
import string

# words = 'the quick brown fox jumps over a lazy dog'
words = 'Sphinx of black quartz, judge my vow'
alpha = set(string.ascii_lowercase)

def check_pangram(words):
    if set(words.lower()) >= alpha:
        return True
    else:
        return False

print(check_pangram(words))

# I created a set of the lower case alphabet, and compared the two.
# for once, this is quicker then the suggested answer!

