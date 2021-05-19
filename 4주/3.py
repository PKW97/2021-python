from  random import randint

for i in range(3):
    a = randint(1,99)
    b = randint(1,99)
    c = randint(1,99)
    
print("%d %d %d중에서 최대: %d" % (a,b,c,max(a,b,c)))
