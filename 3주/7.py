
a = -7
mask = 0xf9
b = a & mask

a1 = -6
mask1 = 0xfa
b1 = a1 & mask1

a2 = -5
mask2 = 0xfb
b2 = a2 & mask2

a3 = -4
mask3 = 0xfc
b3 = a3 & mask3

a4 = -3
mask4 = 0xfd
b4 = a4 & mask4

a5 = -2
mask5 = 0xfe
b5 = a5 & mask5

a6 = -1
mask6 = 0xff
b6 = a6 & mask6

a7 = 0
mask7 = 0
b7 = a7 & mask7

print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a, b, b, b))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a1, b1, b1, b1))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a2, b2, b2, b2))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a3, b3, b3, b3))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a4, b4, b4, b4))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a5, b5, b5, b5))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a6, b6, b6, b6))
print("10진수: {:2d}, 2진수: {:8b}, 8진수: {:3o}, 16진수: {:2x}".format(a7, b7, b7, b7))
