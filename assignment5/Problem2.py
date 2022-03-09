def ASCII_shift(original_string, step_size):
    new_string = ""
    for char in original_string:
        if char.isalpha():
            new_string += chr(ord(char)+step_size)
        else:
            new_string += char
    return new_string


while True:
    original_string = input("Enter message to be encrypted: ")
    if original_string == "QUIT":
        break
    else:
        step_size = int(input("Enter step size: "))
        print("\tORIGINAL MESSAGE")
        print("\t" + original_string)
        print("\tENCRYPTED MESSAGE")
        print("\t" + ASCII_shift(original_string, step_size))
