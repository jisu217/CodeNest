# HW1_1_202404002 강지수
# 월별 평균 기온

# 학번/이름 출력문
print("*****************")
print("202404002/강지수")
print("*****************")

# 7월, 8월, 9월에 측정한 온도 데이터
weather = {
"Jul":['28.01','27.5','24.13','30.67','27.17','25.22','34.21','24.28','24.26','30.12','32.06','25.56'],
"Aug":['24.08','29.63','23.4','25.84','33.47','34.91','23.96','34.11','26.71'],
"Sep":['27.98','20.75','20.25','21.92','30.44','24.54','28.3','29.35','19.78','21.77','26.3'],
}
month= {"Jul": "7", "Aug": "8", "Sep": "9"}

# 평균 기온 계산
def weather_average(temperatures):
    temperatures = [float(temp) for temp in temperatures]
    return sum(temperatures) / len(temperatures)

# 월별 평균 기온 출력
print(f"{month['Jul']}월 평균기온:{weather_average(weather['Jul']):.2f}도")
print(f"{month['Aug']}월 평균기온:{weather_average(weather['Aug']):.2f}도")
print(f"{month['Sep']}월 평균기온:{weather_average(weather['Sep']):.2f}도")

# 홈워크 풀면서 공부한 내용
# print(f"{month[0]}월 평균기온:{weather_average["Jul"].2f}도")
# print(f"{month[1]}월 평균기온:{weather_average["Aug"].2f}도")
# print(f"{month[2]}월 평균기온:{weather_average["Sep"].2f}도")이 아닌
# print(f"{month['Jul']}월 평균기온:{weather_average(weather['Jul']):.2f}도")
# print(f"{month['Aug']}월 평균기온:{weather_average(weather['Aug']):.2f}도")
# print(f"{month['Sep']}월 평균기온:{weather_average(weather['Sep']):.2f}도")
# (temperatures): 함수에 전달될 입력 인자(매개변수)
# weather_average(['28.01', '27.5', '24.13']) -> temperatures 변수 ['28.01', '27.5', '24.13']

# [float(temp) for temp in temperatures]: ['28.01', '27.5', '24.13'] -> [28.01, 27.5, 24.13]