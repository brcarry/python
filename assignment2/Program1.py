money = int(input("Please enter your budget for each country (in dollars): "))

print("With your %d you will have the following local currency available\n" % money)

euro = 0.89*money
rupees = 85.07*euro
rial = 561.02*rupees
yuan = rial/6634.91
fiji = 0.34*yuan
bahamas = fiji/2.14

print(format("France","7s"),format(euro,">17,.2f")," euro",sep="")
print(format("India","7s"),format(rupees,">17,.2f")," rupees",sep="")
print(format("Iran","7s"),format(rial,">17,.2f")," rial",sep="")
print(format("China","7s"),format(yuan,">17,.2f")," yuan",sep="")
print(format("India","7s"),format(fiji,">17,.2f")," Fijian dollars",sep="")
print(format("India","7s"),format(bahamas,">17,.2f")," Bahamian dollars",sep="")

#没有找到更间接的格式化输出的方法quq
#采用的方式是把每一行拆分成两段，每一段为定长并分别向左向右对齐可以满足题目要求

