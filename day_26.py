# DAY 26 : SORT WORDS
# Write a function called sort_words that takes a string of words as an
# argument, removes the whitespaces, and returns a list of letters
# sorted in alphabetical order. Letters will be seperated by commas. All
# letters should appear once in the list. This means that you sort and
# remove duplicates. For example 'love life' should return as ['e,f,i,l,o,v]

words = input("Please say a few words :")

def sorted_words(words):
    new_list = [words[x] for x in range(len(words)) if words[x] != " "]
    sort_list = [','.join(sorted(set(new_list)))]
    return sort_list
    
print(sorted_words(words))

