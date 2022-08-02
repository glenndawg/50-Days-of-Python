# Day 40: Pig Latin
# Write a function called translate that takes the following words and
# translates them into pig Latin.
# Here are the rules:
# 1. If a word starts with a vowel (a,e, i, o, u) add ‘yay’ at the end.
# For example ‘eat’ will become ‘eatyay’
# 2. If a word starts with anything other than a vowel, move the
# first letter to the end and add ‘ay’ to the end. For example
# ‘day’ will become ‘ayday’.
# Your code should return:
# yay ovelay ythonpay

sentence = 'i love python'
words = sentence.split()

vowels =['a','e','i','o','u','A','E','I','O','U']

def translate(words):
    pl = []
    for word in words:
        if word[0] in vowels:
            pl.append(word + 'yay')
        elif word[0] not in vowels:
            pl.append(word[1:] + word[0] + 'ay')
    print(' '.join(pl))
    

translate(words)  