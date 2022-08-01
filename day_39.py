# Day 39: Password Generator
# Create a function called generate_password that generates any
# length of password for the user. The password should have a
# random mix of upper letters, lower letters, numbers, and
# punctuation symbols. The function should ask the user how
# strong they want the password to be. The user should pick from -
# weak, strong, and very strong. If the user picks weak, the function
# should generate a 5 character long password. If the user picks
# strong, generate an 8 character password and if they pick very
# strong, generate a 12 character password.
import string
import random
 
while True:
    try:
        pswd_type = int(input("Would you like a weak (1), strong (2), or very strong (3) password : "))
        if pswd_type in (1,2,3):
            break
        else:
            print("Please enter a value of 1,2 or 3")
    except ValueError:
        print("Please enter a valid number")

def generate_pswd(pswd_type):
    length = 0
    chars = (string.ascii_letters + string.digits + string.punctuation)
    if pswd_type == 1: 
        length = 5
    if pswd_type == 2: 
        length = 8
    if pswd_type == 3: 
        length = 12    
    pswd = [random.choice(chars) for i in range(length)]
    print(''.join(pswd))
    
generate_pswd(pswd_type)

