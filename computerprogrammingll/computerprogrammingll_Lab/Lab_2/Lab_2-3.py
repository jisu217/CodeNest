# 화씨 섭씨로 변환하기
# * 연산자 "//" 와 "/"의 차이 확인하기

print("화씨->섭씨")
F_temp = float(input("화씨:"))
C_temp = (F_temp-32)*5//9
print("%.2fF -> %.2fC" %(F_temp,C_temp)) # -1.00C

print("화씨->섭씨")
F_temp = float(input("화씨:"))
C_temp = (F_temp-32)*5/9
print("%.2fF -> %.2fC" %(F_temp,C_temp)) # -0.56C

# //: 소수점을 버리고 몫만 반환 int or float
# /: 일반적인 나눗셈 float
