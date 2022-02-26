while True:
    c = input("Enter a character: ")
    if len(c) != 1:
        print("LOGIC ERROR: Enter single character.")
    else:
        break
    
while True:
    n = int(input("Enter an odd number between 1 and 9 (inclusive): "))
    if n < 1 or n > 9:
        print("LOGIC ERROR: Entry outside range.")
    elif n % 2 == 0:
        print("LOGIC ERROR: Enter an odd integer.")
    else:
        break
    
half = n//2
for i in range(half):
    print((half-i)*" " + (2*i+1)*c)
print(c*n)
for i in range(half, 0, -1):
    print((half-i+1)*" " + (2*i-1)*c)