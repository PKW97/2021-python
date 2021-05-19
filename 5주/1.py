from random import randint

list = list()

for i in range(10):
    r = randint(1,99)
    list.append(r)
print("리스트", list)
print("정렬리스트", sorted(list))
print("역순 리스트", sorted(list,reverse=True))