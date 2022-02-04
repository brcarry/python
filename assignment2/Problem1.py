money = float(input("How much money did you win? "))
n = int(input("How many people are splitting the winnings? "))
rate = int(input("What is the percent tax rate on lottery winnings? "))

print("\nAs a group, you’ve won ${:,.2f}! Congratulations!".format(money))
print("Split {:d} ways, that amounts to ${:,.2f} in winnings per person.".format(n, money/n))
print("Since the tax rate is {:d}%, each person must pay ${:,.2f} in taxes.".format(rate, money/n*rate/100))
print("Each person will take home ${:,.2f} after taxes.".format(money/n*(100-rate)/100))