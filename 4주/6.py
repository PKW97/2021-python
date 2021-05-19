from random import randint

a = randint(1,99)
b = randint(1,99)
print("%d * %d = %d" % (a, b, a*b))
print()

while True:
    a = randint(1,99)
    b = randint(1,99)
    

    str = input("계속 y / n ? ")
    if str == "y":
        print("%d * %d = %d" % (a, b, a*b))
        print()
    elif str == "n":
        break
