# Quiz02_202404002 강지수
# 길이 변환 프로그램

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 사용자로부터 cm길이를 입력받는 코드
length = int(input("길이(cm): "))

feet_conversion_factor = 0.0328084
yard_conversion_factor = 0.0109361
inch_conversion_factor = 0.393701

# 입력 받은 cm길이를 피트, 야드, 인치로 변환하는 코드
length_conversion_feet = length * feet_conversion_factor  # 피트 = cm * 0.0328084
length_conversion_yard = length * yard_conversion_factor  # 야드 = cm * 0.0109361
length_conversion_inch = length * inch_conversion_factor  # 인치 = cm * 0.393701

# 계산 결과를 출력하는 코드
print(str(length) + "cm=%.4ffeet" % length_conversion_feet)
print(str(length) + "cm=%.4fyard" % length_conversion_yard)
print(str(length) + "cm=%.4finch" % length_conversion_inch)
