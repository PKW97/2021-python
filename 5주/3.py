str = 'HelloPython!'
str1 = list(str)

print(str1)
print()

print("+ 012345678901")
print("  HelloPython!")
print("- 210987654321")

more = True
while more:
    s1, s2, s3= input("슬라이스[?:?:?] 3개 입력 >> ").split()
    a = int(s1)
    b = int(s2)
    c = int(s3)
    if (a+b+c) == 0:
        print("종료".center(30, '*'))
        more = False
    else:
        print(str1[a:b:c])
