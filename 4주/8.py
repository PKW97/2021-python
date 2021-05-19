n = 56

print("첫 값은 %d이다." % (n))

while True:
    c = input("산술 연산의 종류를 입력하세요. >> ")
    
    if c == "*":
        n2 = int(input("두 번째 피연산자를 입력하세요. >> "))
        print("%d * %d = %d" % (n, n2, n*n2))    
    elif c == "/":
        n2 = int(input("두 번째 피연산자를 입력하세요. >> "))
        print("%d / %d = %d" % (n, n2, n/n2))
    elif c == "+":
        n2 = int(input("두 번째 피연산자를 입력하세요. >> "))
        print("%d + %d = %d" % (n, n2, n+n2))
    elif c == "-":
        n2 = int(input("두 번째 피연산자를 입력하세요. >> "))
        print("%d - %d = %d" % (n, n2, n-n2))
    else:
        print("종료".center(20,'*'))
        break
