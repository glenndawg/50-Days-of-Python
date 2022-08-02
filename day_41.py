# Day 41: Only Words with Vowels
# Create a function called words_with_vowels, this function takes a
# string of words and returns a list of only words that have vowels in
# them. For example ‘ You have no rhythm’ should return
# [‘You’,’have’, ‘no’].

sent = 'You have no rythm time'
vowels =['a','e','i','o','u','A','E','I','O','U']

def words_with_vowels(sent):
    words = []
    sent = sent.split()
    for word in sent:
        for i in word:
            if i in vowels:
                words.append(word)
                break
    print(words)

words_with_vowels(sent)