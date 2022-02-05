import random, secrets

f = input("First initial: ")
l = input("Last initial: ")


print(f.lower() + l.lower() + str(random.randint(1000, 9999)))
print(secrets.token_hex(3))

#random.randint(a, b)
#Return a random integer N such that a <= N <= b. Alias for randrange(a, b+1)

#secrets.token_hex([nbytes=None])
#Return a random text string, in hexadecimal. The string has nbytes random bytes, each byte converted to two hex digits. If nbytes is None or not supplied, a reasonable default is used.