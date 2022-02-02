first_name = input("First Name: ")
last_name = input("Last Name: ")
addr1 = input("Street Address (line 1): ")
addr2 = input("Street Address (line 2): ")
city = input("City: ")
state = input("State: ")
ZIP = input("ZIP: ")

print("\n" + "+"*3 + "\n")
#print("\n+++\n")感觉简单字符直接输入或许更快 

print(
    first_name + " " + last_name + \
    "'s mailing address is:\n" + \
    addr1 + "\n" + \
    addr2 + "\n" + \
    city + ", " + state + " " +ZIP
    )