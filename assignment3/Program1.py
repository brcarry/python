date = int(input("Please enter your birthday using the format mmdd: "))

month = date // 100
day = date % 100

maxDay = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
monthName = ["", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]

if maxDay[month] < day:
    print("You have entered an invalid date.  Please re-run the program and try again")
else:
    #输入的日期有效，将日期对应的数字转换成对应格式的字符串
    month = monthName[month]
    if day % 10 == 1:
        day = str(day) + "st"
    elif day % 10 == 2:
        day = str(day) + "nd"
    elif day % 10 == 3:
        day = str(day) + "rd"
    else:
        day = str(day) + "th"
        
    #判断星座
    if 121 <= date <= 219:
        print("Your birthday is {:s} {:s} and you are an Aquarius".format(month, day))
    elif 220 <= date <= 320:
        print("Your birthday is {:s} {:s} and you are an Pisces".format(month, day))
    elif 321 <= date <= 420:
        print("Your birthday is {:s} {:s} and you are an Aries".format(month, day))
    elif 421 <= date <= 521:
        print("Your birthday is {:s} {:s} and you are an Taurus".format(month, day))
    elif 522 <= date <= 621:
        print("Your birthday is {:s} {:s} and you are an Gemini".format(month, day))
    elif 622 <= date <= 722:
        print("Your birthday is {:s} {:s} and you are an Cancer".format(month, day))
    elif 723 <= date <= 822:
        print("Your birthday is {:s} {:s} and you are an Leo".format(month, day))
    elif 823 <= date <= 923:
        print("Your birthday is {:s} {:s} and you are an Virgo".format(month, day))
    elif 924 <= date <= 1023:
        print("Your birthday is {:s} {:s} and you are an Libra".format(month, day))
    elif 1024 <= date <= 1122:
        print("Your birthday is {:s} {:s} and you are an Scorpio".format(month, day))
    elif 1123 <= date <= 1221:
        print("Your birthday is {:s} {:s} and you are an Sagittarius".format(month, day))
    else:
        print("Your birthday is {:s} {:s} and you are an Capricorn".format(month, day))
   
