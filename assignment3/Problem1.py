year = int(input("Enter year: "))

if year < 1582:
    print(year, "is before the adoption of the Gregorian calendar.")
else:
    if year % 4 == 0 and year % 100 != 0:
        print("\t" + str(year), "is a leap year.")
    elif year % 400 == 0:
        print("\t" + str(year), "is a leap year.")
    else:
        print("\t" + str(year), "is NOT a leap year.")