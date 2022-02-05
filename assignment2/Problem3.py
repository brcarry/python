income = float(input("Enter income from 2021: $"))

if income <= 9950:
    tax = 0.1*income
elif income <= 40525:
    tax = 995 + 0.12*(income-9950)
elif income <= 86375:
    tax = 4664 + 0.22*(income-40525)
elif income <= 164925:
    tax = 14751 + 0.24*(income-86375)
elif income <= 209425:
    tax = 33603 + 0.32*(income-164925)
elif income <= 523600:
    tax = 47843 + 0.35*(income-209425)
else:
    tax = 157804.25 + 0.37*(income-523600)
    
print("You owe ${:,.2f} in taxes for income earned in FY2021.".format(tax))