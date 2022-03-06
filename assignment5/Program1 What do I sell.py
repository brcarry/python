min_floor = 2
max_floor = 9
min_apartment = 1
max_apartment = 9
min_rent = 0
min_rent_floor = 0

print("This program will determine which floor of a building is bringing in the least rent\n")
print("Let's get going ...")
while True:
    num_floor = int(input("How many floors are in the building? "))
    if num_floor < min_floor:
        print("There must be more than one floor in the building")
    elif num_floor > max_floor:
        print("There cannot be more than 9 floors in the building")
    else:
        print("")
        break

for i in range(1, num_floor+1):
    while True:
        num_apartment = int(input("How many apartments are there on floor #{}? ".format(i)))
        if num_apartment < min_apartment:
            print("There must be at least one apartment on each floor.  Please try again.")
        elif num_apartment > max_apartment:
            print("There cannot be more than 9 apartments on each floor.  Please try again.")
        else:
            break

    sum_rent = 0
    for j in range(1, num_apartment+1):
        while True:
            rent = int(input("What is the rent for apartment {}0{}? ".format(i, j)))
            if rent > 0:
                break
            else:
                print("The rent must be a positive number")
        sum_rent += rent

    print("The rent for this floor is $" + format(sum_rent, ","))
    print("")

    if min_rent == 0:
        min_rent = sum_rent
        min_rent_floor = i
    else:
        if sum_rent < min_rent:
            min_rent = sum_rent
            min_rent_floor = i

print("The floor with the lowest rent is #{}".format(min_rent_floor))
print("The total monthly rent received on floor #{} is $".format(min_rent_floor) + format(min_rent, ","))

        



print("Hello world")