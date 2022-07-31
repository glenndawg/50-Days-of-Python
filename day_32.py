# Day 32: Password Validator
# Write a function called password_validator. The function asks the
# user to enter a password. A valid password should have at least one
# upper letter, one lower letter, and one number. It should not be
# less than 8 characters long. When the user enters a password, the
# function should check if the password is valid. If the password is
# valid, the function should return the valid password. If the password
# is not valid, the function should tell the users the errors in the
# password and prompt the user to enter another password. The
# code should only stop once the user enters a valid password. (use
# while loop).

instructions = ('Your password should contain at least one uppercase'
                'one lowercase, onenumber and be at least 8 char long')
print(instructions)

while True:
    pswd = input("Please enter your password :")
    if len(pswd) < 8:
        print("You password needs to be at least 8 characters")
    elif pswd.isupper() is True:
        print("You must use at least one lowercase letter")
    elif pswd.islower() is True:
        print("You must use at least one uppercase letter")
    elif True not in [x.isdigit() for x in pswd]:
        print("Please incluse at least one number")
    else:
        break

print(f'Your password is legit')



