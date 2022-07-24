# DAY 20 : Capitalize First Letter
# Write a function called capitalize. This function takes a string as an
# argument and capitalizes the first letter of each word. For Example,
# 'i like learning' becomes 'I Like Learning"

words = input("Please enter a short sentence : ")

def capitalize(words):
    cap_words = str.title(words)
    return cap_words

print(f"The new sentence is : {capitalize(words)}")

# There is a function for everything...almost!