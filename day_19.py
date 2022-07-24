# DAY 19 : WORDS AND ELEMENTS
# Write two functions. The first function is called count_words which
# takes a string of words and counts how many words are in the string.
# The second function called count_elements takes a string of words
# and counts how many elements are in the string. Do not count the 
# whitespaces. The first function will return the number of words in a
# string and the second one will return the number of elements (less 
# whitespace). If you pass "I Love Learning", the count_words function
# should return 3 words and count_elements should return 13 elements.

words = input("Please enter a short sentence : ")

def count_words(words):
    global word_list
    word_list = words.split()
    word_count = len(word_list)
    return word_count

def count_elements(word_list):
    count = 0
    for i in range(len(word_list)):
        count += len(word_list[i])
    return count

print(f"The number of words is {count_words(words)}")
print(f"The nember of elements is {count_elements(word_list)}")