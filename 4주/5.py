
c = 20

while True:
    
    f = c * 9/5 + 32
    f2 = c * 2 + 30
    abs = f2 - f
    print("섭씨: %d 화씨: %.1f 화씨(약식): %d 차이: %.1f" % (c, f, f2, abs))
    c += 3
    if c > 41:
        break
