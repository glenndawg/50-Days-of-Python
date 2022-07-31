# DAY 30 : Most repeated Name
# Write a function called repeated_name that finds the most repeated
# name in the following list.

name =['John','Peter','John','Peter','Jones','Peter']

def repeated_name(name):
    counts = dict()
    for i in name:
        counts[i] = counts.get(i,0) +1
    print(counts)
    max_value = max(counts.values())
    max_key = [k for k,v in counts.items() if v == max_value][0]
    print(f"The name {max_key} is in the list {max_value} times")
    
repeated_name(name)

# or, as per the answer, the very eay away:
# from collections import counter
# def frequent_name(name):
#   return max(counter(name).most common())
