ABC = int(input())
DEF = int(input())

# 두 번째 숫자의 각 자리수 추출
D = DEF // 100 # 백의 자리
E = (DEF // 10) % 10 # 십의 자리
F = DEF % 10 # 일의 자리

print(ABC*F) # 세 자리 수 × 일의 자리
print(ABC*E) # 세 자리 수 × 십의 자리
print(ABC*D) # 세 자리 수 × 백의 자리
print(ABC*DEF) # 전체 곱셈 결과