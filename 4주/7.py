
n = int(input("소수(prime number)인지를 판별한 2 이상의 정수 입력 >> "))

for i in range(2, n):
    if n % i == 0:
        break
    elif i+1 == n:
        i = True
if i == True:
    print("%d는 소수이다" % (n))
