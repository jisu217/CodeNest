N = int(input()) # 설문조사를 한 사람의 수
bed = 0
good = 0

for i in range(N) :
    answer = input()
    if answer == '0' :
       bed += 1
    if answer == '1':
       good += 1

if bed > good :
   print("Junhee is not cute!")
else :
     print("Junhee is cute!")


