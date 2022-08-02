# Day 42: Spelling Checker
# Write a function called spelling_checker. This code asks the user
# to input a word and if a user inputs a wrong spelling it should
# suggest the correct spelling by asking the user if they meant to type
# that word. If the user says no, it should ask the user to enter the
# word again. If the user says yes, it should return the correct word.
# If the word entered by the user is correctly spelled the function
# should return the correct word. Use the module textblob.
from textblob import TextBlob

def spelling_checker():
    ans = 'no'
    while ans == 'no':
        word = TextBlob(input("Please input a word : "))
        if word.correct() == word:
            print(f"nice job : {word.correct()}")
            break
        else:
            ans = input(f"Did you mean to type {word.correct()} ?")
            if ans == 'yes':
                print(word.correct())
            continue

spelling_checker()

# Sweet, spell check!!!