import random

while True:
    money = int(input("How much money do you want to start off with? "))
    if money >= 50:
        break
    else:
        print("You need at least $50 to start playing")

money_ori = money#记录最初金额

while True:
    
    if money == 0:
        print("That's a shame.  You have lost ${} during this session".format(money_ori))
    
    bet = int(input("How much do you want to bet (Enter 0 to end)? "))
    if bet == 0:
        win = money - money_ori
        if win < 0:
            print("That's a shame.  You have lost ${} during this session".format(abs(win)))
        elif win > 0:
            print("Well done.  You have won ${} during this session.".format(win))
        else:
            print("Not bad.  You broke even during this session")
        break
    
    elif bet > money:
        print("You don't have enough to bet that much")
        
    else:
        print("Come out roll")
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        if a+b == 7 or a+b == 11:
            print("\tRoll is {} and {}:{} >-  You win".format(a, b, format(a+b, ">3d")))
            money += bet
            print("You now have ${}".format(money))
            continue
        elif a+b == 2 or a+b == 3 or a+b == 12:
            print("\tRoll is {} and {}:{} >-  You lose".format(a, b, format(a+b, ">3d")))

            money -= bet
            print("You now have ${}".format(money))
            continue
        else:
            point = a+b
            print("\tRoll is {} and {}:{}".format(a, b, format(a+b, ">3d")))
            print("The point is {}".format(point))
        
        while True:
            a = random.randint(1, 6)
            b = random.randint(1, 6)
            if a+b == 7 or a+b == 11:
                print("\tRoll is {} and {}:{} >-  You win".format(a, b, format(a+b, ">3d")))
                money += bet*point
                print("You now have ${}".format(money))
                break
            elif a+b == 2 or a+b == 3 or a+b == 12:
                print("\tRoll is {} and {}:{} >-  You lose".format(a, b, format(a+b, ">3d")))
                if bet*point > money:
                    money = 0
                    print("You now have $0")
                else:
                    money -= bet*point
                    print("You now have ${}".format(money))
                break
            else:
                print("\tRoll is {} and {}:{} >-  Roll again".format(a, b, format(a+b, ">3d")))
                