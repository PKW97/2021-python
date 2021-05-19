sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]

a = 0
for i in range(1, 8, 2):
    sports.insert(i, num[a])
    a+=1
print(sports)

sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
for i in range(1, 8, 2):
    sports.insert(i, '')
print(sports)

sports[1::2] = num[:]
print(sports)