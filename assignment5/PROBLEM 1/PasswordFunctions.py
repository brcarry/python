# Import string
import string

# FUNCTION: password_input()
# INPUT: none.
# PROCESSING:
#   Asks user to input password.
#   Checks user input for length.
#   Prompts re-entry if password is less than 8 characters.
# OUTPUT: returns password.
def password_input():
    while True:
        password = input("Enter a password: ")
        if len(password) >= 8:
            break
        else:
            print("INVALID PASSWORD\nPassword too short!\n")
            continue
    return password

# FUNCTION: uppercase_check(arg)
# INPUT: string argument.
# PROCESSING:
#   Uses a for loop to iterate over arg.
#   Returns True if a character is uppercase.
#   Otherwise returns False.
# OUTPUT: returns True or False.
def uppercase_check(arg):
    uppercase_element = False
    for i in arg:
        if i in string.ascii_uppercase:
            uppercase_element = True
            break
    return uppercase_element
