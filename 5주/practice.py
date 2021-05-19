list = [39,34,45,73,12,92,2,47,39]
list1 = sorted(list)
list2 = list1[::-1]
list3 = sorted(list, reverse=True)

print("리스트", list)
print("정렬 리스트", list1)
print("역순 리스트", list2)
print("역순 리스트", list3)