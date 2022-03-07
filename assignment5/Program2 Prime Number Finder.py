from re import T
from statistics import mode
from tkinter.tix import Tree


print(
    "This program can find prime numbers.\n\
It can function in one of five different modes\n\
Mode A: Accept a number and determine if it is a prime number\n\
Mode B: Produce a list of prime numbers up to 1,000\n\
Mode C: Produce a table of prime numbers up to 1,000\n\
Mode D: Produce a list of prime numbers based upon a user supplied range\n\
Mode E: Produce a table of prime numbers based upon a user supplied range"
)

while True:
    mode = input("Which Mode would you like to use? ")
    if mode != "A" and mode != "B" and mode != "C" and mode != "D" and mode != "E":
        print("Sorry.  I didn't understand what you entered.  Please try again.")
    else:
        break

if mode == "A":
    while True:
        sub_mode = input("Do you want to see a) the steps or b) just the result? ")
        if sub_mode != "a" and sub_mode != "b":
            print("Sorry.  The only options are a or b")
        else:
            break
    while True:
        num = int(input("Enter a positive number greater than 1 to test: "))
        if num <= 1:
            print("I can only process positive numbers greater than 1")
        else:
            break
    if sub_mode == "a":
        for i in range(2, num):
            if num % i == 0:
                print("{} is a divisor of {} ... stopping".format(i, num))
                print("{} is not a prime number".format(num))
                break
            elif i == num-1:
                print("{} is NOT a divisor of {} ... continuing".format(i, num))
                print("{} is a prime number".format(num))
            else:
                print("{} is NOT a divisor of {} ... continuing".format(i, num))
    elif sub_mode == "b":
        for i in range(2, num):
            if num % i == 0:
                print("{} is not a prime number".format(num))
                break
            elif i == num-1:
                print("{} is a prime number".format(num))
elif mode == "B":
    for j in range(1, 1001):
        if j == 1:
            print("1 is technically not a prime number.")
        elif j == 2:
            print("2 is a prime number")
        else:
            for i in range(2, j):
                if j % i == 0:
                    break
                elif i == j-1:
                    print("{} is a prime number".format(j))
elif mode == "C":
    cnt = 0
    for j in range(1, 1001):
        if j == 2:
            print(format(j, ">4d"), end="")
            cnt += 1
        else:
            for i in range(2, j):
                if j % i == 0:
                    break
                elif i == j-1:
                    print(format(j, ">4d"), end="")
                    cnt += 1
                    if cnt % 10 == 0:
                        print("")
elif mode == "D":
    while True:
        num_start = int(input("Please enter the starting number: "))
        if num_start <= 0:
            print("Sorry.  I can only process positive numbers")
        else:
            break
    while True:
        num_end = int(input("Please enter the ending number: "))
        if num_end < num_start:
            print("Sorry.  Ending number should be larger than starting number")
        else:
            break
    for j in range(num_start, num_end+1):
        if j == 1:
            print("1 is technically not a prime number.")
        elif j == 2:
            print("2 is a prime number")
        else:
            for i in range(2, j):
                if j % i == 0:
                    break
                elif i == j-1:
                    print("{} is a prime number".format(j))
else:
    while True:
        num_start = int(input("Please enter the starting number: "))
        if num_start <= 0:
            print("Sorry.  I can only process positive numbers")
        else:
            break
    while True:
        num_end = int(input("Please enter the ending number: "))
        if num_end < num_start:
            print("Sorry.  Ending number should be larger than starting number")
        else:
            break
    for j in range(num_end, num_start-1, -1): #先通过倒序，找到范围内最大的质数，用来确定宽度
        flag = False
        if j == 1:
            flag = True #其实没有必要
            break
        elif j == 2:
            flag = True
            break
        else:
            for i in range(2, j):
                if j % i == 0:
                    flag = False
                    break
                elif i == j-1:
                    flag = True
                    break
        if flag == True:
            break
    
    width = len(str(j))+1
    cnt = 0
    for j in range(num_start, num_end+1):
        if j == 2:
            print(" "*(width - len(str(j)) + str(j)), end="")
            cnt += 1
        else:
            for i in range(2, j):
                if j % i == 0:
                    break
                elif i == j-1:
                    print(" "*(width - len(str(j))) + str(j), end="")
                    cnt += 1
                    if cnt % 10 == 0:
                        print("")


    