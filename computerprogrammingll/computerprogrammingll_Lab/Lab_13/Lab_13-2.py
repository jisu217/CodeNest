# 한국 유튜버 top 10

import numpy as np

ChName = ['TWICE','승비니 Seungbini','officialpsy','1MILLION Dance Studio',
'BANGTANTV','1theK (원더케이)','Mnet K-POP','HYBE LABELS','Jane ASMR 제인',
'SMTOWN','CuRe 구래','김프로KIMPRO','Stray Kids',"GH'S",'CRAZY GREAPA',
'KBS WORLD TV', 'BLACKPINK', 'BeatboxJCOP','JYP Entertainment','ToyPuddingTV']

Subscribers = np.array([17700000, 25500000, 19100000, 26300000, 79300000, 24800000,
21200000, 76000000, 18200000, 32800000, 26400000, 68500000,
18400000, 23300000, 19500000, 19900000, 95100000, 34100000,
29800000, 27300000], dtype=int)

AvgViews = np.array([ 217800, 2663000, 6360400, 14500, 1336900, 20100,
9922, 2385000, 105900, 2754600, 24168900, 22689600,
1188600, 9196900, 6913900, 3752, 11896800, 8188900,
880200, 102600], dtype=int)

# 구독자 순
sortIDX = np.argsort(-Subscribers) # 음수를 붙여 내림차순 정렬, argsort: 원래 배열에서 값을 정렬했을 때의 인덱스를 가져오는 함수
#ChName = ChName[sortIDX] # list이기 때문에 안됨

sortSubscb = Subscribers[sortIDX]
sortAvgView = AvgViews[sortIDX]

print("[한국 유튜버 구독자수 Top5]")
for i in sortIDX[:5] :
    print(ChName[i]+"-", end="")
    print(f"{sortSubscb[i]}명", end="")
    print(f"(조회수:{sortAvgView[i]})")

# 평균 조회수 천만 이상
print("\n[평균 조회수가 10,000,000(천만인상)인 유튜버]")
idx = np.where(AvgViews>10000000)[0] # where: 조건에 맞는 인덱스를 반환하는 함수
for i in idx :
    print(ChName[i])
