name1 = input("Name 1: ")
name2 = input("Name 2: ")
name3 = input("Name 3: ")

print("\n1. " + name1, name2, name3, sep=", ")
print("\n2. ***" + name2, name3, name1, sep="***", end="***\n")
print("\n3. " + name3, name1, name2, sep="\n   ", end="!")