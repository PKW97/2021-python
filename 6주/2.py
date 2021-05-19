com = {'삼성에스디에스':24200, '삼성전자':47000, '엔씨소프트':52600, '핸디소프트':5120, '골프존':215000, '기아':56300}

while True:
    name = input('주식 이름? ')
    if name in com:
        print(name, com[name])
        print()
    else:
        print('주식 이름 없음')
        break