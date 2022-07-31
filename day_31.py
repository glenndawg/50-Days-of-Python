# DAY 31 : Longest Word
# Write a function that has one parameter and takes a list of words as
# an argument. The function returns the longest word from the list.
# Name the function longest_word. The function should return the
# longest word and the number of letters in that word. For example, if
# you pass ['Java','JavaScript','Python'], your function should return
# ['10,JavaScript]

words = ['Java','JavaScript','Python']

def longest_word(words):
    long = max(words, key = len)
    print(len(long),long)

longest_word(words)

# or , per answer you can loop through and make a new list
# b = []
# for word in words:
#   b.append([len(word), word])
# return max(b)