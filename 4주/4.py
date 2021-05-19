h, w = input("당신의 키(cm)와 몸무게(kg)는? >> ").split()
he = float(h)
we = float(w)

print("키: %.1f(cm), 몸무게: %.1f(km)" % (he, we))
bmi = we / ((he/100) ** 2)

if 40 <= bmi:
    print("BMI: %.1f 고도비만" % (bmi))
elif 35 <= bmi < 40:
    print("BMI: %.1f 중등도 비만" % (bmi))
elif 30 <= bmi < 35:
    print("BMI: %.1f 비만" % (bmi))
elif 25 <= bmi < 30:
    print("BMI: %.1f 과체중" % (bmi))
elif 18.5 <= bmi < 25:
    print("BMI: %.1f 정상" % (bmi))
else:
    print("BMI: %.1f 저체중" % (bmi))

