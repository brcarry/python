def num_cleaner(s):
    l = list(s)
    formatted_s = ""
    for item in l:
        if "0" <= item <= "9":
            formatted_s += item
    return formatted_s


def num_formatter(s):
    l = list(s)
    l.insert(6, "-")
    l.insert(3, ")")
    l.insert(0, "(")
    formatted_s = ""
    return formatted_s.join(l)


string_input = ""
f1 = open("LastName_user_input.txt","w")
f2 = open("LastName_formatted_numbers.txt","w")

while True:
    string_input = input()
    f1.write(string_input)
    f1.write("\n")
    if string_input == "Q":
        break
    
    number_input = num_cleaner(string_input)
    
    if len(number_input) != 10:
        print("Please input 10 digits. Try again")
        continue
    
    f2.write(num_formatter(number_input))
    f2.write("\n")

f1.close()
f2.close()
        
    
    
    
    
    
    