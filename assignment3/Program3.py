weight = float(input("Please tell us about your shipping needs ...\nHow much do your item(s) weigh in pounds (e.g. 3.2)? "))
priority = int(input("How soon do you want your item(s) to arrive?\n1. 5 days - Standard rate\n2. 3 days - Express rate\n3. 2 days - Super-Express rate\n4. 1 day  - Hyper-Express rate\nPlease enter 1 - 4: "))
cost = float(input("What was the purchase price of your item(s)? "))

weight_ori = weight
if weight < 2:
    weight *= 3
elif weight < 5:
    weight *= 4
elif weight <10:
    weight *= 5
else:
    weight *=6

if priority == 1:
    priority = 2
elif priority == 2:
    priority = 8
elif priority == 3:
    priority = 15
elif priority == 4:
    priority = 45

if cost < 20:
    discount = 0
elif cost < 50:
    discount = 0.1
elif cost < 100:
    discount = 0.2
else:
    discount = 0.5

# 保持字符串总长为定值的方法升级：
# 拼接 + 统计长度 + 补全

print("-------------------------Results---------------------------------")

a = "The regular rate for a package that is: " + format(weight_ori, ".2f") + " pounds is"
b = "$" + format(weight, ".2f")
print(a + " " * (65 - len(a) - len(b)) + b)

a = "The handling fee for an Express package is:"
b = "$" + format(priority, ".2f")
print(a + " " * (65 - len(a) - len(b)) + b)

if cost >= 20:
    a = "Your $" + format(cost, ".2f") + " purchase entitles you to a shipping discount of"
    b = format( 100*discount, ".2f") + "%"
    print(a + " " * (66 - len(a) - len(b)) + b)

a = "The total shipping cost (including the discount) is:"
b = "$" + format((1 - discount)*(priority + weight), ".2f")
print(a + " " * (65 - len(a) - len(b)) + b)
