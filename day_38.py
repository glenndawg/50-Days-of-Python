# Day 38: Guess a Number
# Write a function called guess_a_number. The function should ask
# a user to guess a randomly generated number. If the user guesses
# a higher number, the code should tell them that the guess is too high,
# if the user guesses low, the code should tell them that their guess is
# too low. The user should get a maximum of three guesses. When the
# user guesses right, the code should declare them a winner. After
# three wrong guesses, the code should declare them a loser.
import random

random_num = int(random.randrange(0,9,1))
print(random_num) # one must know the answer to check, haha!

def guess_a_number():
    count = 1 
    while True:
        if count <= 3:
            guess = int(input("Please guess the number from 0 to 9 :"))
            count += 1
            if guess == random_num:
                print("You have guessed correctly. WINNER!")
                break  
            elif guess > random_num:
                print('Your guess is too high')
            elif guess < random_num:
                print('Your guess is too low')
        else:
            print("You have guessed incorrectly. LOSER!")
            break

guess_a_number()

