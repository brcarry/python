import random

cnt = 1
while True:
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    print("***Roll {}***".format(cnt))
    print("Die 1:", a)
    print("Die 2:", b)
    cnt +=1
    if a+b == 7:
        print("Game over, you rolled a 7.")
        break
    elif a == 1 and b == 1:
        print("You rolled snake eyes!")
    elif a == b:
        print("You rolled a hard {}!".format(a+b))