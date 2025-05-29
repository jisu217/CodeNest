# 딕셔너리 정의
my_dict = {'one': 1, 'two': 2}

# 딕셔너리에 값 추가
my_dict['three'] = 3
print(my_dict)  # {'one': 1, 'two': 2, 'three': 3}

# 딕셔너리 값 수정
my_dict['one'] = 11
print(my_dict)  # {'one': 11, 'two': 2, 'three': 3}

# 딕셔너리 값 삭제 (del)
del my_dict['one']
print(my_dict)  # {'two': 2, 'three': 3}

# 딕셔너리 값 삭제 (pop)
my_dict.pop('two')
print(my_dict)  # {'three': 3}
