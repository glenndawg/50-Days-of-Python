# Day 45: Words and Special Characters
# Write a function called analyse_string that returns the number of
# special characters (#$%&'()*+,-./:;<=>?@[\]^_`{|}~), words, and, total
# characters (all letters and special characters minus whitespaces) in
# a string. Return everything in a dictionary format:
# {“special character”: “number”, “words”: “number”, “total
# characters”: “number”}
# Use the string below as an argument:
# “Python has a string format operator %. This functions analogously to
# printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2)
# evaluates to "spam=blah eggs=2".
import string

word = """Python has a string format operator %. This functions analogously to
          printf format strings in C, e.g. "spam=%s eggs=%d" % ("blah", 2)
          evaluates to "spam=blah eggs=2"""

w_count = 0
char_count = 0
special_char = dict()

def analyze_string(word):
    spec_char = 0
    w_count = len(word.split())
    word = word.replace(' ','')
    char_count = len(word)
    for i in word:
        if i in string.punctuation:
            spec_char += 1      
    special_char.update({"Special character": spec_char})
    special_char.update({"Words": w_count})
    special_char.update({"Total character": char_count})
    print(special_char)

analyze_string(word)

