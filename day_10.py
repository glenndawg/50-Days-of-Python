# DAY 10 : HIDE MY PASSWORD
# Write a function called hide_password that takes no parameters.
# The function takes an input(a password) from a user and returns a
# hidden password, For Example, if the user enters 'hello' as a 
# password the function should return '****' as a password and tell the 
# user that the password is 4 characters long.

def hide_password():
    pswd = input("Please enter your password : ")
    new_pswd = len(pswd) * '*'
    return new_pswd

print(f"Your new password is '{hide_password()}' and is 4 characters long")

