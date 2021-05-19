
degree = int(input('온도 입력 >> '))

f = degree * 9/5 + 32
f2 = degree * 2 + 30

print('정확 계산: 섭씨:', degree, '화씨:', f)
print('약식 계싼: 섭씨:', degree, '화씨:', f2)
print('차이:', f - f2)
