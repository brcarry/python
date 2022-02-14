month = input("Enter birth month (MM): ")
if len(month) != 2 or month.isnumeric() == False or int(month) <= 0 or int(month) >12:
    print("Invalid month entry.")
else:
    day = input("Enter birth day (DD): ")
    if len(day) != 2 or day.isnumeric() == False or int(day) <= 0:
        print("Invalid birth day entry.")
    else:
        if int(month) == 1 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 2 and int(day) > 29:
            print("Invalid birth day entry.")
        elif int(month) == 3 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 4 and int(day) > 30:
            print("Invalid birth day entry.")
        elif int(month) == 5 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 6 and int(day) > 30:
            print("Invalid birth day entry.")
        elif int(month) == 7 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 8 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 9 and int(day) > 30:
            print("Invalid birth day entry.")
        elif int(month) == 10 and int(day) > 31:
            print("Invalid birth day entry.")
        elif int(month) == 11 and int(day) > 30:
            print("Invalid birth day entry.")
        elif int(month) == 12 and int(day) > 31:
            print("Invalid birth day entry.")
        else:
            PIN = input("Enter PIN: ")
            if len(PIN) != 4 or PIN.isnumeric() == False:
                print("Invalid PIN.")
            elif PIN == month + day or PIN == day + month:
                print("Invalid PIN.")
            elif PIN == "0000" or PIN == "1111" or PIN == "2222" or PIN == "3333" or PIN == "4444" or PIN == "5555" or PIN == "6666" or PIN == "7777" or PIN == "8888" or PIN == "9999":
                print("Invalid PIN.")
            elif PIN == "1234" or PIN == "2345" or PIN == "3456" or PIN == "4567" or PIN == "5678" or PIN == "6789":
                print("Invalid PIN.")
            else:
                print("Valid PIN")