
first = str(input('첫 번째 16진수 실수 입력 >> '))
second = str(input('두 번째 16진수 실수 입력 >> '))

f = float.fromhex('f')
s = float.fromhex('e.1')

print('실수1:', f, '실수2:', s)
print('합:', f + s)
print('차:', f - s)
print('곱하기:', f * s)
print('나누기:', f / s)
