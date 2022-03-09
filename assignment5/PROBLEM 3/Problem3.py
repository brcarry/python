import PasswordFunctions
import string
'''
• lowercase_check(arg) – checks whether arg contains lowercase letter 
• digit_check(arg)– checks whether arg contains lowercase letter 
• special_check(arg)– checks whether arg contains special character 
• allowed_check(arg) – checks whether arg contains not allowed characters 
• element_check(arg) – checks whether arg contains three or more elements
'''

def lowercase_check(arg):
    flag = False
    for i in arg:
        if i in string.ascii_lowercase:
            flag = True
            break
    return flag

def digit_check(arg):
    flag = False
    for i in arg:
        if i in "0123456789":
            flag = True
            break
    return flag

def special_check(arg):
    flag = False
    for i in arg:
        if i in "*!@#^&_–=[]|;~,./?":
            flag = True
            break
    return flag

def allowed_check(arg):
    flag = False
    for i in arg:
        if i in "*!@#^&_–=[]|;~,./?":
            continue
        elif i.isdigit():
            continue
        elif i in string.ascii_letters:
            continue
        else:
            flag = True
            break
    return flag

def element_check(arg):
    cnt = 0
    if lowercase_check(arg):
        cnt += 1
    if PasswordFunctions.uppercase_check(arg):
        cnt += 1
    if digit_check(arg):
        cnt += 1
    if special_check(arg):
        cnt += 1
    if cnt >= 3:
        return True
    else:
        return False

def password_check():
    while True:
        password = PasswordFunctions.password_input()
        if allowed_check(password):
            print("INVALID PASSWORD.")
            print("Password contains an unsupported character.\n")
        elif element_check(password) == False:
            print("INVALID PASSWORD.")
            print("Password does not contain 3 or more required elements.\n")
        else:
            print("VALID PASSWORD.")
            break

password_check()