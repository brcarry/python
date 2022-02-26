while True:
    n = int(input("Enter a positive integer: "))
    if n < 1:
        print("Invalid input, try again.")
    else:
        break

n_ori = n#保存原始数据
binary = ""
while n != 0:
    binary = str(n % 2) + binary
    n = n // 2

print("The binary representation of {} is {}.".format(n_ori, binary))