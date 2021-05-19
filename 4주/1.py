month = int(input("월 입력? "))

if 4 <=month <= 5:
    print(str(month)+"월 봄")
elif 6 <= month <=8:
    print(str(month)+"월 여름")
elif 9 <= month <= 10:
    print(str(month)+"월 가을")
else:
    print(str(month)+"월 겨울")
