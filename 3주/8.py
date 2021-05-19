
a = int(input("정수 입력 >> "))
a2 = int(input("2의 지수승 입력 >> "))


print("정수 {0} >> {1}, 결과: {2}".format(a, a2, a << a2))
print("정수 {0} * 2**{1}, 결과: {2}".format(a, a2, a * 2**a2))
print("2진수(32비트): {0:32b} 정수: {0}".format(a))
print("2진수(32비트): {2:32b} 정수: {0} << {1}".format(a, a2, a << a2))
print("2진수(32비트): {2:32b} 정수: {0} * 2**{1}".format(a, a2, a * 2**a2)) 
