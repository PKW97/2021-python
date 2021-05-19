from random import randint

money = 12000

for i in range(5):
    n = randint(35,50)
    if n <= 40:
        print("근로 시간 %d시간, 주급 %d" % (n, n * money))
    else:
        print("근로 시간 %d시간, 주급 %d" % (n, (40 * money) +(n - 40) * (money * 1.5)))
