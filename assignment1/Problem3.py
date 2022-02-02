import math

money = float(input("Enter amount of change needed: $"))

t_money = money#对变量money进行保护，可以试试看直接用money最后会输出什么结果

quarters = int(math.floor(t_money/0.25))
t_money = t_money - quarters*0.25
dimes = int(math.floor(t_money/0.1))
t_money = t_money - dimes*0.1
nickles = int(math.floor(t_money/0.05))
t_money = t_money - nickles*0.05
pennies = int(round(t_money/0.01,0))
#为什么最后一个不用math.floor呢？
#可以单步调试看看如果继续用math.floor函数进行取整，最终会输出什么？
#根本原因是浮点数有精度限制
#所以本地最保险的做法是先把money*100，转换成int型，再进行运算哦~
#可以试试看qwq

print(
    "The best way to make $%.2f change in coins is:\n" % money + \
    "\t" + format("Quarters:","<10") + str(quarters) + "\n" + \
    "\t" + format("Dimes:","<10") + str(dimes) + "\n" + \
    "\t" + format("Nickles:","<10") + str(nickles) + "\n" + \
    "\t" + format("Pennies:","<10") + str(pennies)
    )

#第一个字符串中%.2f涉及字符串的格式化输出，可以参考
#https://www.cnblogs.com/qinchao0317/p/10699717.html