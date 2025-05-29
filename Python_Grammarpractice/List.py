rainbow = ['빨강', '주황', '노랑', '초록', '파랑', '남색', '보라']

# 음수 인덱스를 사용하여 마지막 요소 가져오기
last_color_negative_index = rainbow[-1] # 리스트의 길이가 어떻게 되든지 항상 마지막 요소를 가져오기 때문에 유용
print('무지개의 마지막 색은 {}이다'.format(last_color_negative_index))

# 양수 인덱스를 사용하여 마지막 요소 가져오기
last_color_positive_index = rainbow[6]
print('무지개의 마지막 색은 {}이다'.format(last_color_positive_index))
