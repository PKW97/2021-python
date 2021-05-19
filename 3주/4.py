
url = 'https://docs.python.org/3/tutorial'

a = url.find(':')
aword = url[:a]

b = url.find('/')
b2 = url.find('3')
bword = url[b+2:b2-1]

c = url.rfind('/')
cword = url[c+1:]


print(aword)
print(bword)
print(cword)

