money = float(input("This program will project how much you will owe the bank at the end of each year assuming that you have an interest only mortgage.\nTo begin, enter the initial size of the mortgage: "))
rate = float(input("Next, enter the annual interest rate: "))
interest = money*rate/100

print("Your maximum monthly payment will be",format(interest/12,",.2f"))

payment = 12*float(input("Now, enter your planned monthly payment: "))

print("Year  Starting Balance   Interest   Payment   Ending Balance")

for i in range(3):
    print(format(i+1,"<6d"),format(money,"<19.1f"),format(interest,"<11,.2f"),format(payment,"<10,.2f"),format(money+interest-payment,"<,.2f"),sep="")
    money = money+interest-payment
    interest = money*rate/100

#如果课程内容还没有讲到循环，可以将for循环拆成三个条语句
#其中i的取值为0,1,2