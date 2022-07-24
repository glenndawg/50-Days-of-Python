# DAY 15 : SAME IN REVERSE
# Write a functin called same_in_reverse that takes a string and
# chceks if the string reads the same in reverse. If it is the same, the
# code should return True if not, it should return False. For Example,
# 'dad' should return True, because it reads the same in reverse.

while True:
    try:
        word = str(input("Please enter a string :"))
        break
    except ValueError:
        print("Please enter a string")

def same_in_reverse(word):
    reverse = word[::-1]
    if reverse == word:
        answer = True
    else:
        answer = False
    return answer

print(f"Is the word you entered the same in reverse ?: {same_in_reverse(word)}")



