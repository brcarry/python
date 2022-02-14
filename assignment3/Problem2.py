month = int(input("Enter month: "))
date = int(input("Enter date: "))

if month == 2:
    week = 1 + date % 7
    month = "February"
elif month == 3:
    week = 1 + date % 7
    month = "March"
else:
    week = 4 + date % 7
    month = "April"

if week == 1:
    week = "Monday"
elif week == 2:
    week = "Tuesday"
elif week == 3:
    week = "Wednesday"
elif week == 4:
    week = "Thrusday"
elif week == 5:
    week = "Friday"
elif week == 6:
    week = "Saturday"
else:
    week = "Sunday"

print(month, str(date) + ",","2022 is a",week)
