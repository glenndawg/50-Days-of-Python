# Day 34: Just Digits
# In this challenge, copy the text below and save it as a CSV file.
# Save it in the same folder as your Python file. Save it as python.csv.
# Write a function called just_digits that reads the text from the CSV
# file and returns only digit elements from the file. Your function should
# return 1991, 2, 200, 3, 2008 as a list of strings.

file = open('python.csv','r') 
data = file.read().split(' ')
data = [i.replace(',','') for i in data]


def just_digits(data):
    print(data)
    num_list = []
    for word in data:
        if word.isdigit():
            print(word) # I do this as a print test when I run the code
            num_list.append(word)
    print(num_list)

just_digits(data)   

# This is almost exatly like the answer, but why is it only finding one number?
# maybe my csv file is not correct. I tried the code in the answer also, and I also 
# only got one number. Hmmm??



