V = int(input())
Vote = input()

count1 = 0
count2 = 0

for i in range(V) :
    if Vote[i] == "A" :
       count1 += 1

    if Vote[i] == "B" :
       count2 += 1

if count1 > count2 :
   print("A")
elif count1 < count2 :
     print("B")
else :
     print("Tie")



