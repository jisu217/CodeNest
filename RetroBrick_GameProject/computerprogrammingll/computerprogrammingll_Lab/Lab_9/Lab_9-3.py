# 어떤 반의 점수 평균, 최고점 및 최저점 학생의 이름과 점수 출력

def maxIDX(list1, list2) :

    maxIDX = 0 # 최대값이 있는 index

    for i in range(len(list1)) :

        if list1[maxIDX] < list1[i] :
            maxIDX = i

    return list1[maxIDX], list2[maxIDX]

def minIDX(list1, list2) :

    minIDX = 0

    for i in range(len(list1)) :

        if list1[minIDX] > list1[i] :
            minIDX = i

    return list1[minIDX], list2[minIDX]

def avglist(lists) :

    total = 0

    for n in lists :
        total += n

    return total / len(lists)

names=['John', 'Emily', 'Michael', 'Sophia', 'James', 'Olivia', 'Daniel', 'Emma',
'Matthew', 'Isabella', 'David', 'Ava', 'Christopher', 'Mia', 'Andrew']
scores=[89, 76, 65, 93, 55, 42, 78, 88, 64, 79, 95, 54, 33, 99, 61]

print(f'평 균:\t{avglist(scores)}점')

s, n = maxIDX(scores, names)
formattedName = "%10s" % n
print(f"최고점:{formattedName} \t {s}점")

s, n = minIDX(scores, names)
formattedName = "%10s" % n
print(f"최저점:{formattedName} \t {s}점")