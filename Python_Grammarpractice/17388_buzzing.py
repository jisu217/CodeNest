# 와글와글 숭고한

S, K, H = map(int, input().split())

if S + K + H >= 100 :
   print("OK")

else :
     result = [(S, "Soongsil"), (K, "Korea"), (H, "Hanyang")]
     result.sort()
     print(result[0][1])