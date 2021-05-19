books = {'파이썬 개론':['강환수'], 'Perfect C':['강환수', '이동규'], '컴퓨터 개론':['강환수', '조진형', '신용현']}

for i in books.keys():
    print("책 이름: {}, 저자: {}".format(i, books[i]))

print(books.values())
books.items()

