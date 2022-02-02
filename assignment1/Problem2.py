dollar = float(input("Enter USD to convert: $"))

euros = format (dollar*1.129,",.2f" )
rupees = format (dollar*74.32, ",.2f")
francs = format (dollar*0.9188, ",.2f")
yen = format (dollar*115.27, ",.2f")
yuan = format(dollar*6.355, ",.2f")

#唯一一些更优的调整就是在后续输出时，不需要再用str对euros等变量进行转换
#因为format函数的返回值就是str类型
#而dollar仍为float类型
#可以通过运行以下代码验证（去掉注释即可）
#print(type(dollar))
#print(type(euros))

print ("This is how much $" + str(dollar) +"USD is in:")
print ("\t"+"Euros:"+ "\t"+format(euros, '>10'))
print ("\t"+"Rupees:"+ "\t"+format(rupees, '>10'))
print ("\t"+"Francs:"+ "\t"+format(francs, '>10'))
print ("\t"+"Yen:"+ "\t"+format(yen, '>10'))
print ("\t"+"Yuan:"+"\t"+ format(yuan, '>10'))
