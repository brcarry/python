import random

n = int(input("Enter size for your pattern (3-8): "))
c = random.choice(["!", "@", "#", "$", "%", "^", "&", "*", "(", ")"])

print("\nPattern #1\n")
for i in range(n):
    print(" "*i + c*(n-i))
    
print("\nPattern #2\n")
print(c*n)
for i in range(n-2):
    print(c + " "*(n-2) + c)
print(c*n)

print("\nPattern #3\n")
for i in range(n):
    if i // 2 == 0:
        print(c*n)
    else:
        print(" "*n + c*n)

print("\nPattern #4\n")
for i in range(n):
    print(" "*i + c*n)


#注意这里是range(n+1)否则不会打印最后一行
print("\nPattern #5\n")
for i in range(n+1):
    print(" "*i + c*(n-i) + str(i+1) + c*(n-i))